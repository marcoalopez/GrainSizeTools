welcome = """
======================================================================================
Welcome to GrainSizeTools script v3.0
======================================================================================
GrainSizeTools is a free open-source cross-platform script to visualize and characterize
the grain size in polycrystalline materials and estimate differential stress via
paleopizometers.
"""
info = """
METHODS AVAILABLE
======================================================================================
List of main functions
======================================================================================
summarize              -> estimate... 
conf_interval          -> estimate the confidence interval...

plot.distribution
plot.area_weighted
plot.normalized
plot.qq_plot

stereology.Saltykov
stereology.calc_shape
======================================================================================

You can get more information about the methods in the following ways:
    (1) Typing help plus the name of the function e.g. help(calc_shape)
    (2) In the Spyder IDE by writing the name of the function and clicking Ctrl + I
    (3) Visiting the script documentation at https://marcoalopez.github.io/GrainSizeTools/
    (4) Get a list of the methods available: get.function_list()
"""


def functions_list():
    print(info)
    return None


if __name__ == '__main__':
    pass
else:
    print(welcome)
    print(info)
