# The stereology module

TODO

## The Saltykov method

```python
stereology.Saltykov(dataset['diameters'], numbins=11, calc_vol=50)
```

```
=======================================
volume fraction (up to 50 microns) = 41.65 %
bin size = 14.24
=======================================
```



## The two-step method

TODO

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

