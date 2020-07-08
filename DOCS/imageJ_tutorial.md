*last update 2020/07/08*

How to measure the areas of the grain profiles with ImageJ
-------------

> **Before you start:** This tutorial assumes that you have installed the ImageJ application. If this is not the case, go [here](http://imagej.nih.gov/ij/) to download and install it. You can also install different flavours of the ImageJ application that will work similarly (see [here](http://fiji.sc/ImageJ) for a summary). As a cautionary note, this is not a detailed tutorial on image analysis methods using ImageJ, but a quick systematic tutorial on how to measure the areas of the grain profiles from a thin section to later estimate the grain size and grain size distribution using the GrainSizeTools script. If you are interested in image analysis methods (e.g. grain segmentation techniques, shape characterization, etc.) you should have a look at the list of references at the end of this tutorial.

### *Previous considerations on the Grain Boundary Maps*

Grain size in rocks are usually measured in thin sections (2D data) through image analysis such as grain boundary maps (Fig. 1).

![Figure 1. An example of a grain boundary map](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/GBmap.png)  
*Figure 1. An example of a grain boundary map*

These measures are mostly made on digital images consisting of pixels, known as a [raster graphic image](https://en.wikipedia.org/wiki/Raster_graphics). For example, in an 8-bit grayscale image, each pixel contains three values of information: its location in the image -their x and y coordinates- and its value of grey in a range that goes from 0 (black) to 255 (white) (i.e. it allows 256 different grey intensities). In a  binary image, commonly used for grain boundary maps (Fig. 1), only two possible values exist, 0 for black pixels (the grains) and 1 for white pixels (the grain boundary).

One of the key points about raster images is that they are resolution-dependent. This is each pixel has a physical dimension and, hence, the resolution depends on the number of pixels per unit area or length; it is usually measured in pixel per (square) inch (PPI) (see [Image resolution](https://en.wikipedia.org/wiki/Image_resolution) and [Pixel density](https://en.wikipedia.org/wiki/Pixel_density)). This concept is key as the resolution of the raw image -the image obtained directly from the device attached to the microscope- will limit the precision of the measures. Knowing the size of the pixels is therefore essential and makes it possible to set the scale of the image to correctly measure the areas of the grain sections. So be sure to track the resolution of the image at each step, from the raw image you get from the microscope to the grain boundary map on which you make the measurements.

> 👉 It is important not to confuse the pixel resolution with the actual spatial resolution of the image. Spatial resolution refers to the true resolution of the image and this is not only limited by pixel density but also physically. For example, conventional SEM techniques have a maximum spatial resolution depending on acquisition conditions, with a maximum spatial resolution around 50 to 100 nm whatever the pixels in the image recorded. In optics, the resolution is approximated by *R = 0.61λ / A*, where *λ* is the wavelength of the light, typically taken as 0.4 μm, and *A* is the numerical aperture of the lens system. For more information see [here](https://en.wikipedia.org/wiki/Diffraction-limited_system)
>
> As an example, think in a digital image of a square inch in size and made of just one black pixel (i.e. with a resolution of PPI = 1). If we double the resolution of the image, we will obtain the same image but now formed by four black pixels instead of one. The new pixel resolution per unit length will be PPI = 2 (or 4 per unit area), however, the spatial resolution of the image remains the same. Strictly speaking, spatial resolution refers to the number of independent pixel values per unit area/length.

The list of techniques that make possible the transition from a raw image to a grain boundary map, known as grain segmentation, is extensive and depends largely on the image source. Thus, digital images may come from a transmission or reflected light microscopy, semi-automatic techniques coupled to light microscopy such as the CIP method (e.g. Heilbronner 2000), electron microscopy either from BSD images or EBSD maps or even from electron microprobes through compositional mapping. All these techniques produce images with variable features and artefacts (i.e. different resolutions, colour *vs* greyscale, nature of the artefacts, grain size boundary *vs* phase maps, etc.). Addressing these segmentation methods is beyond the scope of this tutorial and the reader is referred to the two references cited at the end of this document. This tutorial focuses instead on showing in a very general way the features of grain boundary maps and how to measure their characteristics with the ImageJ software.

Once the grain segmentation is done, it is crucial to ensure that the pixel boundaries of the grain are at least two or three pixels wide (Fig. 2). This will prevent the formation of undesirable artefacts since when two black pixels belonging to two different grains are placed adjacent to each other, both grains will be considered the same grain by the image analysis software.

<img src="https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/Fig_PS_pixels.png" width="500">  
*Figure 2. Detail of grain boundaries in a grain boundary map. The figure shows the boundaries (in white) between three grains in a grain boundary map. The squares represent the pixels in the image. The boundaries are two pixels wide approximately.*

### *Measuring the areas of the grain profiles*

1) Open the grain boundary map with the ImageJ application

2) To measure the areas of the grain profiles it is first necessary to convert the grain boundary map into a binary image. If this was not done previously, go to ```Process>Binary``` and click on ```Make binary```. Also, make sure that the areas of grain profiles are in black and the grain boundaries in white and not the other way around. If not, invert the image in ```Edit>Invert```.

3) Then, it is necessary to set the scale of the image. Go to ```Analize>Set Scale```. A new window will appear (Fig. 3). To set the scale, you need to know the size of a feature, such as the width of the image, or the size of an object such as a scale bar. The size of the image in pixels can be check in the upper left corner of the window, within the parentheses, containing the image. To use a particular object of the image as scale the procedure is: i) Use the line selection tool in the toolbar (Fig. 3) and draw a line along the length of the feature or scale bar; ii) go to ```Analize>Set Scale```; iii) the distance of the drawn line in pixels will appear in the upper box, so enter the dimension of the object/scale bar in the 'known distance' box and set the units in the 'Unit length' box; iv) do not check 'Global' unless you want that all your images have the same calibration and click ok. Now, you can check in the upper left corner of the window the size of the image in microns (millimetres or whatever) and pixels.

