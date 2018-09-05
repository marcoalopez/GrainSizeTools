#!/usr/bin/env python
import sys
import os
from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

with open('license.txt') as fh:
    license = fh.read()

# Check for Python 3
v = sys.version_info
if (v[0] >= 3 and v[:2] < (3, 5)):
    error = "ERROR: GrainSizeTools requires Python version 3.5 or above."
    print(error, file=sys.stderr)
    sys.exit(1)

sys.path.append(os.path.join(sys.path[0], 'grain_size_tools'))

setup(
    name="grain_size_tools",
    version="2.0.1",
    author="Marco A. Lopez-Sanchez",
    author_email="marcoalopez@outlook.com",
    description="A Python script for estimating grain size, grain size populations, and differential stress via piezometers from thin sections",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marcoalopez/GrainSizeTools",
    license=license,
    packages=find_packages(),
    scripts=['grain_size_tools/GrainSizeTools_script.py', 'grain_size_tools/tools.py', 'grain_size_tools/plots.py', 'grain_size_tools/piezometers.py'],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache-2.0 License",
        "Operating System :: OS Independent",
    ),
)
