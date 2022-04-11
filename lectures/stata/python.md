(stata/python)=
# Stata and Python

One of the major new features supported since [Stata16](https://www.stata.com/stata-news/news34-3/),
and improved greatly in [Stata17](https://www.stata.com/stata-news/news36-2/),
is the addition of [python integration](https://www.stata.com/new-in-stata/python-integration/).

These pages are intended to be a guide for `stata` users that would like to use
`python` as part of their `data` and `analysis` workflows. 

This gives you access to many powerful tools that are available in the `python` ecosystem, 
in addition to alternative data preparation tools such as `pandas` which may be preferred
once you learn `python` programming.

:::{margin}
In [Stata17](https://www.stata.com/stata-news/news36-2/) StataCorp introduced a
`python` module called `pystata` which brings much tighter integration between the two
software environments. This includes the implementation of a `jupyter` kernel for use
in `jupyter notebooks` or `jupyterlab` environments.
:::

There are `two` primary ways we can use `python` effectively with `stata`:

1. [Using **stata** from **python** (Stata17)](stata/stata-from-python)
2. [Using **python** from **stata** (Stata16)](stata/python-from-stata)

```{note}
It is also possible to use `python` and `stata` together as independant tools by
using file based workflows. This can be a productive workflow strategy and is
covered in [Using **stata** with **python** (via file based workflows)](stata/python-files)
```

## Stata Resources

1. [Stata Manual](https://www.stata.com/manuals/ppython.pdf)
2. [Stata Blog Posts](https://blog.stata.com/category/programming/)


