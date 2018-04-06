*last update 2018/04/06* 

Getting Started: A step-by-step tutorial
-------------

> **Important note:**
> Please, **update to version 1.4.5**. It is also advisable to **update the plotting library matplotlib to version 2.x** since all the plots are optimized for such version.

### *Open and running the script*

First of all, make sure you have the required software and necessary Python libraries installed (see [requirements](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/Requirements.md) for details), and that you downloaded the latest version of the GrainSizeTools script (currently the v1.4). If this is the case, then you need to open the script in a integrated development environment (IDE) to interact with it (Fig. 1). For this, open the Canopy editor -if you installed the Enthought package- or the Spyder IDE -if you installed the Anaconda package-, and open the GrainSizeTools script using ```File>Open```. The script will appear in the editor as shown in figure 1.

![Figure 1. The Python editor and the shell in the Enthought Canopy environment](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/IDEs.png)  
*Figure 1. The editor and the Python shell (a.k.a. the console) in the the Spyder integrated development environment (IDE). The Enthough Canopy and the Spyder IDEs are both MATLAB-like IDEs optimized for numerical computing and data analysis using Python. They also provide a file explorer, a variable explorer, or a history log among other interesting features.*

To use the script it is necessary to run it. To do this, just click on the green "play" icon in the tool bar or go to ```Run>Run file``` in the menu bar (Fig. 2).

![Figure 2. Running a script in the Canopy editor (left) and in the IDLE editor (right)](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/RunScript_Canopy.png)  
*Figure 2. Running a script in the Enthought's Canopy (left) and Spyder (right) IDEs.*

The following text will appear in the shell/console (Fig. 1):
```
======================================================================================
Welcome to GrainSizeTools script v1.4.4
======================================================================================

GrainSizeTools is a free open-source cross-platform script to visualize and characterize
the grain size in polycrystalline materials from thin sections and estimate differential
stresses via paleopizometers.

METHODS AVAILABLE
==================  ==================================================================
Functions           Description
==================  ==================================================================
extract_areas       Extract the areas of the grains from a text file (txt, csv or xlsx)
calc_diameters      Calculate the diameter via the equivalent circular diameter
find_grain_size     Estimate the apparent grain size and visualize their distribution
derive3D            Estimate the actual grain size distribution via steorology methods
quartz_piezometer   Estimate diff. stress from grain size in quartz using piezometers
olivine_piezometer  Estimate diff. stress from grain size in olivine using piezometers
other_pizometers    Estimate diff. stress from grain size in other phases
confidence_interval Estimate the confidence interval using the t distribution
==================  ==================================================================

You can get information on the different methods by:
    (1) Typing help(function name) in the console. e.g. help(conf_interval)
    (2) In the Spyder IDE by writing the name of the function and clicking Ctrl + I
    (3) Visit script documentation at https://marcoalopez.github.io/GrainSizeTools/


EXAMPLES
--------
Extracting data using the automatic mode:
>>> areas = extract_areas()

Estimate the equivalent circular diameters:
>>> diameters = calc_diameters(areas)

Estimate and visualize different apparent grain size measures
>>> find_grain_size(areas, diameters, plot='sqrt')

Estimate differential stress using piezometric relations
>>> quartz_piezometer(grain_size=5.7, piezometer='Stipp_Tullis')

Estimate the actual 3D grain size distribution from thin sections
>>> derive3D(diameters, numbins=15, set_limit=40)
>>> derive3D(diameters, numbins=15, set_limit=None, fit=True)
```
Once you see this text, all the tools implemented in the GrainSizeTools script will be available by typing some commands in the shell as will be explained below.

### *A brief note on the organization of the script*

The script is organized in a modular way using Python functions helping to modify, reuse or extend the code. A Python function looks like this in the editor:

```python
def calc_diameters(areas, correct_diameter=0):
    """ Calculate the diameters from the sectional areas via the equivalent circular
    diameter.

    Parameters
    ----------
    areas: array_like
        the sectional areas of the grains

    correct_diameter: a positive integer or float
        this adds the width of the grain boundaries to correct the diameters. If
        correct_diameter is not declared no correction is considered.

    Returns
    -------
    A numpy array with the equivalent circular diameters
    """

    # calculate diameters via equivalent circular diameter
    diameters = 2 * sqrt(areas/pi)

    # diameter correction adding edges (if applicable)
    if correct_diameter != 0:
        diameters += correct_diameter

    return diameters
```

