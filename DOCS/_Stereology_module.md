# The stereology module

> 📣 If you are using **JupyterLab** or the **Notebook**  you have a similar step-by-step tutorial in a notebook format within the ``example_notebook`` folder that comes with the script and [online](https://github.com/marcoalopez/GrainSizeTools/blob/master/grain_size_tools/example_notebooks/stereology_module_examples.ipynb).

The main purpose of stereology is to extract quantitative information from microscope images relating two-dimensional measures obtained on sections to three-dimensional parameters defining the structure. The aim of stereology is not to reconstruct the 3D geometry of the material (as in tomography) but to estimate  a particular 3D feature. In this case, we aim to approximate the actual (3D) grain size distribution from the apparent (2D) grain size distribution obtained in sections.

GrainSizeTools script includes two stereological methods: 1) the Saltykov, and 2) the two-step methods. Before looking at its functionalities, applications and limitations, let's import the example dataset.

```python
# Import the example dataset
filepath = 'C:/Users/marco/Documents/GitHub/GrainSizeTools/grain_size_tools/DATA/data_set.txt'
dataset = pd.read_csv(filepath, sep='\t')
dataset['diameters'] = 2 * np.sqrt(dataset['Area'] / np.pi)  # estimate ECD
```

## The Saltykov method

> **What is it?**
>
> It is a stereological method that approximates the actual grain size distribution from the histogram of the apparent grain size distribution. The method is distribution-free, meaning that no assumption is made upon the type of statistical distribution, making the method very versatile.
>
> **What do I use it for?**
>
> Its main use (in geosciences) is to estimate the volume fraction of a specific range of grain sizes.
>
> **What are its limitations?**
>
> The method presents several limitations for its use in rocks
>
> - It assumes that grains are non-touching spheres uniformly distributed in a matrix (e.g. bubbles within a piece of glass). This never holds for polycrystalline rocks. To apply the method, the grains should be at least approximately equiaxed, which is normally fulfilled in recrystallized grains.
> - Due to the use of the histogram, the number of classes determines the accuracy and success of the method. There is a trade-off here because the smaller the number of classes, the better the numerical stability of the method, but the worse the approximation of the targeted distribution and vice versa. The issue is that no method exists to find an optimal number of classes and this has to be set by the user. The use of the histogram also implies that we cannot obtain a complete description of the grain size distribution.
> - The method lacks a formulation for estimating errors during the unfolding procedure.
> - You cannot obtain an estimate of the actual average grain size (3D) as individual data is lost when using the histogram (i.e. The Saltykov method reconstructs the 3D histogram, not every apparent diameter in the actual one as this is mathematically impossible).
>

TODO: explain the details of the method

```python
stereology.Saltykov(dataset['diameters'], numbins=11, calc_vol=50)
```

```
=======================================
volume fraction (up to 50 microns) = 41.65 %
bin size = 14.24
=======================================
```

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/saltykov.png?raw=true)

Now let's assume that we want to use the class densities estimated by Saltykov's method to calculate the specific volume of each or one of the classes. We have two options here.

```python
def Saltykov(diameters,
             numbins=10,
             calc_vol=None,
             text_file=None,
             return_data=False,
             left_edge=0):
    """ Estimate the actual (3D) distribution of grain size from the population
    of apparent diameters measured in a thin section using a Saltykov-type
    algorithm (Saltykov 1967; Sahagian and Proussevitch 1998).

    The Saltykov method is optimal to estimate the volume of a particular grain
    size fraction as well as to obtain a qualitative view of the appearance of
    the actual 3D grain size population, either in uni- or multimodal populations.

    Parameters
    ----------
    diameters : array_like
        the apparent diameters of the grains.

    numbins : positive integer, optional
        the number of bins/classes of the histogram. If not declared,
        is set to 10 by default.

    calc_vol : positive scalar or None, optional
        if the user specifies a diameter, the function will return the volume
        occupied by the grain fraction up to that diameter.

    text_file : string or None, optional
        if the user specifies a name, the function will store a csv file
        with that name containing the Saltykov output.

    return_data : bool, optional
       if True the function will return the position of the midpoints and
       the frequencies.

    left_edge : positive scalar or 'min', optional
        set the left edge of the histogram. Default is zero.

    Call functions
    --------------
    - unfold_population
    - Saltykov_plot

    Examples
    --------
    >>> Saltykov(diameters)
    >>> Saltykov(diameters, numbins=16, calc_vol=40)
    >>> Saltykov(diameters, text_file='foo.csv')
    >>> mid_points, frequencies = Saltykov(diameters, return_data=True)

    References
    ----------
    Saltykov SA (1967) http://doi.org/10.1007/978-3-642-88260-9_31
    Sahagian and Proussevitch (1998) https://doi.org/10.1016/S0377-0273(98)00043-2

    Return
    ------
    Statistical descriptors, a plot, and/or a file with the data (optional)
```

