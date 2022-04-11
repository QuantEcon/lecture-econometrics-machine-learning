(stata/setup-stata-in-python)=
# Setup Stata in Python

Since `Stata17` the recommended way to access `stata` from `python` is through
the official python package [pystata](https://www.stata.com/python/pystata/).

## [pystata](https://www.stata.com/python/pystata/)

The [pystata](https://www.stata.com/python/pystata/) Python package, written
and maintained by StataCorp, enables python programs to call stata from
within the Python context.

The requirements to use `pystata` are:

1. Stata 17 or later versions
2. Python 2.7 or 3.4+

### Installation

The easiest way to install the [pystata](https://www.stata.com/python/pystata/) package
is to use `pip`

```bash
pip install stata_setup
```

to ensure you get the latest version you can add `--upgrade`

```bash
pip install --upgrade stata_setup
```

This installs a package called `stata_setup`.

```{note}
This package is essentially a setup utility, which provides the
linking fabric to connect Python with stata17+ and locates
the pystata software bundeled with `stata`.
```

Once this package is installed you will need to run it to link `python` with
the installed `stata` application. For example if you want to link to an
installed version of `Stata17 SE` you need to know where the application
is installed on your computer. The below offer the default locations for
various operating systems.

:::{tabbed} Mac OS X
```python
import stata_setup
stata_setup.config("/Applications/Stata", "se")
```
:::

:::{tabbed} Windows 
```python
import stata_setup
stata_setup.config("C:/Program Files/Stata17", "se")
```
:::

:::{tabbed} Linux 
```python
import stata_setup
stata_setup.config("/usr/local/stata17", "se")
```
:::

Once you have linked the `stata` application successfully you will see 
the `stata` terminal output

```{figure} img/pystata-setup-python.png
```

## Other Jupyter Integrations

```{tip}
Since the release of `Stata17` it is recommended to use the official
integration through `pystata`.
```

There are two other noteworthy approaches to using `stata` with `jupyter`:

1. [Stata Jupyter Kernel](https://github.com/kylebarron/stata_kernel)
2. [IPyStata](https://github.com/TiesdeKok/ipystata)

which have different approaches to supporting `stata` in the `jupyter` context

### Stata Jupyter Kernel

:::{margin}
There is also [excellent documentation](https://kylebarron.dev/stata_kernel/)
available.
:::

The [Stata Jupyter Kernel](https://github.com/kylebarron/stata_kernel)
enables using `stata` directly in `jupyter` notebooks.

It is effectively an alternative interface to use `stata` if you like
`jupyter` as an interface.

This can be useful if you want to write notebooks that are `integrated`
with `stata` code.

It supports a [wide range of interaction with `stata`](https://kylebarron.dev/stata_kernel/#stata_kernel-features)

To install using `anaconda` tools you can use the following commands
in a `jupyter notebook`:

:::{margin}
```{tip}
It is important to specify `-y` when issuing install requests via
`conda` as there is no way to accept the user requested `y` input
to proceed with install. `pip` doesn't have this issue as it doesn't
request user input.
:::

```bash
!conda install -y -c conda-forge stata_kernel
```

once the software is installed you need to install the `jupyter kernel`
on your computer

```bash
!python -m stata_kernel.install
```

:::{warning}
**[macOS]** When I ran the kernel install step I got the following `error`:

```bash
Cannot import kernel
Installing Jupyter kernel spec
WARNING: Could not find Stata path.
Refer to the documentation to see how to set it manually:

https://kylebarron.dev/stata_kernel/using_stata_kernel/configuration
```

and had to manually set the `stata` path in the `.stata_kernel.conf` file located
in your home directory to the following:

```bash
# Path to stata executable. If you type this in your terminal, it should
# start the Stata console
stata_path = /Applications/Stata/StataIC.app/Contents/MacOS/StataIC

# **macOS only**
# The manner in which the kernel connects to Stata. Either 'console' or
# 'automation'. 'console' is the default because it allows multiple
# independent sessions of Stata at the same time.
execution_mode = automation
```

Unfortunately `StataIC` is limited on `mac os` so I had to use `automation`
instead of `console` as per
[this issue in the docs](https://kylebarron.dev/stata_kernel/using_stata_kernel/configuration/)
However this does enable the use of `browse`
:::

If you start `jupyter notebook` you should now see a `stata` kernel option. If selected a `jupyter`
notebook will open with a connection to `stata`. You can verify this on the top-right of the 
notebook

```{figure} img/jupyter-stata-kernel.png
```

#### Demo Notebook

You can download the {download}`notebook from here <notebooks/stata-jupyter-kernel.ipynb>`

Then browse to your download location and load the notebook with **jupyter**:

```bash
cd ~/Downloads
jupyter notebook stata-jupyter-kernel.ipynb
```

### IPyStata

[IPyStata](https://github.com/TiesdeKok/ipystata) provides an alternative
approach which provides support for running `stata` commands using `ipython magics`.

So you remain in a `python` notebook and interface with stata when needed.

:::{margin}
There is a [nice presentation](http://fmwww.bc.edu/repec/chic2016/chicago16_dekok.pdf)
that runs through this integration.
:::

To install you can use `pip`:

```bash
pip install ipystata
```

:::{margin}
The `PyPI` release is from [17th March 2017](https://pypi.org/project/ipystata/#history)

This is a bit of a red flag in my view as releases are best distributed via PyPI.
However for tired open-source contributors this can be one short-cut taken to reduce workload.
:::

however the `released version` via `PyPI` is a lot older than the `master` branch of the code repository
so to get the latest you could install using:

```bash
pip install git+https://github.com/TiesdeKok/ipystata
```

The [documentation](https://nbviewer.jupyter.org/github/TiesdeKok/ipystata/blob/master/ipystata/Example.ipynb)
largely consists of a demo notebook and the [README](https://github.com/TiesdeKok/ipystata/blob/master/README.md).

#### Setup

To setup the package you then need to configure it to know where `stata` is on your computer.

Open a `Jupyter` notebook that is attached to the `python` kernel.

```python
import ipystata
from ipystata.config import config_stata
config_stata("<path-to-stata>")
```

This will look something like:

:::{tabbed} macOS
```python
config_stata("/Applications/Stata/StataSE.app/Contents/MacOS/stataSE")
```
:::

:::{tabbed} Windows
```python
config_stata("C:\Program Files (x86)\Stata14\StataSE-64.exe")
```

:::

This is documented [here](https://github.com/TiesdeKok/ipystata#set-installation-directory-for-stata)

#### Demo Notebook

You can download the {download}`notebook from here <notebooks/jupyter-ipystata.ipynb>`

Then browse to your download location and load the notebook with **jupyter**:

```bash
cd ~/Downloads
jupyter notebook jupyter-ipystata.ipynb
```