Getting Started: A step-by-step tutorial
-------------

> **Note:**
> This tutorial assumes no previous knowledge of the Python programming language. Please, **update as soon as possible to version 1.3.1**, it contains important changes that are not fully compatible with previous versions.

### *Open and running the script*

Once you installed the required software (see [requirements](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/Requirements.md)) and downloaded the latest version of the GrainSizeTools script (make sure it is the 1.3.1 version), you will need to open the script in a integrated development environment (IDE) to interact with it (Fig. 1). For this, open the Canopy IDE -if you installed the Enthought Canopy package-, or the Spyder IDE -if you installed the Anaconda package- and open the GrainSizeTools script using ```File>Open```. The script will appear in the editor as shown in figure 1.

![Figure 1. The Python editor and the shell in the Enthought Canopy environment](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/IDEs.png)  
*Figure 1. The editor and the Python shell (aka. the console) in the Enthought Canopy (top) and the Spyder (bottom) integrated development environments (IDE). Both are MATLAB-like IDEs optimized for numerical computing and data analysis using Python. They also provide a file explorer, a variable explorer, or a history log among others features.*

To use the script it is necessary to run it. To do this, just click in the tool bar on the green triangle icon or go to ```Run>Run file``` in the menu bar (Fig. 2).

![Figure 2. Running a script in the Canopy editor (left) and in the IDLE editor (right)](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/RunScript_Canopy.png)  
*Figure 2. Running a script in the Enthought's Canopy (left) and Spyder (right) IDEs.*

The following text will appear in the shell/console (Fig. 1):
```
Welcome to the GrainSizeTools script v. 1.3.1
Your current working directory is...
To change the working directory use: os.chdir('new path')

Please to avoid problems check that your Numpy version below is 1.11 or higher:
The installed Numpy version in your system is...
```
Once you see this text, all the tools implemented in the GrainSizeTools script will be available by typing some commands in the shell as will be explained below.

### *A brief note on the organization of the script*

The script is organized in a modular way using Python functions, which helps to modify, reuse or extend the code if needed. A Python function looks like this in the editor:

```python
def calc_diameters(areas, correct_diameter=0):
    """ Calculate the diameters from the sectional areas via the equivalent circular
    diameter.

    PARAMETERS    
    areas:
    a numpy array with the sectional areas of the grains

    correct_diameter:
    Correct the diameters estimated from the areas of the grains by adding the
    the width of the grain boundaries. If correct_diameter is not declared, it
    is considered 0. A float or integer.
    """

    # calculate diameters via equivalent circular diameter
    diameters = 2 * sqrt(areas/pi)

    # diameter correction adding edges (if applicable)
    if correct_diameter != 0:
        diameters += correct_diameter

    return diameters
```

To sum up, the name following the Python keyword ```def```, in this example ```calc_diameters```, is the name of the function. The sequence of names within the parentheses are the formal parameters of the function, the inputs. In this case the function has two inputs, the arameter ```areas``` that correspond with an array containing the areas of the grain profiles previously measured, and the parameter ```correct_diameter``` that corresponds to a number of type integer or float (i.e. an irrational number) that sometimes is required for correcting the size of the grains. Note that in this case the default value is set to zero. The text between the triple quotation marks provides information about the function, describing the conditions that must be met by the user and the output obtained. This information can be accessed from the shell by using the command help() and specifying the name of the function within the parentheses or, in the Spyder IDE, by pressing Ctrl+I once you wrote the name of a function. Below, it is the code block.

The names of the Python functions in the script are self-explanatory and each one has been implemented to perform a single task. Although a lot of functions exist within the script, we will only need to use four, and usually less than four, to obtain the results. For more details, you can look at the section [*Specifications of main functions in the GrainSizeTools script*](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/specifications.md).

### *Using the script to visualize and estimate the grain size features*

#### Loading the data and extracting the areas of the grain profiles

The first step requires to load the areas of the grain profiles measured in the thin section. It is therefore assumed that they were previously estimated with the *ImageJ* or similar software, and that the results were saved as a txt or csv file. If you do not know how to do this, then go to the section [How to measure the grain profile areas with ImageJ](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/imageJ_tutorial.md).

![Figure 3. Tabular-like files obtaining from the ImageJ app](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/figure_imageJ_files.png)  
*Figure 3. Tabular-like files obtaining from the ImageJ app. At left, the tab-separated txt file. At right, the csv comma-separated version.*

People usually perform different types of measures at the same time in the *ImageJ* application. Consequently, we usually obtain a text file with the data in a spreadsheet-like form (Fig. 3). In our case, we need to extract the information corresponding to the column named 'Area', which is the one that contains the areas of the grain profiles. To do this, the script implements a function named ```extract_areas``` that automatically do this data for us. To invoke this function we write in the shell:

```python
>>> areas = extract_areas()
```
where ```areas``` is just a name for a Python object, known as variable, in which the data extracted will be stored into memory. This will allow us to access and manipulate later the areas of the grain profiles using other functions. Almost any name can be used to create a variable in Python. As an example, if you want to load several files belonging to different datasets, you can name them ```areas1```, ```areas2``` or ```my_data1``` , ```my_data2``` and so on. In Python variable names can contain upper and lowercase letters (the language is case-sensitive), digits and the special character *_*, but cannot start with a digit. In addition, there are some special keywords reserved for the Python language (e.g. True, False, if, else, etc.). Do not worry about it, the shell will highlight the word if you are using one of these. The function ```extract_areas``` is responsible for automatically extracting the areas from the dataset and loading them into the variable defined. Since the script version 1.3.1, you do not need to introduce any parameter/input within the parentheses. Once you press the Enter key, a new window will pop up showing a file selection dialog so that you can search and open the file that contains the dataset. Then, the function will automatically extract the information corresponding to the areas of the grains profiles and store them into the variable. To check that everything is ok, the shell will return the first and last rows of the dataset and the first and last values of the areas extracted as follows:

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

