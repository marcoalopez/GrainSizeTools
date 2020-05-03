# Paleopiezometry based on dynamically recrystallized grain size



The script includes a function for estimating differential stress based on "average" recrystallized grain sizes named ``calc_diffstress()``. This function requires

- defining the mineral phase and the piezometer relation to use,

-  entering the (apparent) grain size as the **equivalent circular diameter in microns**,
- measured with a **specific type of "average" with no stereological correction**,
- and set the type of stress, either uniaxial compression/extension or plane stress, for proper stress correction.

For the first requirement, the GrainSizeTools script includes common mineral phases such as quartz, calcite, olivine and albite (more available soon) and a large list of piezometer relations (17 so far). Also, the script facilitates to write ad hoc piezometric relations.

For the second requirement, the function will automatically convert the equivalent circular diameter to linear intercepts where applicable using de Hoff and Rhines (1968) correction. This is, **you don't have to worry about whether the piezometer was originally calibrated using linear intercepts**, always use the equivalent circular diameters in microns.

The third requirement is key for a correct estimation of the differential stress since each paleopiezometer was calibrated for a specific average grain size (e.g. the arithmetic mean, median or RMS mean) and, hence, **only provides valid results if the same type of average is used**. Also, **you should not use any type of stereological correction for the estimation of the average grain size**, if the author(s) of the piezometer used any type of stereological correction, the average grain size will be automatically corrected by the function. 

The fourth requirement means that the user has to decide whether to correct or not the estimate of the differential stress for plane stress using the correction factor proposed by Paterson and Olgaard (2000). The rationale for this is that the experiments designed to calibrate piezometers are mainly performed in uniaxial compression while natural shear zones approximately behave as plane stress volumes.

In the next subsection, we will show examples of how to obtain information about the different piezometers and define these parameters.


## Get information on piezometric relations

Table 1 provides a list of the all piezometric relations currently available in the GrainSizeTools script with features (the type of average to use and the DRX mechanism) and references. The experimentally-derived parameters are provided in Tables 2 to 5.

Besides, you can get information interactively on the different available piezometric relations from the console just by typing ``piezometers.*()``, where * is the mineral phase, either ``quartz``, ``calcite``, ``olivine``, or ``feldspar``. For example:

```python
piezometers.quartz()
```

```
Available piezometers:
'Cross'
'Cross_hr'
'Holyoke'
'Holyoke_BLG'
'Shimizu'
'Stipp_Tullis'
'Stipp_Tullis_BLG'
'Twiss'
```

If you want to get the details of a particular piezometric relationship you can do so as follows. Remember that the relationship between recrystallized grain size and differential stress is ***σ~d~ = Bg^-m^***  where σ~d~ and g are the differential stress and the average grain size respectively.

```python
piezometers.quartz('Twiss')
```

```
(550,
 0.68,
 'Ensure that you entered the apparent grain size as the arithmetic mean grain size',
 True,
 1.5)
```

