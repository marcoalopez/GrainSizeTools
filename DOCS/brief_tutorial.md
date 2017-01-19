Getting Started: A step-by-step tutorial
-------------

> **Note:**
> This tutorial assumes no previous knowledge of the Python programming language. It is important to **update as soon as possible to version 1.3**, it contains important changes that are not fully compatible with previous versions.

### *Open and running the script*

Once you had the required software installed in your system (see [requirements](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/Requirements.md)) and the latest version of the GrainSizeTools script on your computer (make sure it is the 1.3 version), you will need to open the script in a integrated development environment (IDE) to interact with it (Fig. 1). For this, open the Canopy IDE -if you installed the Enthought Canopy package-, or the Spyder IDE -if you installed the Anaconda package- and open the GrainSizeTools script using ```File>Open```. The script will appear in the editor as shown in figure 1.

![Figure 1. The Python editor and the shell in the Enthought Canopy environment](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/IDEs.png)
*Figure 1. The editor and the Python shell (aka. the console) in the Enthought Canopy (top) and the Spyder (bottom) integrated development environments (IDE). Both are MATLAB-like IDEs optimized for numerical computing and data analysis using Python. They also provide a file explorer, a variable explorer, or a history log among others features.*

To use the script it is necessary to run it. To do this, just click in the tool bar on the green triangle icon or go to ```Run>Run file``` in the menu bar (Fig. 2).

![Figure 2. Running a script in the Canopy editor (left) and in the IDLE editor (right)](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/RunScript_Canopy.png)  
*Figure 2. Running a script in the Enthought's Canopy (left) and Spyder (right) IDEs.*

The following text will appear in the shell/console (Fig. 1):
```
Welcome to the GrainSizeTools script v. 1.3
Your current working directory is...
To change the working directory use: os.chdir('new path')

Please to avoid problems check that your Numpy version below is 1.11 or higher:
The installed Numpy version in your system is...
```
Once you see this text, all the tools implemented in the GrainSizeTools script will be available by typing some commands in the shell as will be explained below.


### *A brief note on the organization of the script*

The script is organized in a modular way using Python functions, which facilitates to modify, reuse or extend the code if needed. A Python function looks like this in the editor:

```python
def calc_diameters(areas, addPerimeter=0):
    """ Calculate the diameters from the sectional areas via the equivalent circular
    diameter.

    PARAMETERS    
    areas:
    a numpy array with the sectional areas of the grains

    addPerimeter:
    Correct the diameters estimated from the areas by adding the perimeter of
    the grain. If addPerimeter is not declared, it is considered 0. A float or
    integer.
    """

    # calculate diameters via equivalent circular diameter
    diameters = 2 * sqrt(areas/pi)

    # diameter correction adding edges (if applicable)
    if addPerimeter != 0:
        diameters += addPerimeter

    return diameters
```

To sum up, the name following the Python keyword ```def``` -in this example ```calc_diameters```- is the name of the function. The sequence of names within the parentheses are the formal parameters of the function, the inputs. In this case the function has two inputs, the name ```areas``` that correspond with an array containing the areas of the grain profiles previously measured, and the name ```addPerimeter``` that corresponds to a number of type integer or float (i.e. an irrational number) that sometimes is necessary for correcting the size of the grains. Note that in this case the default value is set to zero. The text between the triple quotation marks provides information about the function, describing the conditions that must be met by the user and the output obtained. Below, it is the code block.

The names of the Python functions defined in the script are self-explanatory. Each function has been implemented to perform a single task. Although there are a lot of functions within the script, we will only need to use four functions (usually less than four) to obtain the required results. For more details, you can look at the section [*Specifications of main functions in the GrainSizeTools script*](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/specifications.md).

### *Using the script to visualize and estimate the grain size features*

#### Loading the data and extracting the areas of the grain profiles

The first step requires to load the areas of the grain profiles measured in the thin section. It is therefore assumed that they were estimated previously using the *ImageJ* or similar software, and that the results were saved as a txt or csv file. If you do not know how to do this, then go to the section [How to measure the grain profile areas with ImageJ](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/imageJ_tutorial.md).

