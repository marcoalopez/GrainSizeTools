# Using the steorology module

Stereology is a set of mathematical methods designed to provide quantitative information about a three-dimensional feature from measurements made on two-dimensional sections. Unlike tomography, which aims to reconstruct the 3D geometry of a material, stereology is used to estimate specific 3D features. Here we will use stereological methods to approximate the true grain size distribution from the grain size distribution observed in the sections.

The GrainSizeTools script includes two stereological methods for this purpose: 1) the Saltykov method, and 2) the two-step method.

## The Saltykov method

> **What is it?**  
> The Saltykov method is a stereological technique that approximates the true grain size distribution from the histogram of the distribution of apparent grain size sections. The method is versatile as it does not assume any particular type of statistical distribution.
>
> **What do I use it for?**  
> In the geosciences, the Saltykov method is used primarily to estimate the volume fraction of a given range of grain sizes, but also to estimate the actual average grain size (see cautionary note below).
>
> **What are its limitations?**  
> Despite its utility, the Saltykov method has several limitations when applied to rocks:
>
> - **Assumption of Non-Touching Spheres**. The method assumes non-touching spheres uniformly distributed in a matrix (e.g. bubbles in a piece of glass), a condition rarely met in polycrystalline rocks. To apply the method, the grains should be at least approximately equiaxed, which is typically the case for recrystallized grains.
> - **Dependence on Histogram Classes**. The accuracy of the method is affected by the number of classes in the histogram. There's a trade-off: fewer classes improve the numerical stability of the method, but worsen the approximation of the target distribution, and vice versa. Currently, there is no exact method for finding the optimal number of classes, and this must be set by the user or determined by a rule of thumb. Using the histogram also means that we cannot get a complete description of the grain size distribution.
> - **Lack of Error Estimation Formulation**. The Saltykov method lacks a formulated procedure for estimating errors during the unfolding process, which limits the ability to assess the reliability of the results
> - **Inability to Estimate True Average Grain Size**. It's impossible to obtain an estimate of the true average grain size (3D) because individual data is lost when using the histogram. In other words, the Saltykov method attempts to reconstruct the histogram of the true grain size population, not to convert each apparent diameter into the true one. While there are methods to estimate an average from the resulting histogram, it's important to emphasize that **this estimate is derived from a stereological model, not actual empirical data**.

To apply this method, we use the ``calc_shape`` function of the stereology module. Let's have a look at the documentation for this function first:

```python
stereology.Saltykov?
```

```reStructuredText
Signature:
stereology.Saltykov(
    diameters,
    numbins=10,
    calc_vol=None,
    text_file=None,
    return_data=False,
    left_edge=0,
)
Docstring:
Estimate the actual (3D) distribution of grain size from the population
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



```python
# Import the example dataset
filepath = 'C:/Users/marco/Documents/GitHub/GrainSizeTools/grain_size_tools/DATA/data_set.txt'
dataset = pd.read_csv(filepath, sep='\t')

# estimate equivalent circular diameters
dataset['diameters'] = 2 * np.sqrt(dataset['Area'] / np.pi)

# apply the Saltykov method from stereology module
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

So for example if you have a volume of rock of say 100 cm² and you want to estimate what proportion of that volume is occupied by each grain size class/range, you could estimate it as follows:

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
> The two-step method is a stereological technique that approximates the true grain size distribution from the histogram of the distribution of apparent grain size intervals. It differs from the Saltykov method in that the population is not described by a histogram but by a mathematical distribution. The method is thus **distribution dependent**, i.e. it assumes that the grain sizes follow a lognormal distribution. The method fits a lognormal distribution to the output of the Saltykov method, hence the name "two-step method".
>
> **What do I use it for? **  
> The Two-Step Method is primarily used to estimate the lognormal distribution of grain sizes, which includes determining the shape and location of the distribution. It can also be used to estimate the volume fraction of a particular range of grain sizes.
>
> **What are its limitations? ** 
>
> - **Distribution Dependency**. The method assumes a lognormal distribution for grain size, which may not accurately represent certain materials.
> - **Inherited Limitations from the Saltykov method**. The method is partially based on the Saltykov method and therefore inherits some of its limitations. The method however do not require to define a specific number of classes. 

To apply this method, we use the ``calc_shape`` function of the stereology module. Let's have a look at the documentation for this function first:

