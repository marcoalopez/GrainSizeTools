# Getting started

> [!CAUTION]
> This wiki is incomplete and will be the official documentation for the new script version to be released in 2024.

In this section, we will learn

- How to install Python using the Anaconda or Miniconda distributions.
- How to install GrainSizeTools.
- How to use Python with tools like Jupyter Notebook or JupyterLab.
- How to interact with the script and import data.

## Step 1. Install Python for data science

GrainSizeTools requires installing Python 3, the Python scientific libraries [NumPy](http://www.numpy.org/ ) [SciPy](http://www.scipy.org/ ), [Pandas](http://pandas.pydata.org ), [Matplotlib](http://matplotlib.org/ ), and JupyterLab. If you have no previous experience with Python, we recommend downloading and installing the Anaconda Python distribution

https://docs.anaconda.com/free/anaconda/install/

as it contains all the necessary scientific packages (> 5 GB disc space). There are versions for Windows, MacOS and Linux. If you have limited disk space, there is a distribution called [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/) which installs only the Python packages you need. If you prefer to go to this route, click [here](https://github.com/marcoalopez/Python_course/blob/main/notebooks/installing_Python.md) for instructions.

Once Anaconda is installed, launch the Anaconda Navigator and you will see that you have installed various scientifically oriented Integrated Development Systems (IDEs), including **JupyterLab** and the **Jupyter Notebook**. Clicking on any of these IDEs will open the corresponding application in your web browser. The GrainSizeTools documentation is written assuming that you will be working using Jupyter Notebooks.

> [!TIP]
> **Using a dedicated application to work with Jupyter notebooks**
>
> If you prefer to use a dedicated application instead of opening Jupyter Notebooks in your browser, there are several free and paid alternatives. Here we will mention two free alternatives:
>
> - **Visual Studio Code** (a.k.a. Vscode):  https://code.visualstudio.com/
>
> This is a free code editor that can be used with a variety of programming languages including Python and supports Jupyter notebooks via extensions. As an advantage over vanilla Jupyter Lab, it has a handy variable browser. More detailed instructions on how to use Jupyter Notebooks in Vscode at the following link https://code.visualstudio.com/docs/datascience/jupyter-notebooks
>
> - **JupyterLab desktop**: https://github.com/jupyterlab/jupyterlab-desktop/releases
>
> This is a cross-platform desktop application for Jupyter Lab. It is the same application that opens in the browser but in an encapsulated application. You can find the user guide at the following link https://github.com/jupyterlab/jupyterlab-desktop/blob/master/user-guide.md. If you are a beginner, this is the easy road.

## Step 2. Download GrainSizeTools

Once Python is installed, the next step is to download GrainSizeTools. Click on the download link below (there is also a direct link on the GrainSizeTools website).

https://github.com/marcoalopez/GrainSizeTools/releases

and download the latest version of the script by clicking on the zip file as shown below

TODO-> figure

### Script organization

The GrainSizeTools folder contains various Python files (.py), a folder named DATA with a CSV file inside, and various Jupyter notebooks (.ipynb files) that are templates for performing different types of grain size data analysis.

TODO -> figure

## Step 3. Understanding Jupyter Notebooks

To improve the reproducibility of the grain size studies, we suggest working with the Jupyter Notebooks templates provided in the script, especially if you have no previous experience with the Python language. The [Jupyter Notebook](https://jupyter.org/) is a document that can contain live code, equations, visualisations and narrative text. This is ideal for generating reports and including them as supplementary material in your publications so that any researcher can reproduce your results.

TODO -> Figure showing a Jupyter Notebook

Figure X. An example of a Jupyter Notebook with code, equations (using Latex), visualizations and narrative text.

JupyterLab and VSCode with the Jupyter Notebook extension are the next generation of the Classic Jupyter Notebook application interface, providing an easy-to-use environment focused on data science.

![](https://github.com/marcoalopez/GrainSizeTools/blob/master/FIGURES/Jupyter_lab.png?raw=true)

Figure X. The JupyterLab interface...TODO. More info at https://jupyterlab.readthedocs.io/en/latest/user/interface.html#the-jupyterlab-interface



> [!NOTE]
> Explaining how Jupyter Notebooks work in detail is beyond the scope of this wiki page. Fortunately, there are very good tutorials available. To familiarize yourself with how Jupyter Notebooks work, we recommend the following tutorials:
>
> - https://www.youtube.com/watch?v=HW29067qVWk This is a video by Corey Schafer that explains in a clear, entertaining and concise way how to install and use a Jupyter Notebook, the usage part starts at about 4:20. For the tutorial, Corey uses the classic Jupyter Notebook application instead of JupyterLab, but it works similarly.
> - TODO

## Understanding the script structure and the workflow

The script consists of seven Python files, listed below, which must be in the same directory.

- ``GrainSizeTools.py``: This file imports all the modules needed for the script to work. This is the only executed Python file in the Jupyter Notebook templates.
- ``averages.py``: This module contains a set of functions for calculating different types of averages and margins of error.
- ``plot.py``: This module contains a set of functions for generating different types of ad hoc plots used by the script.
- ``stereology.py``: This module contains a set of functions to approximate true grain size distributions from sectional measurements using stereological methods.
- ``piezometric_database.py``: This file contains the database of piezometers the script uses.
- ``template.py``: This file contains the default (Matplotlib) parameters used by the script to generate plots.
- ``get.py``: This file contains the welcome message of the script.

They also contain a folder called DATA, where you should place the grain size data you want to quantify, and various Jupyter notebooks. For beginners, it is recommended to use these Jupyter notebooks templates. There are three different notebooks depending on the type of study you want to perform: (i) quantification of grain size distributions (``grainsize_pop_template.ipynb``), (ii) approximation of grain size distributions using stereological methods (``stereology_template.ipynb``), and (iii) paleopiezometry (``paleopiezometry_template.ipynb``). These notebooks contain all the necessary instructions on how to use them through practical examples. The user will only have to change some parameters to adapt them to their study case and delete everything that is not needed. Once this is done, all the analyses and figures will be contained in a single folder, and all the procedures in a single fully reproducible document that can be exported to other formats (pdf, html, etc.) if needed. If you use this workflow, you should ideally copy the entire contents of the script (<<1 MB), i.e. the code, the folder structure and the notebooks, for each grain size study you conduct.

> [!IMPORTANT]
> The GrainSizeTools script is not designed to deal with microscopic images but to quantify and visualize grain size populations and estimate stresses via paleopiezometers. **It is therefore necessary to measure the grain diameters or the cross sectional areas/volumes of the grains in advance and store them in a txt/csv/excel file**. For this task, we strongly recommend to use the [*ImageJ*](http://rsbweb.nih.gov/ij/) application or one of its different flavours (see [here](http://fiji.sc/ImageJ)). ImageJ-type applications are public domain image processing programs widely used in scientific research and run on all operating systems. This wiki includes a short tutorial on how to measure the areas of the grain profiles with ImageJ. The combined use of **ImageJ** and **GrainSizeTools script** is intended to ensure that all data processing steps are done through free and open-source programs/scripts that run under any operating system. If you are dealing with EBSD data instead, we encourage you to use the [MTEX toolbox](https://mtex-toolbox.github.io/) for grain reconstruction.

> [!NOTE]
> The script is organized in a modular way intended to facilitate modifying, reusing and extending the code if necessary. If you have coding skills, don't hesitate to implement your own methods. 

### Open the Jupyter templates

Once you have everything installed, open JupyterLab or Jupyter Notebooks and in the file manager go to the address where the script and templates are located. Open the Jupyter template you want to use and follow the instructions in the template.

TODO

## Importing data using the Pandas library

The way we propose to import the data to be analysed by the script is to use [Pandas](https://pandas.pydata.org/), which is the de facto standard Python library for data analysis and manipulation of tabular data (including CSV, Excel or text files). The library includes several tools for reading files and handling missing data. Once the GrainSizeTools script is run, all the Pandas methods are imported as ``pd`` and available once you write in a cell ``pd.``. TODO

TODO

> [!TIP]
> Although you can use the ``get_filepath()`` function to get a file path through a file selection window as follows
>
> ```python
> >>> filepath = get_filepath()
> ```
> for reproducibility it is best to specify the file path explicitly in the notebook.interface

TODO