![Figure 3. Tabular-like files obtaining from the ImageJ app](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/figure_imageJ_files.png)  
*Figure 3. Tabular-like files obtaining from the ImageJ app. At left, the tab-separated txt file. At right, the csv comma-separated version.*

People usually perform different kinds of measures at the same time in the *ImageJ* application. Consequently, we usually obtain a file with data in a spreadsheet-like form (Fig. 3). We only need to extract the information corresponding to the column named 'Area', which is the one that contains the areas of the grain profiles. To do this, the script implements a ad hoc function named ```extract_areas``` that automatically extract this data for us. To invoke this function we write in the shell (note that different inputs/parameters are separated by commas):

```python
>>> areas = extract_areas('C:/yourFileLocation/nameOfTheFile.csv', form='csv')
```

where ```areas``` is just a name for a Python object, also named variable, in which the data will be stored into memory. This will allow us to access and manipulate later the areas of the grain profiles. Almost any name can be used to create a variable/object in Python. As an example, if you want to load several files belonging to different datasets, you can name them ```areas1```, ```areas2``` or ```sample1``` , ```sample2``` and so on. Variable names can contain upper and lowercase letters (Python language is case-sensitive), digits and the special character *_*, but cannot start with a digit. ```extract_areas``` is the function responsible for extracting the areas and loading the data into the variable defined. Within the parentheses, it is the file location path in quotes (single or double) following by the form of the file to be read (optional). To avoid problems in Windows OS avoid single backslashes to define the filepath (e.g. "C:/yourfilelocation.../nameofthefile.txt") and use instead forward slashes (or double backslashes). The function assumes by default that the datasets were saved as txt files (Fig. 3a), so in such case it is not necessary to define the form. In contrast, if you want to read a csv file you have to specify the form as in the example above (note that in versions previous to 1.3 this parameter was named *type* instead). Once you press the Enter key, the function ```extract_areas``` will automatically extract the information corresponding for the areas of the grains and then store it in the variable. To check that everything is ok, the function will also return in the shell the first and last rows of the dataset and the first and last values of the extracted areas.

If needed, the ```extract_areas``` function also have the option of defining an *ad hoc* column name different from the default. In this case we need to add a new parameter at the end of the function named *col_name*:

```python
>>> areas = extract_areas('C:/yourFileLocation/nameOfTheFile.csv', form='txt', col_name='areas')
```
in this example set to ```'areas'``` instead of the default column name returned by the imageJ ```'Area'```

The data stored in any object/variable can be viewed at any time by invoking its name in the shell and pressing the Enter key, as follows:

```python
>>> areas
>>> array([99.6535, 41.9045, ..., 79.5712, 119.777])
```

Furthermore, both the Canopy and Spyder IDEs have a specific variable explorer to visualize all the variables loaded in the current session.

In the case that the user extracted and stored the areas of the grains with other software or manually, either in a txt or csv file but without a spreadsheet-like form (Fig. 4), there is a  Python/Numpy built-in method named ```np.genfromtxt()``` that can be used to load any data into a variable in a similar way. For example:

```python
>>> areas = np.genfromtxt('C:/yourFileLocation/nameOfTheFile.txt')
```
in case you need to skip the first or whatever number of lines because there is text or other complementary information use the *skip_header* parameter:

```python
>>> areas = np.genfromtxt('C:/yourFileLocation/nameOfTheFile.txt', skip_header=1)
```
In this example, ```skip_header=1``` means that the first line in the txt file will be ignored. You can define any number of lines to ignore.

<img src="https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/notebook.png" width="300">  
*Figure 4. A txt file without spreadsheet-like form. The first line, which is informative, has to be ignored when loading the data*

#### Estimating the apparent diameters from the areas of the grain profiles

The second step is to convert the areas into diameters via the equivalent circular diameter. This is done by a function named ```calc_diameters```. To invoke this function we write in the shell:

```python
>>> diameters = calc_diameters(areas)
```

In the example above, the only parameter declared within the parenthesis are the variable containing the areas of the grain profiles previously loaded in the object ```areas```, and the calculated diameters will be stored in an variable defined as ```diameters``` in our example. In some cases, we would need to correct the perimeter of the grain profiles (Fig. 5). For this, you need to add the following parameter within the parentheses:

