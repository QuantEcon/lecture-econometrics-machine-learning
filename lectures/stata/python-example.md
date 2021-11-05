(stata/python-example)=
# A Common Workflow

In this session we take a look at a typical `workflow` that I find
to be a pretty common.

```{note}
This example could be done pretty easily all within `stata` but this
workflow pattern is pretty common when starting to use `python` to build your
datasets.

However if you have built up resources in `stata` you may be more interested in using
data that you have already compiled in `stata` and you want to explore some `machine learning`
in `python`.
```

## Exploring Data in Jupyter

The work often starts by finding and exploring data in `jupyter` notebooks as in the below
demonstration notebook.

### Local Notebook Option

You can download the {download}`notebook from here <notebooks/gravity-model-example.ipynb>`

You can get the {download}`data files here <notebooks/data/data.zip>`

Then browse to your download location and load **jupyter**:

```bash
jupyter notebook gravity-model-example.ipynb
```

the data files need to be located in a `data` folder in the same directory as the notebook

### Cloud Based Option

You can [launch the notebook](https://mybinder.org/v2/gh/QuantEcon/2021-workshop-rsit/main?filepath=notebooks%2Fsession7%2Fgravity-model-example.ipynb)

```{warning}
Most of this notebook will work except the `stata` calls via `ipystata`
```

## (Optional) Saving the Exploration as a Script

You can then distill the needed steps to build a `dataset` formula as a script

You can download a {download}`example python script <notebooks/gravity-model-example.py>`

```{note}
This is a particularly useful step if your data needs to be updated in the future
```

## Using the Dataset in Stata

You can then open `stata` and continue on with your `statistical analysis`

```{figure} img/stata-import-and-regress.png
```




