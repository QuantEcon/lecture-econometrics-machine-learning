(stata/setup-python-in-stata)=
# Setup Python in Stata

:::{margin}
Stata16 [has been updated for use on Apple Silicon based Macs](https://blog.stata.com/2020/11/10/stata-for-mac-with-apple-silicon/) but older versions will run through translation instead of native support.
:::

```{admonition} Assumptions
This lecture presumes you have already installed `Stata16` on your computer and you are already
proficient with using `stata`
```

```{warning}
Some Universities install `stata` over the network as university provided software.
This can cause issues relating to permissions when installing new softare. If this occurs
you may need to contact your IT department.
```

Integration between computer software is always a tricky problem to solve and typically requires
some investment in setting up the integrations properly.

In this lecture we will focus on setting up `python` in `stata` and getting access to your configuration.

Having good knowledge of how your system is configured can great assist in reducing bugs and issues related
to software problems and environments.

:::{margin}
This workflow has been put together on `macOS`. While the `stata` application is pretty consistent
across platforms such as `Windows`, please open any issues you come across [here](https://github.com/QuantEcon/lecture-econometrics-machine-learning/issues)
:::

Open up the `Stata` application on your computer

```{figure} img/stata-open.png
```

## Checking your Configuration

To check your configuration you can type

```stata
python query
```

in the command window which will provide the following details:

```{figure} img/stata-python-query.png
```

the `output` provides useful information about how `stata` and `python`
are linked together.

```{list-table}
:widths: 15 25
:header-rows: 1

* - Field
  - Description
* - `python_exec`
  - the location on your computer for the `python` interpreter you are using in `stata`
* - `python_userpath`
  - the location for any custom `python` code that you would like added to the python `sys.path`
* - `python system information`
  - this provides additional information about the `python` version and software used.
```

You can also see that `python` hasn't been initialised as we haven't used it in this lecture.

## Searching for Python on your System

Stata can search your system for any `python` installations and list them by typing

```stata
python search
```

in the command window.

```{figure} img/stata-python-search.png
```

:::{note}
If `python` is not yet configured you will see:

```stata
. python search

no Python installation found; minimum version required is 2.7.
r(111)
```

this will require you to install a python environment such as [anaconda](https://python-programming.quantecon.org/getting_started.html#anaconda)
:::

## Setting the python distribution

Linking `stata` to a specific `python` installation (such as `anaconda`) can be done
using the `set python_exec` command such as:

:::{tabbed} macOS
```stata
set python_exec /Users/<user>/anaconda3/bin/python
```
:::

:::{tabbed} Windows
```stata
set python_exec C:\Users\<users>\anaconda3\python.exe
```
:::

:::{warning}
If you have already started a python session in `stata` you will need to quit stata
and reopen it before using `set python_exec`
:::

This can be used together with `python search` to know which path to provide.

You can then check the setting has taken effect using `python query`.

## Updating your `sys.path` in `python`

`python` uses `sys.path` to specify the search path for looking up
`python packages` and other utilities and programs.

You can add a custom path for the python `stata` environment using `set python_userpath`

:::{tabbed} macOS
```stata
set python_userpath /Users/<user>/mypythoncode
```
:::

:::{tabbed} Windows
```stata
set python_userpath C:\Users\<users>\mypythoncode
```
:::

Then check the setting has taken effect using `python query`.

## Testing Python

:::{margin}
```{admonition} macOS + Anaconda Issue
I ran into [this issue](https://www.statalist.org/forums/forum/general-stata-discussion/general/1578573-python-integration-pandas-package-causing-stata-to-close) on my `macOS` installation
of Stata and found the suggestion solution was required to prevent this behavior
```
:::

To check that everything is setup and ready to go you can run the
[first python example](stata/python-interactive) and verify
everything is working.