# Import and handling of (tabular) data

## Using the Spyder data importer

If you are in Spyder, the easiest way to import data is through the Spyder data importer. To do this, select the variable browser and then click on the import data icon in the upper left (Fig. 3). A new window will pop up showing different import options (Fig. 4).

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/new_variable_explorer.png?raw=true)

*Figure 3. The variable explorer window in Spyder. Note that the variable explorer label is selected at the bottom (indicated with an arrow). To launch the data importer click on the top left icon (indicated by a circle).*

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/import_data.png?raw=true)

*Figure 4. The two-step process for importing data with the Spyder data importer. At left, the first step where the main options are the (1) the variable name, (2) the type of data to import (set to data), (3) the column separator (set to Tab), and (4) the rows to skip (set to 0 as this assumes that the first row is the column names). At right, the second step where you can preview the data and set the variable type. In this case, choose import as DataFrame, which is the best choice for tabular data.*

Once you press "Done" (in the bottom right) the dataset will appear within the variable explorer window as shown in figure 3. Note that it provides information about the type of variable (a Dataframe), the number of rows and columns (2661 x 11), and the column names. If you want to get more details or edit something, double-click on this variable and a new window will pop up (Fig. 5). Also, you can do a right-click on this variable and several options will appear.

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/variable_explorer02.png?raw=true)

*Figure 5. Representation of the dataset in the Spyder variable explorer. Note that the colours change with values.*

> 👉 More info on the Spyder variable explorer here: https://docs.spyder-ide.org/variableexplorer.html



---



## Importing tabular data using the console

An alternative option is to import the data using the console. For this, [Pandas](https://pandas.pydata.org/about/index.html) is the de facto standard Python library for data analysis and manipulation of tabular datasets (CSV, excel or text files among others). The library includes several tools for reading files and handling of missing data. Also, when running the GrainSizeTools script pandas is imported as ```pd``` for its general use.

All Pandas methods to read data are all named ```pd.read_*``` where * is the file type. For example:

```python
pd.read_csv()       # read csv or txt files, default delimiter is ','
pd.read_table()     # read general delimited file, default delimiter is '\t' (TAB)
pd.read_excel()     # read excel files
pd.read_html()      # read HTML tables
...                 # etc.
```

> 👉 For other supported file types see https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html

The only mandatory argument for the reading methods is to define the path (local or URL) with the location of the file to be imported. For example:


```python
# read file to create a Pandas DataFrame (i.e. a table)
# note that the file path is within quotes (either single or double)
dataset = pd.read_table('DATA/data_set.txt')
```

Pandas' reading methods give you a lot of control over how a file is read. To keep things simple, we list here the most commonly used options:

```python
sep         # The delimiter to use (alternatively you can also use the word delimiter)
header      # Row number(s) to use as the column names. By default it takes the first row as the column names (header=0). If there is no columns names in the file you must set header=None
skiprows    # Number of lines to skip at the start of the file (an integer).
na_filter   # Detect missing value markers. False by default.
sheet_name  # Only for excel files, the excel sheet name either a number or the full name of the sheet.

```

An example using several optional arguments might be:

```python
dataset = pd.read_csv('DATA/data_set.csv', sep=';', skiprows=5, na_filter=True)
```

which in plain language means that we are importing a ``csv`` file named ``data_set`` that is located in the folder ``DATA``. The data is delimited by a semicolon and we ignore the first five lines of the file (*i.e.* column names are supposed to appear in the sixth row). Last, we want all missing values to be handled during the import. 

> 👉 more details on Pandas csv read method: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

The GrainSizeTools script includes an own method named ```get_filepath()``` to get the path of the file through a file selection dialog instead of directly writing it. This can be used in two ways:

```python
# store the path in a variable (here named filepath for convenience) and then use it when calling the read method
filepath = get_filepath()
dataset = pd.read_csv(filepath, sep='\t')

# use get_filepath() directly within the read method
dataset = pd.read_csv(get_filepath(), sep='\t')
```

Lastly, Pandas also allows to directly import tabular data from the clipboard (i.e. data copied using copy-paste commands). For this, after copying the table (from a text/excel file or a website) call the method: 

```python
dataset = pd.read_clipboard()
```

The copied table will appear in the variable explorer.



---



## Basic tabular data manipulation (Pandas dataframes)

In the examples above, we imported the data as a *Dataframe*, which for simplicity is just a Python “object” containing tabular data.

```python
type(dataset)  # show the variable type
```

```
pandas.core.frame.DataFrame
```

### Visualize the DataFrame

For visualizing the data at any time, you can use the variable explorer in Spyder (Fig. 5) or directly typing the name of the variable in the console and press enter.

```python
# show the DataFrame in the console or the notebook
dataset
```

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/dataframe_output.png?raw=true)

Alternatively, if you want to view few rows use: 

```python
# visualize the first rows, you can define the number of rows whithin the parentheses
dataset.head()
# view the last rows
dataset.tail()
```

### Interacting with columns (creating columns, operations, etc.)

To select one or more columns of the DataFrame, you need to type the name of the DataFrame and then the name of the column within brackets as follows:

```python
# select a specific column of the dataset, note that the name of the column is in quotes.
dataset['AR'] * 2  # select the values of the column named 'AR' and multiply it by two

# select several columns and estimate the arithmetic mean
# note the double brackets when calling more than one column!
np.mean(dataset[['Area', 'Feret']])

# estimate the arithmetic mean of all columns
np.mean(dataset)
```

A real-case scenario might be to estimate the apparent diameters of the grains from the sectional areas using the equivalent circular diameter (ECD) formula, which is

ECD = 2 * √(area / π)

Indeed, this is the case with the imported example dataset where the sectional areas not the apparent diameters are provided. In the example below, we are generating a new column named ``diameters`` with the equivalent circular diameters of the grain


```python
dataset['diameters'] = 2 * np.sqrt(dataset['Area'] / np.pi)
dataset.head()
```

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/dataframe_diameters.png?raw=true)

Now, you can see that a new column named diameters appear when displaying the dataset.



> 👉 In the examples above we define the square root as ``np.sqrt``, the arithmetic mean as ``np.mean``, and pi as  ``np.pi``. In this case, ``np.`` stems for Numpy or numerical Python, a basic package for scientific computing with Python, and the word after the dot with the method or the scientific value to be applied. If you write in the console ``np.`` and then press the TAB key, you will see a large list of available methods. In general, the method names are equivalent to those used in MATLAB but always by adding the ``np.`` first.