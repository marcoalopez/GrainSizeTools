# ============================================================================ #
#                                                                              #
#    This is part of the "GrainSizeTools Script"                               #
#    A Python script for characterizing grain size from thin sections          #
#                                                                              #
#    Copyright (c) 2014-present   Marco A. Lopez-Sanchez                       #
#                                                                              #
#    Licensed under the Apache License, Version 2.0 (the "License");           #
#    you may not use this file except in compliance with the License.          #
#    You may obtain a copy of the License at                                   #
#                                                                              #
#        http://www.apache.org/licenses/LICENSE-2.0                            #
#                                                                              #
#    Unless required by applicable law or agreed to in writing, software       #
#    distributed under the License is distributed on an "AS IS" BASIS,         #
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  #
#    See the License for the specific language governing permissions and       #
#    limitations under the License.                                            #
#                                                                              #
#    Version 3.0.1                                                             #
#    For details see: http://marcoalopez.github.io/GrainSizeTools/             #
#    download at https://github.com/marcoalopez/GrainSizeTools/releases        #
#                                                                              #
# ============================================================================ #

# ============================================================================ #
# This is a curated list of paleopizometers used by the GrainSizeTools script  #
# to estimate differential stress from dynamically recrystallized grain size.  #
# Save this file in the same directory as GrainSizeTools                       #
# ============================================================================ #


def quartz(piezometer=None):
    """ Data base for quartz piezometers. It returns the material parameter,
    the exponent and a warn with the "average" grain size measure to use.

    Parameter
    ---------
    piezometer : string or None
        the piezometric relation

    References
    ----------
    | Cross et al. (2017) https://doi.org/10.1002/2017GL073836
    | Holyoke and Kronenberg (2010) https://doi.org/10.1016/j.tecto.2010.08.001
    | Shimizu (2008) https://doi.org/10.1016/j.jsg.2008.03.004
    | Stipp and Tullis (2003)  https://doi.org/10.1029/2003GL018444
    | Twiss (1977) https://www.doi.org/10.1007/BF01637105

    Assumptions
    -----------
    - The piezometer relations of Stipp and Tullis (2003), Holyoke and Kronenberg
    (2010) and Cross et al. (2007) requires entering the grain size as the square
    root mean apparent grain size calculated using equivalent circular diameters
    with no stereological correction.

    - The piezometer relation of Shimizu (2008) requires entering the grain size
    as the logarithmic median apparent grain size calculated using equivalent
    circular diameters with no stereological correction.

    - The piezometer of Twiss (1977) requires entering the arithmetic mean apparent
    grain size calculated from equivalent circular diameters (ECD) with no stereological
    correction. The function will convert this value to mean linear intercept (LI)
    grain size using the De Hoff and Rhines (1968) empirical relation and assuming
    that LI was originally multiplied by 1.5 (correction factor). Then the final
    relation is: LI = (1.5 / sqrt(4/pi)) * ECD
    """

    if piezometer is None:
        print('Available piezometers:')
        print("'Cross'")
        print("'Cross_hr'")
        print("'Holyoke'")
        print("'Holyoke_BLG'")
        print("'Shimizu'")
        print("'Stipp_Tullis'")
        print("'Stipp_Tullis_BLG'")
        print("'Twiss'")
        return None

    elif piezometer == 'Stipp_Tullis':
        B, m = 669.0, 0.79
        warn = 'Ensure that you entered the apparent grain size as the root mean square (RMS)'
        linear_interceps = False
        correction_factor = False

    elif piezometer == 'Stipp_Tullis_BLG':
        B, m = 1264.1, 1.64
        warn = 'Ensure that you entered the apparent grain size as the root mean square (RMS)'
        linear_interceps = False
        correction_factor = False

    elif piezometer == 'Holyoke':
        B, m = 490.3, 0.79
        warn = 'Ensure that you entered the apparent grain size as the root mean square (RMS)'
        linear_interceps = False
        correction_factor = False

    elif piezometer == 'Holyoke_BLG':
        B, m = 883.9, 1.85
        warn = 'Ensure that you entered the apparent grain size as the root mean square (RMS)'
        linear_interceps = False
        correction_factor = False

    elif piezometer == 'Cross':
        B, m = 593.0, 0.71
        warn = 'Ensure that you entered the apparent grain size as the root mean square (RMS)'
        linear_interceps = False
        correction_factor = False

    elif piezometer == 'Cross_hr':
        B, m = 450.9, 0.63
        warn = 'Ensure that you entered the apparent grain size as the root mean square (RMS)'
        linear_interceps = False
        correction_factor = False

    elif piezometer == 'Shimizu':
        B, m = 352, 0.8
        warn = 'Ensure that you entered the apparent grain size as the median in log(e) scale'
        linear_interceps = False
        correction_factor = False

    elif piezometer == 'Twiss':
        B, m = 550, 0.68
        warn = 'Ensure that you entered the apparent grain size as the arithmetic mean grain size'
        linear_interceps = True
        correction_factor = 1.5

    else:
        quartz()
        raise ValueError('Piezometer name misspelled. Please choose between valid piezometers')

    return B, m, warn, linear_interceps, correction_factor


