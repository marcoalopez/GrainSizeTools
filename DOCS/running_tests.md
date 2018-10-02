# Running test

This document provides a way to check the functionality of the script. For this, use the data provided with the script in the file ``data_set.txt`` , copy the commands indicated in the different sections and paste them in the console, and check if the results are the same. 



## Test the ``extract_column`` function

```python
# find and open the data_set.txt file through a file selection dialog
>>> areas = extract_column()

         Area  Circ.    Feret    ...     MinFeret     AR  Round  Solidity
0  1   157.25  0.680   18.062    ...       13.500  1.101  0.908     0.937
1  2  2059.75  0.771   62.097    ...       46.697  1.314  0.761     0.972
2  3  1961.50  0.842   57.871    ...       46.923  1.139  0.878     0.972
3  4  5428.50  0.709  114.657    ...       63.449  1.896  0.528     0.947
4  5   374.00  0.699   29.262    ...       16.000  1.515  0.660     0.970

[5 rows x 11 columns]
               Area  Circ.   Feret    ...     MinFeret     AR  Round  Solidity
2656  2657   452.50  0.789  28.504    ...       22.500  1.235  0.810     0.960
2657  2658  1081.25  0.756  47.909    ...       31.363  1.446  0.692     0.960
2658  2659   513.50  0.720  32.962    ...       20.496  1.493  0.670     0.953
2659  2660   277.75  0.627  29.436    ...       17.002  1.727  0.579     0.920
2660  2661   725.00  0.748  39.437    ...       28.025  1.351  0.740     0.960

[5 rows x 11 columns]
 
column extracted:
Area = [ 157.25 2059.75 1961.5  ...  513.5   277.75  725.  ]
n = 2661


# Do the same specifying the file path (define your own absolute filepath)
>>> extract_column(file_path='.../GrainSizeTools/data_set.txt')


# Extract other column
>>> extract_column(col_name='Feret')
...
column extracted:
Feret = [18.062 62.097 57.871 ... 32.962 29.436 39.437]


# catching common exceptions
>>> extract_column(col_name='Foo')
...
KeyError: 'Foo'
    
# filepath does not exist
FileNotFoundError: File b'.../data_set.txt' does not exist
```



## Test the ``area2diameter`` function

```python
>>> area2diameter(areas)
array([14.14980277, 51.210889  , 49.97458721, ..., 25.56967943,
       18.80537911, 30.3825389 ])


>>> area2diameter(areas, correct_diameter=1.0)
array([15.14980277, 52.210889  , 50.97458721, ..., 26.56967943,
       19.80537911, 31.3825389 ])
```



## Test the ``calc_grain_size`` function

