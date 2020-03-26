Getting Started: A step-by-step tutorial
=============

> **IMPORTANT NOTE: This documentation only applies to GrainSizeTools v3.0+ Please check your script version before using this tutorial. You will be able to reproduce all the results shown in this tutorial using the dataset provided with the script, the file ``data_set.txt``. Note that this is a beta version and the documentation is still unfinished. If you find a bug or have any questions check the community guidelines. I would be glad to answer it (although it may take a while).**

[TOC]

## Open and running the script

First of all, make sure you have the latest version of the GrainSizeTools (GST) script and a Python scientific distribution installed (see [requirements](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/Requirements.md) for more details). If you are not familiarized with Python, you have two options here: (1) work with the [Spyder](https://www.spyder-ide.org/) integrated development environment (IDE) (Fig. 1), a powerful MATLAB-like scientific IDE optimized for numerical computing and data analysis with Python; or (2) with [Jupyter notebooks](https://jupyter.org/) (Fig. 2), which is a browser-based environment that allows you to create and share documents that may contain live code, equations, visualizations and narrative text. Make your choice and launch it.

![Figure 1. The Python editor and the shell in the Enthought Canopy environment](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/IDEs.png)  *Figure 1. The [Spyder](https://www.spyder-ide.org/) v.4+ integrated development environment (IDE) showing the editor (left), the IPython shell or console (bottom right), and the help window (upper right). This is a MATLAB-like IDE for Python. They also provide a variable explorer, a history log, MATLAB-like cells, code autocompletion, etc.*

![]()

*Figure 2. Jupyter Lab, a browser-based notebook that allows you to create documents that may contain live code, equations (using Latex), visualizations and narrative text* 

If you are in Spyder, open the ``GrainSizeTools_script.py`` file using ```File>Open``` and then run the script clicking on the "play" green icon in the tool bar (or go to ```Run>Run file``` in the menu bar). After running, the following text will appear in the console:

```
module plot imported
module averages imported
module stereology imported
module piezometers imported
module template imported

===================================================================================
Welcome to GrainSizeTools script v3.0beta1
===================================================================================
GrainSizeTools is a free open-source cross-platform script to visualize and
characterize the grain size in polycrystalline materials and estimate
differential stress via paleopizometers.

Get a list of the main methods using: get.function_list()
```

Alternatively, if you are using a Jupyter notebook or want to call the GST script from Spyder using a script you should do it as follows:

```python
# run the script in Jupyter notebook/lab
%run C:/.../GrainSizeTools_script.py  # substitute ...with the full file path

# run the script in Spyder using a script or the console
runfile('C:/...grain_size_tools/GrainSizeTools_script.py', wdir='C:/.../grain_size_tools')
# wdir is the working directory
```

```python
get.functions_list()
```



## Reading and manipulating (tabular) data with Pandas

[Pandas](https://pandas.pydata.org/about/index.html) is the de facto standard Python library for data analysis and manipulation of table-like datasets (csv, excel or txt files among others). The library includes several tools for reading files and handling of missing data. We strongly recommend its use along with the GrainSizeTools script. Indeed, when running the GrainSizeTools script pandas is imported as ```pd``` for its general use.

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

The only mandatory argument for the reading methods (except in the case of "read_clipboard") is to set the path  (local or URL) where the file to be imported is located. For example:


```python
# read file to create a Pandas DataFrame (i.e. a table)
# note that the file path is within quotes (either single or double)
dataset = pd.read_table('DATA/data_set.txt')

# show the DataFrame in the console
dataset
```

Pandas' reading methods give you a lot of control over how a file is read. To keep things simple, the most commonly used arguments are listed below:

```python
sep or delimier  # Delimiter to use.
header  # Row number(s) to use as the column names. By default it takes the first row as the column names (header=0). If there is no columns names in the file you must set header=None
skiprows  # Number of lines to skip at the start of the file (an integer).
na_filter  # Detect missing value markers. False by default.
```

An example might be:

```python
dataset = pd.read_csv('data_set.csv', sep=';', skiprows=5, na_filter=True)
```

To get the path of the file through a file selection dialog instead of writing it, GrainSizeTools has the function ```get_filepath()```. This can be used in two ways:

```python
# store the path in a variable named filepath and then use it when calling the read method
filepath = get_filepath()
dataset = pd.read_csv(filepath, sep=';')

# use get_filepath() directly within the read method
dataset = pd.read_csv(get_filepath(), sep=';')
```

***Manipulating tabular data***

When importing a dataset, the Pandas library creates what is called a *dataframe* which for simplicity is just an “object” containing tabular data. For visualizing the data you can use the variable explorer in Spyder or write the variable that contains the dataframe in the console and press enter. For example:

```python
# visualize the data (in the Spyder console or a Jupyter notebook)
dataset

# Alternatively
dataset.head()  # show only the first rows
dataset.tail()  # show only the last rows

# select and show a specific column of the dataset
dataset['Area']  # select the column named 'Area'
dataset['Area', 'diameters']  # select columns 'Area' and 'diameters'
```

If the dataset imported does no contain the diameters of the grains but the sectional areas, we can estimate the apparent diameters using the equivalent circular diameter formula which is:

$d = 2 \cdot \sqrt{areas / \pi}$

and store them in a new column. For this, we write in the console:


```python
# Estimate the equivalent circular diameters and store them in a column named 'diameters'
dataset['diameters'] = 2 * np.sqrt(dataset['Area'] / np.pi)
dataset.head()
```

TODO

## Grain size population characterization

### Describing the dataset

First we are going to generate descriptive statistics to characterize the grain size population. For this, we use the GST function ```summarize``` and pass the population of diameters:


```python
summarize(dataset['diameters'])
```


    ============================================================================
    CENTRAL TENDENCY ESTIMATORS
    ============================================================================
    Arithmetic mean = 34.79 microns
    Confidence intervals at 95.0 %
    ASTM method: 34.09 - 35.48, (±2.0%), length = 1.393
    mCox method: 34.43 - 36.04 (-1.0%, +3.6%), length = 1.616
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
    Standard deviation = 18.32 (1-sigma)
    Interquartile range (IQR) = 23.98
    Lognormal shape (Multiplicative Standard Deviation) = 1.75
    ============================================================================
    Shapiro-Wilk test warnings:
    Data is not normally distributed!
    Normality test: 0.94, 0.00 (test statistic, p-value)
    ============================================================================

By default, the ```summarize``` function returns:

- Different **central tendency estimators** ("averages") including by default the arithmetic and geometric means, the median, and the KDE-based mode (i.e. frequency peak).
- The **confidence intervals** for the different means and the median at 95% of certainty in absolute and percentage relative to the average (*a.k.a* coefficient of variation). The meaning of these intervals are that given the observed data, there is a 95% probability (one in 20) that the true value of grain size falls within this credible region.
- The methods used to estimate the confidence intervals for each average (excepting for the mode). By default the function ```summarize``` will choose the optimal method depending on distribution features (Lopez-Sanchez, 2020). For more details on how the methods are chosen see TODO.
- Two dispersion measures of the population: the standard deviation and the interquartile range.
- The lognormal shape or MSD
- A Shapiro-Wilk test warning indicating when the data deviates from normally and/or lognormally distributed (when p-value < 0.05).



## Visualizing the grain size distribution and testing lognormality (the plot module)

To visualize grain size distribution we will use the methods implemented in the module named ```plot```.  The main method is called ```plot.distribution()```. We will see a few examples of its use below:

```python
plot.distribution(dataset['diameters'])
```

    =======================================
    Number of classes =  45
    binsize =  6.6
    =======================================
    =======================================
    KDE bandwidth =  4.01
    =======================================

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/new_distribution.png?raw=true)

*Figure X. The default distribution plot showing the histogram and the kernel density estimate (KDE) of the distribution and the location of the arithmetic and geometric means, the median, and the KDE-based mode.*




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
    binsize =  12.22
    =======================================



![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/new_distribution_hist.png?raw=true)

### Plotting the area-weighted distribution

```python
plot.area_weighted(dataset['diameters'], dataset['Area'])
```

    =======================================
    DESCRIPTIVE STATISTICS
    Area-weighted mean grain size = 53.88 microns
    =======================================
    HISTOGRAM FEATURES
    The modal interval is 40.85 - 44.26 microns
    Midpoint (of modal interval) = 62.98 microns
    The number of classes are 46
    The bin size is 3.40 according to the auto rule
    =======================================



![png](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/new_area_weighted.png?raw=true)

### Testing lognormality

Sometimes we will need to test whether the data follows or deviates from a lognormal distribution. For example, to find out if the data set is suitable for applying the two-step stereological method or which confidence interval method is best for the arithmetic mean. The script use two methods to test whether the distribution of grain size follows a lognormal distribution. One is a visual method named [quantile-quantile (q-q) plots]([https://en.wikipedia.org/wiki/Q%E2%80%93Q_plot](https://en.wikipedia.org/wiki/Q–Q_plot)) and the other is a quantitative test named the [Shapiro-Wilk test](https://en.wikipedia.org/wiki/Shapiro–Wilk_test). For this we use the GST function ```test_lognorm``` as follows :

```python
>>> test_lognorm(dataset['diameters'])

# show output
```

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/new_qqplot.png?raw=true)

*Figure. q-q plot of the test dataset*

Regarding the q-q plot, if the points fall right onto the reference line, it means that the grain size values are lognormally or approximately lognormally distributed. The Shapiro-Wilk test will return two different values...TODO. The q-q plot has the advantage that it shows where the distribution deviates from the lognormal distribution. 

In such case, the dataset is appropriate for using the two-step method or characterize the population of apparent diameters using the multiplicative (geometric) standard deviation. To know more about this type of plots see https://serialmentor.com/dataviz/



## Differential stress estimate using piezometric relations (paleopiezometry)

The script includes a function for estimating differential stress via paleopiezomers based on "average" apparent grain sizes called ``calc_diffstress`` . This includes common mineral phases such as quartz, calcite, olivine and albite. The function requires measuring the grain size as equivalent circular diameters and entering the apparent grain sizes ***in microns*** although the type of "average" grain size to be entered depends on the piezometric relation. We provide a list of the all piezometric relations available, the average grain size value to use, and the different experimentally-derived parameters in Tables 1 to 5. In addition, you can get a list of the available piezometric relations in the console just by calling``piezometers.*()``, where * is the mineral phase, either quartz, calcite, olivine, or feldspar. An example below:

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

The ``calc_diffstress`` requires entering three different inputs: (1) the apparent grain size, (2) the mineral phase, and (3) the piezometric relation. We provide some examples below:

```python
>>> calc_diffstress(grain_size=5.7, phase='quartz', piezometer='Stipp_Tullis')

differential stress = 169.16 MPa
Ensure that you entered the apparent grain size as the root mean square (RMS)!

>>> calc_diffstress(grain_size=35, phase='olivine', piezometer='VanderWal_wet')

differential stress = 282.03 MPa
Ensure that you entered the apparent grain size as the mean in linear scale!

>>> calc_diffstress(grain_size=35, phase='calcite', piezometer='Rutter_SGR')

differential stress = 35.58 MPa
Ensure that you entered the apparent grain size as the mean in linear scale!
```

It is key to note that different piezometers require entering **different apparent grain size averages** to provide meaningful estimates. For example, the piezometer relation of Stipp and Tullis (2003) requires entering the grain size as *the root mean square (RMS) using equivalent circular diameters with no stereological correction*, and so on. Table 1 show all the implemented piezometers in GrainSizeTools v3.0+ and the apparent grain size required for each one. Despite some piezometers were originally calibrated using linear intercepts (LI), the script will always require entering a specific grain size average measured as equivalent circular diameters (ECD). The script will automatically approximate the ECD value to linear intercepts using the De Hoff and Rhines (1968) empirical relation. Also, the script takes into account if the authors originally used a specific correction factor for the grain size. For more details on the piezometers and the assumption made use the command ```help()```  in the console as follows:

```python
>>> help(calc_diffstress)
```

**Table 1.** Relation of piezometers (in alphabetical order) and the apparent grain size required to obtain meaningful differential stress estimates

|         Piezometer         |  Apparent grain size†  | DRX mechanism  |    Phase     |           Reference           |
| :------------------------: | :--------------------: | :------------: | :----------: | :---------------------------: |
|       ``Barnhoorn``        |          Mean          |    SRG, GBM    |   calcite    |    Barnhoorn et al. (2004)    |
| ``Cross`` and ``Cross_hr`` |        RMS mean        |    BLG, SGR    |    quartz    |      Cross et al. (2017)      |
|       ``'Holyoke'``        |        RMS mean        |  Regimes 2, 3  |    quartz    | Holyoke and Kronenberg (2010) |
|     ``'Holyoke_BLG'``      |        RMS mean        | Regime 1 (BLG) |    quartz    | Holyoke and Kronenberg (2010) |
|   ```'Jung_Karato'```*§*   |          Mean          |      BLG       | olivine, wet |     Jung & Karato (2001)      |
|   `` 'Platt_Bresser' ``    |        RMS mean        |    BLG, SGR    |   calcite    |  Platt and De Bresser (2017)  |
| ```'Post_Tullis_BLG'```*§* |         Median         |      BLG       |    albite    |    Post and Tullis (1999)     |
|     ```'Rutter_SGR'```     |          Mean          |      SGR       |   calcite    |         Rutter (1995)         |
|     ```'Rutter_GBM'```     |          Mean          |      GBM       |   calcite    |         Rutter (1995)         |
|     `` 'Schmid' ``*§*      |                        |      SGR       |   calcite    |     Schmid et al. (1980)      |
|     ```'Shimizu'```*‡*     | Median in log(e) scale |   SGR + GBM    |    quartz    |        Shimizu (2008)         |
|    ```'Stipp_Tullis'```    |        RMS mean        |  Regimes 2, 3  |    quartz    |     Stipp & Tullis (2003)     |
|  ```'Stipp_Tullis_BLG'```  |        RMS mean        | Regime 1 (BLG) |    quartz    |     Stipp & Tullis (2003)     |
|      ```'Twiss'```*§*      |          Mean          |  Regimes 2, 3  |    quartz    |         Twiss (1977)          |
|       ``'Valcke' ``        |          Mean          |    BLG, SGR    |   calcite    |     Valcke et al. (2015)      |
|  ```'VanderWal_wet'```*§*  |          Mean          |                | Olivine, wet |   Van der Wal et al. (1993)   |

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

|         Reference         |    phase     | DRX  | A†,‡  |  p†  |  B†,‡   |  m†  |
| :-----------------------: | :----------: | :--: | :---: | :--: | :-----: | :--: |
|  Jung and Karato (2001)   | olivine, wet | BLG  | 25704 | 1.18 | 5461.03 | 0.85 |
| Van der Wal et al. (1993) | olivine, wet |      | 14800 | 1.33 |  4250   | 0.75 |



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

Since *v2.0.1*, the ``calc_diffstress`` function allows correcting the differential stress estimates for plane stress using the correction factor proposed by Paterson and Olgaard (2000). The rationale behind this is that experiments designed to calibrate paleopiezometers are performed in uniaxial compression while shear zones approximately behave as plane stress volumes. To correct this Paterson and Olgaard (2000) (see also Behr and Platt, 2013) proposed to multiply the estimates by 2 / √3. To do this we specify:

```python
# Note that we set the parameter 'correction' to True
>>> calc_diffstress(grain_size=5.7, phase='quartz', piezometer='Stipp_Tullis', correction=True)

differential stress = 195.32 MPa
Ensure that you entered the apparent grain size as the root mean square (RMS)!
```





## Stereology (the stereology module)

TODO...(available soon)