Getting Started: A step-by-step tutorial
-------------

> **Note**
> This tutorial assumes that the user know nothing about Python programming language. Hence no previous knowledge of the Python programming language is needed to use the script and obtain the results.

### *Running the script*

Once you download the latest version of the GrainSizeTools script (make sure you have the 1.2 version) and the required software installed in your system (see [requirements](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/Requirements.md)), open the script with the Canopy editor -if you installed the Enthought Canopy package-, or the IDLE/Spyder editor -if you installed the Anaconda package- and run the code. To do this, if you are in the Canopy or the Spyder editor just click on the green play icon in the tool bar or go to *Run* in the menu bar and click on “Run file” (Fig. 1). If you open the script in the IDLE, just press F5 or go to *Run* and click on “Run module” (Fig. 1).

![Figure 1. Running a script in the Canopy editor (left) and in the IDLE editor (right)](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/RunScript_Canopy.jpg)  
*Figure 1. Running a script in the Enthought's Canopy editor (left) and the IDLE (right).*

The following text will appear in the Python shell (Fig. 2):
```
Welcome to the GrainSizeTools script v. 1.2
Your current working directory is C:\...
To change the working directory use: os.chdir('new path')
```
![Figure 2. The Python editor and the shell in the Enthought Canopy environment](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/Canopy_env.png)  
*Figure 2. The Python editor and the Python shell in the Enthought Canopy environment.*

### *A brief note on the organization of the script*

The script is organized in a modular way using Python functions, which facilitates to modify, reuse or extend the code if required. A Python function looks like this in the script:

```python
def calc_diameters(areas, addPerimeter = 0):
    """ Calculate the diameters from the sectional areas assuming that the grains
    have near-equant shapes. It returns a numpy array with the apparent diameters
    calculated.

    PARAMETERS    
    areas:
    a numpy array with the sectional areas of the grains

    addPerimeter:
    a float or integer. Correct the diameters estimated from the
    areas by adding the perimeter of the grain. If addPerimeter is not
    declared, it is considered 0
    """

    # calculate diameters via equivalent circular diameter
    diameters = 2*sqrt(areas/pi)

    # diameter correction adding edges (if applicable)
    if addPerimeter != 0:
        diameters = diameters + addPerimeter

    return diameters
```

To sum up, the name following the Python keyword ```def``` -in this example ```calc_diameters```- is the name of the function. The sequence of names within the parentheses are the formal parameters of the function -the inputs-. In this case the function has two inputs, the name ```areas``` that correspond with an array containing the areas of the grain profiles previously measured, and the name ```addPerimeter``` that corresponds to a number of type integer or float (i.e. an irrational number) that sometimes is necessary for correcting the size of the grains. Note that in this case the default value is set to zero. The text between the triple quotation marks provides information about the function describing the conditions that must be met by the users and the output obtained. Below this, there is the code block.

The names of the Python functions defined in the script are intuitive and self-explanatory. To obtain the results, it is necessary to use four (and usually less than four) of all the functions implemented within the script. For details, look at the section [*Specifications of main functions in the GrainSizeTools script*](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/specifications.md).

### *Using the script to estimate the grain size*

#### Loading the data and extracting the areas of the grain profiles

The first step is to load the data. It is assumed that previously to this step, the areas of the grain profiles was calculated using the *ImageJ* or similar software, and that the result was saved as a txt or csv file (Fig. 3). If you do not know how to do this go to the section [How to measure the grain profile areas with ImageJ](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/imageJ_tutorial.md).

![Figure 3. Tabular-like files obtaining from the ImageJ app](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/figure_imageJ_files.png)  
*Figure 3. Tabular-like files obtaining from the ImageJ app. At left, the txt file. At right, the csv (comma-separated) version.*

As shown in figure 3, we obtain a file with data in a spreadsheet-like form from the *ImageJ* application. Consequently, we need to extract the information corresponding to the column named 'Area', which is the one that contains the areas of the grain profiles. To do this, the script implements a function named ```extract_areas``` that automatically extract this data for us (*Note: in versions before 1.1 this function was named* ```importdata``` instead). To invoke this function we write in the shell (note that different inputs/parameters are separated by commas):

```python
>>> areas = extract_areas('C:/yourFileLocation/nameOfTheFile.csv', type = 'csv')
```

