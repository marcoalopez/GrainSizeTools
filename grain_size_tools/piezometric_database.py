# ============================================================================ #
#                                                                              #
#    This piezometric database is part of the "GrainSizeTools Script"          #
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
#    Database version 2024.02.xx                                               #
#    For details see: http://marcoalopez.github.io/GrainSizeTools/             #
#    download at https://github.com/marcoalopez/GrainSizeTools/releases        #
#                                                                              #
# ============================================================================ #

# ============================================================================ #
# This is a curated list of paleopizometers used by the GrainSizeTools script  #
# to estimate differential stress from dynamically recrystallized grain size.  #
# Save this file in the same directory as GrainSizeTools                       #
# ============================================================================ #

from types import SimpleNamespace

def quartz(piezometer=None):
    """ Database for quartz piezometers.

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
        linear_intercepts = False
        correction_factor = False
        reference = 'https://doi.org/10.1029/2003GL018444'
        notes = None

    elif piezometer == 'Stipp_Tullis_BLG':
        B, m = 1264.1, 1.64
        warn = 'Ensure that you entered the apparent grain size as the root mean square (RMS)'
        linear_intercepts = False
        correction_factor = False
        reference = 'https://doi.org/10.1029/2003GL018444'
        notes = None

    elif piezometer == 'Holyoke':
        B, m = 490.3, 0.79
        warn = 'Ensure that you entered the apparent grain size as the root mean square (RMS)'
        linear_intercepts = False
        correction_factor = False
        reference = 'https://doi.org/10.1016/j.tecto.2010.08.001'
        notes = None

    elif piezometer == 'Holyoke_BLG':
        B, m = 883.9, 1.85
        warn = 'Ensure that you entered the apparent grain size as the root mean square (RMS)'
        linear_intercepts = False
        correction_factor = False
        reference = 'https://doi.org/10.1016/j.tecto.2010.08.001'
        notes = None

    elif piezometer == 'Cross':
        B, m = 593.0, 0.71
        warn = 'Ensure that you entered the apparent grain size as the root mean square (RMS)'
        linear_intercepts = False
        correction_factor = False
        reference = 'https://doi.org/10.1002/2017GL073836'
        notes = None

    elif piezometer == 'Cross_hr':
        B, m = 450.9, 0.63
        warn = 'Ensure that you entered the apparent grain size as the root mean square (RMS)'
        linear_intercepts = False
        correction_factor = False
        reference = 'https://doi.org/10.1002/2017GL073836'
        notes = None

    elif piezometer == 'Shimizu':
        B, m = 352, 0.8
        warn = 'Ensure that you entered the apparent grain size as the median in log(e) scale'
        linear_intercepts = False
        correction_factor = False
        reference = 'https://doi.org/10.1016/j.jsg.2008.03.004'
        notes = 'The Shimizu (2008) piezometer requires entering the grain size as the \
                logarithmic median apparent grain size calculated using equivalent \
                circular diameters with no stereological correction. It uses a different \
                piezometer model to the Twiss model in which the stress estimation is \
                temperature-dependent.'

    elif piezometer == 'Twiss':
        B, m = 550, 0.68
        warn = 'Ensure that you entered the apparent grain size as the arithmetic mean grain size'
        linear_intercepts = True
        correction_factor = 1.5
        reference = 'https://www.doi.org/10.1007/BF01637105'
        notes = 'Twiss (1977) piezometer was calibrated using the linear intercept (LI) grain size \
                multiplied by 1.5 (correction factor). If equivalent circular diameters (ECD) \
                without stereological correction are used, they must be converted to LIs using the \
                empirical equation of De Hoff and Rhines (1968) as follows: \
                LI = (1.5 / sqrt(4/pi)) * ECD'

    else:
        quartz()
        raise ValueError('Piezometer name misspelled. Please choose between valid piezometers')
    
    return SimpleNamespace(B=B,
                           m=m,
                           warn=warn,
                           linear_intercepts=linear_intercepts,
                           correction_factor=correction_factor,
                           reference=reference,
                           notes=notes)


def calcite(piezometer=None):
    """ Database for calcite piezometers.

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
        linear_intercepts = False
        correction_factor = False
        reference = 'https://doi.org/10.1029/95JB02500'
        notes = None

    elif piezometer == 'Rutter_GBM':
        B, m = 2691.53, 0.89
        warn = 'Ensure that you entered the apparent grain size as the arithmetic mean in linear scale'
        linear_intercepts = False
        correction_factor = False
        reference = 'https://doi.org/10.1029/95JB02500'
        notes = None

    elif piezometer == 'Barnhoorn':
        B, m = 537.03, 0.82
        warn = 'Ensure that you entered the apparent grain size as the arithmetic mean in linear scale'
        linear_intercepts = False
        correction_factor = False
        reference = 'https://doi.org/10.1016/j.jsg.2003.11.024'
        notes = None

    elif piezometer == 'Platt_Bresser':
        B, m = 538.40, 0.82
        warn = 'Ensure that you entered the apparent grain size as the root mean square in linear scale'
        linear_intercepts = False
        correction_factor = False
        reference = 'https://doi.org/10.1016/j.jsg.2017.10.012'
        notes = 'Contrary to other calcite piezometers, this one uses the RMS average.'

    elif piezometer == 'Valcke':
        B, m = 1467.92, 1.67
        warn = 'Ensure that you entered the apparent grain size the arithmetic mean in linear scale'
        linear_intercepts = False
        correction_factor = False
        reference = 'https://doi.org/10.1144/SP409.4'
        notes = None

    else:
        calcite()
        raise ValueError('Piezometer name misspelled. Please choose between valid piezometers')

    return SimpleNamespace(B=B,
                           m=m,
                           warn=warn,
                           linear_intercepts=linear_intercepts,
                           correction_factor=correction_factor,
                           reference=reference,
                           notes=notes)


