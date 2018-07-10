---
title: "GrainSizeTools: a Python script for grain size analysis and paleopiezometry based on grain size"
tags:
  - Python
  - grain size analysis
  - grain size distributions
  - recrystallization
  - dynamic recrystallization
  - paleopiezometry
  - stereology
  - Saltykov method
authors:
  - name: Marco A. Lopez-Sanchez
    orcid: 0000-0002-0261-9267
    affiliation: "1, 2"
affiliations:
  - name: Present address - Géosciences Montpellier, Université de Montpellier & CNRS, CC 60, Place E.
7 Bataillon, 34095 Montpellier cedex 5, France
    index: 1
  - name: Departamento de Geología, Universidad de Oviedo, c/Jesús Arias de Velasco s/n, 33005, Oviedo, Spain
    index: 2
date: 07 July 2018
bibliography: paper.bib
---

# Summary

Grain size and grain size distributions are of paramount importance in various sub-disciplines of earth and material sciences. Most polycrystalline materials, however, are not friable and 3D grain reconstruction methods are expensive, time-consuming (serial sectioning), or not always applicable (X-ray tomography) [@Jerram:2007]. Methods for the study of grain size in polycrystalline materials from planar sections are still reliable for many tasks and thus relevant today [@Higgins:2015]. ``GrainSizeTools`` is a script for the analysis of grain size data obtained from different sources of 2D image acquisition (optical microscopy, SEM-EBSD) and image analysis.

The estimation of average grain sizes is key in geodynamics and tectonics to validate lithosphere strength models at depths beyond what is directly accessible by drilling, roughly below 10 kilometres. Indeed, the only way to infer the state of stress and the strength of the lithosphere at these depths is from the indirect measurement on rocks that were previously deformed in depth and later brought to the surface during orogenic processes. To this end, geoscientists use different microstructural features of deformed rocks that change with the magnitude of the applied differential stress called piezometers or paleopiezometers [@Twiss and Moores:2007]. One of the most common and easy to measure microstructure is the average grain size produced during deformation by dislocation creep (i.e. the average dynamically recrystallized grain size). Although different experimentally-derived piezometric relations exist in literature, those based on grain size have been calibrated using a wide variety of measurement protocols, which makes their application and comparison difficult. There is therefore a critical need to unify protocols and create a curated database of paleopizometers for the different mineral phases.

In summary, we pursue three different goals with the script:

- promoting best practices and reproducibility in grain size analysis using robust statistics, avoiding manual steps during data processing, and promoting standard procedures for grain size characterization
- maintain a curated and up-to-date database of grain-size based paleopiezometers for different mineral phases
- provide a platform to implement and test new methods for grain size characterization in recrystallized materials (e.g. [@Lopez-Sanchez and Llana-Funez:2015, @Lopez-Sanchez and Llana-Funez:2016])

The script is written in Python, a non-proprietary language, and released under the Apache 2.0 license. It only uses standard and well-maintained Python scientific libraries as dependencies, such as Numpy [@Oliphan:2007], Scipy [@Jones:2001], Pandas [@McKinney:2010], and Matplotlib [@Hunter:2007]. The script is therefore designed to be free for use, open for inspection and modification, flexible, and future-proof.

Except for data import, the script operates through command-line. However, it is designated in a way that it does not require previous knowledge of Python programming language. Since the script is focused on research, the command-line approach facilitates reproducibility. For advanced users, the script is organized in a modular way using short and one-task functions, which facilitates code reuse and extension. Ongoing developments include the implementation of new grain size characterization methods and piezometer calibrations.



# Acknowledgements

I would like to thank Sergio Llana-Fúnez for providing me support over the past few years. The development of this script was partially supported by the Spanish Ministry of Economy and Competitiveness (MINECO) excellence research [grant number CGL2014-53388-P], and by a postdoctoral fellowship co-funded by the European Union and the Government of the Principality of Asturias through the "Clarín-Cofund" program [grant number ACA17-32] within the 7th WP of the Marie Skłodowska-Curie Actions.



# References

