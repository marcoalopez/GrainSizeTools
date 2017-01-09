Specifications of main functions in the GrainSizeTools script
-------------

#### **extract_areas** (*filePath*, *form='txt', col_name='Area'*)
Extract the data corresponding to the areas of grain profiles from tabular-like
data generated with the ImageJ application. Use always forward slashes (or double
backslashes) in the file path to avoid problems.

> **Inputs:**
>
> ***filePath***: *string*  
> the file location in the OS in quotes.
>
> ***form***: *string; optional*  
> the form of the file, either 'txt' or 'csv'.
>
>***col_name***: *string; optional*
> The name of the column that contains the areas of the grain profiles. It is set to 'Area' by default.
>
> **Returns**:  
> A numpy array with the areas of the grain profiles.

#### **calc_diameters** (*areas, addPerimeter=0*)
Calculate the diameters from the sectional areas via the equivalent circular diameter.

> **Inputs:**
>
> ***areas***: *array_like*  
> A numpy array with the sectional areas of the grains
>
> ***addPerimeter***: *integer or float; optional*  
> Correct the diameters estimated from the areas by adding the perimeter of
the grain. If addPerimeter is not declared, it is considered 0. A float or
integer.

>**Returns**:  
> A numpy array with the diameters of the grains.

#### **find_grain_size** (*areas, diameters, plot='lin', binsize='auto'*)
Estimate different 1D measures of grain size from a population of apparent diameters
and their areas. It includes the mean, the area-weighted mean, the median and the
frequency peak grain sizes.

> **Inputs:**
>
> ***areas***: *array_like*  
> A numpy array with the areas of the grain profiles
>
> ***diameters***: *array_like*  
> A numpy array with the apparent diameters of the grains
>
> ***plot***: *string; optional*
> the preferred type of plot and grain size estimation. This can be 'lin' for a
linear frequency vs diameter plot, 'log' for a frequency vs logarithmic diameter
plot, 'sqrt' for a frequency vs square root diameter plot, and 'area' for a
area-weighted frequency vs diameter plot.
>
> ***binsize***: *string, integer or float; optional*  
> the method used to calculate the bin size. This can be 'auto', 'fd' (Freedman-Diaconis
rule), 'doane' (Doane's rule), 'scott' (Scott rule), 'sturges' (Sturge's rule), or a scalar
of type integer or float. If not specified, the 'auto' rule is used by default.
>
>**Returns**:  
> A number of 1D grain size values to use in paleopiezometry (or paleowattmetry) studies and the chosen plot. The values includes the mean, the median, the area-weighted mean and the frequency peak via the Gaussian kernel density estimator grain sizes. It also provides other values of interest such as the bin size and bandwidth estimated as well as the methods chosen.

#### **derive3D** (*diameters, numbins=10, set_limit=None, fit=False, initial_guess=False*)
>Estimates the actual distribution of grain size from the population of
apparent diameters measured in a thin section using two approaches:

>i) the Saltykov method (Saltykov 1967; Sahagian and Proussevitch 1998)
ii) the two-step method (Lopez-Sanchez and Llana-Funez, 2016).

>The Saltykov method is optimal to estimate the volume of a particular grain size
fraction as well as to obtain a qualitative view of the appearance of the actual
3D grain size population, either in uni- or multimodal populations.

>The two-step method is aimed at estimating quantitatively the shape of the
actual 3D distribution of grain sizes. The method only works properly for
unimodal lognormal-like grain size populations (i.e. completely recrystallized
rocks) and returns the MSD (i.e. shape) and median (i.e. scale) values that
describe the lognormal population of grain sizes at their lineal scale. For
details see Lopez-Sanchez and Llana-Funez (2016).

> **Inputs:**
>
> ***diameters***: *array_like*  
> A numpy array or Python list with the apparent diameters of the grains.
>
> ***numbins***: *integer; optional*  
> The number of bins/classes of the histrogram. If not declared, is set by
default to 10. An integer.
>
> ***set_limit***: *integer or float; optional*  
> If the user defines a number, the script will return the volume occupied by the
grain fraction of size less than or equal to that value. An integer or float.
>
> ***fit***: *True or False*  
> If False, the standard Saltykov method is applied. If True, the two-step method
is applied.
>
>***initial_guess***: *True or False*  
> If False, the script will use the default guessing values to fit the lognormal
distribution. If True, the script will ask the user to define the MSD and
median guessing values.
>
>**Returns**:  
> In the case of the Saltykov method: The bin size, the frequencies (probabilities) of the different classes and a plot containing two subplots: i) the distribution of the actual grain size population according to the Saltykov method and ii) the volume-weighted cumulative distribution. The frequencies are normalized such that the integral over the range is one. Note that the sum of these values will not be equal to one unless bins of unity width are chosen. In the case of the two-step method: The optimal MSD (shape) and median (scale) values and the precision of the estimation at a 3-sigma level.  Also a plot containing the unfolded population using the Saltykov method and the fitted lognormal probability density function with a trust region.

[next section](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/imageJ_tutorial.md)  
[table of contents](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/imageJ_tutorial.md)

----------
