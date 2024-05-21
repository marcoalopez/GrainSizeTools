from dataclasses import dataclass
from typing import Dict, ClassVar, Any
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
    correction_factor: Any
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

        return None


@dataclass
class quartz(Piezometer):
    piezometers: ClassVar[Dict[str, "quartz"]] = {}


@dataclass
class olivine(Piezometer):
    piezometers: ClassVar[Dict[str, "olivine"]] = {}


@dataclass
class calcite(Piezometer):
    piezometers: ClassVar[Dict[str, "calcite"]] = {}


@dataclass
class feldspar(Piezometer):
    piezometers: ClassVar[Dict[str, "feldspar"]] = {}


def load_piezometers_from_yaml(filepath):
    # read the YAML file, i.e. the database
    with open(filepath, "r") as file:
        database = yaml.safe_load(file)

        # get database version
        version = database["database"][0]["version"]

        for mineral, data in database.items():
            for feature in data:
                name = feature.pop("piezometer")

                # Create and Store Piezometer Instances
                if mineral == "quartz":
                    piezo = quartz(name=name, **feature)
                    quartz.piezometers[name] = piezo
                    setattr(quartz, name, piezo)

                elif mineral == "olivine":
                    piezo = olivine(name=name, **feature)
                    olivine.piezometers[name] = piezo
                    setattr(olivine, name, piezo)

                elif mineral == "calcite":
                    piezo = calcite(name=name, **feature)
                    calcite.piezometers[name] = piezo
                    setattr(calcite, name, piezo)

                elif mineral == "feldspar":
                    piezo = feldspar(name=name, **feature)
                    feldspar.piezometers[name] = piezo
                    setattr(feldspar, name, piezo)
    
    return version


if __name__ == "__main__":
    version = load_piezometers_from_yaml("piezometric_database.yaml")
    print(f"piezometric database v{version} loaded")

