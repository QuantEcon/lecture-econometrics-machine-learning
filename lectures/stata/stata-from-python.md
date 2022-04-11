(stata/stata-from-python)=
# Using Stata from Python

```{tip}
It is always a good idea to check your `stata` configuration before proceeding.
This can be done in [](stata/setup-stata-in-python)
```

# Jupyter

While stata can be used from any `python` kernel, [jupyter](https://jupyter.org) offers
a convenient interface, particularly when working with data and models, due to its
interactive nature.

If you haven't used [jupyter notebooks](https://jupyter.org) before I recommend you spend
some time familiarizing yourself with them. We will focus much of this page on this
interface choice. [This datacamp tutorial](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook) is a good
starting point.

To start a jupyter notebook server from a terminal:

```bash
jupyter notebook
```

and then to conect to the `stata17+` application you need to run `stata_setup`

```{figure} img/pystata-setup-python.png
```

The `notebook` will then show a familiar printout, which is the same as if you were using `stata`.

You need to keep in mind that you are actually in a python environment. You **cannot** start typing
stata commands and expect them to work. To run **stata** commands you will need to use what are called
IPython magics. IPython stands for Interactive Python and it is the `python` kernel you are using 
by default when you load `jupyter` and connect through to the `python` kernel. The magics are ways to
transform a jupyter notebook cell. 

The `pystata` package provides a number of `IPython` magics

1. {code}`%%stata`
2. {code}`%%mata`

```{tip}
Unless you are an advanced `stata` user you will likely never need to use the `mata` interface. 
The `mata` magic is used to execute `mata` code, which is a `C` like matrix programming language
and is used extensively in writing stata programs and routines.
```

The `%%` indicates that the entire `code` cell will be dispatched to `stata` for execution. 

You can also use `line` based magics such as `%stata` which enables you to execute a single line command.




