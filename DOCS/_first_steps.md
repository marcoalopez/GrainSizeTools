# Getting started: first steps using the GrainSizeTools script

Installing Python for data science
-------------

GrainSizeTools script requires [Python](https://www.python.org/ ) 3.5+ or higher and the Python scientific libraries [*NumPy*](http://www.numpy.org/ ) [*SciPy*](http://www.scipy.org/ ), [*Pandas*](http://pandas.pydata.org ) and [*Matplotlib*](http://matplotlib.org/ ). If you have no previous experience with Python, I recommend downloading and installing the [Anaconda Python distribution](https://www.anaconda.com/distribution/ ) (Python 3.x version), as it includes all the required the scientific packages (> 5 GB disk space). In case you have a limited space in your hard disk, there is a distribution named [miniconda](http://conda.pydata.org/miniconda.html ) that only installs the Python packages you actually need. For both cases you have versions for Windows, MacOS and Linux.

Anaconda Python Distribution: https://www.anaconda.com/distribution/ 

Miniconda: http://conda.pydata.org/miniconda.html 

Once Anaconda is installed, launch the Anaconda Navigator and you will see that you have installed three different scientific-oriented integrated development systems (IDEs): **Spyder**, **JupyterLab**, and **Jupyter Notebook**. The GrainSizeTools documentation is written assuming that you will carry out the work in one of these IDEs (see next section). 

> 👉 Scope: The GrainSizeTools script is not designed to deal with microscopic images but to analyse and visualize grain size populations and estimate stresses via paleopiezometers. **It is therefore necessary to measure the grain diameters or the sectional areas/volumes of the grains in advance and store them in a txt/csv/excel file**. For this task, we highly encourage you to use the [*ImageJ*](http://rsbweb.nih.gov/ij/) application or one of their different flavours (see [here](http://fiji.sc/ImageJ)). ImageJ-type applications are public-domain image processing programs widely used for scientific research that runs on Windows, macOS, and Linux platforms. The documentation contains a quick tutorial on how to measure the areas of the grain profiles with ImageJ, see *Table of Contents*. The combined use of **ImageJ** and **GrainSizeTools script** is intended to ensure that all data processing steps are done through free and open-source programs/scripts that run under any operating system. If you are dealing with EBSD data instead, we encourage you to use the [MTEX toolbox](https://mtex-toolbox.github.io/) for grain reconstruction (a tutorial on this will be available soon).



## Open and running the script

First of all, make sure you have the latest version of the GrainSizeTools (GST) script. If you are not familiarized with Python, I propose two main options:

1. Use the [Spyder](https://www.spyder-ide.org/) integrated development environment (IDE) (Fig. 1), a MATLAB-like scientific IDE optimized for numerical computing and data analysis with Python. If you are familiar with MATLAB this is the easiest way to go.

2. Use the [JupyterLab or the Notebook](https://jupyter.org/) (Fig. 2), a browser-based environment that allows you to create and share documents that may contain live code, equations, visualizations and narrative text. JupyterLab is just the next generation of the “classic” Jupyter Notebook so you can use either one interchangeably.

Make your choice and launch it from the Anaconda navigator or just by typing ``Spyder`` or ``jupyter lab`` in the terminal.

![Figure 1. The Python editor and the shell in the Enthought Canopy environment](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/IDEs.png)  *Figure 1. The [Spyder](https://www.spyder-ide.org/) v.4+ integrated development environment (IDE) showing the editor (left), the IPython shell or console (bottom right), and the help-variable explorer window (top right). This is a MATLAB-like IDE for Python that provides a variable explorer, a history log, MATLAB-like cells, code auto-completion, etc.*

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/Jupyter_lab.png?raw=true)

*Figure 2. The JupyterLab development environment, a browser-based notebook that allows creating documents that may contain live code, equations (using Latex), visualizations and narrative text*.

In Spyder, open the ``GrainSizeTools_script.py`` file using ```File>Open``` and then run the script clicking on the "play" green icon in the toolbar (or go to ```Run>Run file``` in the menu bar). After running, the following text will appear in the console:

```
module plot imported
module averages imported
module stereology imported
module piezometers imported
module template imported

======================================================================================
Welcome to GrainSizeTools script
======================================================================================
A free open-source cross-platform script to visualize and characterize grain size
population and estimate differential stress via paleopizometers.

Version: v3.0RC0 (2020-04-23)
Documentation: https://marcoalopez.github.io/GrainSizeTools/

Type get.functions_list() to get a list of the main methods
```

Alternatively, if you are using **JupyterLab** or the **Notebook** you have a similar step-by-step tutorial in a notebook format within the ``example_notebook`` folder that comes with the script as well as [online](https://github.com/marcoalopez/GrainSizeTools/blob/master/grain_size_tools/example_notebooks/getting_started.ipynb).



## Get information on the GrainSizeTools methods

As indicated in the welcome message, we can get a list of the main methods by typing in the console:

```python
get.functions_list()
```

![](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/function_list.png)

The script is implemented around several modules. To access a method within a module you will have to type the name of the module and then, separated by a dot, the name of the method. For example to access the method ``qq_plot`` of the plot module you should write

```python
plot.qq_plot()
```
and provide the required parameters within the parenthesis.

To access the methods within a module, type the module name plus the dot and hit the tab key and a complete list of methods will pop up.

#### Get detailed information on methods

You can get detailed information about any method or function of the script in different ways. The first is through the console using the character ? before the method

```python
?conf_interval
```

Another option in Spyder is to get the information interactively without having to call it from the console. To do this, just hit Ctrl+I every time you write a method , all the information will automatically appear in the "Help" window.

## Importing data using the Spyder data importer

Spyder allows importing the data through a graphical interface named the Spyder data importer. To do this, select the variable explorer and then click on the import data icon in the upper left (Fig. 3). A new window will pop up showing different import options (Fig. 4).

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/new_variable_explorer.png?raw=true)

*Figure 3. The variable explorer window in Spyder. Note that the variable explorer label is selected at the bottom (indicated with an arrow). To launch the data importer click on the top left icon (indicated by a circle).*

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/import_data.png?raw=true)

*Figure 4. The two-step process for importing data with the Spyder data importer. At left, the first step where the main options are the (1) the variable name, (2) the type of data to import (set to data), (3) the column separator (set to Tab), and (4) the rows to skip (set to 0 as this assumes that the first row is the column names). At right, the second step where you can preview the data and set the variable type. In this case, choose import as DataFrame, which is the best choice for tabular data.*

Once you hit "Done" (in the bottom right) the dataset will appear in the variable explorer window as shown in figure 3. Note that it provides information about the type of variable (a Dataframe), the number of rows and columns (2661 x 11), and the column names. If you want to get more details or edit something, double-click on this variable and a new window will pop up (Fig. 5). Also, you can do a right-click on this variable and several options will appear.

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/variable_explorer02.png?raw=true)

*Figure 5. Representation of the dataset in the Spyder variable explorer. Note that the colours change with values.*

> 👉 More info on the Spyder variable explorer here: https://docs.spyder-ide.org/variableexplorer.html



## Importing tabular data using the console

An alternative option is to import the data using the console. For this, [Pandas](https://pandas.pydata.org/about/index.html) is the de facto standard Python library for data analysis and manipulation of table-like datasets (CSV, excel or text files among others). The library includes several tools for reading files and handling of missing data and when running the GrainSizeTools script pandas is imported as ```pd``` for its general use.

All Pandas methods to read data are all named ```pd.read_*``` where * is the file type. For example:

```python
pd.read_csv()          # read csv or txt files, default delimiter is ','
pd.read_table()        # read general delimited file, default delimiter is '\t' (TAB)
pd.read_excel()        # read excel files
pd.read_html()         # read HTML tables
# etc.
```

For other supported file types see https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html

The only mandatory argument for the reading methods is to define the path (local or URL) with the location of the file to be imported. For example:


```python
# set the filepath, note that is enclosed in quotation marks
filepath = 'C:/Users/marco/Documents/GitHub/GrainSizeTools/grain_size_tools/DATA/data_set.txt'

# import the data
dataset = pd.read_table(filepath)

#display the data
dataset
```

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/dataframe_output.png?raw=true)

Some important things to note about the code snippet used above are:

- We used the ``pd.read_table()`` method to import the file. By default, this method assumes that the data to import is stored in a text file separated by tabs. Alternatively you can use the ``pd.read_csv()`` method (note that csv means comma-separated values) and set the delimiter to ``'\t'`` as follows: ``pd.read_csv(filepath, sep='\t')``.
- When calling the variable ``dataset`` it returs a visualization of the dataset imported, which is a tabular-like dataset with 2661 entries and 11 columns with different grain properties.

In Python, this type of tabular-like objects are called (Pandas) *DataFrame* and allow a flexible and easy to use data analysis. Just for checking:

```python
# show the variable type
type(dataset)

pandas.core.frame.DataFrame
```

Pandas' reading methods give you a lot of control over how a file is read. To keep things simple, I list the most commonly used arguments:

```python
sep         # Delimiter/separator to use.
header      # Row number(s) to use as the column names. By default it takes the first row as the column names (header=0). If there is no columns names in the file you must set header=None
skiprows    # Number of lines to skip at the start of the file (an integer).
na_filter   # Detect missing value markers. False by default.
sheet_name  # Only for excel files, the excel sheet name either a number or the full name of the sheet.

```

An example using several optional arguments might be:

```python
dataset = pd.read_csv('DATA/data_set.csv', sep=';', skiprows=5, na_filter=True)
```

which in plain language means that we are importing a (fictitious) ``csv`` file named ``data_set`` that is located in the folder ``DATA``. The data is delimited by a semicolon and we ignore the first five lines of the file (*i.e.* column names are supposed to appear in the sixth row). Last, we want all missing values to be handled during the import. 

> 👉 more details on Pandas csv read method: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

The script includes a method named ```get_filepath()``` to get the path of a file through a file selection dialog instead of directly writing it. This can be used in two ways:

```python
# store the path in a variable (here named filepath for convenience) and then use it when calling the read method
filepath = get_filepath()
dataset = pd.read_csv(filepath, sep='\t')

# use get_filepath() directly within the read method
dataset = pd.read_csv(get_filepath(), sep='\t')
```

Lastly, Pandas also allows to directly import tabular data from the clipboard (i.e. data copied using copy-paste commands). For example, after copying the table from a text file, excel spreadsheet or a website using: 

```python
dataset = pd.read_clipboard()
```



## Basic data manipulation (using Pandas)

Let's first see how the data set looks like. Instead of calling the variable (as in the example before) we now use the ``head()`` and ``tail()`` methods so that it only shows us the first (or last) rows of the data set

```python
dataset.head()  # returns 5 rows by default, you can define any number within the parenthesis
```

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/dataframe_output_head5.png?raw=true)

The example dataset has 11 different columns (one without a name). To interact with one of the columns we must call its name in square brackets with the name in quotes as follows:

```python
# get the column 'Area' and multiplied by two
dataset['Area'] * 2
```

```
0         314.5
1        4119.5
2        3923.0
3       10857.0
4         748.0
         ...   
2656      905.0
2657     2162.5
2658     1027.0
2659      555.5
2660     1450.0
Name: Area, Length: 2661, dtype: float64
```

If you want to remove one or more columns, you can do it with the ``drop()`` method. For example, let's remove the column without a name.

```python
# Remove the column without a name from the DataFrame
dataset = dataset.drop(' ', axis=1)
dataset.head(3)
```

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/dataframe_output_head3.png?raw=true)