```python
# check with default options
>>> diameters = area2diameter(areas)
>>> calc_grain_size(diameters)

DESCRIPTIVE STATISTICS
 
Arithmetic mean grain size = 34.79 microns
Standard deviation = 18.32 (1-sigma)
RMS mean = 39.31 microns
Geometric mean = 30.1 microns
 
Median grain size = 31.53 microns
Interquartile range (IQR) = 23.98
 
Peak grain size (based on KDE) = 24.28 microns
KDE bandwidth = 4.01 (silverman rule)
 
HISTOGRAM FEATURES
The modal interval is 16.83 - 20.24
The number of classes are 45
The bin size is 3.41 according to the auto rule


# check using different grain size scales (use arithmetic mean and SD to compare)
>>> calc_grain_size(diameters, plot='sqrt')
...
Arithmetic mean grain size = 5.7 microns
Standard deviation = 1.53 (1-sigma)


>>> calc_grain_size(diameters, plot='log')
...
Arithmetic mean grain size = 3.4 microns
Standard deviation = 0.56 (1-sigma)


>>> calc_grain_size(diameters, plot='log10')
...
Arithmetic mean grain size = 1.48 microns
Standard deviation = 0.24 (1-sigma)
 

>>> calc_grain_size(diameters, areas=areas, plot='area')
... 
Area-weighted mean grain size = 53.88 microns
...
The number of classes are 46
The bin size is 3.4 according to the auto rule


>>> calc_grain_size(diameters, areas=areas, plot='norm')
Define the normalization factor (1 to 3) 
1 -> mean; 2 -> median; 3 -> max_freq: 1
... 
Arithmetic mean grain size = 1.0 microns
Standard deviation = 0.16 (1-sigma)

Define the normalization factor (1 to 3) 
1 -> mean; 2 -> median; 3 -> max_freq: 2
... 
Median grain size = 1.0 microns
Interquartile range (IQR) = 0.22

Define the normalization factor (1 to 3) 
1 -> mean; 2 -> median; 3 -> max_freq: 3
...     
Peak grain size (based on KDE) = 1.0 microns
KDE bandwidth = 0.03 (silverman rule)


# catching common mistakes/exceptions
# bad name
>>> calc_grain_size(diameters, plot='foo')
ValueError: The type of plot has been misspelled, please use 'lin', 'log', 'log10', 'sqrt', 'norm', or 'area'
    
 # missing areas when using the area weighted approach
>>> calc_grain_size(diameters, plot='areas')
You must provide the areas of the grain sections!

# wrong choice when using normalization approach
>>> calc_grain_size(diameters, areas=areas, plot='norm')
Define the normalization factor (1 to 3) 
1 -> mean; 2 -> median; 3 -> max_freq: 4
ValueError: Normalization factor has to be defined as 1, 2, or 3
```

```python
# Test binsize functionality. Note that we just check a number (not all) of different plug-in methods since this functionality belong to the numpy package and hence it is already tested by numpy developers.

>>> calc_grain_size(diameters, binsize='doane')
...
The bin size is 9.02 according to the doane rule


>>> calc_grain_size(diameters, binsize='scott')
...
The bin size is 4.51 according to the scott rule


# ad hoc bin size
>>> calc_grain_size(diameters, binsize=7.5)
...
HISTOGRAM FEATURES
The modal interval is 18.19 - 25.69
The number of classes are 21


# catching common mistakes
# bad name
>>> calc_grain_size(diameters, binsize='foo')
ValueError: 'foo' is not a valid estimator for `bins`
```

```python
# Test kde bandwidth functionality

>>> calc_grain_size(diameters, bandwidth='scott')
...
Peak grain size (based on KDE) = 24.2 microns
KDE bandwidth = 3.78 (scott rule)
...

>>> calc_grain_size(diameters, bandwidth=6.0)
...
Peak grain size (based on KDE) = 25.29 microns
KDE bandwidth = 6.0
...

# catching common mistakes/exceptions
# bad name
>>> calc_grain_size(diameters, bandwidth='foo')
ValueError: `bw_method` should be 'scott', 'silverman', a scalar or a callable.
```



## Test the ``Saltykov`` function

```python
>>> Saltykov(diameters)  # check plot
bin size = 15.66


>>> Saltykov(diameters, numbins=14)  # check plot
bin size = 11.19


>>> Saltykov(diameters, numbins=16, calc_vol=40) 
volume fraction (up to 40 microns) = 20.33 %
bin size = 9.79


# Get the frequency and the right edges of the classes
>>> Saltykov(diameters, return_data=True)
(array([  7.82979491,  23.48938472,  39.14897454,  54.80856436,
         70.46815417,  86.12774399, 101.78733381, 117.44692362,
        133.10651344, 148.76610326]),
 array([2.67457256e-03, 2.30102443e-02, 2.03855325e-02, 1.15382229e-02,
        3.80778332e-03, 1.86010761e-03, 5.21259159e-04, 2.47891410e-05,
        0.00000000e+00, 3.61215495e-05]))


# generating text files with the output
>>> Saltykov(diameters, text_file='foo.csv')
The file foo.csv was created  # check file
bin size = 15.66

>>> Saltykov(diameters, text_file='bar.txt')
The file bar.txt was created  # check file
bin size = 15.66


# test left edge (see plot)
>>> Saltykov(diameters, left_edge=5.0)
>>> Saltykov(diameters, left_edge='min')  # check using min(diameters)


# catching common mistakes
# set a grain size higher than the greatest grain size in the population to estimate the volume (it should return 100%)
>>> Saltykov(diameters, calc_vol=10000)
volume fraction (up to 10000 microns) = 100 %


# not specifiying the correct type of text file
>>> Saltykov(diameters, text_file='foo')
>>> Saltykov(diameters, text_file='foo.xlsx')
ValueError: text file must be specified as .csv or .txt
```