To sum up, the name following the Python keyword ```def```, in this example ```calc_diameters```, is the name of the function. The sequence of names within the parentheses are the formal parameters of the function (i.e. the inputs). In this case the function has two inputs, the parameter ```areas``` that correspond with an array containing the areas of the grain profiles previously measured, and the parameter ```correct_diameter``` that corresponds to a number that sometimes is required for correcting the size of the grains. Note that in this case the default value is set by default to zero. The text between the triple quotation marks provides information about the function, describing the conditions that must be met by the user as well as the output obtained. This information can be accessed from the shell by using the command ```help()``` and specifying the name of the function within the parentheses or, in the Spyder IDE, by pressing *Ctrl+I* once you wrote the name of the function. Below, it is the code block.

The names of the Python functions in the script are self-explanatory and each one has been implemented to perform a single task. Although there are a lot of functions within the script, we will only need to call less than four functions to obtain the results.

### *Using the script to visualize and estimate the grain size*

#### Loading the data and extracting the areas of the grain profiles

The first step requires to load the areas of the grain profiles measured in the thin section. It is therefore assumed that they were previously estimated using the *ImageJ* or similar software, and that the results were saved as a txt, csv, or xlsx (Fig. 3). If you do not know how to do this, then go to the section [How to measure the grain profile areas with ImageJ](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/imageJ_tutorial.md).

![Figure 3. Tabular-like files obtaining from the ImageJ app](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/figure_imageJ_files.png)  
*Figure 3. Tabular-like files obtaining from the ImageJ app. At left, the tab-separated txt file. At right, the csv comma-separated version.*

People usually perform different types of measures at the same time in the *ImageJ* application ultimately obtained a text file with the data in a spreadsheet-like form (Fig. 3). In this case, we need to extract the information corresponding to the column named 'Area', which is the one that contains the areas of the grain profiles. To do this, the script implements a function named ```extract_areas``` that automatically do this for us. To invoke this function we write in the shell:

```python
>>> areas = extract_areas()
```
where ```areas``` is just a name for a Python object, known as variable, in which the data extracted will be stored into memory. This will allow us to access and manipulate later the areas of the grain profiles using other functions. Almost any name can be used to create a variable in Python. As an example, if you want to load several datasets, you can name them ```areas1```, ```areas2``` or ```my_data1``` , ```my_data2``` and so on. In Python, variable names can contain upper and lowercase letters (the language is case-sensitive), digits and the special character *_*, but cannot start with a digit. In addition, there are some special keywords reserved for the language (e.g. True, False, if, else, etc.). Do not worry about it, the shell will highlight the word if you are using one of these. The function ```extract_areas``` is responsible for automatically extracting the areas from the dataset and loading them into the variable defined. Since the script version 1.3.1, you do not need to introduce any parameter/input within the parentheses. Once you press the Enter key, a new window will pop up showing a file selection dialog so that you can search and open the file that contains the dataset. Then, the function will automatically extract the information corresponding to the areas of the grains profiles and store them into the variable. To check that everything is ok, the shell will return the first and last rows of the dataset and the first and last values of the areas extracted as follows:

```
>>> areas = extract_areas()

         Area  Circ.     AR  Round  Solidity
0  1   157.25  0.680  1.101  0.908     0.937
1  2  2059.75  0.771  1.314  0.761     0.972
2  3  1961.50  0.842  1.139  0.878     0.972
3  4  5428.50  0.709  1.896  0.528     0.947
4  5   374.00  0.699  1.515  0.660     0.970
...
               Area  Circ.     AR  Round  Solidity
2656  2657   452.50  0.789  1.235  0.810     0.960
2657  2658  1081.25  0.756  1.446  0.692     0.960
2658  2659   513.50  0.720  1.493  0.670     0.953
2659  2660   277.75  0.627  1.727  0.579     0.920
2660  2661   725.00  0.748  1.351  0.740     0.960

column extracted = [  157.25  2059.75  1961.5  ...,   513.5    277.75   725.  ]
n = 2661
```

The data stored in any variable can be viewed at any time by invoking its name in the shell and pressing the Enter key. Furthermore, both the Canopy and Spyder IDEs have a specific variable explorer to visualize the variables loaded in the current session. The automatic mode assumes that the column containing the areas of the grain profiles is named ```'Area'``` in the text file (as shown in Fig. 3), which is the default name used by the ImageJ application. If the name of the column is different you can specify it as follows:

```python
>>> areas = extract_areas(file_path='auto', col_name='areas')
```

In this example, we introduced two different inputs/parameters within the parentheses. The first one is responsible for defining the file path. In this case it is set by default to 'auto', which means that the automatic mode showed above is on. The second one is the column name (col_name), in this example set to ```'areas'``` instead of the default ```'Area'```. Note that different inputs/parameters are comma-separated.

Another option, which was the only one available in old versions (< v1.3.1), is to introduce the inputs/parameters manually. For this write in the shell:

