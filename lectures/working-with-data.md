# Working with Data

## JSON

[Javascript Object Notation (JSON)](https://www.json.org/json-en.html)
is a lightweight data interchange format that is commonly used
to transfer data between systems that strikes a balance between `human` readability
and simple for `machines` to parse and generate.

Despite its name it is programming language agnostic and can be read by
a large range of programming languages and systems.

It is commonly used by datasets and online API's to provide access to metadata, such as
variables and associated information when working with online datasets.

```{note}
JSON is a text-based format.
```

### Basic JSON

An example JSON string:

```{literalinclude} _examples/json/basic-example.json
```

From a `python` perspective this is equivalent to a dictionary (or `dict` object):

```ipython
In [1]: import json
In [2]: f = open("basic-example.json", "r")
In [3]: a = json.load(f)
In [4]: f.close()
```

When reading the json data in using [json library](https://docs.python.org/3/library/json.html)
the object will be returned as a `dict`

```ipython
In [5]: a
Out[5]: {'firstname': 'Harry', 'lastname': 'Smith', 'age': 42}
```

where each piece of data is associated with a key.

A really useful property of this data format is the notion of `hierarchy` and `nestedness`.

Perhaps you want to extend your data format to be more general and would like to introduce
concept of more than 1 person in your program. This can be done by simply grouping data into
grouped objects such as an identifier such as a `tax number` (or some other unique identifier):

```{literalinclude} _examples/json/basic-example-2.json
```

Once the above data is loaded you can then retrieve a python `dict` that contains all the information
about tax payer with the id `9172832`.

This enables a large range of `schema` to be defined to move data between systems.


### JSON as a Data Interchange Format

We will use the [American Community Survey](https://www.census.gov/data/developers/data-sets/acs-5year.html) published by the U.S. Census Bureau to compute average household income at the census tract level.

```{note}
You will need to register for a US Census API Key for this code to work
```



```{exercise}
Use the techniques above to compute the average household income by gender.
```


```{seealso}
There are also a number of python wrappers that have been written that makes working with
Census ACS easier that interfacing directly with the API such as [datamade/census](https://github.com/datamade/census).
These wrapper packages can be a convenient way to fetch the data you need more
easily, however they have their limits and sometimes you can't always achieve what you need
with them.
```

### JSON as a Document

If you use [jupyter notebooks](https://jupyter.org) they are actually documents based on `json` which is
passed through `jupyter` kernels to engage with underlying programming languages.

Take the following simple notebook:

```{figure} _notebooks/simple-notebook.png
```

This document is represented by a collection of elements that are defined
by the `jupyter notebook` specification and enables `jupyter clients` to talk with the underlying
`jupyter` system.

The document structure consists of `cells` and `metadata` that enables `jupyter` to connect the 
document to the correct `jupyter kernel` and programming language.

A simple `jupyter notebook` document looks like:

```json
{
 "cells": [],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
```

Where the first cell is a `markdown` cell that contains the markdown text

```json
{
  "cells": [
   "cell_type": "markdown",
   "id": "41f18377",
   "metadata": {},
   "source": [
    "# Title"
   ]
  ]
}
```

the second cell is a `code-cell`

```json
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1a955059",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  }
 ]
}
```

Each `cell_type` includes context specific metadata such as `execution_count` that saves
all of the necessary information for the `jupyter notebook` to render in your web browser.