where ```areas``` is just a name for a Python object, also named variable, in which the data will be stored into memory. This will allow us to manipulate later the areas of the grain profiles when required. Almost any name can be used to create a variable in Python. As an example, if you want to load several files belonging to different datasets, you can name them ```areas1```, ```areas2``` or ```sample1``` , ```sample2``` and so on. Variable names can contain upper and lowercase letters, digits and the special character *underscore*, but cannot start with a digit. ```extract_areas``` is the function responsible for extracting the areas and loading the data into the variable defined. Within the parentheses, it is the file location path in the OS in quotes (single or double) following by the type of the file to be read (optional). To avoid problems in windows, make sure that you use a forward slash (or double backslashes) instead of single backslashes to define the filepath (e.g. "C:/yourfilelocation.../nameofthefile.txt"). The function assumes by default that the datasets were saved as txt files (Fig. 3a), so in such case it is not necessary to define the type. In contrast, if you want to read a csv file you have to specify the type (as in the example above). Once you press the Enter key, the function ```extract_areas``` will automatically extract the information corresponding for the areas of the grains. To check that everything is ok, the function will also return in the shell the first rows of the dataset and the first and last values of the extracted values.

If needed, the ```extract_areas``` function also have the option of defining a different column name. In this case we need to add a new parameter at the end:

```python
>>> areas = extract_areas('C:/yourFileLocation/nameOfTheFile.csv', type = 'txt', col_name='areas')
```
in this example set to ```'areas'``` instead of the default column name returned by the imageJ ```'Area'```

In the case that the user extracted and stored the areas of the grains manually, either in a txt or csv file (i.e. without a spreadsheet-like form; Fig. 4), you can use the built-in method ```np.genfromtxt()``` to load the data into a variable in a similar way. As an example:

```python
>>> areas = np.genfromtxt('C:/yourFileLocation/nameOfTheFile.txt')
```
or
```python
>>> areas = np.genfromtxt('C:/yourFileLocation/nameOfTheFile.txt', skip_header = 1)
```
if you need to skip the first or whatever number of lines because there is text or other information. In this example, the parameter ```skip_header = 1``` means that the first line in the txt file is not considered, but you can define any number of lines to skip.

<img src="https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/notebook.jpg" width="350">  
*Figure 4. A txt file without spreadsheet-like form.*

> **Hint**: If you need to load a large number of data sets, you probably prefer not having to specify the absolute file paths of all of them. Python establishes by default a current working directory in which all the files can be accessed directly by specifying just the name of the file (or a sub-folder and the name of the file; *i.e.* a relative path). For example, if your current working directory is ```c:/user/yourname```, this means that you no longer need to specify the entire file path for all the files stored within this directory. For example, to load a csv file named 'my_sample.csv' that it is stored in that location you just need to write:
>
> ```python
>>>> areas = extract_areas('my_sample.csv', type = 'csv')
>```
>  In the case that the file 'my_sample.csv' were stored in ```c:/user/yourname/my_samples``` we will write:
> ```python
>>>> areas = extract_areas('my_samples/my_sample.csv', type = 'csv')
>```
> and so on. When you run the script, the script shows your current working directory. Also, you can retrieve your current working directory at any time by typing in the shell ```os.getcwd()``` and modify it to another path using the function ```os.chdir('new default path')```. Note that the new file path defined within the parentheses is in quotes. This also works when using the ```np.genfromtxt``` method.

The data stored in any variable can be viewed at any time by invoking the name of the variable in the shell and pressing the Enter key, as follows:

```python
>>> areas
>>> array([99.6535, 41.9045, ..., 79.5712, 119.777])
```

Furthermore, both the Canopy and the Spyder editors have a specific variable explorer to visualize the variables available in the current session. Lastly, to see the length of an array stored use the ```len()``` method:

```python
>>> len(areas)
>>> 2754
```
#### Estimating the apparent diameters from the areas of the grain profiles

The second step is to convert the areas into diameters via the equivalent circular diameter. For this, it was implemented a function named ```calc_diameters```. To invoke this function we write in the shell:

```python
>>> diameters = calc_diameters(areas)
```