## Test the ``calc_shape`` function

```python
# default parameters
>>> calc_shape(diameters)
OPTIMAL VALUES
Number of clasess: 11
MSD (shape) = 1.63 ± 0.06
Geometric mean (location) = 36.05 ± 1.27


>>> calc_shape(diameters, class_range=(12, 18))
OPTIMAL VALUES
Number of clasess: 12
MSD (shape) = 1.64 ± 0.07
Geometric mean (location) = 36.22 ± 1.62


>>> calc_shape(diameters, initial_guess=True)
Define an initial guess for the MSD parameter (the default value is 1.2; MSD > 1.0): 1.6
Define an initial guess for the geometric mean (the default value is 35.0): 40.0
# You should obtain the same results provided in the first example
```





```python
>>> my_results = [165.3, 174.2, 180.1]
>>> confidence_interval(data=my_results, confidence=0.95)
Confidence set at 99.0 %
Mean = 173.2 ± 42.69
Max / min = 215.89 / 130.51
Coefficient of variation = 24.6 %


>>> confidence_interval(data=my_results, confidence=0.99)
Confidence set at 99.0 %
Mean = 173.2 ± 42.69
Max / min = 215.89 / 130.51
Coefficient of variation = 24.6 %


# catching common mistakes
confidence_interval(data=my_results, confidence=1.2)
...
ValueError: alpha must be between 0 and 1 inclusive
```





```python
# check "Available piezometers
>>> quartz()
Available piezometers:
'Cross'
'Cross_hr'
'Holyoke'
'Holyoke_BLG'
'Shimizu'
'Stipp_Tullis'
'Stipp_Tullis_BLG'
'Twiss'

>>> olivine()
Available piezometers:
'Jung_Karato'
'VanderWal_wet'

>>> feldspar()
Available piezometers:
'Post_Tullis_BLG'

>>> calcite()
Available piezometers:
'Barnhoorn'
'Platt_Bresser'
'Rutter_SGR'
'Rutter_GBM'
'Valcke'

# Check estimates (TODO: Automatize this using all the piezometers!)
>>> calc_diffstress(grain_size=5.7, phase='quartz', piezometer='Stipp_Tullis')
differential stress = 169.16 MPa
Ensure that you entered the apparent grain size as the root mean square (RMS)!


>>> calc_diffstress(grain_size=35, phase='olivine', piezometer='VanderWal_wet')
differential stress = 282.03 MPa
Ensure that you entered the apparent grain size as the mean in linear scale!


>>> calc_diffstress(grain_size=35, phase='calcite', piezometer='Rutter_SGR')
differential stress = 35.58 MPa
Ensure that you entered the apparent grain size as the mean in linear scale!


# Catching exceptions
# wrong phase name
>>> calc_diffstress(grain_size=5.7, phase='foo', piezometer='Stipp_Tullis')
ValueError: Phase name misspelled. Please choose between valid mineral names

# wrong piezometer name
>>> calc_diffstress(grain_size=5.7, phase='calcite', piezometer='Stipp_Tullis')
Available piezometers:
'Barnhoorn'
'Platt_Bresser'
'Rutter_SGR'
'Rutter_GBM'
'Valcke
...
ValueError: Piezometer name misspelled. Please choose between valid piezometer
    
# missing required positional arguments
>>> calc_diffstress(grain_size=5.7, phase='calcite')
TypeError: calc_diffstress() missing 1 required positional argument: 'piezometer'
        
>>> calc_diffstress(grain_size=5.7, piezometer='Stipp_Tullis')
TypeError: calc_diffstress() missing 1 required positional argument: 'phase'
```