Note the five different outputs separated by commas which correspond with:
- the constant *B* of the piezometric relation
- the exponent *m* of the piezometric relation
- A warning indicating the average to use with this piezometric relation
- An indication of whether the piezometric relation was calibrated using linear intercepts (if ``False`` the piezometric relation was calibrated using equivalent circular diameters.
- The stereological correction factor used (if applicable). If ``False``, no stereological correction applies.



**Table 1.** Relation of piezometers (in alphabetical order) and the apparent grain size required to obtain meaningful differential stress estimates

|         Piezometer         |  Apparent grain size†  | DRX mechanism  |      Phase       |           Reference           |
| :------------------------: | :--------------------: | :------------: | :--------------: | :---------------------------: |
|       ``Barnhoorn``        |      arith. mean       |    SRG, GBM    |     calcite      |    Barnhoorn et al. (2004)    |
| ``Cross`` and ``Cross_hr`` |        RMS mean        |    BLG, SGR    |      quartz      |      Cross et al. (2017)      |
|       ``'Holyoke'``        |        RMS mean        |  Regimes 2, 3  |      quartz      | Holyoke and Kronenberg (2010) |
|     ``'Holyoke_BLG'``      |        RMS mean        | Regime 1 (BLG) |      quartz      | Holyoke and Kronenberg (2010) |
|   ```'Jung_Karato'```*§*   |      arith. mean       |      BLG       |   olivine, wet   |     Jung & Karato (2001)      |
|   `` 'Platt_Bresser' ``    |        RMS mean        |    BLG, SGR    |     calcite      |  Platt and De Bresser (2017)  |
| ```'Post_Tullis_BLG'```*§* |         Median         |      BLG       |      albite      |    Post and Tullis (1999)     |
|     ```'Rutter_SGR'```     |      arith. mean       |      SGR       |     calcite      |         Rutter (1995)         |
|     ```'Rutter_GBM'```     |      arith. mean       |      GBM       |     calcite      |         Rutter (1995)         |
|     `` 'Schmid' ``*§*      |                        |      SGR       |     calcite      |     Schmid et al. (1980)      |
|     ```'Shimizu'```*‡*     | Median in log(e) scale |   SGR + GBM    |      quartz      |        Shimizu (2008)         |
|    ```'Stipp_Tullis'```    |        RMS mean        |  Regimes 2, 3  |      quartz      |     Stipp & Tullis (2003)     |
|  ```'Stipp_Tullis_BLG'```  |        RMS mean        | Regime 1 (BLG) |      quartz      |     Stipp & Tullis (2003)     |
|      ```'Twiss'```*§*      |      arith. mean       |  Regimes 2, 3  |      quartz      |         Twiss (1977)          |
|       ``'Valcke' ``        |      arith. mean       |    BLG, SGR    |     calcite      |     Valcke et al. (2015)      |
|  ```'VanderWal_wet'```*§*  |      arith. mean       |                | Olivine, dry/wet |   Van der Wal et al. (1993)   |

*† Apparent grain size measured as equivalent circular diameters (ECD) with no stereological correction and reported in microns. The use of non-linear scales is indicated*  
*‡ Shimizu piezometer requires to provide the temperature during deformation in K*  
*§ These piezometers were originally calibrated using linear intercepts (LI) instead of ECD*



**Table 2**. Parameters relating the average apparent size of dynamically recrystallized grains and differential stress in quartz using a relation in the form ***d = A&sigma;<sup>-p</sup>*** or ***&sigma; = Bd<sup>-m</sup>***

|           Reference            |   phase   |     DRX      |  A†,‡   |  p†  |  B†,‡  |  m†  |
| :----------------------------: | :-------: | :----------: | :-----: | :--: | :----: | :--: |
|     Cross et al. (2017)*§*     |  quartz   | Regimes 2, 3 | 8128.3  | 1.41 | 593.0  | 0.71 |
|     Cross et al. (2017)*§*     | quartz hr | Regimes 2, 3 | 16595.9 | 1.59 | 450.9  | 0.63 |
| Holyoke & Kronenberg (2010)*¶* |  quartz   | Regimes 2, 3 |  2451   | 1.26 | 490.3  | 0.79 |
| Holyoke & Kronenberg (2010)*¶* |  quartz   |   Regime 1   |   39    | 0.54 | 883.9  | 1.85 |
|         Shimizu (2008)         |  quartz   |  SGR + GBM   |  1525   | 1.25 |  352   | 0.8  |
|    Stipp and Tullis (2003)     |  quartz   | Regimes 2, 3 | 3630.8  | 1.26 | 669.0  | 0.79 |
|    Stipp and Tullis (2003)     |  quartz   |   Regime 1   |   78    | 0.61 | 1264.1 | 1.64 |
|          Twiss (1977)          |  quartz   | Regimes 2, 3 |  1230   | 1.47 |  550   | 0.68 |

*† **B** and **m** relate to **A** and **p** as follows: B = A<sup>1/p</sup> and m = 1/p*   
*‡ **A** and **B** are in [&mu;m MPa<sup>p, m</sup>]*  
*§ Cross et al. (2017) reanalysed the samples of Stipp and Tullis (2003) using EBSD data for reconstructing the grains. Specifically, they use grain maps with a 1 m and a 200 nm (hr - high-resolution) step sizes . This is the preferred piezometer for quartz when grain size data comes from EBSD maps*  
*¶ Holyoke and Kronenberg (2010) provides a recalibration of the Stipp and Tullis (2003) piezometer*  



**Table 3**. Parameters relating the average apparent size of dynamically recrystallized grains and differential stress in olivine

|         Reference         |      phase       | DRX  | A†,‡  |  p†  |  B†,‡   |  m†  |
| :-----------------------: | :--------------: | :--: | :---: | :--: | :-----: | :--: |
|  Jung and Karato (2001)   |   olivine, wet   | BLG  | 25704 | 1.18 | 5461.03 | 0.85 |
| Van der Wal et al. (1993) | olivine, dry/wet |      | 15000 | 1.33 | 1355.4  | 0.75 |
|   Tasaka et al. (2015)    |   olivine wet    |      | 6310  | 1.33 |  719.7  | 0.75 |



**Table 4**. Parameters relating the average apparent size of dynamically recrystallized grains and differential stress in calcite

|          Reference          |  phase  |   DRX    |  A†,‡  |  p†  |  B†,‡   |  m†  |
| :-------------------------: | :-----: | :------: | :----: | :--: | :-----: | :--: |
|   Barnhoorn et al. (2004)   | calcite | SRG, GBM | 2134.4 | 1.22 | 537.03  | 0.82 |
| Platt and De Bresser (2017) | calcite | BLG, SGR |  2141  | 1.22 | 538.40  | 0.82 |
|        Rutter (1995)        | calcite |   SGR    | 2026.8 | 1.14 | 812.83  | 0.88 |
|        Rutter (1995)        | calcite |   GBM    | 7143.8 | 1.12 | 2691.53 | 0.89 |
|    Valcke et al. (2015)     | calcite | BLG, SGR | 79.43  | 0.6  | 1467.92 | 1.67 |



**Table 5**. Parameters relating the average apparent size of dynamically recrystallized grains and differential stress in albite

|       Reference        | phase  | DRX  | A†,‡ |  p†  | B†,‡  |  m†  |
| :--------------------: | :----: | :--: | :--: | :--: | :---: | :--: |
| Post and Tullis (1999) | albite | BLG  |  55  | 0.66 | 433.4 | 1.52 |



## Estimate differential stress using the ``calc_diffstress()`` function

Let us first look at the documentation of the:

```python
?calc_diffstress

Signature: calc_diffstress(grain_size, phase, piezometer, correction=False)
Docstring:
Apply different piezometric relations to estimate the differential
stress from average apparent grain sizes. The piezometric relation has
the following general form:

df = B * grain_size**-m

where df is the differential stress in [MPa], B is an experimentally
derived parameter in [MPa micron**m], grain_size is the aparent grain
size in [microns], and m is an experimentally derived exponent.

Parameters
----------
grain_size : positive scalar or array-like
    the apparent grain size in microns

phase : string {'quartz', 'olivine', 'calcite', or 'feldspar'}
    the mineral phase

piezometer : string
    the piezometric relation

correction : bool, default False
    correct the stress values for plane stress (Paterson and Olgaard, 2000)

 References
-----------
Paterson and Olgaard (2000) https://doi.org/10.1016/S0191-8141(00)00042-0
de Hoff and Rhines (1968) Quantitative Microscopy. Mcgraw-Hill. New York.

Call functions
--------------
piezometers.quartz
piezometers.olivine
piezometers.calcite
piezometers.albite

Assumptions
-----------
- Independence of temperature (excepting Shimizu piezometer), total strain,
flow stress, and water content.
- Recrystallized grains are equidimensional or close to equidimensional when
using a single section.
- The piezometer relations requires entering the grain size as "average"
apparent grain size values calculated using equivalent circular diameters
(ECD) with no stereological correction. See documentation for more details.
- When required, the grain size value will be converted from ECD to linear
intercept (LI) using a correction factor based on de Hoff and Rhines (1968):
LI = (correction factor / sqrt(4/pi)) * ECD
- Stress estimates can be corrected from uniaxial compression (experiments)
to plane strain (nature) multiplying the paleopiezometer by 2/sqrt(3)
(Paterson and Olgaard, 2000)

Returns
-------
The differential stress in MPa (a float)
File:      c:\users\marco\documents\github\grainsizetools\grain_size_tools\grainsizetools_script.py
Type:      function

```

As indicated in the documentation, the ``calc_diffstress()`` requires three (obligatory) inputs: (1) the average grain size in microns, (2) the mineral phase, and (3) the piezometric relation to use. We provide a few examples below:

```python
calc_diffstress(12, phase='quartz', piezometer='Twiss')
```

```
============================================================================
differential stress = 83.65 MPa

INFO:
Ensure that you entered the apparent grain size as the arithmetic mean grain size
ECD was converted to linear intercepts using de Hoff and Rhines (1968) correction
===========================================================================
```

The function returns the differential stress (in MPa) plus some relevant information about the corrections made and the type of average expected. Most piezometric calibrations were calibrated using uniaxial compression deformation experiments while in nature most shear zones approximately behaves as plane stress. Due to this, it may be necessary to correct the differential stress value. The ``calc_diffstress()`` allows you to apply the correction proposed by Paterson and Olgaard (2000) for this as follows (note the slightly different value of differential stress):

```python
# Apply the same piezometric relation but correct the estimate for plane stress
calc_diffstress(12, phase='quartz', piezometer='Twiss', correction=True)
```

```
============================================================================
differential stress = 96.59 MPa

INFO:
Ensure that you entered the apparent grain size as the arithmetic mean grain size
ECD was converted to linear intercepts using de Hoff and Rhines (1968) correction
============================================================================
```

Note that the stress estimate is a bit different compare to the value without the correction.

Some paleopiezometers require uncommon averages such as the root mean square or RMS, for example:

```python
piezometers.quartz('Stipp_Tullis')

(669.0,
 0.79,
 'Ensure that you entered the apparent grain size as the root mean square (RMS)',
 False,
 False)
```

In this case you should estimate the RMS as  
$RMS = \sqrt{\dfrac{1}{n} (x_{1}^2 + x_{2}^2 + ... + x_{n}^2)}$

```python
# Import the example dataset
filepath = 'C:/Users/marco/Documents/GitHub/GrainSizeTools/grain_size_tools/DATA/data_set.txt'
dataset = pd.read_csv(filepath, sep='\t')
dataset['diameters'] = 2 * np.sqrt(dataset['Area'] / np.pi)  # estimate ECD

# estimate the root mean squared
rms = np.sqrt(np.mean(dataset['diameters']**2))  # note that in Python the exponent operator is ** (as in Fortran) not ^ (as in Matlab)

calc_diffstress(rms, phase='quartz', piezometer='Stipp_Tullis')
```

```
============================================================================
differential stress = 36.79 MPa

INFO:
Ensure that you entered the apparent grain size as the root mean square (RMS)
============================================================================
```



## Estimation of the differential stress using arrays of values

Alternatively, you can use (NumPy) arrays as input to estimate several differential stresses at once. In this case, the ``calc_diffstress()`` function will return a NumPy array, so it is generally more useful to store it in a variable as in the example below.

```python
ameans = np.array([12.23, 13.71, 12.76, 11.73, 12.69, 10.67])  # a set of average grain size values
estimates = calc_diffstress(ameans, phase='olivine', piezometer='VanderWal_wet')
estimates
```

```
============================================================================
INFO:
Ensure that you entered the apparent grain size as the arithmetic mean in linear scale
ECD was converted to linear intercepts using de Hoff and Rhines (1968) correction
Differential stresses in MPa

array([167.41, 153.66, 162.16, 172.73, 162.83, 185.45])
```

If the set of estimated values belongs to the same structural element (e.g. different areas of the same mylonite or different rocks within the same shear zone), you may want to estimate the average differential stress from all the data. The GrainSizeTools script provides a method named ``conf_interval()`` for this.

```python
?conf_interval

Signature: conf_interval(data, confidence=0.95)
Docstring:
Estimate the confidence interval using the t-distribution with n-1
degrees of freedom t(n-1). This is the way to go when sample size is
small (n < 30) and the standard deviation cannot be estimated accurately.
For large datasets, the t-distribution approaches the normal distribution.

Parameters
----------
data : array-like
    the dataset

confidence : float between 0 and 1, optional
    the confidence interval, default = 0.95

Assumptions
-----------
the data follows a normal or symmetric distrubution (when sample size
is large)

call_function(s)
----------------
Scipy's t.interval

Returns
-------
the arithmetic mean, the error, and the limits of the confidence interval
File:      c:\users\marco\documents\github\grainsizetools\grain_size_tools\grainsizetools_script.py
Type:      function
```

```python
conf_interval(estimates)
```

```
Mean = 167.37 ± 11.41
Confidence set at 95.0 %
Max / min = 178.79 / 155.96
Coefficient of variation = ±6.8 %
```