def olivine(piezometer=None):
    """ Database for olivine piezometers

    Parameter
    ---------
    piezometer : string or None
        the piezometric relation
    """

    if piezometer is None:
        print('Available piezometers:')
        print("'Jung_Karato'")
        print("'VanderWal_wet'")
        # print("'Tasaka_wet'")
        return None

    elif piezometer == 'Jung_Karato':
        B, m = 5461.03, 0.85
        warn = 'Ensure that you entered the apparent grain size as the arithmetic mean in linear scale'
        linear_intercepts = True
        correction_factor = 1.5
        reference = 'https://doi.org/10.1016/S0191-8141(01)00005-0'
        notes = 'The Jung & Karato (2001) piezometer was calibrated using the linear intercept (LI) \
                grain size multiplied by 1.5 (correction factor). If equivalent circular diameters (ECD) \
                without stereological correction are used, they must be converted to LIs using the \
                empirical equation of De Hoff and Rhines (1968) as follows: \
                LI = (1.5 / sqrt(4/pi)) * ECD'

    elif piezometer == 'VanderWal_wet':
        B, m = 1355.4, 0.75
        warn = 'Ensure that you entered the apparent grain size as the arithmetic mean in linear scale'
        linear_intercepts = True
        correction_factor = 1.5
        reference = 'https://doi.org/10.1029/93GL01382'
        notes = 'The Van der Wal (1993) piezometer was calibrated using the linear intercept (LI) \
                grain size multiplied by 1.5 (correction factor). If equivalent circular diameters (ECD) \
                without stereological correction are used, they must be converted to LIs using the \
                empirical equation of De Hoff and Rhines (1968) as follows: \
                LI = (1.5 / sqrt(4/pi)) * ECD'

    # elif piezometer == 'Tasaka_wet':
    #     B, m = 719.7, 0.75
    #     warn = 'Ensure that you entered the apparent grain size as the arithmetic mean in linear scale'
    #     linear_intercepts = False
    #     correction_factor = 4 / 3.141592
    #     reference = 'https://doi.org/10.1002/2015JB012096'
    #     notes = None

    else:
        olivine()
        raise ValueError('Piezometer name misspelled. Please choose between valid piezometers')

    return SimpleNamespace(B=B,
                           m=m,
                           warn=warn,
                           linear_intercepts=linear_intercepts,
                           correction_factor=correction_factor,
                           reference=reference,
                           notes=notes)


def feldspar(piezometer=None):
    """ Database for feldspar piezometers

    Parameter
    ---------
    piezometer : string or None
        the piezometric relation

    References
    ----------
    | Post and Tullis (1999) https://doi.org/10.1016/S0040-1951(98)00260-1

    """

    if piezometer is None:
        print('Available piezometers:')
        print("'Post_Tullis_BLG'")
        return None

    elif piezometer == 'Post_Tullis_BLG':
        B, m = 433.4, 1.52
        warn = 'Ensure that you entered the apparent grain size as the median in linear scale'
        linear_intercepts = True
        correction_factor = 1.0
        reference = 'https://doi.org/10.1016/S0040-1951(98)00260-1'
        notes = 'The Post and Tullis (1999) piezometer was calibrated using the median of the  \
                equivalent circular diameters (ECD) grain size with no stereological correction.'

    else:
        feldspar()
        raise ValueError('Piezometer name misspelled. Please choose between valid piezometers')

    return SimpleNamespace(B=B,
                           m=m,
                           warn=warn,
                           linear_intercepts=linear_intercepts,
                           correction_factor=correction_factor,
                           reference=reference,
                           notes=notes)


if __name__ == '__main__':
    pass
else:
    print('database v.2024.02.xx imported')
