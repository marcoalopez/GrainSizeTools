# The stereology module

> 📣 If you are using **Jupyter lab** or Jupyter notebooks you have a similar step-by-step tutorial in a notebook format within the ``example_notebook`` folder that comes with the script and [online](https://github.com/marcoalopez/GrainSizeTools/blob/master/grain_size_tools/example_notebooks/stereology_module_examples.ipynb).

The main purpose of stereology is to extract quantitative information from microscope images. It is a set of mathematical methods relating two-dimensional measures obtained on sections to three-dimensional parameters defining the structure. Note that the aim of stereology is not to reconstruct the 3D geometry of the material (as in tomography) but to estimate  a particular 3D feature. In this particular case, to approximate the actual (3D) grain size distribution from the apparent (2D) grain size distribution obtained in sections. In this particular case, to approximate the actual (3D) grain size distribution from the apparent (2D) grain size distribution obtained in sections. 

GrainSizeTools script includes two stereological methods: 1) the Saltykov method, and 2) the two-step method. Before looking at its functionalities, applications and limitations, let's import the example dataset.

```python
# Import the example dataset
filepath = 'C:/Users/marco/Documents/GitHub/GrainSizeTools/grain_size_tools/DATA/data_set.txt'
dataset = pd.read_csv(filepath, sep='\t')
dataset['diameters'] = 2 * np.sqrt(dataset['Area'] / np.pi)  # estimate ECD
```

## The Saltykov method

TODO: explain functionalities, applications and limitations

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

TODO: functionalities, applications and limitations

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