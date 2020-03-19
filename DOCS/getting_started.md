Getting Started: A step-by-step tutorial
=============

> **IMPORTANT NOTE: This documentation only applies to GrainSizeTools v3.0+ Please check your script version before using this tutorial. You will be able to reproduce all the results shown in this tutorial using the dataset provided with the script, the file ``data_set.txt``**

## Open and running the script

First of all, make sure you have the latest version of the GrainSizeTools script and a Python scientific distribution installed (see [requirements](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/Requirements.md) for more details). If you are not familiarized with Python, you have two options here: (1) work with the [Spyder](https://www.spyder-ide.org/) integrated development environment (IDE), which is a powerful MATLAB-like scientific IDE optimized for numerical computing and data analysis with Python; or (2) with [Jupyter notebooks](https://jupyter.org/), which is a browser-based environment that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Make your choice and launch it.

![Figure 1. The Python editor and the shell in the Enthought Canopy environment](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/IDEs.png)  *Figure 1. The [Spyder](https://www.spyder-ide.org/) v.4+ integrated development environment (IDE) showing the editor (left), the IPython shell or console (bottom right), and the help window (upper right). This is a MATLAB-like IDE for Python. They also provide a variable explorer, a history log, MATLAB-like cells, code autocompletion, etc.*

If you are in Spyder, open the ``GrainSizeTools_script.py`` file using ```File>Open```. The script will appear in the code editor as shown in figure 1 and then run the script clicking on the "play" green icon in the tool bar (or go to ```Run>Run file``` in the menu bar). If you are using jupyter notebooks, you should run the script as follows:

```python
%run .../GrainSizeTools_script.py  # substitute ...with the file path
```

The following text will appear in the console or below:

```
module plot imported
module averages imported
module stereology imported
module piezometers imported
module template imported

===================================================================================
Welcome to GrainSizeTools script v3.0
===================================================================================
GrainSizeTools is a free open-source cross-platform script to visualize and characterize the grain size in polycrystalline materials and estimate differential stress via paleopizometers.

Get a list of the main methods using: get.function_list()
```



## Reading data with Pandas

[Pandas](https://pandas.pydata.org/about/index.html) is the de facto standard Python library for data analysis and manipulation of table-like datasets (csv, excel or txt files among others). The library includes several tools for reading files and handling of missing data. We strongly recommend its use with the GrainSizeTools script, and when running the GrainSizeTools script pandas is imported as ```pd``` for its general use.

All Pandas methods to read data are all named ```pd.read_*``` where * is the file type. For example:

```python
pd.read_csv()          # read csv or txt files, default delimiter is ','
pd.read_table()        # read general delimited file, default delimiter is '\t' (TAB)
pd.read_excel()        # read excel files
pd.read_html()         # read HTML tables
pd.read_clipboard()    # read text from clipboard (copy-paste)
...
```

For other supported file types see https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html

The only mandatory argument (except in the case of "read_clipboard") is the path to a file or URL.
For example:


```python
# read file and create a Pandas DataFrame (i.e. a table)
dataset = pd.read_table('DATA/data_set.txt')

# show the DataFrame in the console
dataset
```

Pandas' reading methods give you a lot of control over how a file is read. To keep things simple, the most commonly used arguments are listed below:

```python
sep or delimier
# Delimiter to use.
header
# Row number(s) to use as the column names. By default it takes the first row as the column names (header=0). If there is no columns names in the file you must set header=None
skiprows
# Number of lines to skip (int) at the start of the file
na_filter
# Detect missing value markers. False by default.
```

An example might be:

```python
dataset = pd.read_csv('data_set.csv', sep=';', skiprows=5, na_filter=True)
```

To get the path of the file through a file selection dialog instead of writing it, GrainSizeTools has the function ```get_filepath()```. This can be used in two ways:

```python
# store the path in a variable and then use that variable
filepath = get_filepath()
dataset = pd.read_csv(filepath, sep=';')

# or directly within the read method
dataset = pd.read_csv(get_filepath(), sep=';')
```



## Manipulating DataFrames to interact with the script

```python
# visualize the data in the console (in Spyder you can use directly the variable explorer)
dataset
dataset.head()  # show only the first rows
dataset.tail()  # show only the last rows

# select a column
dataset['Area']  # select the column named 'Area'
```

In this case, the dataset imported does no contain the diameters of the grains. Then we can estimate the apparent diameters from the section areas using the equivalent circular diameter formula which is $d = 2 \cdot \sqrt{areas / \pi}$ and store them in a new column. For this, we write in the console:


```python
# Estimate the equivalent circular diameters and store them in a column named 'diameters'
dataset['diameters'] = 2 * np.sqrt(dataset['Area'] / np.pi)
dataset.head()
```

TODO

## Grain size population characterization

TODO

## Visualize the grain size distribution and test lognormality (the plot module)

TODO

## Piezometry

TODO



## Stereology (the stereology module)

TODO