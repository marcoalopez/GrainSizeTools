Getting Started: A brief tutorial on how to use the script
-------------

> **Note**
> This simple tutorial assumes that you do not know nothing about Python programming language. This means that it is no necessary a prior knowledge of Python language to use this script and get the results. Just follow the instructions.

### *Running the script*

Once the required software is installed in your system (see [requirements](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/Requirements.md)) and the script downloaded, the first thing is to open the script in a Python editor such as the Canopy editor -if you installed the Enthought Canpopy package-, the IDLE -the Python default editor- or the Spyder editor -a scientific Python development environment that comes with the Anaconda package-. Then, to use the script, it is necessary to run the code. For this, if you are in the Canopy environment just click on the play green icon or go to the *Run* menu and click on “Run file” (Fig. 1). If you open the script in the IDLE, just press F5 or go to Run menu and click “Run module” (Fig. 1).

![Figure 1. Run a script in the Canopy editor (left) and in the IDLE editor (right)](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/RunScript_Canopy.jpg)
*Figure 1. Run a script in the Canopy editor (left) and in the IDLE editor (right)*

The following statement will appear in the Python shell (Fig. 2):
```python
Welcome to the GrainSizeTools script v. 0.3
See release notes in the Readme.txt file
```
![Figure 2. The python editor and the python shell in the Enthought Canopy environment](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/Canopy_example.jpg)
*Figure 2. The python editor and the python shell in the Enthought Canopy environment*

### *Organization of the script*

The script is organized in a modular way using Python functions. This facilitates to modify, reuse or extend the code if required. A Python function looks like this in the editor: 