In the example above, the only parameter declared within the parenthesis are the variable containing the areas of the grain profiles previously loaded in the variable named ```areas```. In some cases, we need to correct the perimeter of the grain profiles (Fig. 5). For this, just add the following parameter within the parentheses:

```python
>>> diameters = calc_diameters(areas, addPerimeter = 0.05)
```

or just

```python
>>> diameters = calc_diameters(areas, 0.05)
```

This example means that for each apparent diameter calculated from the sectional areas, 0.05 is added. If the parameter ```addPerimeters``` is not declared within the function, as in the example above, it is assumed that no perimeter correction is needed.

<img src="https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/Fig_PS_pixels.png" width="500">  
*Figure 5. Example of perimeter correction. The figure shows the boundaries (in white) between three grains in a grain boundary map. The squares are the pixels of the image. The boundaries are two pixel wide approximately. If, for example, each pixel corresponds to 1 micron, we need to add 2 microns to the diameters estimated from the equivalent circular areas.*

Once the sectional areas and the apparent grain sizes were calculated and stored, we have two choices: (1) estimate an unidimensional value of grain size for paleopiezometry/paleowattmetry studies, or (2) derive the actual 3D grain size distribution from the population of apparent grain sizes using the Saltykov method (Saltykov, 1967) or an extension of the Saltykov method named the two-step method (Lopez-Sanchez and Llana-Fúnez, *in review*).

#### *Obtaining an unidimensional value of grain size (paleopiezometry/paleowattmetry studies)*

