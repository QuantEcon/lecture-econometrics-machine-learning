import pandas as pd
import wbgapi as wb

# Load Datasets
exports = pd.read_csv("data/exports_2013.csv")
cepii = pd.read_csv("data/cepii_2013.csv")

# Harmonise Column Names
exports.columns = ['year', 'iso3_d','iso3_o', 'evalue']

# Merge
dataset = exports[['year', 'iso3_o', 'iso3_d', 'evalue']]
dataset = dataset.merge(cepii, how='left', on=['year', 'iso3_o', 'iso3_d'])

# Select Data for Regression Dataset
regdata = dataset[['year','iso3_o','iso3_d','evalue','dist','gdp_o', 'gdp_d']]

# Add WDI GDP Data
wdi_gdp = wb.data.DataFrame(['NY.GDP.MKTP.CD'], time="YR2013")
# Origin Countries
regdata = regdata.merge(wdi_gdp, how='left', left_on=['iso3_o'], right_index=True)
regdata = regdata.rename(columns={'NY.GDP.MKTP.CD' : 'wdi_gdp_o'})
regdata['wdi_gdp_o'] = regdata['wdi_gdp_o'] / 1000
# Destination Countries
regdata = regdata.merge(wdi_gdp, how='left', left_on=['iso3_d'], right_index=True)
regdata = regdata.rename(columns={'NY.GDP.MKTP.CD' : 'wdi_gdp_d'})
regdata['wdi_gdp_d'] = regdata['wdi_gdp_d'] / 1000

# Save in DTA
regdata.to_stata("./data/gravity_model2.dta", write_index=False)