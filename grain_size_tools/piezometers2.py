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


def summarized(piezometers) -> None:
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
    feldspar = SimpleNamespace(**database["database"]["mineral_phases"]["olivine"])

    piezometers = SimpleNamespace(
        quartz=quartz, olivine=olivine, calcite=calcite, feldspar=feldspar
    )

    return version, piezometers


if __name__ == "__main__":
    version, piezometers = load_piezometers_from_yaml("piezometric_database.yaml")
    print(f"piezometric database v{version} loaded")