If you want to remove more than one column pass a list of columns instead as in the example below:

```python
dataset.drop(['FeretX', 'FeretY'], axis=1)
```

### Create new columns

The example dataset does not contain any column with the grain diameters and therefore we have to estimate them. For example, assuming the data comes from a thin section, you can estimate the apparent diameters from the section areas using the equivalent circular diameter (ECD) formula which is

ECD = 2 * √(area / π)

we will call the new column ``'diameters'``


```python
# Estimate the ECDs and store them in a column named 'diameters'
dataset['diameters'] = 2 * np.sqrt(dataset['Area'] / np.pi)
dataset.head()
```

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/dataframe_output_newcol.png?raw=true)

You can see a new column named diameters.

> 👉 In the examples above we define the square root as ``np.sqrt``, the arithmetic mean as ``np.mean``, and pi as  ``np.pi``. In this case, ``np.`` stems for NumPy or numerical Python, a basic package for scientific computing with Python, and the keyword after the dot is the method or the scientific value to be applied. If you write in the console ``np.`` and then press the TAB key, you will see a large list of available methods. In general, the method names are equivalent to those used in MATLAB but always by adding the ``np.`` first.

### A list of useful Pandas methods

Some things you might want to try (just copy-paste in interactive cells below and explore):

```python
# Reduction
dataset.mean()          # estimate the mean for all columns
dataset['Area'].mean()  # estimate the mean only for the column Area
dataset.std()           # estimate the (Bessel corrected) standard deviation
dataset.median()        # estimate the median
dataset.mad()           # estimate the mean absolute deviation
dataset.var()           # estimate the unbiased variace
dataset.sem()           # estimate the standard error of the mean
dataset.skew()          # estimate the sample skewness
dataset.kurt()          # estimate the sample kurtosis
dataset.quantile()      # estimate the sample quantile

# Information
dataset.describe()   # generate descriptive statistics
dataset.info()       # display info of the DataFrame
dataset.shape()      # (rows, columns)
dataset.count()      # number of non-null values

# Data cleaning
dataset.dropna()        # remove missing values from the data

# Writing to disk
dataset.to_csv(filename)    # save as csv file, the filename must be within quotes
dataset.to_excel(filename)  # save as excel file
```



***Well, I'm afraid you've come to the end. Where do you want to go?***

[return me to the home page](https://marcoalopez.github.io/GrainSizeTools/)  

[take me to “Getting started: first steps using the GrainSizeTools script”](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/_first_steps.md)

[take me to “Describing the population of grain sizes”](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/_describe.md)

[take me to “The plot module: visualizing grain size distributions”](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/_Plot_module.md)

[take me to “Paleopiezometry based on dynamically recrystallized grain size”](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/_Paleopizometry.md)

[take me to “The stereology module”](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/_Stereology_module.md)