In this example, we introduced two different inputs/parameters within the parentheses. The first one is responsible for defining the file path. In this case it is set to 'auto', which means that the automatic mode showed above is on. The second one is the column name (col_name), in this example set to ```'areas'``` instead of the default ```'Area'```. Note that different inputs/parameters are comma-separated.

Another option, which was the only one available in previous versions (< v1.3.1), is to introduce the inputs/parameters manually. For this write in the shell:

```python
>>> areas = extract_areas('C:/...yourFileLocation.../nameOfTheFile.csv', col_name='areas')
```

in this case we define the file location path in quotes, either single or double, following by the column name if required. If the column name is 'Areas' you just need to write the file path. To avoid problems in Windows OS do not use single backslashes to define it and use instead forward slashes (e.g. "C:/yourfilelocation.../nameofthefile.txt") or double backslashes. Also note that you won't need to specify the file type (txt or csv) as in previous versions of the script.

In the case that the user extracted and stored the areas of the grains in a different form from the one proposed here, this is either in a txt or csv file but without a spreadsheet-like form (Fig. 4), there is a Python/Numpy built-in method named ```np.genfromtxt()``` that can be used to load any text data (txt or csv) into a variable in a similar way. For example:

```python
>>> areas = np.genfromtxt('C:/yourFileLocation/nameOfTheFile.txt')
```
or if you need to skip the first or any other number of lines because there is text or complementary information, then use the *skip_header* parameter:

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

The parameter declared within the parenthesis are the name of the variable that contains the areas of the grain profiles. Also, we need to define a new variable to store the diameters estimated from the areas, in this example defined as ```diameters```. In some cases, we would need to correct the size of the grain profiles (Fig. 5). For this, you need to add a new parameter within the parentheses:

```python
>>> diameters = calc_diameters(areas, correct_diameter=0.05)
```

This example means that for each apparent diameter calculated from the sectional areas, 0.05 will be added. If the parameter ```correct_diameter``` is not declared within the function, as in the first example, it is assumed that no diameter correction is needed.

<img src="https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/Fig_PS_pixels.png" width="450">  
*Figure 5. Example of correction of sizes in a grain boundary map. The figure is a raster showing the grain boundaries (in white) between three grains. The squares are the pixels of the image. The boundaries are two pixel wide, approximately. If, for example, each pixel corresponds to 1 micron, we will need to add 2 microns to the diameters estimated from the equivalent circular areas.*

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

Since the version 1.3 of the script, this function includes different plug-in methods to estimate an "optimal" bin size, including an automatic mode. The default automatic mode ```'auto'``` use the Freedman-Diaconis rule when using large datasets (> 1000) and the Sturges rule for small datasets. The other methods available are the Freedman-Diaconis ```'fd'```, Scott ```'scott'```, Rice ```'rice'```, Sturges ```'sturges'```, Doane ```'doane'```, and square-root ```'sqrt'``` bin sizes. For more details on the methods see [here](https://docs.scipy.org/doc/numpy/reference/generated/numpy.histogram.html). You can also use and *ad hoc* bin/class size (see an example below). We encourage you to use the default method ```'auto'```, or the ```'doane'``` and ```'scott'``` methods in case you have a lognormal- or a normal-like distribution respectively. To specify the method we write in the shell:

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

Regarding the number of bins/classes, no best number of bins exists yet (Lopez-Sanchez and Llana-Fúnez 2016). Due to the nature of the Saltykov method, the smaller the number of classes, the better the numerical stability of the method and the larger the number of classes, the better the approximation of the wanted distribution. Ultimately, the strategy to follow is about finding the maximum number of classes (i.e. the best resolution) that produces stable results. Based on experience, previous works proposed to use between 10 to 15 classes (e.g. Exner 1972), although depending on the quality of the dataset it seems that it can be used safely up to 20 classes or even more (e.g. Heilbronner and Barret 2014, Lopez-Sanchez and Llana-Fúnez 2016). Yet, no method (i.e. algorithm) appears to be generally best for choosing an optimal number of classes (or bin size) for the Saltykov method. Hence, the only way to find the maximum number of classes with consistent results is to use a trial and error strategy. In the experience of the GrainSizeTools developer, the Doane's method seems to work well for this when the distribution is lognormal-like. So, if you do not want to define your own number of classes we propose the following strategy: i) use the Doane's method with the apparent grain size distribution (i.e. when using the *find_grain_size* function); ii) annotate the number of classes estimated; and iii) use this number when using the Saltykov or the two-step methods. As a last cautionary note, keep in mind that **the Saltykov method requires large samples (n ~ 1000 or larger)** to obtain consistent results, even when using a small number of classes.

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

> Note: usually the current working directory is the same directory where the script is located (although this depends on the Python environment you installed). Hence, in general it is a good idea to locate the scrip in the same directory where the datasets are located.

[next section](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/specifications.md)  
[table of contents](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/tableOfContents.md)

----------
