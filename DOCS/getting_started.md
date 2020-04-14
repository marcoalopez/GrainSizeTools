Getting Started: A step-by-step tutorial
=============

> **IMPORTANT NOTE: This documentation only applies to GrainSizeTools v3.0+ Please check your script version before using this tutorial. You will be able to reproduce all the results shown in this tutorial using the dataset provided with the script, the file ``data_set.txt``. Note that this is a beta version and the documentation is still unfinished. If you find a bug or have any question check the community guidelines. I would be glad to answer it (although it may take a while).**

- [Running the script](#running-the-script)
- [Importing the data using the Spyder data importer](#importing-the-data-using-the-spyder-data-importer)
- [Importing (tabular) data with Pandas (Spyder and Jupyter lab)](#importing--tabular--data-with-pandas--spyder-and-jupyter-lab-)
- [Manipulating tabular data (Pandas dataframes)](#manipulating-tabular-data--pandas-dataframes-)
- [Grain size characterization](#grain-size-characterization)
- [Visualizing grain size distributions and their properties (the plot module)](#visualizing-grain-size-distributions-and-their-properties--the-plot-module-)
  * [Plotting the area-weighted distribution](#plotting-the-area-weighted-distribution)
  * [Testing lognormality](#testing-lognormality)
  * [Normalized grain size distributions](#normalized-grain-size-distributions)
- [Paleopiezometry](#paleopiezometry)
- [Stereology (the stereology module)](#stereology--the-stereology-module-)

## Running the script

First of all, make sure you have the latest version of the GrainSizeTools (GST) script and a Python scientific distribution installed (see [requirements](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/Requirements.md) for more details). If you are not familiarized with Python, you have two main options after opening the Anaconda Python distribution:

1. The [Spyder](https://www.spyder-ide.org/) integrated development environment (IDE) (Fig. 1), a MATLAB-like scientific IDE optimized for numerical computing and data analysis with Python.

2.  The [Jupyter notebook](https://jupyter.org/) (Fig. 2), a browser-based environment that allows you to create and share documents that may contain live code, equations, visualizations and narrative text.

Make your choice and launch it from the Anaconda navigator or just typing Spyder or Jupyter lab in the console.

![Figure 1. The Python editor and the shell in the Enthought Canopy environment](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/IDEs.png)  *Figure 1. The [Spyder](https://www.spyder-ide.org/) v.4+ integrated development environment (IDE) showing the editor (left), the IPython shell or console (bottom right), and the help-variable explorer window (top right). This is a MATLAB-like IDE for Python. They also provide a variable explorer, a history log, MATLAB-like cells, code autocompletion, etc.*

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/Jupyter_lab.png?raw=true)

*Figure 2. The Jupyter Lab development environment, a browser-based notebook that allows you to create documents that may contain live code, equations (using Latex), visualizations and narrative text*.

In Spyder, open the ``GrainSizeTools_script.py`` file using ```File>Open``` and then run the script clicking on the "play" green icon in the tool bar (or go to ```Run>Run file``` in the menu bar). After running, the following text will appear in the console:

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

Version: v3.0beta3 (2020-04-xx)
Documentation: https://marcoalopez.github.io/GrainSizeTools/

Type get.functions_list() to get a list of the main methods
```

Alternatively, if you are using Jupyter lab/notebook you have a similar step-by-step tutorial in the link below and within the ``grain_size_tools`` folder in your hard disk:

https://github.com/marcoalopez/GrainSizeTools/blob/master/grain_size_tools/notebook_example.ipynb

As indicated in the welcome message, we can get a list of the main methods at anytime by using:

```python
get.functions_list()
```

![](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/function_list.png)



## Importing the data using the Spyder data importer

If you are in Spyder, the easiest way to import data is through the Spyder data importer. To do this, select the variable browser and then click on the import data icon in the upper left (Fig. 3). A new window will pop up showing different import options (Fig. 4).

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/new_variable_explorer.png?raw=true)

*Figure 3. The variable explorer window in Spyder. Note that the variable explorer is selected at the bottom (indicated with an arrow). To launch the data importer click on the top left icon (indicated by a circle).*

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/import_data.png?raw=true)

*Figure 4. The two-step process for importing data with the Spyder data importer. At left, the first step where the main options are the (1) the variable name, (2) the type of data to import (set to data), (3) the column separator (set to Tab), and (4) the rows to skip (set to 0 as this assumes that the first row are the column names). At right, the second step where you can preview the data and set the variable type. In this case, choose import as DataFrame, which is the best choice for tabular data.*

Once you press "Done" (in the bottom right) the dataset will appear within the variable explorer window as shown in figure 3. Note that it provides information about the type of variable (a Dataframe), the number of rows and columns (2661 x 11), and the column names. If you want to get more details or edit something, double-click on this variable and a new window will pop up (Fig. 5). Also you can do a right-click on this variable and several options will appear.

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/variable_explorer02.png?raw=true)

*Figure 5. Representation of the dataset in the Spyder variable explorer.*

More info here: https://docs.spyder-ide.org/variableexplorer.html

## Importing (tabular) data with Pandas (Spyder and Jupyter lab)

An alternative option is to import the data using the console. For this, [Pandas](https://pandas.pydata.org/about/index.html) is the de facto standard Python library for data analysis and manipulation of table-like datasets (csv, excel or txt files among others). The library includes several tools for reading files and handling of missing data and when running the GrainSizeTools script pandas is imported as ```pd``` for its general use.

All Pandas methods to read data are all named ```pd.read_*``` where * is the file type. For example:

```python
pd.read_csv()          # read csv or txt files, default delimiter is ','
pd.read_table()        # read general delimited file, default delimiter is '\t' (TAB)
pd.read_excel()        # read excel files
pd.read_html()         # read HTML tables
pd.read_clipboard()    # read text from clipboard (copy-paste)
# etc.
```

For other supported file types see https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html

The only mandatory argument for the reading methods (leaving aside``pd.read_clipboard()``) is to define the path (local or URL) with the location of the file to be imported. For example:


```python
# read file to create a Pandas DataFrame (i.e. a table)
# note that the file path is within quotes (either single or double)
dataset = pd.read_table('DATA/data_set.txt')
```

Pandas' reading methods give you a lot of control over how a file is read. To keep things simple, the most commonly used arguments are listed below:

```python
sep or delimier  # Delimiter to use.
header  # Row number(s) to use as the column names. By default it takes the first row as the column names (header=0). If there is no columns names in the file you must set header=None
skiprows  # Number of lines to skip at the start of the file (an integer).
na_filter  # Detect missing value markers. False by default.
sheet_name  # Only for excel files, the excel sheet name either a number or the full name of the sheet.

```

A random example using several optional arguments might be:

```python
dataset = pd.read_csv('DATA/data_set.csv', sep=';', skiprows=5, na_filter=True)
```

where we import a csv file delimited by ``;`` ignoring the first five lines of the file, and we want all missing values to be handled during import.

The GST script includes a method named ```get_filepath()``` to get the path of a file through a file selection dialog instead of writing it. This can be used in two ways:

```python
# store the path in a variable (here named filepath for convenience) and then use it when calling the read method
filepath = get_filepath()
dataset = pd.read_csv(filepath, sep=';')

# use get_filepath() directly within the read method
dataset = pd.read_csv(get_filepath(), sep=';')
```
> more details on Pandas csv read method: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html

## Manipulating tabular data (Pandas dataframes)

In the examples above, we imported the data as a *Dataframe*, which for simplicity is just a Python “object” containing tabular data.

```python
type(dataset)  # show the variable type
```

```
pandas.core.frame.DataFrame
```

For visualizing the data at any time, you can use the variable explorer in Spyder (Fig. 5) or directly calling the name of the variable that contains the *Dataframe* in the console and press enter.

```python
# show the DataFrame in the console
dataset
```

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/dataframe_output.png?raw=true)

Alternatively, if you want to view only few rows use: 

```python
# visualize the first rows, you can define the number of rows whithin the parentheses
dataset.head()
# view the last rows
dataset.tail()
```

For interacting with one of the columns of the *dataframe*, you can do it as follows:

```python
# select a specific column of the dataset
dataset['AR']  # select the column named 'AR'

# select several columns and estimate the arithmetic mean
# note the double brackets when calling more than one column!
np.mean(dataset[['Area', 'Feret']])
```

For example, the imported dataset does no contain the diameters of the grains but the sectional areas of the grains. Then, we need to estimate the apparent diameters via the equivalent circular diameter (ECD) formula which is:

ECD = 2 * √(area / π)

and store them in a new column. For example:


```python
# Estimate the ECDs and store them in a column named 'diameters'
dataset['diameters'] = 2 * np.sqrt(dataset['Area'] / np.pi)
dataset.head()
```

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/dataframe_diameters.png?raw=true)

Now, you can see that a new column named diameters appear when displaying the dataset.

> 👉 In the examples above we define the square root as ``np.sqrt``, the arithmetic mean as ``np.mean``, and pi as  ``np.pi``. In this case, ``np.`` stems for Numpy or numerical Python, a basic package for scientific computing with Python, and the word after the dot with the method or the scientific value to be applied. If you write in the console ``np.`` and then press press the TAB key, you will see a huge list of methods available. In general, the name of the methods used are equivalent to those used in MATLAB but always adding the ``np.`` first.



---



## Grain size characterization

To describe the properties of the grain size population use the function ```summarize``` and pass the population of diameters as input:


```python
summarize(dataset['diameters']) # the column name may change depending on your dataset
```

    ============================================================================
    CENTRAL TENDENCY ESTIMATORS
    ============================================================================
    Arithmetic mean = 34.79 microns
    Confidence intervals at 95.0 %
    CLT (ASTM) method: 34.09 - 35.48, (±2.0%), length = 1.393
    ============================================================================
    Geometric mean = 30.10 microns
    Confidence interval at 95.0 %
    CLT method: 29.47 - 30.75 (-2.1%, +2.2%), length = 1.283
    ============================================================================
    Median = 31.53 microns
    Confidence interval at 95.0 %
    robust method: 30.84 - 32.81 (-2.2%, +4.1%), length = 1.970
    ============================================================================
    Mode (KDE-based) = 24.31 microns
    Maximum precision set to 0.1
    KDE bandwidth = 4.01 (silverman rule)
     
    ============================================================================
    DISTRIBUTION FEATURES
    ============================================================================
    Sample size (n) = 2661
    Standard deviation = 18.32 (1-sigma)
    Interquartile range (IQR) = 23.98
    Lognormal shape (Multiplicative Standard Deviation) = 1.75
    ============================================================================
    Shapiro-Wilk test warnings:
    Data is not normally distributed!
    Normality test: 0.94, 0.00 (test statistic, p-value)
    Data is not lognormally distributed!
    Lognormality test: 0.99, 0.00 (test statistic, p-value)
    ============================================================================

By default, the ```summarize``` function returns:

- Different **central tendency estimators** ("averages") including the arithmetic and geometric means, the median, and the KDE-based mode (i.e. frequency peak).
- The **confidence intervals** for the different means and the median at 95% of certainty in absolute and percentage relative to the average (*a.k.a* coefficient of variation). The meaning of these intervals are that given the observed data, there is a 95% probability (one in 20) that the true value of grain size falls within this credible region. It is provides the lower and upper bounds, the error in percentage respect to the average, and the length of the confidence interval. 
- The methods used to estimate the confidence intervals for each average (excepting for the mode). By default the function ```summarize``` will choose the optimal method depending on distribution features (Fig. X)
- The sample size and two population dispersion measures: the (Bessel corrected) [standard deviation](https://en.wikipedia.org/wiki/Standard_deviation) and the [interquartile range](https://en.wikipedia.org/wiki/Interquartile_range).
- The shape of the lognormal distribution using the multiplicative standard deviation (MSD)
- A Shapiro-Wilk test warning indicating when the data deviates from normal and/or lognormal (when p-value < 0.05).

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/avg_map.png?raw=true)

*Figure X. Decision tree flowchart for choosing the optimal confidence interval estimation method. For details on this see [Lopez-Sanchez (2020)](https://doi.org/10.1016/j.jsg.2020.104042)*

The ```summarize()``` method contains different input parameters (arguments) that we will commented on in turn. The help of the function looks like this in the script (use ``?summarize`` or CTRL+I in the console to obtain this): 

```python
def summarize(data,
              avg=('amean', 'gmean', 'median', 'mode'),
              ci_level=0.95,
              bandwidth='silverman',
              precision=0.1):
    """ Estimate different grain size statistics. This includes different means,
    the median, the frequency peak grain size via KDE, the confidence intervals
    using different methods, and the distribution features.

    Parameters
    ----------
    data : array_like
        the diameters (apparent or not) of the grains

    avg : string, tuple or list, optional
        the averages to be estimated

        | Types:
        | 'amean' - arithmetic mean
        | 'gmean' - geometric mean
        | 'median' - median
        | 'mode' - the kernel-based frequency peak of the distribution

    ci_level : scalar between 0 and 1, optional
        the certainty of the confidence interval (default = 0.95)

    bandwidth : string {'silverman' or 'scott'} or positive scalar, optional
        the method to estimate the bandwidth or a scalar directly defining the
        bandwidth. It uses the Silverman plug-in method by default.

    precision : positive scalar or None, optional
        the maximum precision expected for the "peak" kde-based estimator.
        Default is 0.1. Note that this has nothing to do with the
        confidence intervals

    Call functions
    --------------
    - amean, gmean, median, and freq_peak (from averages)

    Examples
    --------
    >>> summarize(dataset['diameters'])
    >>> summarize(dataset['diameters'], ci_level=0.99)
    >>> summarize(np.log(dataset['diameters']), avg=('amean', 'median', 'mode'))
    """
```

TODO

---



## Visualizing grain size distributions and their properties (the plot module)

To visualize the grain size distribution there are several methods implemented in the module named ```plot```.  All methods of the *plot* module can be invoked by writing ```plot.*```, where * refers to the plot to be used.

> 👉 If you write ``plot.`` and then press the tab key a menu will pop up with all the methods implemented in the plot module

The main method is ```plot.distribution()```. This method allows to visualize the grain size population using the histogram and/or the kernel density estimate (KDE) as well as the location of the different averages in the distribution. To use it we invoke this function and pass as an argument the population of grain sizes as follows:

```python
plot.distribution(dataset['diameters'])
```

    =======================================
    Number of classes =  45
    binsize =  3.41
    =======================================
    =======================================
    KDE bandwidth =  4.01
    =======================================

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/new_distribution.png?raw=true)

*Figure X. The default distribution plot showing the histogram and the kernel density estimate (KDE) of the distribution and the location of the arithmetic and geometric means, the median, and the KDE-based mode.*

Note that the methods returns a plot, the number of classes and bin size of the histogram, and the bandwidth (or kernel) of the KDE. The ```plot.distribution()``` method contains different input parameters that we will commented on in turn:

```python
def distribution(data,
                 plot=('hist', 'kde'),
                 avg=('amean', 'gmean', 'median', 'mode'),
                 binsize='auto', bandwidth='silverman'):
    """ Return a plot with the ditribution of (apparent or actual) grain sizes
    in a dataset.

    Parameters
    ----------
    data : array_like
        the apparent diameters of the grains

    plot : string, tuple or list
        the type of plot, either histogram ('hist'), kernel density estimate
        ('kde') or both ('hist', 'kde'). Default is both.

    avg : string, tuple or list
        the central tendency measures o show, either the arithmetic ('amean')
        or geometric ('gmean') means, the median ('median'), and/or the
        KDE-based mode ('mode'). Default all averages.

    binsize : string or positive scalar, optional
        If 'auto', it defines the plug-in method to calculate the bin size.
        When integer or float, it directly specifies the bin size.
        Default: the 'auto' method.

        | Available plug-in methods:
        | 'auto' (fd if sample_size > 1000 or Sturges otherwise)
        | 'doane' (Doane's rule)
        | 'fd' (Freedman-Diaconis rule)
        | 'rice' (Rice's rule)
        | 'scott' (Scott rule)
        | 'sqrt' (square-root rule)
        | 'sturges' (Sturge's rule)

    bandwidth : string {'silverman' or 'scott'} or positive scalar, optional
        the method to estimate the bandwidth or a scalar directly defining the
        bandwidth. It uses the Silverman plug-in method by default.
    ...
    """
```

As we have just seen in the previous example, the only mandatory parameter is ```data``` which corresponds to the populations of diameters. The ``plot`` parameter allows you to define the method to visualize the population, either the histogram, the kernel density estimate or both (the default option). If we want to plot only the KDE or the histogram we do it as follows:


```python
plot.distribution(dataset['diameters'], plot='kde')
```

    =======================================
    KDE bandwidth =  4.01
    =======================================

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/new_distribution_kde.png?raw=true)

```python
plot.distribution(dataset['diameters'], plot='hist', binsize='doane')
```

    =======================================
    Number of classes =  17
    binsize =  9.02
    =======================================



![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/new_distribution_hist.png?raw=true)

In the example above using the histogram we passed as input the optional argument ```binsize```. This parameter allows us to use different plug-in methods implemented in the Numpy package to estimate "optimal" bin sizes for the construction of the histograms. The default mode, called ```'auto'```, uses the Freedman-Diaconis rule for large datasets and the Sturges rule otherwise. Other available plug-in methods are the Freedman-Diaconis ```'fd'```, Scott ```'scott'```, Rice ```'rice'```, Sturges ```'sturges'```, Doane ```'doane'```, and square-root ```'sqrt'```. For more details on these methods see [here](https://docs.scipy.org/doc/numpy/reference/generated/numpy.histogram_bin_edges.html#numpy.histogram_bin_edges).  We encourage you to use the default method ```'auto'```. Empirical experience indicates that the ```'doane'``` and ```'scott'``` methods work also pretty well when you have lognormal- and normal-like distributions, respectively. You can also define an ad-hoc bin size if you pass as input a positive scalar, for example:

```python
plot.distribution(dataset['diameters'], plot='hist', binsize=10.5)
```

The  ```avg``` parameter allows us to define which central tendency measure to show, either the arithmetic mean ```amean```, the geometric mean ```gmean``` means, the median ```median```, and/or the KDE-based mode ```mode```. By default, all averages are displayed.

Lastly, the parameter ``bandwidth`` allows you to define a method to estimate an optimal bandwidth to construct the KDE, either the ``'silverman'`` (the default) or the ``scott`` rules. The ``'silverman'`` and the ``'scott'`` rules, are both optimized for normal-like distributions, so they perform better when using over log-transformed grain sizes. You can also define your own bandwidth/kernel value by declaring a positive scalar instead. For example:

```python
plot.distribution(dataset['diameters'], plot='kde', bandwidth=5.0)
```

Note, however, that the bandwidth affects the location of the KDE-based mode. For consistency, you should use the same method or bandwidth used when calling the ```summarize``` method.



### Plotting the area-weighted distribution

In case you want to plot the area-weighted distribution of grain sizes you can use:

```python
plot.area_weighted(dataset['diameters'], dataset['Area'])
```

    =======================================
    DESCRIPTIVE STATISTICS
    Area-weighted mean grain size = 53.88 microns
    =======================================
    HISTOGRAM FEATURES
    The modal interval is 40.85 - 44.26 microns
    The number of classes are 46
    The bin size is 3.40 according to the auto rule
    =======================================



![png](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/new_area_weighted.png?raw=true)

*Figure X. The area-weighted apparent grain size distribution and the location of the area-weighted mean*

TODO

### Testing lognormality

Sometimes we will need to test whether the data follows or deviates from a lognormal distribution. For example, to find out if the data set is suitable for applying the two-step stereological method or which confidence interval method is best for the arithmetic mean. The script use two methods to test whether the distribution of grain size follows a lognormal distribution. One is a visual method named [quantile-quantile (q-q) plots]([https://en.wikipedia.org/wiki/Q%E2%80%93Q_plot](https://en.wikipedia.org/wiki/Q–Q_plot)) and the other is a quantitative test named the [Shapiro-Wilk test](https://en.wikipedia.org/wiki/Shapiro–Wilk_test). For this we use the GST function ```test_lognorm``` as follows :

```python
plot.qq_plot(dataset['diameters'])
```
```
=======================================
Shapiro-Wilk test (lognormal):
0.99, 0.00 (test statistic, p-value)
It doesnt look like a lognormal distribution (p-value < 0.05)
(╯°□°）╯︵ ┻━┻
=======================================
```

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/new_qqplot.png?raw=true)

*Figure X. The q-q plot of the test dataset. Note that the distribution of apparent grain sizes deviates from the logarithmic at the ends*.

Regarding the q-q plot, if the points fall right onto the reference line, it means that the grain size values are lognormally or approximately lognormally distributed. The Shapiro-Wilk test will return two different values, the test statistic and a p-value. The Shapiro-Wilk test, as put in GST script, considers the distribution to be lognormally distributed when the p-value is greater than 0.05. The q-q plot has the advantage over the Shapiro-Wilk test that it shows where the distribution deviates from the lognormal distribution. 

> 👉 To know more about the q-q plot see https://serialmentor.com/dataviz/



### Normalized grain size distributions

Standardized grain size distributions are representations of the entire grain population standardized using an average, usually the arithmetic mean or median. The advantage of standardized distributions is that they allow comparison of whether or not the grain size distribution is similar to others when the average grain size between the different distributions differs significantly. For example, to check whether two or more grain size distributions have similar shapes we can compare their standard deviations (SD) or their interquartile ranges (IQR).  In this case, to facilitate the comparison, the standardized method shows the normalized distribution on a logarithmic scale based on e and provides the SD or IQR of the normalized population depending on the chosen normalizing factor.

```python
plot.normalized(dataset['diameters'], avg='amean')
```
```
=======================================
Normalized SD = 0.165
KDE bandwidth =  0.04
=======================================
```

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/new_normalized.png?raw=true)

*Figure X. KDE of the log-transformed grain size distribution normalized to the arithmetic mean (note that amean = 1).*



---



## Paleopiezometry

The script includes a function for estimating differential stress via paleopiezometers based on "average" apparent grain sizes called ``calc_diffstress()`` . This includes common mineral phases such as quartz, calcite, olivine and albite. The estimation requires measuring the grain size as equivalent circular diameters and entering the apparent grain sizes ***in microns*** although the type of "average" grain size to be entered depends on the piezometric relation. We provide a list of the all piezometric relations available, the average grain size value to use, and the different experimentally-derived parameters in Tables 1 to 5. In addition, you can get a list of the available piezometric relations in the console just by calling``piezometers.*()``, where * is the mineral phase, either ``quartz``, ``calcite``, ``olivine``, or ``feldspar``. For example:

```python
>>> piezometers.quartz()

Available piezometers:
'Cross'
'Cross_hr'
'Holyoke'
'Holyoke_BLG'
'Shimizu'
'Stipp_Tullis'
'Stipp_Tullis_BLG'
'Twiss'
```

The ``calc_diffstress`` requires  at least entering three different inputs: (1) the apparent grain size, (2) the mineral phase, and (3) the piezometric relation. We provide few examples below:

```python
calc_diffstress(12.0, phase='quartz', piezometer='Twiss')
```
```
============================================================================
differential stress = 83.65 MPa

INFO:
Ensure that you entered the apparent grain size as the arithmeic mean grain size
ECD was converted to linear intercepts using de Hoff and Rhines (1968) correction
============================================================================
```
The ``calc_diffstress`` function allows **correcting the differential stress estimate for plane stress** using the correction factor proposed by Paterson and Olgaard (2000). The rationale behind this is that experiments designed to calibrate paleopiezometers are performed in uniaxial compression while shear zones approximately behave as plane stress volumes. To correct this Paterson and Olgaard (2000) (see also Behr and Platt, 2013) proposed to multiply the estimates by 2 / √3. To do this we specify:

```python
calc_diffstress(12, phase='quartz', piezometer='Twiss', correction=True)
```

```
============================================================================
differential stress = 96.59 MPa

INFO:
Ensure that you entered the apparent grain size as the arithmeic mean grain size
ECD was converted to linear intercepts using de Hoff and Rhines (1968) correction
============================================================================
```
You can pass  as input an array of grain size values instead of a scalar 

```python
ameans = np.array([12.23, 13.71, 12.76, 11.73, 12.69, 10.67])
estimates = calc_diffstress(ameans, phase='olivine', piezometer='VanderWal_wet')
estimates
```

```
============================================================================
INFO:
Ensure that you entered the apparent grain size as the arithmetic mean in linear scale
ECD was converted to linear intercepts using de Hoff and Rhines (1968) correction
Differential stresses in MPa

array([167.41, 153.66, 162.16, 172.73, 162.83, 185.45])
```

It is key to note that different piezometers require entering **different apparent grain size averages** to provide meaningful estimates. For example, the piezometer relation of Stipp and Tullis (2003) requires entering the grain size as *the root mean square (RMS) using equivalent circular diameters with no stereological correction*, and so on. Table 1 show all the implemented piezometers in GrainSizeTools v3.0+ and the apparent grain size required for each one. Despite some piezometers were originally calibrated using linear intercepts (LI), the script will always require entering a specific grain size average measured as equivalent circular diameters (ECD). The script will automatically approximate the ECD value to linear intercepts using the De Hoff and Rhines (1968) empirical relation. Also, the script takes into account if the authors originally used a specific correction factor for the grain size. For more details on the piezometers and the assumption made use the command ```help()```  in the console as follows:

```python
help(calc_diffstress)

# alternatively in Jupyterlab:
?calc_diffstress
```

**Table 1.** Relation of piezometers (in alphabetical order) and the apparent grain size required to obtain meaningful differential stress estimates

|         Piezometer         |  Apparent grain size†  | DRX mechanism  |      Phase       |           Reference           |
| :------------------------: | :--------------------: | :------------: | :--------------: | :---------------------------: |
|       ``Barnhoorn``        |      arith. mean       |    SRG, GBM    |     calcite      |    Barnhoorn et al. (2004)    |
| ``Cross`` and ``Cross_hr`` |        RMS mean        |    BLG, SGR    |      quartz      |      Cross et al. (2017)      |
|       ``'Holyoke'``        |        RMS mean        |  Regimes 2, 3  |      quartz      | Holyoke and Kronenberg (2010) |
|     ``'Holyoke_BLG'``      |        RMS mean        | Regime 1 (BLG) |      quartz      | Holyoke and Kronenberg (2010) |
|   ```'Jung_Karato'```*§*   |      arith. mean       |      BLG       |   olivine, wet   |     Jung & Karato (2001)      |
|   `` 'Platt_Bresser' ``    |        RMS mean        |    BLG, SGR    |     calcite      |  Platt and De Bresser (2017)  |
| ```'Post_Tullis_BLG'```*§* |         Median         |      BLG       |      albite      |    Post and Tullis (1999)     |
|     ```'Rutter_SGR'```     |      arith. mean       |      SGR       |     calcite      |         Rutter (1995)         |
|     ```'Rutter_GBM'```     |      arith. mean       |      GBM       |     calcite      |         Rutter (1995)         |
|     `` 'Schmid' ``*§*      |                        |      SGR       |     calcite      |     Schmid et al. (1980)      |
|     ```'Shimizu'```*‡*     | Median in log(e) scale |   SGR + GBM    |      quartz      |        Shimizu (2008)         |
|    ```'Stipp_Tullis'```    |        RMS mean        |  Regimes 2, 3  |      quartz      |     Stipp & Tullis (2003)     |
|  ```'Stipp_Tullis_BLG'```  |        RMS mean        | Regime 1 (BLG) |      quartz      |     Stipp & Tullis (2003)     |
|      ```'Twiss'```*§*      |      arith. mean       |  Regimes 2, 3  |      quartz      |         Twiss (1977)          |
|       ``'Valcke' ``        |      arith. mean       |    BLG, SGR    |     calcite      |     Valcke et al. (2015)      |
|  ```'VanderWal_wet'```*§*  |      arith. mean       |                | Olivine, dry/wet |   Van der Wal et al. (1993)   |

*† Apparent grain size measured as equivalent circular diameters (ECD) with no stereological correction and reported in microns. The use of non-linear scales are indicated*  
*‡ Shimizu piezometer requires to provide the temperature during deformation in K*  
*§ These piezometers were originally calibrated using linear intercepts (LI) instead of ECD*



**Table 2**. Parameters relating the average apparent size of dynamically recrystallized grains and differential stress in quartz using a relation in the form ***d = A&sigma;<sup>-p</sup>*** or ***&sigma; = Bd<sup>-m</sup>***

|           Reference            |   phase   |     DRX      |  A†,‡   |  p†  |  B†,‡  |  m†  |
| :----------------------------: | :-------: | :----------: | :-----: | :--: | :----: | :--: |
|     Cross et al. (2017)*§*     |  quartz   | Regimes 2, 3 | 8128.3  | 1.41 | 593.0  | 0.71 |
|     Cross et al. (2017)*§*     | quartz hr | Regimes 2, 3 | 16595.9 | 1.59 | 450.9  | 0.63 |
| Holyoke & Kronenberg (2010)*¶* |  quartz   | Regimes 2, 3 |  2451   | 1.26 | 490.3  | 0.79 |
| Holyoke & Kronenberg (2010)*¶* |  quartz   |   Regime 1   |   39    | 0.54 | 883.9  | 1.85 |
|         Shimizu (2008)         |  quartz   |  SGR + GBM   |  1525   | 1.25 |  352   | 0.8  |
|    Stipp and Tullis (2003)     |  quartz   | Regimes 2, 3 | 3630.8  | 1.26 | 669.0  | 0.79 |
|    Stipp and Tullis (2003)     |  quartz   |   Regime 1   |   78    | 0.61 | 1264.1 | 1.64 |
|          Twiss (1977)          |  quartz   | Regimes 2, 3 |  1230   | 1.47 |  550   | 0.68 |

*† **B** and **m** relate to **A** and **p** as follows: B = A<sup>1/p</sup> and m = 1/p*   
*‡ **A** and **B** are in [&mu;m MPa<sup>p, m</sup>]*  
*§ Cross et al. (2017) reanalysed the samples of Stipp and Tullis (2003) using EBSD data for reconstructing the grains. Specifically, they use grain maps with a 1 m and a 200 nm (hr - high-resolution) step sizes . This is the preferred piezometer for quartz when grain size data comes from EBSD maps*  
*¶ Holyoke and Kronenberg (2010) provides a recalibration of the Stipp and Tullis (2003) piezometer*  



**Table 3**. Parameters relating the average apparent size of dynamically recrystallized grains and differential stress in olivine

|         Reference         |      phase       | DRX  | A†,‡  |  p†  |  B†,‡   |  m†  |
| :-----------------------: | :--------------: | :--: | :---: | :--: | :-----: | :--: |
|  Jung and Karato (2001)   |   olivine, wet   | BLG  | 25704 | 1.18 | 5461.03 | 0.85 |
| Van der Wal et al. (1993) | olivine, dry/wet |      | 15000 | 1.33 | 1355.4  | 0.75 |



**Table 4**. Parameters relating the average apparent size of dynamically recrystallized grains and differential stress in calcite

|          Reference          |  phase  |   DRX    |  A†,‡  |  p†  |  B†,‡   |  m†  |
| :-------------------------: | :-----: | :------: | :----: | :--: | :-----: | :--: |
|   Barnhoorn et al. (2004)   | calcite | SRG, GBM | 2134.4 | 1.22 | 537.03  | 0.82 |
| Platt and De Bresser (2017) | calcite | BLG, SGR |  2141  | 1.22 | 538.40  | 0.82 |
|        Rutter (1995)        | calcite |   SGR    | 2026.8 | 1.14 | 812.83  | 0.88 |
|        Rutter (1995)        | calcite |   GBM    | 7143.8 | 1.12 | 2691.53 | 0.89 |
|    Valcke et al. (2015)     | calcite | BLG, SGR | 79.43  | 0.6  | 1467.92 | 1.67 |



**Table 5**. Parameters relating the average apparent size of dynamically recrystallized grains and differential stress in albite

|       Reference        | phase  | DRX  | A†,‡ |  p†  | B†,‡  |  m†  |
| :--------------------: | :----: | :--: | :--: | :--: | :---: | :--: |
| Post and Tullis (1999) | albite | BLG  |  55  | 0.66 | 433.4 | 1.52 |



---



## Stereology (the stereology module)

TODO...(available soon)