Specifications of main functions in the GrainSizeTools script
-------------

####**importdata** (*filePath*)
Load the data from a text file (txt or csv). 

> **Parameters:**
> 
> ***filePath***: *string*
> The file location in the OS in quotes.
> 
> **Returns**:
> An numpy array with the values loaded (e.g the areas or the diameters of the sectional grains).

*Note: In this case, **importdata** is just a function that renames a Numpy method called "genfromtxt". We opted to write our own function to allow specification within the script and simplify things. The user can be call "genfromtxt" or "loadfromtxt" directly instead of "importdata" if desired. More information about the "genfromtxt" of "loadfromtxt" Numpy methods can be found [here](http://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html) or [here](http://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html)*

####**calc_diameters** (*areas, addPerimeter = 0*)
Calculate the diameters from the sectional areas via the equivalent circular diameter assuming that the grains have near-equant shapes.

> **Parameters:**
> 
> ***areas***: *array_like*
> The sectional areas of the grains.
> 
> ***addPerimeter***: *int or float; optional*
> Correct the diameters estimated from the areas by adding the perimeter of the grain. If *addPerimeter* is not declared it is considered zero.

>**Returns**:
> An array with the diameters of the grains.

####**find_grain_size** (*areas, diameters, binsize = 'FD'*)
Estimate a representative numeric value of grain size from the population of apparent diameters and areas.

> **Parameters:**
> 
> ***areas***: *array_like*
> The sectional areas of the grains.
> 
> ***diameters***: *array_like*
> The apparent diameters of the grains.
> 
> ***binsize***: *string, int or float; optional*
> the method used to calculate the bin size. This can be: 'FD' (Fredman-Diaconis rule), 'Scott' (Scott rule) or a
> user-defined scalar constant of type integer or float. If not specified, 'FD' is used by default.
> 
>**Returns**:
> A number of grain size values to use in paleopiezometry or paleowattometry studies and the number and area-weighted plots. The values includes the mean, the median and the area-weighted mean grain size and the frequency peak via the Gaussian kernel density estimator (preferred option) and the mid-poind of the modal interval. It also provides other values of interest such as the bin size and bandwidth estimated and the methods chosen.

####**derive3D** (*diameters, numbins=10*)
Estimates the actual 3D populations of grains from the population of apparent (2D) grain sizes using the Scheil-Schwartz-Saltykov method to unfold the apparent 2D population of grain sizes.

> **Parameters:**
> 
> ***diameters***: *array_like*
> The apparent diameters of the grains.
> 
> ***numbins***: *int; optional*
> The number of classes or bins used to unfold the population. If not declared it uses ten as default.
> 
>**Returns**:
> The bin size, the frequencies (probabilities) of the different classes and a plot containing two subplots: i) the distribution of the actual grain size population according to the Scheil-Schwartz-Saltykov method and ii) the volume cumulative distribution function. The array with the frequencies are normalized such that the integral over the range is 1 (i.e. the frequencies obtained in each class is divided by the bin size). Note that the sum of these values will not be equal to 1 unless bins of unity width are chosen.

----------