The input parameter ``text_file`` allows you to save a text file with the data in tabular format, you only have to declare the name of the file and the file type, either txt or csv (as in the function documentation example). Alternatively, you can use the Saltykov function to directly return the density and the midpoint values of the classes as follows:

```python
mid_points, densities = stereology.Saltykov(dataset['diameters'], numbins=11, return_data=True)
print(densities)
```

```
[1.31536871e-03 2.17302235e-02 2.25631643e-02 1.45570771e-02
 6.13586532e-03 2.24830266e-03 1.29306084e-03 3.60326809e-04
 0.00000000e+00 0.00000000e+00 4.11071036e-05]
```

As you may notice, these density values do not add up to 1 or 100.

```python
np.sum(densities)
```

```
0.07024449636922886
```

This is because the script normalized the frequencies of the different classes so that the integral over the range (not the sum) is one (see FAQs for an explanation on this). If you want to calculate the relative proportion for each class you must multiply the value of the densities by the bin size. After doing this, you can check that the relative densities sum one (i.e. they are proportions relative to one).

```python
corrected_densities = densities * 14.236
np.sum(corrected_densities)
```

```
1.000000650312342
```

So for example if you have a volume of rock of say 100 cm^2^ and you want to estimate what proportion of that volume is occupied by each grain size class/range, you could estimate it as follows:

```python
# I use np.around to round the values
np.around(corrected_densities * 100, 2)
```

```
array([ 1.87, 30.94, 32.12, 20.72,  8.74,  3.2 ,  1.84,  0.51,  0.  ,
        0.  ,  0.06])
```



## The two-step method

> **What is it?**
>
> It is a stereological method that approximates the actual grain size distribution. The method is distribution-dependent, meaning that it is assumed that the distribution of grain sizes follows a lognormal distribution. The method fit a lognormal distribution on top of the Saltykov output, hence the name two-step method.
>
> **What do I use it for?**
>
> Its main use is to estimate the shape of the lognormal distribution, the average grain size (3D), and the volume fraction of a specific range of grain sizes (not yet implemented).
>
> **What are its limitations?**
>
>  The method is partially based on the Saltykov method and therefore inherits some of its limitations. The method however do not require to define a specific number of classes.

```python
stereology.calc_shape(dataset['diameters'])
```

```
=======================================
OPTIMAL VALUES
Number of classes: 11
MSD (lognormal shape) = 1.63 ± 0.06
Geometric mean (scale) = 36.05 ± 1.27
=======================================
```

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/2step.png?raw=true)



***Well, I'm afraid you've come to the end. Where do you want to go?***

[return me to the home page](https://marcoalopez.github.io/GrainSizeTools/)  

[take me to “Getting started: first steps using the GrainSizeTools script”](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/_first_steps.md)

[take me to “Describing the population of grain sizes”](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/_describe.md)

[take me to “The plot module: visualizing grain size distributions”](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/_Plot_module.md)

[take me to “Paleopiezometry based on dynamically recrystallized grain size”](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/_Paleopizometry.md)

[take me to “The stereology module”](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/_Stereology_module.md)