```python
>>> diameters = calc_diameters(areas, addPerimeter=0.05)
```

or just

```python
>>> diameters = calc_diameters(areas, 0.05)
```

This example means that for each apparent diameter calculated from the sectional areas, 0.05 will be added. If the parameter ```addPerimeters``` is not declared within the function, as in the first example, it is assumed that no perimeter correction is needed.

<img src="https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/Fig_PS_pixels.png" width="450">  
*Figure 5. Example of perimeter correction in a grain boundary map. The figure is a raster showing the grain boundaries (in white) between three grains. The squares are the pixels of the image. The boundaries are two pixel wide, approximately. If, for example, each pixel corresponds to 1 micron, we will need to add 2 microns to the diameters estimated from the equivalent circular areas.*

Once we estimated and stored the apparent grain sizes, we have several choices: (1) estimate an unidimensional value of grain size for paleopiezometry/paleowattmetry studies, or (2) derive the actual 3D grain size distribution from the population of apparent grain sizes using the Saltykov method (Saltykov, 1967) or an extension of the Saltykov method named the two-step method (Lopez-Sanchez and Llana-Fúnez, 2016).  

#### *Obtaining an unidimensional value of grain size (paleopiezo/wattmetry studies)*

For this, we need to call the function ```find_grain_size```. This function returns several grain size measures and plots, depending on your needs. The default mode returns a frequency *vs* apparent grain size plot together with the mean, median, and frequency peak grain sizes; the latter using a Gaussian kernel density estimator (see details in [Lopez-Sanchez and Llana-Fúnez 2015](http://www.solid-earth.net/6/475/2015/se-6-475-2015.html)). Other parameters of interest are also provided, such as the bin size, the number of classes, the method used to estimate the bin size, and the bandwidth used for the Gaussian kde according to the Silverman rule (Silverman 1986). As stated in [Lopez-Sanchez and Llana-Fúnez 2015](http://www.solid-earth.net/6/475/2015/se-6-475-2015.html), **to obtain consistent results a minimum of 433 measured grain profiles are required** (error < 4% at a 95% confidence), although we recommend to measure a minimum of 965 when possible (99% confidence).

To estimate a 1D apparent grain size value we write in the shell:

```python
>>> find_grain_size(areas, diameters)
```

First note that contrary to what was shown so far, the function is called directly in the shell since it is no longer necessary to store any data into an object/variable. The inputs are the arrays with the areas and diameters previously estimated. After pressing the Enter key, the shell will show something similar to this:

```
NUMBER WEIGHTED APPROACH (linear apparent grain size):

Mean grain size = 35.79 microns
Median grain size = 32.53 microns

HISTOGRAM FEATURES
The modal interval is 27.02 - 31.52
The number of classes are 35
The bin size is 4.5 according to the scott rule

GAUSSIAN KERNEL DENSITY ESTIMATOR FEATURES
KDE peak (peak grain size) =  25.24 microns
Bandwidth = 4.01 (Silverman rule)
```

Also, a new window with a plot will also appear. The plots will show the location of the different grain size measures respect to the population of apparent grain sizes (Fig. 6). You can save the plots by clicking the floppy disk icon in the tool bar as bitmap (8 file types to choose) or to post-editing in vector image (5 file types to choose). Another interesting option is to modify the plot within the *Matplotlib* window before saving by clicking on the green tick icon in the tool bar.

Although we promote the use of frequency *vs* apparent grain size linear plot (Fig. 6a), the function allows to use other options such as the logarithmic and square-root grain sizes (Figs. 6c, d), widely used in the past, or the area-weighted grain size (e.g. Berger et al. 2011) (Fig. 6b). The advantages and disadvantages of the area weighted plot are explained in detail in [Lopez-Sanchez and Llana-Fúnez 2015](http://www.solid-earth.net/6/475/2015/se-6-475-2015.html). To do this, we need to specify the type of plot as follows:

```python
>>> find_grain_size(areas, diameters, plot='area')
```
in this example setting to use the area-weighted plot. The name of the different plots available are ```'lin'``` for the linear number-weighted plot (set as default), ```'area'``` for the area-weighted plot (as in the example above), ```'sqrt'``` for the square-root grain size plot, and ```'log'``` for the logarithmic grain size plot. Note that the selection of different type of plot also implies to obtain different grain size estimations.

Since the version 1.3 of the script, this function includes different plug-in methods to estimate an "optimal" bin size, including an automatic mode. The default automatic mode ```'auto'``` use the Freedman-Diaconis rule when using large datasets (> 1000) and the Sturges rule for small datasets. The other methods available are the Freedman-Diaconis ```'fd'```, Scott ```'scott'```, Rice ```'rice'```, Sturges ```'sturges'```, Doane ```'doane'```, and square-root ```'sqrt'``` bin sizes. For more details on the methods see [here](https://docs.scipy.org/doc/numpy/reference/generated/numpy.histogram.html). You can also use and *ad hoc* bin/class size (see an example below). We encourage you to use the default method ```'auto'```, the ```'doane'``` method in case you have a lognormal-like distribution of apparent grain sizes, or the ```'scott'``` method in case your distribution is Gaussian-like. To specify the method we write in the shell:

```python
>>> find_grain_size(areas, diameters, plot='lin', binsize='doane')
```

note that you have to define first the type of plot you want and that depending on the type of plot your distribution of apparent grain sizes will change (Fig. 6). Last, an example with a user-defined bin size will be as follows:

```python
>>> find_grain_size(areas, diameters, plot='lin', binsize=10.0)
```

The user-defined bin size can be any number of type integer or float (*i.e.* an irrational number).

![Figure 6. apparent grain size vs frequency plots](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/figure_1.png)  
*Figure 6. Different apparent grain size vs frequency plots of the same population returned by the find_grain_size function. These include the number- (linear) and area-weighted plots (upper part) and the logarithmic and square root apparent grain sizes (lower part)*

#### *Derive the actual 3D distribution of grain sizes from thin sections*

The function responsible to unfold the distribution of apparent grain sizes into the actual 3D grain size distribution is named ```derive3D```. The script implements two methods to do this, the Saltykov and the two-step methods. The Saltykov method is the best option for exploring the dataset and for estimating the volume of a particular grain size fraction. The two-step method is suitable to describe quantitatively the shape of the grain size distribution assuming that they follow a lognormal distribution. This means that the two-step method only yield consistent results when the population of grains considered are completely recrystallized or when the non-recrystallized grains can be previously discarded using shape descriptors. It is therefore necessary to check first whether the distribution of grain sizes is unimodal and lognormal-like (i.e. skewed to the right as in the example shown in figure 7). For more details see [Lopez-Sanchez and Llana-Fúnez (2016)](http://www.sciencedirect.com/science/article/pii/S0191814116301778).

***Using the Saltykov method***

To derive the actual 3D population of grain sizes using the Saltykov method (Saltykov 1967), we need to call the function ```derive3D```as follows:

```python
>>> derive3D(diameters, numbins=14)
```
Since the Saltykov method uses the histogram to derive the actual 3D grain size distribution, the inputs are an array with the apparent diameters of the grains and the desired number of bins/classes of the histogram. If the number of bins is not declared is set to ten by default. The user can use any positive **integer** value. However, it is usually advisable to choose a number not exceeding 20 classes (see later for details). After pressing the Enter key, the function will return something like this in the shell:

```
sample size = 2661
bin size = 11.26

midpoints =  [   5.63   16.89   28.14 ...,  129.45  140.71  151.97]
class freqs. (norm.) = [ 0.      0.0156  0.0223 ...,  0.      0.      0.0001]
cumulative vol. (%) = [   0.      0.78    5.96 ...,   97.97   97.97  100.  ]

A file named Saltykov_output.csv was generated
```

the arrays correspond with the midpoints, the normalized frequencies, and the normalized cumulative volume of the different classes. The text also indicates that a tabular-like csv file with the data contained in the arrays was generated. Lastly, a new window will appear showing two plots (Fig 7). On the left the frequency plot with the estimated 3D grain size distribution in a form of a histogram, and on the right as volume-weighted cumulative density curve. The latter allows the user to estimate qualitatively the percentage of volume occupied by a defined fraction of grain sizes. If the user wants to estimate quantitatively the volume of a particular grain fraction (i.e. the volume occupied by a fraction of grains less or equal to a certain value) we need to add a new parameter within the function as follows:

```python
>>> derive3D(diameters, numbins=12, set_limit=40)
```
In the example above, the grain fraction set to 40 microns means that the script will also return an estimation of the percentage of volume occupied by all the grain fractions up to 40 microns. A line similar to this will also appear in the shell:

```
volume fraction (up to 40 microns) = 22.8 %
```
As a cautionary note, if we use a different number of bins/classes, in this example set at 12, we will obtain slightly different percentages. This is normal due to the inaccuracies of the Saltykov method. In any event, Lopez-Sanchez and Llana-Fúnez (2016) proved that the absolute differences between the volume estimations using a range of classes between 10 and 20 are below ±5. This means that to stay safe we should always take an absolute error margin of ±5 in the volume estimations.

![Figure 7. 3D grain size distribution](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/figure_2.png)  
*Figure 7. The derived 3D grain size distribution and the volume-weighted cumulative grain size distribution using the Saltykov method.*

Regarding the number of bins/classes, no best number of bins exists yet (Lopez-Sanchez and Llana-Fúnez 2016). Due to the nature of the Saltykov method, the smaller the number of classes, the better the numerical stability of the method and the larger the number of classes, the better the approximation of the wanted distribution. Ultimately, the strategy to follow is about finding the maximum number of classes (i.e. the best resolution) that produces stable results. Based on experience, previous works proposed to use between 10 to 15 classes (e.g. Exner 1972), although depending on the quality of the data set it seems that it can be used safely up to 20 classes or even more (e.g. Heilbronner and Barret 2014, Lopez-Sanchez and Llana-Fúnez 2016). Yet, no method (i.e. algorithm) appears to be generally best for choosing an optimal number of classes (or bin size) for the Saltykov method. Hence, the only way to find the maximum number of classes with consistent results is to use a trial and error strategy. In the experience of the GrainSizeTools developer, the Doane's method seems to work well for this when the distribution is lognormal-like. So, if you do not want to define your own number of classes we propose the following strategy: i) use the Doane's method with the apparent grain size distribution (i.e. when using the *find_grain_size* function); ii) annotate the number of classes estimated; and iii) use this number when using the Saltykov or the two-step methods. As a last cautionary note, keep in mind that **the Saltykov method requires large samples (n ~ 1000 or larger)** to obtain consistent results, even when using a small number of classes.

***Using the two-step method***

To estimate the shape of the 3D grain size distribution, the ```derive3D``` function implements a method called "the two-step method" (Lopez-Sanchez and Llana-Fúnez, 2016). This method assumes that the actual 3D population of grain sizes follows a lognormal distribution, a common distribution observed in recrystallized aggregates. Therefore, make sure that the aggregate or the studied area within the rock/alloy/ceramic is completely recrystallized. The method applies a non-linear least squares algorithm to fit a lognormal distribution on top of the Saltykov method using the midpoints of the different classes. The script return two parameters, the **MSD** and the theoretical **median**, which they describe the lognormal distribution at their original scale, as well as the uncertainty associated with the estimations (see details in Lopez-Sanchez and Llana-Fúnez, 2016). In addition, it also returns a frequency plot showing the probability density function fitted (Fig. 8). In particular, the **MSD value** allows to describe the shape of the lognormal distribution independently of the scale of the grain size distribution, which is very convenient for comparative purposes. To apply the two-step method we need to invoke the function ```derive3D``` as follows:

```python
>>> derive3D(diameters, numbins=15, set_limit=None, fit=True)
```

Note that in this case we include a new parameter named ```fit``` that it is set to ```True``` with the "T" capitalized (it is set to ```False``` by default). The function will return something like this in the shell:

```
sample size = 2661
bin size = 11.26

midpoints =  [   5.63   16.89   28.14 ...,  129.45  140.71  151.97]
class freqs. (norm.) = [ 0.      0.0156  0.0223 ...,  0.      0.      0.0001]
cumulative vol. (%) = [   0.      0.78    5.96 ...,   97.97   97.97  100.  ]


Optimal coefficients:
 [MSD(shape) ; median]
 1.65 ; 36.91

Confidence interval
 [MSD(shape) ; median]
 0.09 ; 2.33

A file named twoStep_output.csv was generated
```

In this example, the MSD and median estimations have to be readed as MSD = 1.65 ± 0.09 and Median = 36.91 ± 2.33. The script also generates a tabular-like csv file with the data contained in the arrays. Sometimes, the least squares algorithm will fail at fitting the lognormal distribution to the unfolded data (e.g. Fig. 8b). This is due to the algorithm used to find the optimal MSD and median values, the Levenberg–Marquardt algorithm (Marquardt, 1963), only converges to a global minimum when their initial guesses are already somewhat close to the final solution. Based on our experience in quartz aggregates, the initial guesses were set by default at 1.2 and 25.0 for the MSD and median values respectively. However, when the algorithm fails it would be necessary to change these default values by adding a new parameter as follows:

```python
>>> derive3D(diameters, numbins=15, set_limit=None, fit=True, initial_guess=True)
```
When the ```initial_guess``` parameter is set to ```True```, the script will ask to set a new starting values for both parameters (it also indicates which are the default ones). Based in our experience, a useful strategy is to let the MSD value in its default value (1.2) and decreasing the median value every five units until the fitting procedure yield a good fit (*e.g.* 25 -> 20 -> 15...) (Fig. 8).

![Figure 8. Two-step method plots](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/two-step_method.png)  
*Figure 8. Plots obtained using the two-step method. At left, an example with the lognormal pdf well fitted to the data points. The shadow zone is the trust region for the fitting procedure. At right, an example with a wrong fit due to the use of unsuitable initial guess values. Note the discrepancy between the data points and the line representing the best fitting.*

#### ***Other general methods of interest***

**See the length of an array stored**

```python
>>> len(name of the variable)
>>> 2754
```

**Calculate the mean and the standard deviation of any variabe/object stored**
```python
>>> mean(name of the variable)
>>> std(name of the variable)
```

**Merging data sets**

A useful *Numpy* method to merge two or more datasets is called ```hstack()```, which stack arrays in sequence as follows (*please, note the use of double parenthesis*):

```python
>>> np.hstack((name of the array1, name of the Array2,...))
```

As an example if we have two different data sets and we want to merge the areas and the diameters estimated in a single variable we write into the Python shell (variable names are just random examples):

```python
>>> all_areas = np.hstack((areas1, areas2))
>>> all_diameters = np.hstack((diameters1, diameters2))
```

Note that in this example we merged the original data sets into two new variables named ```all_areas``` and ```all_diameters``` respectively. Therefore, we do not overwrite any of the original variables and we can used them later if required. In contrast, if you use a variable name already defined:

```python
>>> areas1 = np.hstack((areas1, areas2))
```
The variable ```areas1``` is now a new array with the values of the two data sets, and the original dataset stored in the variable ```areas1``` no longer exists since these variables (strictly speaking Numpy arrays) are mutable Python objects.

**Loading several data sets: the fastest (appropriate) way**

If you need to load a large number of data sets, you probably prefer not having to specify the absolute file paths of each file. Python establishes by default a current working directory in which all the files can be accessed directly by specifying just the name of the file (or a relative path if they are in a sub-folder). For example, if the current working directory is ```c:/user/yourname```, you no longer need to specify the entire file path for the files stored within this directory. For example, to load a csv file named 'my_sample.csv' stored in that location you just need to write:

```python
>>> areas = extract_areas('my_sample.csv', form='csv')
```
or in the case that the file 'my_sample.csv' were stored in ```c:/user/yourname/my_samples``` we will write:
```python
>>> areas = extract_areas('my_samples/my_sample.csv', form='csv')
```
and so on.

When you run the script for the first time, your current working directory will appear in the Python shell. Also, you can retrieve your current working directory at any time by typing in the shell ```os.getcwd()```, as well as modify it to another path using the function ```os.chdir('new default path')```. Note that the new file path defined within the parentheses is in quotes. The same rules apply when using the ```np.genfromtxt``` method.

> Note: although it depends on the Python package you have installed, usually the current working directory is the same directory where the script is located. Hence, in general it is a good idea to locate the scrip in the same directory where the datasets are located.

[next section](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/specifications.md)  
[table of contents](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/tableOfContents.md)

----------
