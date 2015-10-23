Getting Started: A step-by-step tutorial on how to use the script
-------------

> **Note**
> This step-by-step tutorial assumes that you do not know anything about Python programming language. This means that it is no necessary a prior knowledge of Python language to use the script and get the results. Just follow the instructions.

### *Running the script*

Once the required software is installed in your system (see [requirements](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/Requirements.md)) and the script downloaded, the first thing is to open the script in a Python editor, such as the Canopy editor -if you installed the Enthought Canopy package-, the IDLE -the Python default editor- or the Spyder editor -a scientific Python development environment that comes with the Anaconda package-, and run the code. For this, if you are in the Canopy or the Spyder editor just click on the play green icon or go to the *Run* menu and click on “Run file” (Fig. 1). If you open the script in the IDLE, just press F5 or go to the *Run menu* and click on “Run module” (Fig. 1).

![Figure 1. Runnig a script in the Canopy editor (left) and in the IDLE editor (right)](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/RunScript_Canopy.jpg)  
*Figure 1. Runnig a script in the Enthought's Canopy editor (left) and the IDLE (right)*

The following statement will appear in the Python shell (Fig. 2):
```python
Welcome to the GrainSizeTools script v. 1.0
See release notes in the Readme.txt file
```
![Figure 2. The Python editor and the shell in the Enthought Canopy environment](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/Canopy_env.png)  
*Figure 2. The Python editor and the Python shell in the Enthought Canopy environment*

### *Organization of the script*

The script is organized in a modular way using Python functions, which facilitates to modify, reuse or extend the code if required. A Python function looks like this in the editor: 

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

To sum up, the name following the Python keyword ```def``` - in this example ```calc_diameters```- is the name of the function. The sequence of names within the parentheses are the formal parameters of the function -the inputs-. In this case, there are two inputs, the name ```areas``` that correspond with an array containing the areas of the grain profiles previously measured, and the name ```addPerimeter``` that corresponds to a number of type integer or float (i.e. an irrational number) that sometimes is necessary for correcting the size of the grains. Note that in this case the default value is set to zero. The text between the triple quotation marks provides information about the function describing the conditions that must be met by the users and the output obtained. Below this, there is the code block.

The names of the Python functions defined in the script are intuitive and self-explanatory. To get the results, it is only necessary to use four (and usually less than four) of all the functions implemented within the script. For details, you can take a look at the section [*Specifications of main functions in the GrainSizeTools script*](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/specifications.md).

### *Using the script to estimate grain size features*

#### Loading the data

The first step is to load the data into memory. It is assumed that previously to this step, the areas of the grain profiles was calculated using the *ImageJ* software and that the result was saved as a txt or csv file (Fig. 3). If you do not know how to obtain this, take a look at the section [A brief tutorial on how to measure the grain profile areas with ImageJ](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/imageJ_tutorial.md). 

![Figure 3. Tabular-like files obtaining from the ImageJ app](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/figure_imageJ_files.png)  
*Figure 3. Tabular-like files obtaining from the ImageJ app. At left, the txt file. At right, the csv (comma-separated) version*

As you can see in figure 3, we obtain a file with data in a tabular (spreadsheet-like) form from the *ImageJ* application. This means that we will need to extract the information corresponding to the column named 'Area', which is the one that contains the necessary information required by the script. To do this, the script implements a function named ```importdata``` that automatically extract this data for us (*Note: this feature has been implemented in the version 1.0 that it will be released soon*). To invoke this function we write in the Python shell:

```python
>>> areas = importdata('C:/yourFileLocation/nameOfTheFile.csv', type = 'csv')
```

where ```areas``` is just a name for a Python object, also known as variable, in which the data could be stored into memory. This will allow us to later manipulate the areas of the grains when required. Almost any name can be used to create a variable in Python. As an example, if you want to load a number of files belonging to different datasets, you can name them ```areas1```, ```areas2``` or ```areas_sample1``` , ```areas_sample2``` and so on. Variable names can contain upper- and lowercase letters, digits and the special character '_', but cannot start with a digit.  ```importdata``` is the function responsible for extracting and loading the data into the variable defined. Within the parentheses, it is the file location path in the OS in quotes (single or double) following by the type of the file to be read. To avoid problems, make sure that a forward slash (or double backslashes) is used to define the filePath (e.g. "C:/yourfilelocation.../nameofthefile.txt") instead of single backslashes. The function assumes by default that the datasets were saved as txt files (Fig. 3a), so in such case it is not necessary to define the type. In contrast, if you want to read a csv file you have to specify the type (as in the example above). Once you press the Enter key, the function ```importdata``` will automatically extract the information corresponding for the areas of the grains. To check that everything is ok, the function will also return in the shell the first rows of the dataset read and the first and last values of the variable stored.

