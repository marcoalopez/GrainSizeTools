# Paleopiezometry

*Define paleopizometry -> TODO*

The script includes a function for estimating differential stress via paleopiezometers based on "average" apparent grain sizes called ``calc_diffstress()`` and requires

- define the mineral phase and the piezometer relation to use

-  entering the (apparent) grain size as equivalent circular diameters in microns **with no stereological correction**
- entering a specific type of "average" grain size that depends on the piezometric relation used
- set the type of stress, either uniaxial compression/extension or plane stress, for proper stress correction

For the first requirement, the GrainSizeTools script includes common mineral phases such as quartz, calcite, olivine and albite (more available soon). 

For the second requirement, the ``calc_diffstress()`` function will automatically convert the equivalent circular diameter to linear intercepts using de Hoff and Rhines (1968) correction where applicable. Likewise, if the original author(s) of the piezometer used any type of stereological correction, this will be automatically applied to correct the value. This is, you don't have to worry about whether the piezometer was calibrated using linear intercepts or stereological corrections, always use the equivalent circular diameters in microns **with no stereological correction**

The third requirement is key for a correct estimation of the stress since each paleopiezometer was calibrated for a specific average grain size and, hence, **only provide valid results if the same type of average (arithmetic mean, median...) is used**.

The fourth requirement means that the user has to decide whether or not **to correct the estimate of the differential stress for plane stress** using the correction factor proposed by Paterson and Olgaard (2000). The rationale for this is that the experiments designed to calibrate piezometers are mainly performed in uniaxial compression while natural shear zones approximately behave as plane stress volumes.

Below are examples of how to obtain information about the different piezometers and define these parameters.


## Get information on paleopizometric relations

Table 1 provides a list of the all piezometric relations currently available in the GrainSizeTools script with features (the type of average to use and DRX mechanism) and references. The different experimentally-derived parameters can be seen in Tables 2 to 5.

You can get information from the console on the available piezometric relations  just by typing ``piezometers.*()``, where * is the mineral phase, either ``quartz``, ``calcite``, ``olivine``, or ``feldspar``. For example:

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

Also, if you want to obtain the complete information of a specific piezometer you can do it in the following way:

```python
piezometers.quartz('Twiss')
```

```

```

where...TODO

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

*† Apparent grain size measured as equivalent circular diameters (ECD) with no stereological correction and reported in microns. The use of non-linear scales are indicated*  
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



## Using the ``calc_diffstress()`` function

The ``calc_diffstress`` requires three (obligatory) inputs: (1) the apparent grain size **in microns**, (2) the mineral phase, and (3) the piezometric relation to use. We provide few examples below:

```python
calc_diffstress(12.0, phase='quartz', piezometer='Twiss')
```

```
============================================================================
differential stress = 83.65 MPa

INFO:
Ensure that you entered the apparent grain size as the arithmeic mean grain size
ECD was converted to linear intercepts using de Hoff and Rhines (1968) correction
============================================================================
```

TODO



```python
# Apply the same piezometric relation but correct the estimate for plane stress
calc_diffstress(12.0, phase='quartz', piezometer='Twiss', correction=True)
```

```
============================================================================
differential stress = 96.59 MPa

INFO:
Ensure that you entered the apparent grain size as the arithmeic mean grain size
ECD was converted to linear intercepts using de Hoff and Rhines (1968) correction
============================================================================
```

Note that the stress estimate is a bit different compare to the value without the correction.



You can pass as input an array of grain size values instead of a scalar value, in this case the function will returns an array of values 

```python
ameans = np.array([12.23, 13.71, 12.76, 11.73, 12.69, 10.67])
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

For example, the piezometer relation of Stipp and Tullis (2003) requires entering the grain size as *the root mean square (RMS) using equivalent circular diameters with no stereological correction*, and so on. Table 1 show all the implemented piezometers in GrainSizeTools v3.0+ and the apparent grain size required for each one. Despite some piezometers were originally calibrated using linear intercepts (LI), the script will always require entering a specific grain size average measured as equivalent circular diameters (ECD). The script will automatically approximate the ECD value to linear intercepts using the De Hoff and Rhines (1968) empirical relation. Also, the script takes into account if the authors originally used a specific correction factor for the grain size. For more details on the piezometers and the assumption made use the command ```help()```  in the console as follows:

```python
help(calc_diffstress)

# alternatively in Jupyterlab:
?calc_diffstress
```