![Figure 3. Set scale menu](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/Set%20scale.png)  
*Figure 3. At left, the Set Scale window. In the upper right, the ImageJ menu and tool bars. The line selection tool is the fifth element from the left (which is actually selected). In the bottom right, the upper left corner of the window that contains the grain boundary map. The numbers are the size in microns and the size in pixels (in brackets).*

4) The next step requires to set the measurements to be done. For this, go to ```Analize>Set Measurements``` and a new window will appear. Make sure that 'Area' is selected. You can also set at the bottom of the window the desired number of decimal places. Hit ok.

5) To measure the areas of our grain profiles we need to go to ```Analize>Analize Particles```. A new window will appear with different options (Fig. 4). The first two are for establishing certain conditions to exclude anything that is not an object of interest in the image. The first one is based on the size of the objects in pixels by establishing a range of size. We usually set a minimum of four pixels and the maximum set to infinity to rule out possible artefacts hard to detect by the eye. This ultimately depends on the quality and the nature of your grain boundary map. For example, people working with high-resolution EBSD maps usually discard any grain with less than ten pixels. The second option is based on the roundness of the grains. We usually leave the default range values 0.00-1.00, but again this depends on your data and purpose. For example, the roundness parameter could be useful to differentiate between non-recrystallized and recrystallized grains in some cases. Just below, the 'show' drop-down menu allows the user to obtain different types of images when the particle analysis is done. We usually set this to 'Outlines' to obtain an image with all the grains measured outlined and numbered, which can be useful later to check the data set. Finally, the user can choose between different options. In our case, it is just necessary to select 'Display results'. Hit ok.

![Figure 4. Analize Particles menu](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/AnalizeParticles.png)  
*Figure 4. Analyze particles window showing the different options*

6) After a while, several windows will appear. At least, one containing the results of the measures (Fig. 5), and others containing the image with the grains outlined and numbered. Note that the numbers displayed within the grains in the image correspond to the values showed in the first column of the results. To save the image go to the ImageJ menu bar, click on ```File>Save As```, and choose the file type you prefer (we encourage you to use PNG or TIFF for such type of image). To save the results we have different options. In the menu bar of the window containing the results, go to ```Results>Options```  and a new window will appear (Fig. 6). In the third line, you can choose to save the results as a text (.txt), CSV comma-separated (.csv) or Excel (.xls) file types. We encourage you to choose either *txt* or *CSV* since both are widely supported formats to exchange tabular data. Regarding the 'Results Table Options' at the bottom, make sure that 'Save column headers' are selected since this headers will be used by the GrainSizeTools script to automatically extract the data from the column 'Area'. Finally, in the same window go to ```File>Save As``` and choose a name for the file. You are done.

<img src="https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/Fig_imageJ_results.png" width="700">  
*Figure 5. The results windows showing all the measures done on the grains by the ImageJ application.*

![Figure 6. ImageJ I/O options window](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/Fig_ImageJ_IOoptions.png)  
*Figure 6. ImageJ I/O options window.*

### *List of useful references*

**Note**: This list of references is not intended to be exhaustive in any way. It simply reflects some books, articles or websites that I find interesting on the topic. I intend to expand this list over time. Regarding the ImageJ application, there are many tutorials on the web, see for example [here](http://imagej.nih.gov/ij/docs/index.html) or [here](http://imagej.net/Category:Tutorials)

Russ, J.C., 2011. The image processing handbook. CRC Press. Taylor & Francis Group

> This is a general-purpose book on image analysis written by professor John C. Russ from the Material Sciences and Engineering at North Carolina State University. Although the book is not specifically focused on structural geology, thin sections, or even rocks, it covers a wide variety of procedures in image analysis and contains very nice examples of image enhancement, segmentation techniques or shape characterization. I find the text very clear and well-written, so if you are looking for a general-purpose image analysis book, this is the best one I know.

Heilbronner, R., Barret, S., 2014. Image Analysis in Earth Sciences. Springer-Verlag Berlin Heidelberg. doi:[10.1007/978-3-642-10343-8](http://link.springer.com/book/10.1007%2F978-3-642-10343-8)

> This book focuses on image analysis related to Earth Sciences putting much emphasis on methods used in structural geology. The first two chapters deal with image processing and grain segmentation techniques using the software Image SXM, which is a different flavour of the ImageJ family applications (see [here](http://fiji.sc/ImageJ)).

[return to GrainSizeTools website](https://marcoalopez.github.io/GrainSizeTools/)  