In case you previously extracted manually the information of the areas of the grains and then stored in a txt or csv file (i.e. without a spreadsheet-like form; Fig. 4), you can use the method ```np.genfromtxt()``` to load the data into a variable as follows:
```python
>>> areas = np.genfromtxt('C:/yourFileLocation/nameOfTheFile.txt')
```
In case you need to skip the first lines because there is a text or other information instead of the values:
```python
>>> areas = np.genfromtxt('C:/yourFileLocation/nameOfTheFile.txt', skip_header = 1)
```
In this case, the parameter ```skip_header = 1``` means that the first line in the txt file is not considered. You can define any number of lines to skip.

<img src="https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/notebook.jpg" width="350">  
*Figure 4. A txt file without spreadsheet-like form*

> **Tip**: If you need to load a large number of data sets, you probably prefer not having to specify all the absolute file paths for all your stored data sets. Python establishes by default a current working directory in which all the files can be accessed directly by specifying the name of the file or the folder and the name of the file (*i.e.* a relative path). For example, if your current working directory is ```c:/user/yourname```, this means that for all the files stored within this directory you no longer need to specify this part of the file path. For example, to load a csv file named 'my_sample.csv' that it is stored in that location you just need write:
> ```python
>>> areas = importdata('my_sample.csv', type = 'csv')
```
>  In case the file 'my_sample.csv' were stored in ```c:/user/yourname/my_samples``` will write:
> ```python
>>> areas = importdata('my_samples/my_sample.csv', type = 'csv')
``` 
> and so on. You can retrieve your current working directory by typing in the shell ```os.getcwd()```. Furthermore, you can change the current working directory to another path using the function ```os.chdir('new default path')```. Note that the file path defined within the parentheses is in quotes. This also works when using the ```np.genfromtxt``` method.

The data stored in any variable can be viewed at any time by invoking the name of the variable in the Python shell and pressing the Enter key, as follows (as a random example):

```python
>>> areas
>>> array([99.6535, 41.9045, ..., 79.5712, 119.777])
```

Furthermore, both the Canopy and the Spyder editors have a specific variable explorer to visualize all the variables loaded in the current session. Also, to see the lenght of an array stored we can use the ```len()``` method:

```python
>>> len(areas)
>>> 2754 
```
#### Estimating the apparent diameters from the areas of the grain profiles

The second step is to convert the areas into diameters via the equivalent circular diameter. For this, it was implemented a function named ```calc_diameters```. To invoke this function we write in the shell:

```python
>>> diameters = calc_diameters(areas)
```

In the example above, the only parameter declared within the parenthesis are the variable containing the areas of the grain profiles previously loaded in the variable ```areas```. In some cases a perimeter correction is needed (Fig. 5). For this, just add the following parameter (note that different inputs/parameters are separated by commas):

```python
>>> diameters = calc_diameters(areas, addPerimeter = 0.05)
```

or just

```python
>>> diameters = calc_diameters(areas, 0.05)
```

This example means that for each apparent diameter calculated from the sectional areas, 0.05 is added. If the parameter ```addPerimeters``` is not declared within the function, as in the first example, it is assumed that no perimeter correction is needed.

<img src="https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/Fig_PS_pixels.png" width="500">  
*Figure 5. Example of perimeter correction. The figure shows the boundaries (in white) between three grains in a grain boundary map. The squares are the pixels of the image. The boundaries are two pixel wide approximately. If, for example, each pixel corresponds to 1 micron, we need to add 2 microns to the diameters estimated from the equivalent circular areas.*

Once the sectional areas and the apparent grain sizes are loaded into memory, we have two choices: (1) estimate a single value of grain size (1D grain size measure) for paleopiezometry/paleowattometry studies, or (2) derive the actual 3D population of grain sizes from the population of apparent grain sizes using the Scheil-Schwartz-Saltykov method (Saltykov, 1967) or the two-step method (Lopez-Sanchez and Llana-Fúnez, *submitted*).

#### *Obtaining a single 1D value of grain size (paleopiezometry studies)*

In case we want to obtain a single value of grain size, we need to invoke the function ```find_grain_size```as follows:

```python
>>> find_grain_size(areas, diameters)
```

Note that contrary to what was shown so far, the function is called directly in the Python shell since it is not necessary to store any data into a variable. The inputs are the arrays with the areas and diameters previously stored in the variables and, if desired, the bin size. The function includes two plug-in methods to estimate an 'optimal' bin size, the Scott (Scott 1979) and the Freedman-Diaconis (Freedman and Diaconis 1981) rules. The ```find_grain_size``` function uses by default the Scott rule. If we want to use the Freedman-Diaconis rule instead or an user-defined bin size, it can be do it as follows:

