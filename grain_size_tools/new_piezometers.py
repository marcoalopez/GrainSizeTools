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

from dataclasses import dataclass
from typing import Dict, ClassVar, Optional, Type
import yaml

@dataclass
class Piezometer:
    name: str
    year: int
    reference: str
    B: float
    m: float
    warn: str
    linear_intercepts: bool
    correction_factor: Optional[float]
    notes: str

    def summary(self):
        print(
            f"Piezometer: {self.name}\n"
            f"Year: {self.year}\n"
            f"Reference: {self.reference}\n"
            f"B: {self.B}\n"
            f"m: {self.m}\n"
            f"Warning: {self.warn}\n"
            f"Linear Intercepts: {self.linear_intercepts}\n"
            f"Correction Factor: {self.correction_factor}\n"
            f"Notes: {self.notes}\n"
        )


@dataclass
class Quartz(Piezometer):
    piezometers: ClassVar[Dict[str, "Quartz"]] = {}

    @classmethod
    def add_piezometer(cls, piezometer: "Quartz"):
        cls.piezometers[piezometer.name] = piezometer

    @classmethod
    def get_piezometer(cls, name: str) -> Optional["Quartz"]:
        return cls.piezometers.get(name)

@dataclass
class Olivine(Piezometer):
    piezometers: ClassVar[Dict[str, "Olivine"]] = {}

    @classmethod
    def add_piezometer(cls, piezometer: "Olivine"):
        cls.piezometers[piezometer.name] = piezometer

    @classmethod
    def get_piezometer(cls, name: str) -> Optional["Olivine"]:
        return cls.piezometers.get(name)

@dataclass
class Calcite(Piezometer):
    piezometers: ClassVar[Dict[str, "Calcite"]] = {}

    @classmethod
    def add_piezometer(cls, piezometer: "Calcite"):
        cls.piezometers[piezometer.name] = piezometer

    @classmethod
    def get_piezometer(cls, name: str) -> Optional["Calcite"]:
        return cls.piezometers.get(name)

@dataclass
class Feldspar(Piezometer):
    piezometers: ClassVar[Dict[str, "Feldspar"]] = {}

    @classmethod
    def add_piezometer(cls, piezometer: "Feldspar"):
        cls.piezometers[piezometer.name] = piezometer

    @classmethod
    def get_piezometer(cls, name: str) -> Optional["Feldspar"]:
        return cls.piezometers.get(name)


# Map to relate mineral names to classes
mineral_class_map = {
    "quartz": Quartz,
    "olivine": Olivine,
    "calcite": Calcite,
    "feldspar": Feldspar,
}

def load_piezometers_from_yaml(filepath: str) -> str:
    with open(filepath, "r") as file:
        database = yaml.safe_load(file)

    version = database["database"][0]["version"]

    for mineral, data in database.items():
        # Skip the version entry in the YAML
        if mineral == "database":
            continue
        
        cls = mineral_class_map.get(mineral.lower())
        if cls is None:
            print(f"Unknown mineral type: {mineral}")
            continue

        for feature in data:
            name = feature.pop("piezometer")
            piezo = cls(name=name, **feature)
            cls.add_piezometer(piezo)
            setattr(cls, name, piezo)

    return version


if __name__ == "__main__":
    version = load_piezometers_from_yaml("piezometric_database.yaml")
    print(f"piezometric database v{version} loaded")