```python
>>> areas = extract_areas('C:/...yourFileLocation.../nameOfTheFile.csv', col_name='areas')
```

in this case we define the file location path in quotes, either single or double, following by the column name if required. If the column name is 'Areas' you just need to write the file path. To avoid problems in Windows OS do not use single backslashes to define the filepath but forward slashes (e.g. "C:/yourfilelocation.../nameofthefile.txt") or double backslashes.

In the case that the user extracted and stored the areas of the grains in a different form from the one proposed here, this is either in a txt or csv file but without a spreadsheet-like form (Fig. 4), there is a Python/Numpy built-in method named ```np.genfromtxt()``` that can be used to load text data in txt or csv into a variable in a similar way. For example:

```python
>>> areas = np.genfromtxt('C:/yourFileLocation/nameOfTheFile.txt')
```
In case you need to skip the first or any other number of lines because there is text or complementary information, then use the *skip_header* parameter as follows:

```python
>>> areas = np.genfromtxt('C:/yourFileLocation/nameOfTheFile.txt', skip_header=1)
```
In this example, ```skip_header=1``` means that the first line in the txt file will be ignored.

<img src="https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/notebook.png" width="300">  

*Figure 4. A txt file without spreadsheet-like form. The first line, which is informative, has to be ignored when loading the data*  

#### *Estimating the apparent diameters from the areas of the grain profiles*

The second step is to convert the areas into diameters via the equivalent circular diameter. This is done by a function named ```calc_diameters```. To invoke this function we write in the shell:

```python
>>> diameters = calc_diameters(areas)
```

The parameter declared within the parenthesis are the name of the variable that contains the areas of the grain profiles. Also, we need to define a new variable to store the diameters estimated from the areas, ```diameters``` in this example. In some cases, we would need to correct the size of the grain profiles (Fig. 5). For this, you need to add a new parameter within the parentheses:

```python
>>> diameters = calc_diameters(areas, correct_diameter=0.05)
```

This example means that for each apparent diameter calculated from the sectional areas, 0.05 will be added. If the parameter ```correct_diameter``` is not declared within the function, as in the first example, it is assumed that no diameter correction is needed.

<img src="https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/Fig_PS_pixels.png" width="450">  

*Figure 5. Example of correction of sizes in a grain boundary map. The figure is a raster showing the grain boundaries (in white) between three grains. The squares are the pixels of the image. The boundaries are two pixel wide, approximately. If, for example, each pixel corresponds to 1 micron, we will need to add 2 microns to the diameters estimated from the equivalent circular areas.*  

Once we estimated and stored the apparent grain sizes, we have several choices: (1) estimate an unidimensional value of grain size for paleopiezometry/paleowattmetry studies, or (2) derive the actual 3D grain size distribution from the population of apparent grain sizes using the Saltykov method (Saltykov, 1967; Sahagian and Proussevitch, 1998) or an extension of the Saltykov method named the two-step method (Lopez-Sanchez and Llana-Fúnez, 2016).  

#### *Obtaining apparent grain size measures*

