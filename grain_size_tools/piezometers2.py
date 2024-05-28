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
#    Version 3.2.0                                                             #
#    For details see: http://marcoalopez.github.io/GrainSizeTools/             #
#    download at https://github.com/marcoalopez/GrainSizeTools/releases        #
#                                                                              #
# ============================================================================ #

import yaml
from types import SimpleNamespace
import numpy as np


def calc_diffstress(grain_size, piezometer, correction=False):
    """ Apply different piezometric relation to estimate differential stress
    based on average apparent grain sizes. The piezometric relation has
    the following general form:

    diff_stress = B * grain_size**-m

    where differential stress is in [MPa], B is an experimentally
    derived parameter in [MPa micron**m], grain_size is the aparent grain
    size in [microns], and m is an experimentally derived exponent.

    Parameters
    ----------
    grain_size : positive scalar or array-like
        the apparent grain size in microns

    piezometer : SimpleNamespace
        the piezometric relation

    correction : bool, default False
        correct the stress values for plane stress (Paterson and Olgaard, 2000)

     References
    -----------
    Paterson and Olgaard (2000) https://doi.org/10.1016/S0191-8141(00)00042-0
    de Hoff and Rhines (1968) Quantitative Microscopy. Mcgraw-Hill. New York.

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
    """

    # Special cases (convert from ECD to linear intercepts)
    if piezometer.linear_interceps is True:
        grain_size = (piezometer.correction_factor / (np.sqrt(4 / np.pi))) * grain_size
        print('diameters were converted to linear intercepts using de Hoff and Rhines (1968) correction...')

    # Estimate differential stress
    if piezometer == 'Shimizu':
        T = float(input("Please, enter the temperature [in C degrees] during deformation: "))
        diff_stress = piezometer.B * grain_size**(-piezometer.m) * np.exp(698 / (T + 273.15))
        if correction is True:
            print('Differential stress corrected for plane stress (Paterson and Olgaard, 2000)')
            diff_stress = diff_stress * 2 / np.sqrt(3)

    else:
        diff_stress = piezometer.B * grain_size**-piezometer.m
        if correction is True:
            print('Differential stress corrected for plane stress (Paterson and Olgaard, 2000)')
            diff_stress = diff_stress * 2 / np.sqrt(3)

    print('============================================================================')
    if isinstance(diff_stress, (int, float)):
        print(f'differential stress = {diff_stress:0.2f} MPa')
        print('')
        print('INFO:')
        print(piezometer.warn)
        print('============================================================================')
        return None
    else:
        print('INFO:')
        print(piezometer.warn)
        print('Differential stresses in MPa')

        return np.around(diff_stress, 2)


def list_piezometers(piezometers) -> None:
    for mineral_phase, ref in piezometers.__dict__.items():
        print(f"{mineral_phase}:")

        for piezo_relations, _ in ref.__dict__.items():
            print("  ", piezo_relations)


def summary(database) -> None:
    for feature, data in database.items():
        print(f"{feature}: {data}")


def load_piezometers_from_yaml(filepath: str) -> tuple[str, SimpleNamespace]:
    """_summary_

    Parameters
    ----------
    filepath : str
        _description_

    Returns
    -------
    str, SimpleNamespace
        _description_
    """

    # read YALM database
    with open("piezometric_database.yaml", "r") as file:
        database = yaml.safe_load(file)

    # get database version
    version = database["database"]["version"]

    # construct dime dataclases for all mineral phases
    quartz = SimpleNamespace(**database["database"]["mineral_phases"]["quartz"])
    olivine = SimpleNamespace(**database["database"]["mineral_phases"]["olivine"])
    calcite = SimpleNamespace(**database["database"]["mineral_phases"]["calcite"])
    feldspar = SimpleNamespace(**database["database"]["mineral_phases"]["feldspar"])

    piezometers = SimpleNamespace(
        quartz=quartz, olivine=olivine, calcite=calcite, feldspar=feldspar
    )

    return version, piezometers


if __name__ == "__main__":
    print('Welcome to the GrainSizetool piezometers module')
    version, piezometers = load_piezometers_from_yaml("piezometric_database.yaml")
    print(f"piezometric database v{version} loaded")
    print('')
    print("Piezometric relations avalilable:")
    list_piezometers(piezometers)