```python
def calc_diameters(areas, addPerimeter = 0):
    """ Calculate the diameters from the sectional areas assuming that the grains
    have near-equant shapes.

    PARAMETERS
    areas: a numpy array with the sectional areas of the grains
    addPerimeter: a float or integer. Correct the diameters estimated from the
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

Briefly, the name following the Python keyword ```def``` - in this example ```calc_diameters```- is the function name. Within the parentheses following the function name are the formal parameter/s of the function -the input/s-. In this case there are two inputs, the array with the areas of the grains measured and the perimeter needed to correct the size of the grains. The text between the triple quotation marks provide information about the function, which in this case describes the conditions that must be met by the users and the output obtained. Below this, there is the code block.

The names of the Python functions defined in the script are intuitive and self-explanatory. To obtain the results, it is only necessary to use four of all the functions implemented within the script (specifically, the first four). For function details, see the section [Specifications of main functions in the GrainSizeTools script](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/specifications.md).

### *Using the script to calculate a single measure of grain size*

The **first step** is to load the stored data. It is assumed that previously to this step, it was calculated the sectional areas using an image analysis software and save the results as a txt or csv file (Fig. 3).

![Figure 3. Format of the txt file](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/notebook.jpg)
*Figure 3. Format of the txt file*

To load the data set into memory we will use the ```importdata``` function. To invoke this function we write in the Python shell:

```python
>>> areas = importdata('C:/yourFileLocation/nameOfTheFile.txt')
```

where ```areas``` is just a name for the Python object in which the data could be stored into memory, this is also known as a variable. This will allow us to manipulate the data set of areas when required. Any name can be used to create a variable. As an example, in the case that the data set to load were the diameters of grains instead of the areas, it would be useful to call the variable ```diameters```, or if you want to load several files with different data sets of areas you can named ```areas1```, ```areas2``` and so on. In Python, variable names can contain upper- and lowercase letters, digits and the special character _. However, variable names cannot start with a digit. ```importdata``` is the function responsible for loading the data into the variable. Between the parentheses, the file location path in the OS in quotes (single or double). To avoid problems, it is advisable to use forward slash or double backslashes to define the filePath (e.g. "C:/yourfilelocation.../nameofthefile.txt") instead of single backslash. Once the data set is loaded, the data can be simply viewed by invoking the name of the variable in the Python shell and pressing the enter key, as follows:

```python
>>> areas
```

we would obtain (as a random example):

```python
>>> array([99.6535, 41.9045, ..., 79.5712, 119.777])
```

A useful method to check if all data is properly loaded is to verify is the size of the data set is correct. This can be checked using the Python built-in method ```len``` as follows:

```python
>>> len(areas)
```

This will return the number of items in the variable declared within the parenthesis.

The **second step** is to convert the areas into diameters via the equivalent circular diameter. For this, it was implemented a function named ```calc_diameters```. To invoke the function we write in the shell:

```python
>>> diameters = calc_diameters(areas)
```

In the example above, the only parameter declared are the variable ```areas``` previously loaded. In some cases a perimeter correction of the grains is needed. We can correct the diameters calculated by adding the following parameter (note that different inputs are separated by commas):

```python
>>> diameters = calc_diameters(areas, addPerimeter = 0.05)
```

or just

```python
>>> diameters = calc_diameters(areas, 0.05)
```

This example means that for each apparent diameter calculated from the sectional areas, 0.05 is added. If the parameter ```addPerimeters``` is not declared within the function, as in the first example, it is assumed that no perimeter correction is needed. 

Once the sectional areas and the apparent grain sizes are loaded into memory, we have two choices: (1) estimate a single value of grain size for paleopiezometry/paleowattometry studies, or (2) derive the actual 3D population of grain sizes from the population of apparent 2D grain sizes using the Scheil-Schwartz-Saltykov algorithm.

### *Obtaining a single value of grain size (paleopiezometry studies)*

In case we have to obtain a single value of grain size, we need to invoke the function ```find_grain_size```as follows:

```python
>>> find_grain_size(areas, diameters)
```

Note that contrary to what was shown so far, the function is called directly in the Python shell since it is not necessary to store any data into a variable . The inputs are the arrays with the areas and diameters previously stored into memory and, if desired, the bin size. As specified in [Lopez-Sanchez and Llana-Fúnez (*2015*)](http://bit.ly/1ND45Sw) and within the specification of the function, the function uses by default the Freedman-Diaconis rule (Freedman and Diaconis 1981) to estimate an optimal bin size for the histogram. If we want to use the Scott rule (Scott 1979) instead or an *ad hoc* bin size, it can be do it as follows:

```python
>>> find_grain_size(areas, diameters, binsize = ‘Scott’)
```

to use the Scott rule (note that the name is in quotes and that the first letter is capitalized) or

```python
>>> find_grain_size(areas, diameters, binsize = 10.0)
```

for and *ad hoc* bin size (in this example set to ten). The user-defined bin size can be of type integer or float (*i.e.* an irrational number).

After pressing the enter key, the function will return a number of different values of grain size typically used in paleopiezometry studies, including the mean, the median, the area-weighted mean and the frequency peak grain sizes (see details in [Lopez-Sanchez and Llana-Fúnez 2015][11]). Others parameters of interest such as the bin size estimated (indicating the method used in the estimation) and the bandwidth used for the Gaussian kernel density estimator according to the Silverman rule (Silverman 1986) are also provided. As stated in [Lopez-Sanchez and Llana-Fúnez 2015][11], a minimum of 433 measured grains are needed to yield consistent results, although we recommended to measure at least 965 if possible.

Then, a new window with the number and area weighted plots appear (Fig. 4), showing the location of the different grain sizes estimated. The advantages and disadvantages of these plots are explained in detail in [Lopez-Sanchez and Llana-Fúnez 2015][11]. You can save the plots by clicking the floppy disk icon and save it as bitmap (8 file types to choose) or vector images (5 file types to choose) in case you need to post-edit the plots. Another interesting option is to modify the plot within the *Matplotlib* environment before saving. For this, just click the green tick icon and choose the subplot you want to modify. A new window appear with several options available.

![Figure 4. Number- and area-weighted plots](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/figure_1.png)
*Figure 4. Number- and area-weighted plots*

### *Derive the actual 3D population of grains*

To derive the actual 3D population of grain sizes using the Scheil-Schwartz-Saltykov method, we need to invoke the function ```derive3D```as follows:

```python
>>> derive3D(diameters, numbins=15)
```
The inputs are an array with the apparent diameters of the grains and the number of bins/classes of the histogram. If the number of bins is not declared is set to ten by default. To define the number of classes, the user can use any positive integer value. However, it is advisable to choose a number between 5 and 20 (see below for details). After pressing the enter key, the function will return the bin size estimated and an array with the normalized frequencies of the different classes. Also, a new window with two plots appear (Fig 5). On the left, the derived 3D grain size distribution in a form of the histogram and, on the right, a volume-weighted cumulative density plot. The latter allow the user to estimate by eyeballing which percentage of volume is occupied by a defined range of grain sizes.

![Figure 5. 3D grain size distribution](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/figure_2.png)
*Figure 5. Derived 3D grain size distribution and volume-weighted cumulative grain size distribution*

Regarding the number of bins/classes, it depends on a number of factors, such as the length or the features of the data set, and, therefore, there is no best number of bins. Due to the nature of the Saltykov method, the larger the bin size, the better the numerical stability of the method. In contrast, the smaller the bin size, the better the approximation of the wanted distribution. Ultimately, the strategy to follow is about finding the smallest possible bin size (i.e. the best resolution) that produces stable results. Based on experience, previous works using the Scheil-Schwartz-Saltykov method proposed to use between 10 to 20 classes (e.g. Exner 1972) or even fewer than ten classes (e.g. Higgins 2000). So far, no method (i.e. algorithm) appears to be generally best for choosing an optimal number of classes (or bin size) from a particular population of apparent diameters. Hence, the only way to proceed is to use a strategy of trial and error to find which is the maximum number of classes that produces a consistent result. In figure 6 (**under construction**), we try to explain what a consistent result looks like in the case of a dynamic recrystallized mylonite. As a last cautionary note, to unfold the distribution of apparent diameters into the actual 3D distribution applying a Saltykov-type method/algorithm, large samples are required (n ~ 1000 or larger) to generally obtain consistent results.

#### *Other methods of interest*

**Calculate the mean of an array stored**
```>>> mean(*the name of the variable*)```

**Calculate the standard deviation of an array stored**
```>>> std(*the name of the variable*)```

**Merge two or more data sets**

A useful *Numpy* method to merge two or more data sets is called ```hstack```, which stack arrays in sequence as follows:

```>>> np.hstack((*Name of the array1*, *name of the Array2*,...))```

***Note the use of double parenthesis***

As an example if we have two data sets and we want to merge the areas and the diameters estimated in a single variable we write into the Python shell (variable names are just a random example):

```>>> AllAreas = np.hstack((areas1, areas2))```
```>>> AllDiameters = np.hstack((diameters1, diameters2))```


Note that in this example we merged the original data sets into a two new variables named ```AllAreas``` and ```AllDiameters``` respectively. This means that we do not overwrite any of the original data sets and we can used later if required.

[next section](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/specifications.md)
[table of contents](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/tableOfContents.md)

----------
