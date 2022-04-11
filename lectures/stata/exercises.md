(stata/exercises)=
# Exercises

Here are some exercises to work through in your own time.

:::{exercise}
Using `stata` fetch the `sysauto` dataset using

```stata
sysuse auto
```

**Part 1:**

Use [python-from-stata](stata/python-from-stata) lecture
to transfer the `weight` and `price` variables to `python` and save the
results in a `pd.DataFrame` called `data`.

```python
>>> data
    weight  price
0     2930   4099
1     3350   4749
2     2640   3799
3     3250   4816
4     4080   7827
..     ...    ...
69    2160   7140
70    2040   5397
71    1930   4697
72    1990   6850
73    3170  11995

[74 rows x 2 columns]
```

**Part 2:**

Use the python package [statsmodels](https://www.statsmodels.org/stable/index.html) to run a simple `OLS` regression of `weight ~ price`
and then run this regression in `stata`.
:::

:::{exercise}

Use the `yfinance` package in `python` to fetch the last `3 months` of `Close` 
prince data for:

1. Amazon (AMZN)
2. Microsoft (MSFT)
3. Game Stop (GME)

and construct a dataframe.

**Part 1:**

Choose to use either the [python-from-stata](stata/python-from-stata) lecture
or [file based workflow](stata/python-files) to transfer the
last three months of stock price data ("closing price") to `stata`

Run a simple `ols` regression:

1. comparing `AMZN` and `MSFT` stock price histories
2. comparing `AMZN` and `GME` stock price histories

**Part 2:**

Choose either `stata` or `python` to normalize each stock price history by
dividing the column by the first price of each stock.

The `dataframe` should look like

```{figure} img/python-yfinance-stock-price-normalised.png
:scale: 50%
```

and make a `plot` comparing the three time series.

:::