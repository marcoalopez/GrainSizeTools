GST script quick tutorial
-------------

> This is a quick tutorial showing typical commands to interact with the GST script
> in the shell. You can copy and paste the command lines directly into the shell.
> Variable names have been chosen for convenience, use any other name if desired.  
> The commands shown in this tutorial are for the GST script v1.3. or higher.

#### Loading the data and extracting the areas of the grain profiles

```python
# The automatic (preferred) mode
areas = extract_areas()

# Using the automatic mode but defining a column name different from the default 'Area'
areas = extract_areas(file_path='auto', col_name='the name of the column to be extracted')

# The manual mode: Defining the file path
areas = extract_areas('C:/...yourFileLocation.../nameOfTheFile.csv')

# Loading data from a single-column text file (the skip_header parameter is optional)
areas = np.genfromtxt('C:/yourFileLocation/nameOfTheFile.txt', skip_header=1)
```

#### Estimating the apparent diameters from the areas of the grain profiles

```python
# Estimating the equivalent circular diameter from the grain profiles areas
diameters = calc_diameters(areas)

# Using the diameter correction
diameters = calc_diameters(areas, correct_diameter=0.05) # 0.05 microns will be added
```

#### *Obtaining an unidimensional value of grain size (paleopiezo/wattmetry studies)*

```python
# Default mode (linear grain size distribution, automatic bin size or number of classes)
find_grain_size(areas, diameters)

# Using the area-weighted grain size with automatic bin size
find_grain_size(areas, diameters, plot='area')

# Using the logarithmic grain size with automatic bin size
find_grain_size(areas, diameters, plot='log')

# Using the square-root grain size with automatic bin size
find_grain_size(areas, diameters, plot='sqrt')

# Using a specific plug-in method for estimating the optimal bin size or number of classes
# Plug-in methods include: Freedman-Diaconis:'fd', Scott:'scott', Rice:'rice',
# Sturges:'sturges', Doane:'doane', and square-root:'sqrt' bin sizes
find_grain_size(areas, diameters, plot='lin', binsize='doane')

# Using an ad hoc bin size
find_grain_size(areas, diameters, plot='lin', binsize=10.0)
```

#### *Derive the actual 3D grain size distribution from the apparent grain size distribution*

```python
# Using the Saltykov method with ad hoc number of classes
# if numbins is not declared is set to ten classes by default
derive3D(diameters, numbins=12)

# Estimating the volume of a particular grain size fraction
derive3D(diameters, numbins=12, set_limit=40)

# Using the two-step method
derive3D(diameters, numbins=12, set_limit=None, fit=True)

# Using ad hoc initial guess values for correcting a wrong fit
# The script will ask you about the new guessing values
derive3D(diameters, numbins=12, set_limit=None, fit=True, initial_guess=True)
```
