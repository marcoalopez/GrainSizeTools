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
> - You cannot obtain an estimate of the actual average grain size (3D) as individual data is lost when using the histogram (i.e. The Saltykov method reconstructs the 3D histogram not every apparent diameter in the actual one as this is mathematically impossible).
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