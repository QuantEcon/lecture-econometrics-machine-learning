(stata/python-files)=
# File based Workflows

In many cases it can be convenient to keep `stata` and `python`
workflows largely independent of each other and use files to
transfer data back and forth such as:

1. Dataset Construction (Python)
2. Statistical Modelling (Stata)

or vice-versa.

```{note}
If `data` needs to be computed regularly due to updates in source files.
The `python script` interface in `stata` is useful here as it can
be used to update `data` using a `python script`, saving the update data
to a new `dta` file and then running any `regressions` in `stata`.
```

The support for using a file based workflow is provided by `pandas`
as it has an interface for reading and writing `dta` files.

## Pandas: Reading `dta` files

The documentation on [pd.read_stata()](https://pandas.pydata.org/docs/reference/api/pandas.read_stata.html) is a good resource.

Let's fetch the `auto` dataset provided by `stata` and save it as
a `dta` file.

```stata
sysuse auto
save "auto.dta"
```

You can view this dataset in the `data reader`

```{figure} img/stata-dataeditor-auto.png
```

In `stata` this dataset consists of the following types:

```{list-table}
:widths: 15 25 15
:header-rows: 1

* - Variables
  - Data Type
  - Label
* - make
  - str18
  - Make and Model
* - price
  - int
  - Price
* - mpg
  - int
  - Mileage (mpg)
* - rep78
  - int
  - Repair Record 1978
* - headroom
  - float
  - Headroom (in)
* - trunk
  - int
  - Trunk space (cu. ft.)
* - weight
  - int
  - Weight (lbs)
* - length
  - int
  - Length (in.)
* - turn
  - int
  - Turn Circle (ft.)
* - displacement
  - int
  - Displacement (cu. in.)
* - gear_ratio
  - float
  - Gear Ratio
* - foreign
  - byte
  - Car Type
```

Where `foreign` is `labelled` data represented by `0/1` with labels:

1. `0` = `Domestic`
2. `1` = `Foreign`

Let us now read this `dta` file into `python` using [pd.read_stata()](https://pandas.pydata.org/docs/reference/api/pandas.read_stata.html)

:::{margin}
```{note}
The default saving location for `stata` is in your `Documents` directory. You may want to
write the `dta` file to some other location if you wish for easier access when using `jupyter`
```
:::

Open a `jupyter notebook` and then import the data such as:

```python
import pandas as pd
auto = pd.read_stata("auto.dta")
auto
```

:::{margin}
```{note}
As you can see from the `rep78` variable, missing values are handled in the
transfer (by default) and represented by `np.nan`
```
:::

```{figure} img/python-pandas-read-auto.png
```

The `data types` reported by `auto.dtypes` show that `pandas` has done a good job of fetching
the data faithfully from the `stata` dta file.

```python
auto.dtypes
```

produces the following list:

:::{margin}
```{note}
Labelled Data in `stata` such as `foreign` is converted into [pd.Categorical](https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html).

`pandas` uses a column of `dtype = object` for a column of strings, as `str` objects are a collection of
variable length `str` objects. This means you can edit these strings to an arbitrary length.
```
:::

```
make              object
price              int16
mpg                int16
rep78            float64
headroom         float32
trunk              int16
weight             int16
length             int16
turn               int16
displacement       int16
gear_ratio       float32
foreign         category
dtype: object
```

## Pandas: Writing `dta` files

```{tip}
You can also write other `data` file formats if you have trouble
with the `dta` writer, such as `csv`, `xlsx`. However you often loose
information in this process and you may need to think about `dtypes` during this
translation process between formats in a similar way as when migrating the raw data
via the `stata function interface`.
```

:::{margin}
```{tip}
You may notice that the `to_stata()` method is associated with a `pd.DataFrame` object.
This is different to `pd.read_stata()` which is a top level function for reading in the
`dta` file associated with `pandas`.
```
:::

You can write to `dta` file format using [pd.DataFrame.to_stata()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_stata.html) method associated with `pd.DataFrame`.

```python
import yfinance as yf
dowjones = yf.Ticker("^DJI")
data = dowjones.history(start="2010-01-01", end="2020-12-31")[['Close', 'Volume']]
data.to_stata("yfinance-dji.dta")
```

:::{note}
It is also possible to write these `dta` files from within a stata python program
such as:

```stata
python:
import yfinance as yf
dowjones = yf.Ticker("^DJI")
data = dowjones.history(start="2010-01-01", end="2020-12-31")[['Close', 'Volume']]
data.to_stata("yfinance-dji.dta")
end
use yfinance-dji.dta, clear
```

or alternatively running a `python script`
:::

This will save a `dta` file that can be opened with `stata` and viewed
in the `data editor`

```{figure} img/python-pandas-yfinance-data-tostata-dataeditor1.png
```

In `python` if you run

```python
data.index[0]
```

you will see the `index` is constructed of `Timestamp` objects

```
Timestamp('2009-12-31 00:00:00')
```

These objects have been transferred for you into `stata` date variables as `tc`.

You can now format this data straight away which is convenient as it reduces the
amount of `translation` you need to think about.

```stata
format %tcCCYY-NN-DD Date
```

The `data viewer` now consists of nicely formatted `dates`

```{figure} img/python-pandas-yfinance-data-tostata-dataeditor2.png
```

You may notice the default `datetime` object has been translated nicely but `pandas`
has used stata `tc` format (by default) as [per the documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_stata.html).
We can specify `td` dates using the `convert_dates=` keyword argument and specifying the `column`
and which `datetime` conversion to use such as:

```stata
python:
data = data.reset_index()
data.to_stata("yfinance-dji2.dta", convert_dates={'Date' : 'td'})
end
```

### Errors you can come across writing `dta` files

The `pandas` object is more general than the stata `dta` format so there are cases where
the data can't be written to `dta` format.

Let's use the following `pd.DataFrame` to look at this issue:

```python
import pandas as pd
data = {
    'a' : [pd.Series([1,2,3]), pd.Series([4,5,6])],
    'b' : [[1,2,3],[4,5,6]],
    'c' : [1,2],
}
data = pd.DataFrame(data)
```

you will get a `DataFrame` that looks like the following (and associated `dtypes`)

``` {figure} img/python-pandas-tostata-error-data.png
:scale: 50%
```

As you can see the first column consists of `pd.Series` objects. The pandas DataFrame is
capable of storing any `python` object as elements in a general column `dtype=object`

To get the first element of column `a` you can use

```python
data['a'][0]
```

which displays the `object` which is a `pd.Series`

```python
0    1
1    2
2    3
dtype: int64
```

```{note}
In practice, when working with data, this is not very common but I wanted to
demonstrate that the `pd.DataFrame` object is capable of storing complex data types.
```

If you now try and write this `dataframe` to disk using the `to_stata()` method you
will get a `ValueError` as there is no way to store the `pd.Series` objects in column
`a` int a `dta` file.

```python
data.to_stata("test.dta")
```

you will get the following `Traceback`

```python
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-28-43f621af9c2f> in <module>
----> 1 data.to_stata("test.dta")

~/anaconda3/lib/python3.8/site-packages/pandas/util/_decorators.py in wrapper(*args, **kwargs)
    212                 else:
    213                     kwargs[new_arg_name] = new_arg_value
--> 214             return func(*args, **kwargs)
    215 
    216         return cast(F, wrapper)

~/anaconda3/lib/python3.8/site-packages/pandas/core/frame.py in to_stata(self, path, convert_dates, write_index, byteorder, time_stamp, data_label, variable_labels, version, convert_strl)
   1967             kwargs["version"] = version
   1968 
-> 1969         writer = statawriter(
   1970             path,
   1971             self,

~/anaconda3/lib/python3.8/site-packages/pandas/io/stata.py in __init__(self, fname, data, convert_dates, write_index, byteorder, time_stamp, data_label, variable_labels)
   2078         self._own_file = True
   2079         # attach nobs, nvars, data, varlist, typlist
-> 2080         self._prepare_pandas(data)
   2081 
   2082         if byteorder is None:

~/anaconda3/lib/python3.8/site-packages/pandas/io/stata.py in _prepare_pandas(self, data)
   2307 
   2308         # Verify object arrays are strings and encode to bytes
-> 2309         self._encode_strings()
   2310 
   2311         self._set_formats_and_types(dtypes)

~/anaconda3/lib/python3.8/site-packages/pandas/io/stata.py in _encode_strings(self)
   2337                 if not ((inferred_dtype in ("string", "unicode")) or len(column) == 0):
   2338                     col = column.name
-> 2339                     raise ValueError(
   2340                         f"""\
   2341 Column `{col}` cannot be exported.\n\nOnly string-like object arrays

ValueError: Column `a` cannot be exported.

Only string-like object arrays
containing all strings or a mix of strings and None can be exported.
Object arrays containing only null values are prohibited. Other object
types cannot be exported and must first be converted to one of the
supported types.
```

If you try exporting column `b` you would similarly get a `ValueError` as `stata`
can't represent lists of numbers.

This is sensible for the domain in which `stata` operates. For regressions we need
to store variables that contains some `data` such as `int`, `float`, `str` values
that `stata` can directly operate on.

#### Dates

If you try passing `datetime` objects from `pandas` that includes `time zone` information you will
get a `NotImplementedError` as `stata`.

Generally this type of error indicates that this is **not supported**.

This could mean that `stata` might be able to work with `time zone` data but it hasn't
been implemented in the `pandas` code -- or the `target` data type can't support the
additional information.

In this case you will need to cast the `datetime` into a simpler `datetime` object.