For this, we need to call the function ```find_grain_size```. This function returns several grain size measures and plots, depending on your needs. The default mode returns a frequency *vs* apparent grain size plot together with the mean, median, and frequency peak grain sizes; the latter using a Gaussian kernel density estimator (see details in [Lopez-Sanchez and Llana-Fúnez 2015](http://www.solid-earth.net/6/475/2015/se-6-475-2015.html)). Other parameters of interest are also provided, such as the bin size, the number of classes, the method used to estimate the bin size, and the bandwidth used for the Gaussian kde according to the Silverman rule (Silverman 1986). As stated in [Lopez-Sanchez and Llana-Fúnez 2015](http://www.solid-earth.net/6/475/2015/se-6-475-2015.html), **to obtain consistent results a minimum of 433 measured grain profiles are required** (error < 4% at a 95% confidence), although we recommend to measure a minimum of 965 when possible (99% confidence).

To estimate a 1D apparent grain size value we write in the shell:

```python
>>> find_grain_size(areas, diameters)
```

First note that contrary to what was shown so far, the function is called directly in the shell since it is no longer necessary to store any data into an object/variable. The inputs are the arrays containing the areas and diameters. After pressing the Enter key, the shell will display something like this:

```
NUMBER WEIGHTED APPROACH (linear apparent grain size):

Mean grain size = 35.79 microns
Standard deviation = xx (1-sigma)
Median grain size = 32.53 microns
Interquartile range (IQR) = 23.98

HISTOGRAM FEATURES
The modal interval is 27.02 - 31.52
The number of classes are 35
The bin size is 4.5 according to the scott rule

GAUSSIAN KERNEL DENSITY ESTIMATOR FEATURES
KDE peak (peak grain size) =  25.24 microns
Bandwidth = 4.01 (Silverman rule)
```

Also, a new window with a plot will appear. The plots will show the apparent grain size distribution and the location of the different grain size measures (Fig. 6). You can save the plots by clicking the floppy disk icon in the tool bar as bitmap (8 file types to choose) or to post-editing in vector image (5 file types to choose). Another interesting option is to modify the appearance of the plot within the *Matplotlib* environment before saving by clicking on the configuration icon in the toolbar.

Although we promote the use of frequency *vs* apparent grain size linear plot (Fig. 6a), the function allows to use other options such as the logarithmic and square-root grain sizes (Figs. 6c, d) or the area-weighted grain size (e.g. Berger et al. 2011) (Fig. 6b). The advantages and disadvantages of the area weighted plot are explained in detail in [Lopez-Sanchez and Llana-Fúnez 2015](http://www.solid-earth.net/6/475/2015/se-6-475-2015.html). To do this, we need to specify the type of plot as follows:

```python
>>> find_grain_size(areas, diameters, plot='area')
```
in this example setting to use the area-weighted plot. The name of the different plots available are ```'lin'``` for the linear number-weighted plot (the default), ```'area'``` for the area-weighted plot (as in the example above), ```'sqrt'``` for the square-root grain size plot, and ```'log'``` for the logarithmic grain size plot. Note that the selection of different scales also implies to obtain different grain size estimations. Last, it is very important to note that **the mean of the square root or logarithmic grain sizes is not the same as the square root or the logarithm of the grain size mean**!

The function includes different plug-in methods to estimate an "optimal" bin size, including an automatic mode. The default automatic mode ```'auto'``` use the Freedman-Diaconis rule when using large datasets (> 1000) and the Sturges rule for small datasets. Other available rules are the Freedman-Diaconis ```'fd'```, Scott ```'scott'```, Rice ```'rice'```, Sturges ```'sturges'```, Doane ```'doane'```, and square-root ```'sqrt'``` bin sizes. For more details on the methods see [here](https://docs.scipy.org/doc/numpy/reference/generated/numpy.histogram.html).  We encourage you to use the default method ```'auto'```. Empirical experience indicates that the ```'doane'``` and ```'scott'``` methods work also pretty well when you have a lognormal- or a normal-like distributions, respectively. To specify the method we write in the shell:

```python
>>> find_grain_size(areas, diameters, plot='lin', binsize='doane')
```

note that you have to define first the type of plot you want and that the type of plot will change the appearance of your distribution (Fig. 6). You can also use and *ad hoc* bin/class size of type integer or float (*i.e.* an irrational number) as follows:

```python
>>> find_grain_size(areas, diameters, plot='lin', binsize=10.0)
```

The user-defined bin size can be any number of type integer or float (*i.e.* an irrational number).

![Figure 6. apparent grain size vs frequency plots](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/apparent_GS.png?raw=true)  
*Figure 6. Different apparent grain size vs frequency plots of the same population returned by the find_grain_size function. These include the number-weighted grain size distribution using linear (upper left), square root (upper right), or logarithmic (lower left) scales, and area-weighted distributions (lower right)*

#### *Estimating differential stress using piezometric relations (paleopiezometry)*

The script includes several functions for estimating differential stress from apparent grain size (i.e. using piezometric relations). This includes mineral phases such as quartz, calcite, olivine and albite (other phases will be added in the future). The function requires measuring the grain size as equivalent circular diameters and entering the apparent grain sizes ***in microns***. There are three different functions for this: ```quartz_piezometer``` for quartz, ```olivine_piezometer``` for olivine, and ```other_piezometers``` for other mineral phases. We provide some examples below:

```python
>>> quartz_piezometer(grain_size=5.7, piezometer='Stipp_Tullis')
Ensure that you have entered the apparent grain size as the square root mean!

differential stress = 169.16 MPa

>>> olivine_piezometer(grain_size=35, piezometer='Jung_Karato')
Ensure that you have entered the apparent grain size as the linear scale mean!

differential stress = 208.8 MPa

>>> other_piezometers(grain_size=5.7, piezometer='calcite_Rutter_SGR')
Ensure that you have entered the apparent grain size as the square root mean!

differential stress = 175.72 MPa
```
It is key to note that different piezometers require entering **different types of apparent grain sizes** to provide meaningful estimates of differential stress. For example, the piezometer relation of Stipp and Tullis (2003) requires entering the grain size as *the square root mean grain size from equivalent circular diameters with no stereological correction* (i.e. mean sqrt apparent grain size), and so on. Table 1 show all the implemented piezometers in GrainSizeTools v1.4.2 and the apparent grain size required for each one. Despite some piezometers were originally calibrated using linear intercepts (LI), the script will always require entering a specific apparent grain size measured as equivalent circular diameters (ECD), the script will automatically convert this ECD value to linear intercepts using the De Hoff and Rhines (1968) empirical relation.

**Table 1.** Relation of piezometers put in the GrainSizeTools script and the apparent grain size required to obtain meaningful differential stress estimates

|             Piezometer             | Apparent grain size†  | DRX mechanism  |    Phase     |           Reference           |
| :--------------------------------: | :-------------------: | :------------: | :----------: | :---------------------------: |
|        ```'Stipp_Tullis'```        |   Square root mean    |  Regimes 2, 3  |    Quartz    |     Stipp & Tullis (2003)     |
|      ```'Stipp_Tullis_BLG'```      |   Square root mean    | Regime 1 (BLG) |    Quartz    |     Stipp & Tullis (2003)     |
|          ```'Holyoke'```           |   Square root mean    |  Regimes 2, 3  |    Quartz    | Holyoke and Kronenberg (2010) |
|        ```'Holyoke_BLG'```         |   Square root mean    | Regime 1 (BLG) |    Quartz    | Holyoke and Kronenberg (2010) |
|         ```'Shimizu'```*‡*         |  Logarithmic median   |   SGR + GBM    |    Quartz    |        Shimizu (2008)         |
| ```'Cross'``` and ```'Cross_hr'``` |   Square root mean    |    BLG, SGR    |    Quartz    |      Cross et al. (2017)      |
|          ```'Twiss'```*§*          |   Logarithmic mean    |  Regimes 2, 3  |    Quartz    |         Twiss (1977)          |
|     ```'calcite_Rutter_SGR'```     |   Square root mean    |      SGR       |   Calcite    |         Rutter (1995)         |
|     ```'calcite_Rutter_GBM'```     |   Square root mean    |      GBM       |   Calcite    |         Rutter (1995)         |
|    ```'albite_PostT_BLG'```*§*     | Median (linear scale) |      BLG       |    Albite    |    Post and Tullis (1999)     |
|      ```'VanderWal_wet'```*§*      |  Mean (linear scale)  |                | Olivine, wet |   Van der Wal et al. (1993)   |
|       ```'Jung_Karato'```*§*       |  Mean (linear scale)  |      BLG       | Olivine, wet |     Jung & Karato (2001)      |

*† Apparent grain size measured as equivalent circular diameters (ECD) with no stereological correction and reported in microns either in linear, square root or logarithmic scales*  
*‡ Shimizu piezometer requires to provide the temperature during deformation in K*  
*§ These piezometers were originally calibrated using linear intercepts (LI) instead of ECD*

For more details on the piezometers and the assumption made use the command ```help()```  in the console as follows:

```python
>>> help(quartz_piezometer)
```

The constant values as put in the script are described in Table 2 below.

**Table 2**. Parameters relating the apparent size of dynamically recrystallized grains and the differential stress using a relation in the form ***d = A&sigma;<sup>-p</sup>*** or ***&sigma; = Bd<sup>-m</sup>***

|           Reference            |    phase     |     DRX      |  A†,‡   |  p†  |  B†,‡   |  m†  |
| :----------------------------: | :----------: | :----------: | :-----: | :--: | :-----: | :--: |
|    Stipp and Tullis (2003)     |    quartz    | Regimes 2, 3 | 3630.8  | 1.26 |  669.0  | 0.79 |
|    Stipp and Tullis (2003)     |    quartz    |   Regime 1   |   78    | 0.61 | 1264.1  | 1.64 |
| Holyoke & Kronenberg (2010)*§* |    quartz    | Regimes 2, 3 |  2451   | 1.26 |  490.3  | 0.79 |
| Holyoke & Kronenberg (2010)*§* |    quartz    |   Regime 1   |   39    | 0.54 |  883.9  | 1.85 |
|         Shimizu (2008)         |    quartz    |  SGR + GBM   |  1525   | 1.25 |   352   | 0.8  |
|      Cross et al. (2017)¶      |    quartz    | Regimes 2, 3 | 8128.3  | 1.41 |  593.0  | 0.71 |
|      Cross et al. (2017)¶      |  quartz, hr  | Regimes 2, 3 | 16595.9 | 1.59 |  450.9  | 0.63 |
|          Twiss (1977)          |    quartz    | Regimes 2, 3 |  12.3   | 1.47 |   5.5   | 0.68 |
|     Jung and Karato (2001)     | olivine, wet |     BLG      |  25704  | 1.18 | 5461.03 | 0.85 |
|   Van der Wal et al. (1993)    | olivine, wet |              | 0.0148  | 1.33 | 0.0425  | 0.75 |
|         Rutter (1995)          |   calcite    |     SGR      | 2026.8  | 1.14 | 812.83  | 0.88 |
|         Rutter (1995)          |   calcite    |     GBM      | 7143.8  | 1.12 | 2691.53 | 0.89 |
|     Post and Tullis (1999)     |    albite    |     BLG      |   55    | 0.66 |  433.4  | 1.52 |

*† **B** and **m** relate to **A** and **p** as follows: B = A<sup>1/p</sup> and m = 1/p*   
*‡ **A** and **B** are in [&mu;m MPa<sup>p, m</sup>] excepting Twiss (1977) in [mm MPa<sup>p, m</sup>] and Van der Wal et al. (1993) in [m MPa<sup>p, m</sup>]*  
*§ Holyoke and Kronenberg (2010) is a linear recalibration of the Stipp and Tullis (2003) piezometer*  
*¶ Cross et al. (2017) reanalysed the samples of Stipp and Tullis (2003) using EBSD data for reconstructing the grains. Specifically, they use grain maps with a 1 &mu;m and a 200 nm (hr - high resolution) step sizes . This is the preferred piezometer for quartz when grain size data comes from EBSD maps*

#### Estimating a robust confidence interval

As pointed out in the scope section, the optimal approach is to obtain several measures of stress or grain sizes and then estimate a confidence interval. Since v1.4.4+, the script implements a function called ```confidende_interval```for this. The script assume that the sample size is small (< 10) and hence it uses the student's t-distribution with n-1 degrees of freedom to estimate a robust confidence interval.  For large datasets the t-distribution approaches the normal distribution so you can also use this method for large datasets. The function has two inputs, the dataset, required, and the confidence interval, optional and set at 0.95 by default. For example:

```python
>>> my_results = [165.3, 174.2, 180.1]
>>> confidence_interval(data=my_results, confidence=0.95)
```

The function will return the following information in the console:

```
Confidence set at 95.0 %
Mean = 173.2 ± 18.51
Max / min = 191.71 / 154.69
Coefficient of variation = 10.7 %
```

The coefficient of variation express the confidence interval in percentage respect to the mean and thus it can be used to compare errors between samples with different mean values.

#### Derive the actual 3D distribution of grain sizes from thin sections

The function responsible to unfold the distribution of apparent grain sizes into the actual 3D grain size distribution is named ```derive3D```. The script implements two methods to do this, the Saltykov and the two-step methods. The Saltykov method is the best option for exploring the dataset and for estimating the volume of a particular grain size fraction. The two-step method is suitable to describe quantitatively the shape of the grain size distribution assuming that they follow a lognormal distribution. This means that the two-step method only yield consistent results when the population of grains considered are completely recrystallized or when the non-recrystallized grains can be previously discarded using shape descriptors or any other relevant paramater such as the density of dislocations. It is therefore necessary to check first whether the linear distribution of grain sizes is unimodal and lognormal-like (i.e. skewed to the right as in the example shown in figure 7). For more details see [Lopez-Sanchez and Llana-Fúnez (2016)](http://www.sciencedirect.com/science/article/pii/S0191814116301778).

***Applying the Saltykov method***

To derive the actual 3D population of grain sizes using the Saltykov method (Saltykov, 1967; Sahagian and Proussevitch, 1998), we need to call the function ```derive3D```as follows:

```python
>>> derive3D(diameters, numbins=14)
```
Since the Saltykov method uses the histogram to derive the actual 3D grain size distribution, the inputs are an array containing the population of apparent diameters of the grains and the number of classes. If the number of classes is not declared is set to ten by default. The user can use any positive **integer** value. However, it is usually advisable to choose a number not exceeding 20 classes (see later for details). After pressing the Enter key, the function will return something like this in the shell:

```
sample size = 2661
bin size = 11.26

A file named Saltykov_output.csv containing the midpoints and the class frequencies,
was generated
```

The text indicates the sample size, the bin size, and that a tabular-like csv file containing different numerical values was generated. Also, a window will pop up showing two plots (Fig 7). On the left it is the frequency plot with the estimated 3D grain size distribution in the form of a histogram, and on the right the volume-weighted cumulative density curve. The latter allows the user to estimate qualitatively the percentage of volume occupied by a defined fraction of grain sizes. If the user wants to estimate quantitatively the volume of a particular grain fraction (i.e. the volume occupied by a fraction of grains less or equal to a certain value) we need to add a new parameter within the function as follows:

```python
>>> derive3D(diameters, numbins=12, set_limit=40)
```
In the example above, the grain fraction is set to 40 microns, which means that the script will also return an estimation of the percentage of volume occupied by all the grain fractions up to 40 microns. A new line will appear in the shell:

```
volume fraction (up to 40 microns) = 22.8 %
```
As a cautionary note, if we use a different number of bins/classes, in this example set randomly at 12, we will obtain slightly different volume estimates. This is normal due to the inaccuracies of the Saltykov method. In any event, Lopez-Sanchez and Llana-Fúnez (2016) proved that the absolute differences between the volume estimations using a range of classes between 10 and 20 are below ±5. This means that to stay safe we should always take an absolute error margin of ±5 in the volume estimations.

![Figure 7. 3D grain size distribution](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/figure_2.png)  
*Figure 7. The derived 3D grain size distribution and the volume-weighted cumulative grain size distribution using the Saltykov method.*

Lastly, due to the nature of the Saltykov method, the smaller the number of classes the better the numerical stability of the method, and the larger the number of classes the better the approximation of the wanted distribution. Ultimately, the strategy to follow is about finding the maximum number of classes (i.e. the best resolution) that produces stable results. Based on experience, previous works proposed to use between 10 to 15 classes (e.g. Exner 1972), although depending on the quality and the size of the dataset it seems that it can be used safely up to 20 classes or even more (e.g. Heilbronner and Barret 2014, Lopez-Sanchez and Llana-Fúnez 2016). Yet, no method (i.e. algorithm) appears to be generally best for choosing an optimal number of classes (or bin size) for the Saltykov method. Hence, the only way to find the maximum number of classes with consistent results is to use a trial and error strategy and observe if the appearance is coherent or not. As a last cautionary note, **the Saltykov method requires large samples (n ~ 1000 or larger)** to obtain consistent results, even when using a small number of classes.

***Applying the two-step method***

To estimate the shape of the 3D grain size distribution, the ```derive3D``` function implements a method called "the two-step method" (Lopez-Sanchez and Llana-Fúnez, 2016). This method assumes that the actual 3D population of grain sizes follows a lognormal distribution, a common distribution observed in recrystallized aggregates. Hence, make sure that the aggregate or the studied area within the rock/alloy/ceramic is completely recrystallized. The method applies a non-linear least squares algorithm to fit a lognormal distribution on top of the Saltykov method using the midpoints of the different classes. The method return two parameters, the **MSD** and the theoretical **median**, both enough to fully describe a lognormal distribution at their original (linear) scale, and the uncertainty associated with these estimates (see details in Lopez-Sanchez and Llana-Fúnez, 2016). In addition, it also returns a frequency plot showing the probability density function estimated (Fig. 8). In particular, the **MSD value** allows to describe the shape of the lognormal distribution independently of the scale (i.e. the range) of the grain size distribution, which is very convenient for comparative purposes. To apply the two-step method we need to invoke the function ```derive3D``` as follows:

```python
>>> derive3D(diameters, numbins=15, set_limit=None, fit=True)
```

Note that in this case we include a new parameter named ```fit``` that it is set to ```True``` with the "T" capitalized (it is set to ```False``` by default). The function will return something like this in the shell:

```
sample size = 2661
bin size = 10.44

Optimal coefficients:
MSD (shape) = 1.69 ± 0.07
Median (location) = 35.51 ± 1.73 (caution: not fully realiable)

A file named twoStep_output.csv containing the midpoints, class frequencies,
and cumulative volumes was generated
```

Sometimes, the least squares algorithm will fail at fitting the lognormal distribution to the unfolded data (e.g. Fig. 8b). This is due to the algorithm used to find the optimal MSD and median values, the Levenberg–Marquardt algorithm (Marquardt, 1963), only converges to a global minimum when their initial guesses are already somewhat close to the final solution. Based on our experience in quartz aggregates, the initial guesses were set by default at 1.2 and 25.0 for the MSD and median values respectively. However, if the algorithm fails it is possible to change the default values by adding a following parameter:

```python
>>> derive3D(diameters, numbins=15, set_limit=None, fit=True, initial_guess=True)
```
When the ```initial_guess``` parameter is set to ```True```, the script will ask to set a new starting values for both parameters (it also indicates which are the default ones). Based in our experience, a useful strategy is to let the MSD value in its default value (1.2) and decreasing the median value every five units until the fitting procedure yield a good fit (*e.g.* 25 -> 20 -> 15...) (Fig. 8).

![Figure 8. Two-step method plots](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/two-step_method.png)  
*Figure 8. Plots obtained using the two-step method. At left, an example with the lognormal pdf well fitted to the data points. The shadow zone is the trust region for the fitting procedure. At right, an example with a wrong fit due to the use of unsuitable initial guess values. Note the discrepancy between the data points and the line representing the best fitting.*

#### ***Comparing different grain size populations using box plots***

[Box (or box-and-whisker) plot](https://en.wikipedia.org/wiki/Box_plot) is a non-parametric method to display numerical datasets through their quartiles and median, being a very efficient way for comparing **unimodal** datasets graphically. Figure 9 show the different elements represented in a typical box plot.

![figure 9. Box plot elements](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/boxplot_01.png)
*Figure 9. Box plot elements*  

To create a box plot using the Matplotlib library we need to create first a variable with all the data sets to represent. For this we create a Python list as follows (variable names have been chosen for convenience):

```python
>>> all_data = [dataset1, dataset2, dataset3, dataset4] # Note that a Python list is a list of elements within brackets separated by commas
```

Then we create the plot (Fig. 10):

```python
>>> plt.boxplot(all_data)
>>> plt.show() # write this and click return if the plot did not appear automatically
```
To create a more convenience plot (Fig. 10) we propose using the following **optional** parameters:

```python
# First make a list specifying the labels of the samples (this is optional). Ensure that the number of items in the brackets coincide with the number of datasets to plot.
>>> label_list = ['SampleA', 'SampleB', 'SampleC', 'SampleD']
# Then make the plot ading the following instructions
>>> plt.boxplot(all_data, vert=False, meanline=True, showmeans=True, labels=label_list)
>>> plt.xlabel('apparent diameter ($\mu m$)') # add the x-axis label
>>> plt.show() # write this and click return if the plot did not appear automatically
```

The parameters defined in the boxplot are:

- ```vert```: if False makes the boxes horizontal instead of vertical (it is True by default).
- ```meanline``` and ```showmeans```: if True will show the location of the mean within the plots.
- ```labels```: add labels to the different datasets.

![figure 10. Examples of box plots](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/Boxplot_02.png)
*Figure 10. Box plot comparing four unimodal datasets obtained from the same sample but located in different places along the thin section. At left, a box plot with the default appearance. At right, the same box plot with the optional parameters showing above. Dashed lines are the mean. Note that the all the datasets show similar median, means, IQRs, and whisker locations. In contrast, the fliers (points) approximately above 100 microns vary greatly.*

#### ***Other methods of interest***

**Obtain common descriptive statistic parameters**

```python
>>> mean(array_name)  # Estimate the mean
>>> std(array_name)  # Estimate the standard deviation
>>> median(array_name)  # Estimate the median
>>> iqr(array_name)  # Estimate the interquartile range
```

**Merging datasets**

A useful *Numpy* method to merge two or more datasets is called ```hstack()```, which stack arrays in sequence as follows (*please, note the use of double parenthesis*):

```python
>>> np.hstack((name of the array1, name of the Array2,...))
```

As an example if we have two different datasets and we want to merge the areas and the diameters estimated in a single variable we write into the Python shell (variable names are just random examples):

```python
>>> all_areas = np.hstack((areas1, areas2))
>>> all_diameters = np.hstack((diameters1, diameters2))
```

Note that in this example we merged the original datasets into two new variables named ```all_areas``` and ```all_diameters``` respectively. Therefore, we do not overwrite any of the original variables and we can used them later if required. In contrast, if you use a variable name already defined:

```python
>>> areas1 = np.hstack((areas1, areas2))
```
The variable ```areas1``` is now a new array with the values of the two datasets, and the original dataset stored in the variable ```areas1``` no longer exists since these variables (strictly speaking Numpy arrays) are mutable Python objects.

**Loading several datasets: the fastest (appropriate) way**

If you need to load a large number of datasets, you probably prefer not having to search across multiple folders in the file dialog window or to manually specify the absolute file paths of each file. Python establishes by default a current working directory in which all the files can be accessed directly by specifying just the name of the file (or a relative path if they are in a sub-folder). For example, if the current working directory is ```c:/user/yourname```, you no longer need to specify the entire file path for the files stored within this directory. For example, to load a csv file named 'my_sample.csv' stored in that location you just need to write:

```python
>>> areas = extract_areas('my_sample.csv')
```

When you run the script for the first time, your current working directory will appear in the Python shell. Also, you can retrieve your current working directory at any time by typing in the shell ```os.getcwd()```, as well as to modify it to another path using the function ```os.chdir('new default path')```. The same rules apply when using the ```np.genfromtxt``` method.

> Note: usually the current working directory is the same directory where the script is located (although this depends on the Python environment you have installed). Hence, sometimes it is a good idea to locate the scrip in the same directory where the datasets are located.

[next section](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/quick_tutorial.md)  
[table of contents](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/tableOfContents.md)

----------
