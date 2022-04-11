(stata/python-from-stata)=
# Using Python from Stata

:::{margin}
The [stata manual](https://www.stata.com/manuals/ppython.pdf) has a section
on the `python` command.

This [blog post](https://blog.stata.com/2020/08/25/stata-python-integration-part-2-three-ways-to-use-python-in-stata/)
does a really good job of explaining the different methods for using `python` in `stata`.
:::

```{tip}
It is always a good idea to check your `python` configuration before proceeding.
This can be done in [](stata/setup-python-in-stata)
```

There are `three` primary interfaces to running `python` within `stata`:

1. [](stata/python-interactive)
2. [](stata/python-do)
3. [](stata/python-scripts)

We will then look at how to transfer data between `python` and `stata`
in both directions through the `stata function interface`.

(stata/python-interactive)=
## Running `python` Interactively with a First Example

You can run `python` interactively within `stata` in a manner that is the
equivalent of running the `python` REPL program through a terminal.

This is activated by typing `python` in the command window.

```{figure} img/stata-python.png
```

You are now interfacing directly with the `python` interpreter as indicated in
the `Result` window.

You can now write `python code` such as:

```python
print("Hello World!")
```

```{figure} img/stata-python-hello-world.png
```

once you hit enter `stata` sends the code snippet to the python interpreter
for processing and shows the result

```{figure} img/stata-python-hello-world-result.png
```

:::{margin}
```{note}
For `python` users the use of `end` takes some getting used to as the usual
way to exit the `python` REPL is using the `exit()` function. Stata uses `end`
across its ecosystem and is consistent with `stata`.
```
:::

To stop interfacing with the `python` interpreter you need to type `end` in
the command window

```{figure} img/stata-python-hello-world-end.png
```

this will return you to the standard `stata` interface.

:::{tip}
If you have a one line `python` command you can use
```stata
python: print("Hello World!")
```
which will pass the code to `python`, display the results
directly below in the `Results` window, and return you to
the `stata` command environment.

```{figure} img/stata-python-hello-world-oneline.png
```
:::

(stata/python-do)=
## Running `python` in a `do` file

Another option for running `python` code is through the `do` file.

Let's open the `do` file editor and add:

:::{margin}
This can be {download}`downloaded from here as a do file <do/example1.do>`
:::

```stata
di "Stata Here"
python: print("Python Here")
```

```{figure} img/stata-example1-do.png
```

and when you click on the `Do` button you get the result:

```{figure} img/stata-example1-do-run.png
```

where the results from `python` are displayed similarly to `stata` output.

However, most of the time you will want to add in a **block of code** such as:

```python
for i in range(0,2):
    print("Python Here")
```

This can be done by delimiting the `python code` within the `do` file using either

```stata
python
<python code>
end
```

or

```stata
python:
<python code>
end
```

The difference between these two `delimiters` is in how `stata` handles any
errors in `python`.

The `python` delimiter will continue to execute the rest
of the `python` code if an error is encountered, while the `python:` delimiter will **immediately**
return control to `stata` once the error is encountered.

:::{margin}
We have made an error by incorrectly spelling the `range` function.

This can be {download}`downloaded from here as a do file <do/example2a.do>`
:::

```stata
di "Stata Here"
python
for i in rang(2):
   print("Python Here")
print("Python Done")
end
di "Back in Stata Land!"
```

```{figure} img/stata-example2a-do-error.png
```

As you can see `stata` has continued to execute code past the point at which there is
an error.

However if you use `python:` the execution will halt at the point of the `error`.

:::{margin}
This can be {download}`downloaded from here as a do file <do/example2b.do>`
:::

```stata
di "Stata Here"
python:
for i in rang(2):
   print("Python Here")
print("Python Done")
end
di "Back in Stata Land!"
```

```{figure} img/stata-example2b-do-error.png
```

```{tip}
I tend to use `python:` as I prefer to get to the error quickly to fix the problem
without any distracting output below it. Also in a long running program you will want
to fix the issue prior to the rest of the program executing.
```

We can use the error message to fix the issue now and run the fixed `do` file

:::{margin}
This can be {download}`downloaded from here as a do file <do/example2c.do>`
:::

```stata
di "Stata Here"
python:
for i in range(2):
   print("Python Here")
print("Python Done")
end
di "Back in Stata Land!"
```

```{figure} img/stata-example2c-do-run.png
```

### The Do File Editor and White Space

```{admonition} Reminder
Whitespace is used by `python` to declare `scopes` and is an integral part
of the language definition
```

The `do` file editor doesn't provide you with full `text editor` support when writing
`python` code in the `do` file editor.

For example if you type:

```stata
python:
for i in range(10):
|<curser placed here>
```

the `editor` will **not** automatically indent your code.

However once you have set the
curser to the correct indentation level it will retain that indentation level for
subsequent lines.

```stata
python:
for i in range(10):
    |
    |<curser placed here>
```

So you need to be careful with `whitespace`

Also what you type in the `delimiters` is directly passed to `python`
so you can't indent these `code-blocks` such as:

```stata
di "Stata Here"
python:
    print("Python Here")
```

`python` will return the following error:

```{figure} img/stata-do-whitespace-error.png
```

(stata/python-scripts)=
## Running `python` scripts in `stata`

A third option is to run a `python script` that contains some `python code`

If you save the following code in a file `example3.py`:

:::{margin}
This can be {download}`downloaded from here as a py file <do/example3.py>`
:::

```python
print("Python Here")
for i in range(2):
    print(f"{i} times hello")
print("I'm outta here")
```

you can then run this script in `stata` using:

:::{margin}
```{tip}
You will need to update you `working directory` before running the
python script
```
:::

```stata
python script example.py
```

with the output:

```{figure} img/stata-python-script-example.png
```

```{tip}
This can be a very useful way to run `python` code as it leaves you
to write `python` code in any text editor you like such as
[vscode](https://code.visualstudio.com).
```

## Interacting between `Stata` and `Python`

```{tip}
In many cases it can be simpler to keep `python` and `stata`
workflows independent of each other and use `files` to transfer
data between them.

This is covered in [](stata/python-files)
```

So far the `python` and `stata` runtime environments have been
independent of each other to learn about how to run `python` code
within `stata` (i.e. they haven't shared any data)

For many applications we want some level of `interaction` between `stata`
and `python` by copying back and forth objects between the different runtime
environments.

`Stata` makes various components of its internals available to `python` via
the [stata function interface (sfi)](stata/python-sfi)
to enable such interaction with:

1. [Dataset](https://www.stata.com/python/api16/Data.html) which connects `python` with the current
   in memory `stata` dataset
2. [Macros](https://www.stata.com/python/api16/Macro.html) which connects `python` with `stata`
   macros

In addition it also provides access to [many other `stata` components](stata/python-sfi).

### Copying Data from Stata to Python

```{admonition} Stata Blog Post
This section is heavily inspired by [this excellent stata blog post](https://blog.stata.com/2020/11/05/stata-python-integration-part-8-using-the-stata-function-interface-to-copy-data-from-stata-to-python/)
```

```stata
sysuse auto
list foreign
```

Listing the `foreign` data in `stata` shows

```{figure} img/stata-sysuse-auto-list-foreign.png
```

We can then use `sfi.Data` to transfer the `raw` data to `python` using the `.get` method
of the `Data` object from the `stata function interface` package.

```stata
python
from sfi import Data
dataraw = Data.get('foreign')
dataraw
end
```

and it looks like

```{figure} img/stata-sysuse-auto-python-raw.png
```

Notice that the `data` looks different.

```{note}
`stata` has a concept of `labels`
```

If you use the `data explorer` you will see that the `foreign` variable consists of
`0,1` that are associated with labels `domestic` and `foreign` (respectively).

```{figure} img/stata-sysuse-auto-dataviewier-foreign.png
```

We may want to get more information about the `get` method so the best place
to look is the [documentation on sfi.Data](https://www.stata.com/python/api16/Data.html).
Then you can click on the [get method](https://www.stata.com/python/api16/Data.html#sfi.Data.get)

```{tip}
You **can't** use the `ipython` features such as `Data.get?` in this context because
`python` is interfacing directly with the `python` interpreter and not the
`ipython` interpreter (such as when you're using `jupyter`)
```

That page looks like:

```{figure} img/stata-docs-sfi-data-get.png
```

You can see that an option is to fetch the `value label` using `valuelabel=True`

```stata
python
from sfi import Data
dataraw = Data.get('foreign', valuelabel=True)
dataraw
end
```

and the `raw data` is now returned as strings taking the value of the `labels` that
have been applied to the data

```{figure} img/stata-sysuse-auto-foreign-valuelabels.png
```

#### Obtaining more variables at once

You can obtain more variables using the `get` method. Based on the documentation you can use
the following methods to specify what variables to fetch:

```
var (int, str, or list-like, optional) – Variables to access.
It can be specified as a single variable index or name, or an
iterable of variable indices or names. If var is not specified,
all the variables are specified.
```

In addition you can also specify which observations (`obs`) you would like:

```
obs (int or list-like, optional) – Observations to access.
It can be specified as a single observation index or an iterable
of observation indices. If obs is not specified, all the
observations are specified.
```

So let's use this information and run

```stata
python
from sfi import Data
dataraw = Data.get('foreign mpg rep78', range(45,56))
dataraw
end
```

this code saves a `list of list` type object into the `python` object `dataraw`

```{figure} img/stata-sysuse-auto-3vars-range.png
```

The data is written as a list of `rows`/`obs` in the order that the variables are requested,
which in this case is: `foreign mpg rep78` such as the first element:

```python
[[0, 18, 2], ...
```

:::{margin}
```{note}
`range` is a `python` object that behaves like a list when constructing `ranges`.
```
:::

The `range(45,56)` request will fetch observations `46` to `56` as shown in the `data` browser

:::{margin}
```{note}
The stata `data viewer` is indexed by `1` while `python` is indexed by `0`
```
:::

```{figure} img/stata-sysuse-auto-dataviewer-range.png
```

As per the `documentation` you can also specify a `list-like` object instead of a string separated
by a space such as `['foreign', 'mpg', 'rep78']`:

```stata
python
from sfi import Data
dataraw = Data.get(['foreign', 'mpg', 'rep78'], range(45,56))
dataraw
end
```

which will return the same data

```{figure} img/stata-sysuse-auto-3vars-range-list.png
```

```{exercise}
What happens now if you specify `valuelabel=True` for the above `python`
code?
```

:::{margin}
Current `Stata` support is for moving `raw data` to the python context. It is left
to the user to push that raw data into some other object such as `pd.DataFrame`
or `pd.Series`.

I hope support for `pd.DataFrame` will be coming in a future release.
:::

#### pd.DataFrame and pd.Series:

The discussion so far has focused on fetching `raw data` out of `stata` and copying
it to the `python` environment. But in many applications we are likely to want higher
productivity objects such as pandas `DataFrame` and `Series`.

Let's try

```stata
python
from sfi import Data
import pandas as pd
dataraw = Data.get('foreign mpg rep78', range(45,56))
df = pd.DataFrame(dataraw)
df
end
```

You will notice that the `raw data` has now been placed in a `pd.DataFrame`
but `columns` and `index` variables haven't come across:

```{figure} img/stata-sysuse-auto-3vars-range-dataframe.png
```

You may want to parameterize your requests so you can use them in both
the `sfi.Data.get` method in addition to a `pd.DataFrame` method when
converting the `raw data` into a `pd.DataFrame`

You can save the variable selection as a python variable:

```python
vars = ['foreign', 'mpg', 'rep78']
```

then you can use these variables for both `stata` and `python`

:::{margin}
I have used:

1. `range(45,56)` for `stata`, and
2. `range(46,57)` for `pandas`

to harmonise given data in `stata data editor` is indexed by `1`.

It would be nice if `stata` provides `sfi.Data.dataframe` that can help manage these
indexing issues.

```{note}
Most of the time you will not need to harmonise like this as you will
just use the data that has been selected.
```
:::

```stata
python
from sfi import Data
import pandas as pd
vars = ['foreign', 'mpg', 'rep78']
dataraw = Data.get(vars, range(45,56), valuelabel=True)
df = pd.DataFrame(dataraw, index=range(46,57), columns=vars)
df
end
```

which provides a much more consistent `pd.DataFrame` and lines up closely with
the stata context.

```{figure} img/stata-sysuse-auto-3vars-range-dataframe2.png
```

You can compare with stata using in the `command window`

```stata
list foreign mpg rep78 in 46/56
```


```{exercise}
How can you explain the value for the variable `rep78` for observation `51`?
```

:::{note}
There is also a method available `sfi.Data.getAsDict()` that includes the
variable names in a returned dictionary so you can use:

```stata
python
from sfi import Data
import pandas as pd
vars = ['foreign', 'mpg', 'rep78']
dataraw = Data.getAsDict(vars, range(45,56), valuelabel=True)
df = pd.DataFrame(dataraw)
df
end
```
:::

#### Missing Values:

Missing values in `stata` are internally represented by the `largest` value for
each type. 

Within `stata` you typically work with missing values using `.`  such as:

```stata
list rep78 if rep78 != .
```

and much of this detail is taken care of for you.

AS missing values are represented by the `maximum value`:

:::{margin}
This table is from the [stata manual](https://www.stata.com/manuals/u12.pdf#u12.2.2Numericstoragetypes)
:::

```{figure} img/stata-numeric-types-table.png
```

:::{margin}
I am **not** sure why `python` receives the missing value for a `double` numeric type when
`rep78` is coded as an `int` in `stata`. I will need to ask `statacorp`.
:::

`python` will interpret this data as an actual value.

You will want to specify `missingval=np.nan`

```stata
python
from sfi import Data
import numpy as np
import pandas as pd
vars = ['foreign', 'mpg', 'rep78']
dataraw = Data.get(vars, range(45,56), valuelabel=True, missingval=np.nan)
df = pd.DataFrame(dataraw, index=range(46,57), columns=vars)
df
end
```

which returns the following

```{figure} img/stata-sysuse-auto-3vars-range-dataframe3.png
```

### Copying Data from Python to Stata

```{admonition} Stata Blog Post
This section is heavily inspired by [this excellent stata blog post](https://blog.stata.com/2020/11/19/stata-python-integration-part-9-using-the-stata-function-interface-to-copy-data-from-python-to-stata/)
```

It is often the case you will want to do some data work in `python` and have a need to
transfer it to `stata` to do some statistical anaylsis.

The `sfi.Data` interface also contains methods for saving data from `python` into
the default `stata dataframe` (or a `frame` which is new in `Stata16`)

Let us fetch some data from Yahoo Finance using the `yfinance` package in `python`

```stata
python:
import yfinance as yf
dowjones = yf.Ticker("^DJI")
data = dowjones.history(start="2010-01-01", end="2020-12-31")[['Close', 'Volume']]
data
end
```

the `yfinance` package has returned the `dowjones` history tables containing data
between `2010-01-01` and `2020-12-31`

```{figure} img/stata-yfinance-data.png
```

Now we need to migrate that data from `python` into `stata`

```stata
python:
from sfi import Data
Data.setObsTotal(len(data))
end
```

the `stata` data editor now contains space for `len(data)` observations to
be transferred.

```{figure} img/stata-dataeditor-sfi-setObsTotal.png
```

You can then setup `3` variables in stata to save `date`, `close`,
and `volume` information across.

```stata
python:
Data.addVarStr("date", 10)  # Str10
Data.addVarDouble("close")  # Double
Data.addVarInt("volume")    # Int
end
```

the `stata` data editor now contains `3` variables

```{figure} img/stata-dataeditor-sfi-addvar.png
```

:::{warning}
You should start this work with an empty `stata` dataset. The `sfi.Data`
package can return some `cryptic` errors. When trying to create a `date`
Str variable using the code above you will get the following error if the
variable already exists in the dataset.

```python
>>> Data.addVarStr("date", 10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Applications/Stata/ado/base/py/sfi.py", line 487, in addVarStr
    return _stp._st_addvarstr(name, length)
SystemError: failed to add a variable of type str to the current Stata dataset
r(7102);
```

Clearing can be done in stata using

```stata
clear
```
:::

The next step is to migrate the actual data.

You might try saving the `data` directly from the `pandas` dataframe into the `stata` dataset using the
[sfi.Data.store()](https://www.stata.com/python/api16/Data.html#sfi.Data.store) method.

:::{Note}
This method interface is expecting

```
static store(var, obs, val, selectvar=None)
```

where,
1. `var`, `obs`, and `val` are `python arguments`, and
2. `selectvar=None` is a `python keyword argument` with a default value of `None`

This means that `var`, `obs`, and `val` are **required inputs**

This deviates from [sfi.Data.get()](https://www.stata.com/python/api16/Data.html#sfi.Data.get)
:::

```stata
python
Data.store("date", None, data.index)
end
```

however you will run into trouble with the following error:

```{figure} img/stata-yfinance-data-save-data.png
```

`Stata` is similar to `numpy` in that it is very specific about how it saves `data` in memory in
accordance with specified `types`.

In the code above we tried to send through a list of `datetime` objects from
`pandas` and the `stata function interface` doesn't know how to represent
this data in the `stata dataset`.

```stata
python
data.index
data.index[0]
end
```

As you can see the index from the pandas dataframe `data` consists of `Timestamp` objects:

```{figure} img/stata-yfinance-data-index-dateobjects.png
```

Therefore some translation is required in this case to convert `dates` into a `format` that `stata`
can copy into its dataset and then use `stata` tools to convert to `stata` dates.

We know `stata` has a `date` function that we can use:

:::{margin}
```{warning}
If you run this stata script you will `clear` the `stata` dataset so you would
need to start from the begining to bring back in the `yfinance` data via `python`
```
:::

```stata
clear
gen stringdates = ""
set obs 1
replace stringdates = "2010-01-04" in 1
gen date = date(stringdates, "YMD")
list
format %tdCCYY-NN-DD date
list
```

```{figure} img/stata-working-with-date.png
```

So now we can look to convert the `pandas.Timestamp` objects to be represented as simpler `string`
based data that contain the information needed for `stata` to convert those `dates`.

Pandas has a useful method `.astype()` for useful data conversions.

```stata
python
data.index = data.index.astype(str)
data.index[0]
end
```

```{figure} img/stata-python-df-astype(str).png
```

this has used the `in-built` type converter to represent the `index` as `strings`
that is formatted as `YYYY-MM-DD`

Now lets try and save this information into the `stata` dataset:

```
python
Data.store("date", None, data.index)
end
```

You can now open the `data viewer` and see that the dates (as strings) has been copied
over to `stata`:

```{figure} img/stata-dataeditor-sfi-store1.png
```

Let's bring in the numerical data, which is a much simpler process

```
python
Data.store("close", None, data.Close)
Data.store("volume", None, data.Volume)
end
```

We now have the data we need in the `stata` dataset as seen in the `data editor`

```{figure} img/stata-dataeditor-sfi-store2.png
```

Now that the data is copied across we can switch back to `stata` to run
any `analysis` or construct a `plot`

We will first want to convert those dates in `stata` as a post transfer step

```stata
gen sdate = date(date, "YMD")
format %tdCCYY-NN-DD sdate
```

and we can check the conversion in the stata `data editor`

```{figure} img/stata-dataeditor-sfi-store3.png
```

and then we can construct the `plot` as demonstrated in the [original blog post](https://blog.stata.com/2020/11/19/stata-python-integration-part-9-using-the-stata-function-interface-to-copy-data-from-python-to-stata/)

```stata
replace volume = volume / 1000000
twoway (line close sdate, lcolor(green) lwidth(medium))           ///
       (bar volume sdate, fcolor(blue) lcolor(blue) yaxis(2)),    ///
       title("Dow Jones Industrial Average (2010 - 2019)")        ///
       xtitle("") ytitle("") ytitle("", axis(2))                  ///
       xlabel(, labsize(small) angle(horizontal))                 ///
       ylabel(5000(5000)30000,                                    ///
              labsize(small) labcolor(green)                      ///
              angle(horizontal) format(%9.0fc))                   ///
       ylabel(0(5)30,                                             ///
              labsize(small) labcolor(blue)                       ///
              angle(horizontal) axis(2))                          ///
       legend(order(1 "Closing Price" 2 "Volume (millions)")      ///
              cols(1) position(10) ring(0))
```

which produces the following `stata` chart

```{figure} img/stata-blog9-example-corrected.png
```

You may be interested in comparing this to a chart built with `matplotlib` and `pandas`
in the `python` environment.

You can {download}`download this notebook <notebooks/stata-blog9-example-matplotlib.ipynb>`,
or [open this notebook in the cloud](https://mybinder.org/v2/gh/QuantEcon/2021-workshop-rsit/main?filepath=notebooks%2Fsession5%2Fstata-blog9-example-matplotlib.ipynb)

which produces the following `matplotlib` figure:

```{figure} img/stata-blog9-example-matplotlib.png
```

### Persistence between `python` code-blocks in `stata`

Once the `python` interpreter is initialised it is used throughout the `stata`
session.

This means that once variables are created in `python` they will be
available in future `python` code-blocks.

```stata
python:
import pandas as pd
df = pd.DataFrame(range(4), index=['a','b','c','d'])
df
end
```

then you can run some other things in `stata` and then return to `python` and fetch
the `df` object

```stata
python:
df
end
```

such as in this short demonstration

```{figure} img/stata-python-persistence.png
```

(stata/python-sfi)=
## The stata function interface `sfi`

The [python api documentation](https://www.stata.com/python/api16/) contains
the details about the `sfi` package from `stata`.

```{list-table}
:widths: 15 25
:header-rows: 1

* - Class
  - Description
* - [Characteristics](https://www.stata.com/python/api16/Characteristic.html)
  - Access `stata` characteristics
* - [Data](https://www.stata.com/python/api16/Data.html)
  - Access to the current `stata` dataset
* - [Datetimes](https://www.stata.com/python/api16/Datetime.html)
  - Access to `stata` datetimes
* - [Frames](https://www.stata.com/python/api16/Frame.html)
  - Access to `stata` Frames
* - [Macros](https://www.stata.com/python/api16/Macro.html)
  - Access to `stata` macros
* - [Mata](https://www.stata.com/python/api16/Mata.html)
  - An interface with global `mata` matrices
* - [Matrix](https://www.stata.com/python/api16/Matrix.html)
  - Access to `stata` matrices
* - [Missing](https://www.stata.com/python/api16/Missing.html)
  - Access to `stata` missing values
* - [Platform](https://www.stata.com/python/api16/Platform.html)
  - Access to `platform` information
* - [Scalars](https://www.stata.com/python/api16/Scalar.html)
  - Access to `stata` scalars
* - [SFIToolkit](https://www.stata.com/python/api16/SFIToolkit.html)
  - a set of `core` tools for interacting with `stata`
* - [StrLConnector](https://www.stata.com/python/api16/StrLConnector.html)
  - Provide access to `stata strL` datatype in `Data` and/or `Frame`
* - [ValueLabel](https://www.stata.com/python/api16/ValueLabel.html)
  - Access to `stata` value labels
```