def calcite(piezometer=None):
    """ Data base for calcite piezometers. It returns the material parameter,
    the exponent parameter and a warn with the "average" grain size measure to be use.

    Parameter
    ---------
    piezometer : string or None
        the piezometric relation

    References
    ----------
    | Barnhoorn et al. (2004) https://doi.org/10.1016/j.jsg.2003.11.024
    | Platt and De Bresser (2017) https://doi.org/10.1016/j.jsg.2017.10.012
    | Rutter (1995) https://doi.org/10.1029/95JB02500
    | Valcke et al. (2015) https://doi.org/10.1144/SP409.4

    Assumptions
    -----------
    - The piezometer of Rutter (1995) requires entering the grain size
    as the linear mean apparent grain size calculated using equivalent
    circular diameters with no stereological correction.
    """

    if piezometer is None:
        print('Available piezometers:')
        print("'Barnhoorn'")
        print("'Platt_Bresser'")
        print("'Rutter_SGR'")
        print("'Rutter_GBM'")
        print("'Valcke'")
        return None

    elif piezometer == 'Rutter_SGR':
        B, m = 812.83, 0.88
        warn = 'Ensure that you entered the apparent grain size as the arithmetic mean in linear scale'
        linear_interceps = False
        correction_factor = False

    elif piezometer == 'Rutter_GBM':
        B, m = 2691.53, 0.89
        warn = 'Ensure that you entered the apparent grain size as the arithmetic mean in linear scale'
        linear_interceps = False
        correction_factor = False

    elif piezometer == 'Barnhoorn':
        B, m = 537.03, 0.82
        warn = 'Ensure that you entered the apparent grain size as the arithmetic mean in linear scale'
        linear_interceps = False
        correction_factor = False

    elif piezometer == 'Platt_Bresser':
        B, m = 538.40, 0.82
        warn = 'Ensure that you entered the apparent grain size as the root mean square in linear scale'
        linear_interceps = False
        correction_factor = False

    elif piezometer == 'Valcke':
        B, m = 1467.92, 1.67
        warn = 'Ensure that you entered the apparent grain size the arithmetic mean in linear scale'
        linear_interceps = False
        correction_factor = False

    else:
        calcite()
        raise ValueError('Piezometer name misspelled. Please choose between valid piezometers')

    return B, m, warn, linear_interceps, correction_factor


def olivine(piezometer=None):
    """ Data base for calcite piezometers. It returns the material parameter,
    the exponent parameter and a warn with the "average" grain size measure to be use.

    Parameter
    ---------
    piezometer : string or None
        the piezometric relation

    References
    ----------
    | Jung and Karato (2001) https://doi.org/10.1016/S0191-8141(01)00005-0
    | Van der Wal et al. (1993) https://doi.org/10.1029/93GL01382

    Assumptions
    -----------
    - The piezometer of Van der Wal (1993) requires entering the linear mean apparent
    grain size in microns calculated from equivalent circular diameters (ECD) with no
    stereological correction. The function will convert automatically this value to
    linear intercept (LI) grain size using the De Hoff and Rhines (1968) correction.
    It is assumed that LI was multiplied by 1.5 (correction factor), the final relation
    is: LI = (1.5 / sqrt(4/pi)) * ECD

    - The piezometer of Jung and Karato (2001) requires entering the linear mean
    apparent grain size in microns calculated from equivalent circular diameters
    (ECD) with no stereological correction. The function will convert automatically
    this value to linear intercept (LI) grain size using the De Hoff and Rhines
    (1968) empirical equation. Since LI was originally multiplied by 1.5 (correction
    factor), the final relation is: LI = (1.5 / sqrt(4/pi)) * ECD
    """

    if piezometer is None:
        print('Available piezometers:')
        print("'Jung_Karato'")
        print("'VanderWal_wet'")
        print("'Tasaka_wet'")
        return None

    elif piezometer == 'Jung_Karato':
        B, m = 5461.03, 0.85
        warn = 'Ensure that you entered the apparent grain size as the arithmetic mean in linear scale'
        linear_interceps = True
        correction_factor = 1.5

    elif piezometer == 'VanderWal_wet':
        B, m = 1355.4, 0.75
        warn = 'Ensure that you entered the apparent grain size as the arithmetic mean in linear scale'
        linear_interceps = True
        correction_factor = 1.2

    elif piezometer == 'Tasaka_wet':
        B, m = 719.7, 0.75
        warn = 'Ensure that you entered the apparent grain size as the arithmetic mean in linear scale'
        linear_interceps = False
        correction_factor = 1.2

    else:
        olivine()
        raise ValueError('Piezometer name misspelled. Please choose between valid piezometers')

    return B, m, warn, linear_interceps, correction_factor


def feldspar(piezometer=None):
    """ Data base for calcite piezometers. It returns the material parameter, the exponent
    parameter and a warn with the "average" grain size measure to be use.

    Parameter
    ---------
    piezometer : string or None
        the piezometric relation

    References
    ----------
    | Post and Tullis (1999) https://doi.org/10.1016/S0040-1951(98)00260-1

    Assumptions
    -----------
    - The piezometer of Post and Tullis (1999) requires entering the median
    apparent grain size calculated from equivalent circular diameters (ECD) with
    no stereological correction. The function will convert this value to the mean
    linear intercept (LI) grain size using the De Hoff and Rhines (1968) empirical
    relation LI = ECD / sqrt(4/pi)

    Returns
    -------
    The differential stress in MPa, a floating point number
    """

    if piezometer is None:
        print('Available piezometers:')
        print("'Post_Tullis_BLG'")
        return None

    elif piezometer == 'Post_Tullis_BLG':
        B, m = 433.4, 1.52
        warn = 'Ensure that you entered the apparent grain size as the median in linear scale'
        linear_interceps = True
        correction_factor = 1.0

    else:
        feldspar()
        raise ValueError('Piezometer name misspelled. Please choose between valid piezometers')

    return B, m, warn, linear_interceps, correction_factor


if __name__ == '__main__':
    pass
else:
    print('module piezometers imported')