```python
help(stereology.calc_shape)
```

```reStructuredText
calc_shape(diameters, class_range=(10, 20))
    Approximates the shape of the actual (3D) distribution of grain size
    from a population of apparent diameters measured in a thin section using
    the two-step method (Lopez-Sanchez and Llana-Funez, 2016).
    
    The method only works properly for unimodal lognormal-like grain size
    populations and returns the MSD (i.e. shape) and the geometric mean
    (i.e. scale) values, which describe the lognormal population of grain sizes
    at their original (linear) scale.
    
    Parameters
    ----------
    diameters : array_like
        the apparent diameters of the grains
    
    class_range : tupe or list with two values, optional
        the range of classes considered. The algorithm will estimate the optimal
        number of classes within the defined range. Default = (10, 20)
    
    
    Call functions
    --------------
    - Saltykov,
    - fit_log,
    - log_function
    - gen_xgrid
    - twostep_plot
    
    Examples
    --------
    >>> calc_shape(diameters)
    >>> calc_shape(diameters, class_range=(12, 18))
    >>> calc_shape(diameters, initial_guess=True)
    
    References
    ----------
    Saltykov SA (1967) http://doi.org/10.1007/978-3-642-88260-9_31
    Sahagian and Proussevitch (1998) https://doi.org/10.1016/S0377-0273(98)00043-2
    Lopez-Sanchez and Llana-Funez (2016) https://doi.org/10.1016/j.jsg.2016.10.008
    
    Returns
    -------
    A plot with an estimate of the actual (3D) grains size distribution and
    several statistical parameters

```



> [!NOTE]
> **Understanding the MSD Value and its Purpose**  
> MSD, or _Multiplicative Standard Deviation_, is a parameter that characterizes the shape of a grain size distribution using a single value, under the assumption that the distribution follows a lognormal pattern. In simpler terms, the MSD value provides a measure of the asymmetry or skewness of the grain size distribution. An MSD value equal to one corresponds to a normal (Gaussian) distribution, while values greater than one indicate log-normal distributions with varying degrees of asymmetry (Figure a). **Scale-Independent Comparison**. The advantage of this approach is that a single parameter, the MSD, can define the shape of the grain size distribution independently of its scale (Figure b). This makes it very convenient for comparing the shape of two or more grain size distributions.
> 
> ![Figura](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/MSD_value.png)
>**Figure**. Probability density functions of selected lognormal distributions taken from [Lopez-Sanchez and Llana-Fúnez (2016)](http://www.sciencedirect.com/science/article/pii/S0191814116301778). (a) Lognormal distributions with different MSD values (shapes) and the same median/geometric mean (4). (b) Lognormal distributions with the same shape corresponding to an MSD value (1.5) and different medians/geometric means (note that different medians/geometric means imply different scales in the horizontal and vertical directions).

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

The method returns the values of the lognormal distribution that best fits our model, in this case defined by two values: the geometric mean (scale) and its MSD (shape). This distribution can also be used to calculate the volume fraction occupied by a particular particle size range or other averages (e.g. arithmetic mean).

TODO



> [!CAUTION]
>
> ### Why prefer averages from apparent grain size to those estimated from unfolded grain size distributions in palaeopiezometry?
>
> While one might be tempted to use a stereological method to estimate the midpoint of the modal interval or some other unidimensional parameter based on the calculated grain size distribution, we argue that this approach offers no advantages and comes with serious disadvantages.
>
> The rationale is that 3D grain size distributions are estimated using a stereological model. This means that the accuracy of the estimates depends not only on measurement errors but also on the robustness of the model itself. Unfortunately, stereological methods are based on weak geometric assumptions, and their results will always be, at best, approximate. This means that the precision and accuracy of averages estimated from 3D size distributions will be **significantly inferior in performance and reliability** to those based on the original distribution of grain sections. The latter, although estimating an apparent grain size, is based on real data rather than a model.
>
> **Recommendation**. In summary, it's advisable to use stereological methods only when there’s a need to estimate the volume occupied by a particular grain size fraction, to investigate the shape of the true grain size distribution or when you need to use an average based on actual grain sizes (e.g. when you need to compare the average grain size calculated by a tomographic technique with that estimated from a section). Otherwise, for better precision and accuracy, opt for averages based on the apparent grain size distribution.