In case we want to obtain a 1D value of grain size, we need to call the function ```find_grain_size```. This function returns several grain size measures and plots, depending on your needs. The default mode returns a frequency *vs* apparent grain size plot as well as the mean, median, and frequency peak grain sizes using a Gaussian kernel density estimator (see details in [Lopez-Sanchez and Llana-Fúnez 2015](http://www.solid-earth.net/6/475/2015/se-6-475-2015.html)). Other parameters of interest are also provided, such as the bin size, the method used in such estimation, and the bandwidth used for the Gaussian kde according to the Silverman rule (Silverman 1986). As stated in [Lopez-Sanchez and Llana-Fúnez 2015](http://www.solid-earth.net/6/475/2015/se-6-475-2015.html), **a minimum of 433 measured grain profiles are needed to obtain consistent results** (95% confidence), although we recommend to measure a minimum of 965 when possible (99% confidence). For this, we write in the shell:

```python
>>> find_grain_size(areas, diameters)
```

Note that contrary to what was shown so far, the function is called directly since it is no longer necessary to store any data into an object/variable. The inputs are the arrays with the areas and diameters previously estimated and, if desired, the bin size. The function includes two plug-in methods to estimate an 'optimal' bin size, the Scott (Scott, 1979) and the Freedman-Diaconis (Freedman and Diaconis, 1981) rules. The function uses by default the Scott rule. If you want to use the Freedman-Diaconis rule or an user-defined bin size value, it can be do it as follows:

```python
>>> find_grain_size(areas, diameters, plot = 'freq', binsize = 'FD')
```

note that you have to define first the type of plot you want (in this case set to 'freq' see later for other options) and that the acronym is in quotes with both letters capitalized. An example with a user-defined bin size will be:

```python
>>> find_grain_size(areas, diameters, plot = 'freq', binsize = 10.0)
```

The user-defined bin size can be any number of type integer or float (*i.e.* an irrational number). The Freedman-Diaconis rule is a better option over the Scott rule when the user suspect that there are outliers in the population of apparent grain sizes.

Although we promote the use of frequency *vs* apparent grain size plot, the function allows to use other options such as the area-weighted approach (e.g. Berger et al. 2011) (Fig. 6b). The advantages and disadvantages of the area weighted plot are explained in detail in [Lopez-Sanchez and Llana-Fúnez 2015](http://www.solid-earth.net/6/475/2015/se-6-475-2015.html). Also, since in the past some authors used the logarithmic or square root grain sizes instead of using the actual apparent diameters, the function also allows to estimate such grain sizes. To do this, we need to specify the type of plot as follows:

```python
>>> find_grain_size(areas, diameters, plot = 'area')
```
for the area-weighted approach or

```python
>>> find_grain_size(areas, diameters, plot = 'log')
```
for estimating the logarithmic grain size (or ```'sqrt'``` for the square root grain size).

After pressing the Enter key, the different 1D measures and a new window with a plot will appear (Fig. 6). The plots show the location of the different grain sizes estimated respect to the population of apparent grain sizes. You can save the plots by clicking in the floppy disk icon as bitmap (8 file types to choose) or vector image (5 file types to choose) to post-editing. Another interesting option is to modify the plot within the *Matplotlib* environment before saving. For this, just click the green tick icon in the tool bar.

![Figure 6. apparent grain size vs frequency plots](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/figure_1.png)  
*Figure 6. Different apparent grain size vs frequency plots returned by the find_grain_size function. These include the number- and area-weighted plots (upper part) and the logarithmic and square root apparent grain sizes (lower part) *

#### *Derive the actual 3D distribution of grain sizes*

The function responsible to unfold the distribution of apparent grain sizes into the actual 3D grain size distribution is named ```derive3D```. In the script, the first line of the function looks like this:

```python
def derive3D(diameters, numbins=10, set_limit=None, fit=False, initial_guess=False):
```
As specified above, the script implements two methods to do this, the Saltykov and the two-step methods. The Saltykov method is the best option estimating the volume of particular grain size fraction, which is essential to describe the creep behaviour using composite flow laws (e.g. Freeman and Ferguson 1986). In contrast, the two-step method is suitable to describe quantitatively the distribution of grain sizes assuming that they follow a lognormal distribution. This means that the two-step method only yield consistent results when the population of grains considered are completely recrystallized or when the non-recrystallized grains can be previously discarded using shape descriptors (i.e. unimodal lognormal-like distributions). For details see [Lopez-Sanchez and Llana-Fúnez (in review)]().

***Using the Saltykov method***

To derive the actual 3D population of grain sizes using the Saltykov method (Saltykov 1967), we need to call the function ```derive3D```as follows:

```python
>>> derive3D(diameters, numbins=15)
```
Since the Saltykov method uses the histogram to derive the actual 3D grain size distribution, the inputs are an array with the apparent diameters of the grains and the desired number of bins/classes of the histogram. If the number of bins is not declared is set to ten by default. In any event, the user can use any positive **integer** value. However, it is advisable to choose a number smaller than 20 classes (see later for details).

After pressing the Enter key, the function will return the bin size estimated, an array with the normalized frequencies of the different classes, and a new window with two plots (Fig 7). In the new window, at left there are a frequency plot showing the estimated 3D grain size distribution in a form of a histogram and, at right, a volume-weighted cumulative density curve. The latter allow the user to estimate graphically the percentage of volume occupied by a defined fraction of grain sizes. In the case we want to estimate quantitatively the volume of a particular grain fraction (i.e. the volume occupied by a fraction of grains less or equal to a certain value) we need to add a new parameter within the parenthesis as follows:

```python
>>> derive3D(diameters, numbins=12, set_limit=40)
```
In the example above, the grain fraction is set to 40 microns, which means that the script will return an estimation of the volume occupied by all the grain fractions up to 40 microns. As a cautionary note, if we use a different number of bins/classes (in this random example set at 12), we will obtain slightly different results. This is normal due to the inaccuracies of the Saltykov method. In any event, Lopez-Sanchez and Llana-Fúnez (*in review*) proved that the absolute differences between the volume estimations using a range of number of classes in the 10 to 20 interval are less than ±5, which means that to stay safe we should always take an absolute error margin of ±5 in the volume estimations.

![Figure 7. 3D grain size distribution](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/figure_2.png)  
*Figure 7. The derived 3D grain size distribution and the volume-weighted cumulative grain size distribution using the Saltykov method.*

Regarding the number of bins/classes there is no best number of bins since it depends on a number of factors, such as the length and the features of the data set. Due to the nature of the Saltykov method, the smaller the number of classes, the better the numerical stability of the method. In contrast, the larger the number of classes, the better the approximation of the wanted distribution. Ultimately, the strategy to follow is about finding the maximum number of classes (i.e. the best resolution) that produces stable results. Based on experience, previous works using the Saltykov method proposed to use between 10 to 15 classes (e.g. Exner 1972), although depending on the quality of the data set it seems that it can be used safely up to 20 classes (e.g. Heilbronner and Barret 2014, Lopez-Sanchez and Llana-Fúnez *in review*). Yet, no method (i.e. algorithm) appears to be generally best for choosing an optimal number of classes (or bin size) for the Saltykov method. Hence, the only way to find the maximum number of classes that produces a consistent results is to use a trial and error strategy. As a last cautionary note, to obtain consistent results using **the Saltykov method requires large samples (n ~ 1000 or larger)** even when using a small number of classes.

***Using the two-step method***

To estimate quantitatively the actual 3D grain size distribution, the ```derive3D``` function implements since version 1.0 a new method called "the two-step method" (Lopez-Sanchez and Llana-Fúnez, *in review*). This method assumes that the actual 3D population of grain sizes follows a lognormal distribution, which in a deformed rock means that the rock or the studied area within the rock is completely recrystallized. Therefore, to apply the method it is advisable to use the Saltykov method first to observe qualitatively whether the derived distribution of grain sizes is unimodal (i.e. one frequency peak) and lognormal-like, i.e. the population is skewed to the right as in the example in figure 7. The method applies a non-linear least squares algorithm to fit a lognormal distribution on top of the Saltykov method using the midpoints of the different classes. The script return two parameters, the **MSD** and the **median**, which they describe the lognormal distribution at their original scale, as well as the errors associated with the estimation (see details in Lopez-Sanchez and Llana-Fúnez, *submitted*). In addition, it also returns a frequency plot showing the probability density function fitted (Fig. 8). To apply the two-step method we need to invoke the function ```derive3D``` as follows:

```python
>>> derive3D(diameters, numbins=15, set_limit=None, fit=True)
```

Note that in this case we include a new parameter named ```fit``` that it is set to ```True``` with the "T" capitalized (it is set to ```False``` by default). Sometimes, the least squares algorithm will fail at fitting the lognormal distribution to the unfolded data (e.g. Fig. 8). This is due to the Levenberg–Marquardt algorithm (Marquardt, 1963) used to find the optimal MSD and median values. Indeed, this procedure only converges to the global minimum when their initial guesses are already somewhat close to the final solution. Based on our experience, this initial guesses were set by default at 1.2 and 25.0 for the MSD and median values, respectively. However, when the algorithm fails it is necessary to change these default values by adding a new parameter in the ```derive3D``` function as follows:

```python
>>> derive3D(diameters, numbins=15, set_limit=None, fit=True, initial_guess=True)
```
When the ```initial_guess``` parameter is set to ```True```, the script will ask you about the new guess values for both parameters (it also indicates which are the default ones). Based on our experience, a wise strategy is to let the MSD value in its default value (1.2) and decrease the median value every five units until the fitting procedure yield a coherent result (*e.g.* 25 -> 20 -> 15...) (Fig. 8).

![Figure 8. Two-step method plots](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/two-step_method.png)  
*Figure 8. Plots obtained using the two-step method. At left, an example with the lognormal pdf well fitted to the data points. The shadow zone is the trust region for the fitting procedure. At right, an example with a wrong fit due to the use of unsuitable initial guess values. Note the discrepancy between the data points and the line representing the best fitting.*

#### *Other general methods of interest*

**Calculate the mean and the standard deviation of an array stored**
```python
>>> mean(the name of the variable)
>>> std(the name of the variable)
```

**Merging data sets**

A useful *Numpy* method to merge two or more datasets is called ```hstack()```, which stack arrays in sequence as follows (*note the use of double parenthesis*):

```python
>>> np.hstack((name of the array1, name of the Array2,...))
```

As an example if we have two different data sets and we want to merge the areas and the diameters estimated in a single variable we write into the Python shell (variable names are just random examples):

```python
>>> all_areas = np.hstack((areas1, areas2))
>>> all_diameters = np.hstack((diameters1, diameters2))
```

Note that in this example we merged the original data sets into two new variables named ```all_areas``` and ```all_diameters```, respectively. Therefore, we do not overwrite any of the original variables and we can used them later if required. In contrast, if you use a variable name already defined:

```python
>>> areas1 = np.hstack((areas1, areas2))
```
The variable ```areas1``` is now a new array with the values of the two data sets, and the original dataset stored in the variable ```areas1``` no longer exists since these variables (Strictly speaking named Numpy arrays) are mutable Python objects.

[next section](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/specifications.md)  
[table of contents](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/tableOfContents.md)

----------