```python
>>> find_grain_size(areas, diameters, binsize = ‘FD’)
```

note that the name is in quotes with both letters capitalized or

```python
>>> find_grain_size(areas, diameters, binsize = 10.0)
```

to set a user-defined bin size (in this example set to ten). The user-defined bin size can be of type integer or float (*i.e.* an irrational number). Freedman-Diaconis rule is a better option compared to Scott rule when it is suspect that there are outliers in the population of grain profile sizes.

After pressing the Enter key, the function will return a number of different 1D measures of grain size typically used in paleopiezometry studies, including the mean, the median, the area-weighted mean and the frequency peak grain sizes (see details in [Lopez-Sanchez and Llana-Fúnez 2015](http://www.solid-earth.net/6/475/2015/se-6-475-2015.html)). Also, other parameters of interest are also provided, such as the bin size estimated (indicating the method used in the estimation) and the bandwidth used for the Gaussian kernel density estimator according to the Silverman rule (Silverman 1986). As stated in [Lopez-Sanchez and Llana-Fúnez 2015](http://www.solid-earth.net/6/475/2015/se-6-475-2015.html), a minimum of 433 measured grain profiles are needed to yield consistent results, although we recommended to measure at least 965 if possible.

In addition, a new window with the number and area weighted plots appear (Fig. 6), showing the location of the different grain sizes estimated respect to the population of apparent grain sizes. The advantages and disadvantages of these plots are explained in detail in [Lopez-Sanchez and Llana-Fúnez 2015](http://www.solid-earth.net/6/475/2015/se-6-475-2015.html). You can save the plots by clicking in the floppy disk icon (Fig. 6) and save it as bitmap (8 file types to choose) or vector images (5 file types to choose) in case you need to post-edit the plots. Another interesting option is to modify the plot within the *Matplotlib* environment before saving. For this, just click the green tick icon (Fig. 6) and choose the subplot you want to modify. A new window appears with several options available.

![Figure 6. Number- and area-weighted plots](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/figure_1.png)  
*Figure 6. Number- and area-weighted plots returned by the find_grain_size function*

#### *Derive the actual 3D population of grains*

The function responsible to unfold the population of apparent grain sizes into the actual 3D grain size population is named ```derive3D```. In the script the first line of the funtion looks like this:

```python
def derive3D(diameters, numbins=10, set_limit=None, fit=False, initial_guess=False):
```
To derive the actual 3D population of grain sizes using the Scheil-Schwartz-Saltykov method (Saltykov 1967), we need to invoke the function ```derive3D```as follows:

```python
>>> derive3D(diameters, numbins=15)
```
Since the Saltykov method is based on the discretization of the grain size population, the inputs are an array with the apparent diameters of the grains and the desired number of bins/classes of the histogram. If the number of bins is not declared is set to ten by default. To define the number of classes, the user can use any positive **integer** value. However, it is advisable to choose a number between 5 and 20 (see later for details). After pressing the enter key, the function will return the bin size estimated and an array with the normalized frequencies of the different classes. In addition, a new window with two plots appears (Fig 7). At left, a frequency plot showing the estimated 3D grain size distribution in a form of a histogram and, at right, a volume-weighted cumulative density plot. The latter allow the user to estimate by eyeballing which percentage of volume is occupied by a defined fraction of grain sizes. In case we want to estimate the volume of a particular grain fraction (i.e. the volume occupied by a fraction of grains less or equal to a certain value) we need to add a new parameter within the function as follows (*Note: this feature has been implemented in the version 1.0 that it will be released soon*):

```python
>>> derive3D(diameters, numbins=12, set_limit=40)
```
In the example above, we set the grain fraction to 40 microns, which means that the script will return an estimation of the volume occupied by all the grain fractions less or equal to 40 microns within the entire population. As a cautionary note, if we use a different number of bins/classes (in this random example set at 12), we will obtain slighly different results. This is normal due to the inaccuracies of the method involved. In any event, as Lopez-Sanchez and Llana-Fúnez (*submitted*) showed, the differences between the volume estimations using the typical range of number of classes (from 10 to 20) are less than 5%, which means that to stay safe we should always take an error margin of 5% in the volume estimations. 

![Figure 7. 3D grain size distribution](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/figure_2.png)  
*Figure 7. Derived 3D grain size distribution and volume-weighted cumulative grain size distribution using the Saltykov method*

Regarding the number of bins/classes, it depends on a number of factors, such as the length and the features of the data set, and, therefore, there is no best number of bins. Due to the nature of the Saltykov method, the larger the bin size (or the smaller the number of classes), the better the numerical stability of the method. In contrast, the smaller the bin size, the better the approximation of the wanted distribution. Ultimately, the strategy to follow is about finding the maximum number of classes (i.e. the best resolution) that produces stable results. Based on experience, previous works using the Scheil-Schwartz-Saltykov method proposed to use between 10 to 15 classes (e.g. Exner 1972), although depending on the quality of the data set seems that it can be used up to 20 classes without problem (e.g. Heilbronner and Barret 2014, Lopez-Sanchez and Llana-Fúnez *submitted*). So far, no method (i.e. algorithm) appears to be generally best for choosing an optimal number of classes (or bin size) from a particular population of apparent diameters. Hence, the only way to proceed is to use a strategy of trial and error to find which is the maximum number of classes that produces a consistent result. As a last cautionary note, to unfold the distribution of apparent grain diameters into the actual 3D distribution applying a Saltykov-type method/algorithm, large samples are required (n ~ 1000 or larger) to generally obtain consistent results.

To estimate quantitatively the actual 3D grain size population, the ```derive3D``` function implements a method called "the two-step method" (Lopez-Sanchez and Llana-Fúnez, *submitted*; *Note: this feature has been implemented in the version 1.0 that it will be released soon*). This method assumes that the actual 3D population of grain sizes follows a log-normal population, which in a deformed rock means that it is completely dynamically recrystallized. So, it is first required to use the Saltykov method in order to observe qualitatively whether the derived population of grain sizes is unimodal (i.e. only one frequency peak) and approximately follows a log-normal population (i.e. the population is skewed to the right), as in the example showed in the figure 7. The procedure to estimate the optimal parameters that describe the best fitted log-normal density function. The script will return the parameters **shape** and **scale**, which they describe the log-normal population at their original scale, and the errors associated with the estimation (see details in Lopez-Sanchez and Llana-Fúnez, *submitted*). In addition, it also returns a plot showing the results of the Saltykov and the two-step method in a frequency diagram (Fig. 8). To apply the two-step method we need to invoke the function ```derive3D``` as follows:

```python
>>> derive3D(diameters, numbins=15, set_limit=None, fit=True)
```

Note that in this case we include a new parameter named ```fit``` and set it to ```True``` (it set to ```False``` by default). Sometimes the non-linear least squares algorithm will fail at fitting the log-normal population to the unfolded data (e.g. Fig. 8). This is because the procedure used to find the optimal shape and scale values, based on a state-of-the-art non-linear least squares algorithm, only converges to the global minimum when their initial guesses are already somewhat close to the final solution. Based on experience, this initial guesses were set by default at 1.2 and 25.0 for the shape and scale values, respectively. However, when the algorithm fails it is neccesary to change these default values by adding a new parameter in the ```derive3D``` function as follows:

```python
>>> derive3D(diameters, numbins=15, set_limit=None, fit=True, initial_guess=True)
```
When the ```initial_guess``` parameter is set to ```True```, the script will ask you about the new guess values for the shape and scale parameters (it also indicates which are the default ones). Based on our experience, a useful strategy is to let the shape value in its default value (1.2) and decrease the scale value every five units until the fitting procedure yield a coherent result (*e.g.* 25 -> 20 -> 15...) (Fig. 8).

![Figure 8. Two-step method plots](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/two-step_method.png)  
*Figure 8. Plots obtained by the two step method. At left, an example with the log-normal population well fitted to the datapoints. The shadow zone is the trust region at a 3-sigma level for the fitting procedure. At right, an example of a wrong fit due to the use of unsuitable initial guess values. Note the discrepancy between the datapoints and the line representing the best fitting*

#### *Other general methods of interest*

**Calculate the mean and the standard deviation of an array stored**
```python
>>> mean(the name of the variable)
>>> std(the name of the variable)
```

**Merging data sets**

A useful *Numpy* method to merge two or more data sets is called ```hstack()```, which stack arrays in sequence as follows (*note the use of double parenthesis*):

```python
>>> np.hstack((name of the array1, name of the Array2,...))
```

As an example if we have two different data sets and we want to merge the areas and the diameters estimated in a single variable we write into the Python shell (variable names are just a random examples):

```python
>>> all_areas = np.hstack((areas1, areas2))
>>> all_diameters = np.hstack((diameters1, diameters2))
```

Note that in this example we merged the original data sets into two new variables named ```all_areas``` and ```all_diameters``` respectively. This means that we do not overwrite any of the original variables and we can used later if required. In contrast, if you use a variable name already defined:

```python
>>> areas1 = np.hstack((areas1, areas2))
```
The variable ```areas1``` is now a new array with the values of the two data sets, and the original data set stored in the variable ```areas1``` no longer exists since numpy arrays are mutable Python objects.

[next section](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/specifications.md)  
[table of contents](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/tableOfContents.md)

----------
