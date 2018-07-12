import setuptools
import sys

with open("README.md", "r") as fh:
    long_description = fh.read()

# Check for Python 3
v = sys.version_info
if (v[0] >= 3 and v[:2] < (3, 5)):
    error = "ERROR: GrainSizeTools requires Python version 3.5 or above."
    print(error, file=sys.stderr)
    sys.exit(1)

setuptools.setup(
    name="grain_size_tools",
    version="2.0",
    author="Marco A. Lopez-Sanchez",
    author_email="marcoalopez@outlook.com",
    description="A Python script for estimating grain size, grain size populations, and differential stress via piezometers from thin sections",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/marcoalopez/GrainSizeTools",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache-2.0 License",
        "Operating System :: OS Independent",
    ),
)
