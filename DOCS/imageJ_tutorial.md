A brief tutorial on how to measure the grain profile areas with ImageJ
-------------

**Important note:** This step-by-step tutorial assumes that you have installed in the system the ImageJ software. If this is not the case go [here](http://imagej.nih.gov/ij/) to download and install the application. You can also install different flavours of the ImageJ app (see [here](http://fiji.sc/ImageJ) for a summary) that will work in a similar way. As a cautionary note, this is not a detailed tutorial on image analysis using ImageJ at all. This is just a quick step-by-step tutorial to obtain the areas of the grain profiles in a thin section to later use the GrainSizeTools script. If you are really interested in image analysis (e.g. grain segmentation techniques, etc.) you should have a look at the list of references at the end of this tutorial.

### *Previous considerations on the Grain Boundary Maps*

>This section briefly discusses the features required by the images and the grain boundary maps that will be later treated with the ImageJ application.

Grain size studies in rocks are usually based on measures performed in thin sections (2D data) through image analysis. Since the methods implemented in the GrainSizeTools script are based on the measure of the areas of the grain profiles, our final aim is to obtain a grain boundary map (Fig. 1) from the thin section, on which we will carry out the corresponding measures.

![Figure 1. An example of a grain boundary map](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/GBmap.png)  
*Figure 1. An example of a grain boundary map*

Nowadays, these measures are mostly made on digital images made by pixels (e.g. Heilbronner and Barret 2014), also known as raster graphics image. You can obtain some information on raster graphics [here](https://en.wikipedia.org/wiki/Raster_graphics). For example, in a 8-bit grayscale image (the most widely used type of grayscale image), each pixel contains information about its location in the image (their x and y coordinates) and its 'gray' value in a range that goes from 0 (white) to 256 (black) (i.e. it allows 256 different gray intensities). In the case of a grain boundary map (Fig. 1), it is a binary image where only two possible values exist, 0 for white pixels and 1 for black pixels.

One of the key points on digital images made by pixels (raster graphics) is that they are resolution dependent, which means that each pixel have a physical dimension (i.e. a size), therefore, the smaller the size of the pixel, the higher the resolution. The resolution depends on the number of pixels per unit area or length, and it is usually measured in pixel per (square) inch (PPI) (more information about [Image resolution](https://en.wikipedia.org/wiki/Image_resolution) and [Pixel density](https://en.wikipedia.org/wiki/Pixel_density)). This is a key concept since the resolution of the raw image (the image obtained directly from the microscope) will limit the precision of the measures. Known the size of the pixels is, therefore, essential since it will allow us to set the scale of the image allowing the absolute measure of the areas of the grain profiles. Also, it will allow us to later make a perimeter correction when calculating the equivalent diameters from the areas of the grain profiles. So be sure about the image resolution at every step, from the raw image until you get the grain boundary map.

> Note: It is important not to confuse the pixel resolution with the actual spatial resolution of the image. The spatial resolution is the actual resolution of the image and it is limited physically not by the number of pixels per unit area/length (e.g. conventional SEM techniques have a maximum spatial resolution of 50 to 100 nm whatever the pixels in the image recorded). For example, imagine an image of a square inch in size and made of just one black pixel (i.e. with a resolution of ppi = 1). If we double the resolution of the image, we will obtain the same image but now formed by 4 black pixels instead of 1. The new pixel resolution per unit length is ppi = 2 (ppi = 4 per unit area). In contrast, the spatial resolution of the image remains the same. Strictly speaking, the spatial resolution refers to the number of independent pixel values per unit area/length.

The number of techniques that make possible the transition from a raw image to a grain boundary map (named grain segmentation) are numerous and depend largely on the type of image obtained from the microscope. Thus, digital images may come from transmission or reflected light microscopy, additional techniques to light microscopy such as the CIP method (e.g. Heilbronner 2000), electron microscopy either from BSD images or EBSD grain maps or even from electron microprobes through compositional mapping, all of them very different by nature (resolution, color *vs* gray scale, nature of the artifacts, etc.). The presentation of this image analysis techniques is beyond the scope of this tutorial and the reader is referred to the following references for specific examples (Heilbronner 2000, Herwegh 2000) and, particularly, to the book *Image Analysis in Earth Sciences* by Heilbronner and Barret (2014) for a more general treatise on the subject. To sum up, we will focus on the features of the grain boundary maps by itself not in how to convert the raw images in grain boundary maps using automatic or semi-automatic grain segmentation through image analysis.

Once the grain segmentation is done, especially when the grain segmentation was performed by manual outlining using a vector-graphics application, it is crucial to ensure that at the actual pixel resolution the grain boundaries have a width of 2 or more pixels (Fig. 2). This will prevent the formation of undesirable artifacts since at the moment in which two black pixels belonging to two different grains are adjacent to each other, both grains will be considered the same grain by the image analysis software.

<img src="https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/Fig_PS_pixels.png" width="500">  
*Figure 2. Detail of grain boundaries in a grain boundary map. The figure shows the boundaries (in white) between three grains in a grain boundary map. The squares represent the pixels in the image. The boundaries are two pixels wide approximately.*

### *Measuring the areas of the grain profiles*

1) Open the grain boundary map with the ImageJ application

2) To work with the image is necessary to convert the image that contains the grain boundary map into a binary image. If this was not done previously, go to ```Process>Binary``` and click on ```Make binary```. Also, make sure that the areas of grain profiles are in black and the grain boundaries in white and not the other way around. If not, invert the image in ```Edit>Invert```.

3) Then, it is necessary to set the scale of the image. Go to ```Analize>Set Scale```. A new window will appear (Fig. 3). To set the scale, you need to know the size of a feature, such as the width of the image, or the size of an object or a previously applied scale bar and its distance in pixels. The size of the image in pixels can be check in the upper left corner of the window containing the image, it is the numbers within the parentheses. To use a particular object of the image as scale the procedure is: i) Use the line selection tool in the tool bar (Fig. 3) to draw a line along the length of the feature or scale bar; ii) do to ```Analize>Set Scale```; iii) the distance of the drawn line in pixels will appear on the upper box, so enter the dimension of the object/scale bar in the 'known distance' box and set the units in the 'Unit length' box; iv) do not check 'Global' unless you want all your images to have this calibration and click ok. Now, you can check in the upper left corner of the window the size of the image in microns (millimeters or whatever) and in pixels.

![Figure 3. Set scale menu](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/Set%20scale.png)  
*Figure 3. At left, the Set Scale window. In the upper right, the ImageJ menu and tool bars. The line selection tool is the fifth element from the left (which is actually selected). In the bottom right, the upper left corner of the window that contains the grain boundary map. The numbers are the size in microns and the size in pixels (in brackets).*

4) Then, it is necessary to set the measurements to be done. For this, go to ```Analize>Set Measurements``` and a new window will appear. Make sure that 'Area' is selected. You can also set at the bottom of the window the desired number of decimal places. Click ok.

5) To measure the areas of our grain profiles we need to go to ```Analize>Analize Particles```. A new window appears with different options (Fig. 4). The first two are for establishing certain conditions to exclude anything that is not an object of interest in the image. The first one is based on the size of the objects in pixels by establishing a range of size. We usually set a minimum of 4 pixels to rule out possible artifacts hard to detect by the eye in the image (this ultimately depends on the quality and the nature of your grain boundary map) and the maximum to infinity. The second option is based on the roundness of the object (the grains in our case). We usually leave the default range values 0.00-1.00, but again this depends on your data and your purpose. For example, the roundness parameter could be useful to differenciate non-recrystallized *vs* recrystallized grains in some cases. Just below, the 'show' drop-down menu allows the user to obtain different types of images when the particle analysis is done. We usually set this to 'Outlines' to obtain an image with all the grains measured outlined and numbered, which can be useful later to check the data set. Finally, the user can choose between different options. In our case, it is just necessary to select 'Display results'. Click ok.

![Figure 4. Analize Particles menu](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/AnalizeParticles.png)  
*Figure 3. Analize particles window showing the different options*

6) After a while, a number of different windows will appear. At least, one containing the results of the measures (Fig. 5) and other containing the image with the outlined and numbered grains. Note that the numbers displayed within the grains in the image generated by the ImageJ correspond to the values showed in the first (unnamed) column of the results. To save the image go to the ImageJ menubar, click on ```File>Save As```, and choose the file type you prefer (we encouraging you to use PNG or TIFF for such type of image). To save the results we have different options. In the menubar of the window containing the results, go first to ```Results>Options```  and a new window will appear (Fig. 6). In the third line you can choose to save the results as a text (.txt), csv comma-separated (.csv) or excel (.xls) file types. We encourage you to choose either *txt* or *csv* since both are widely supported formats to exchange tabular data. Regarding the 'Results Table Options' at the bottom, make sure that at least 'Save column headers' are selected since this headers will be used later by the GrainSizeTools script to automatically extract the data from the column 'Area'. Finally, in the same window go to ```File>Save As``` and choose a name for the file. That's it.

<img src="https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/Fig_imageJ_results.png" width="700">  
*Figure 4. The results windows showing all the measures done on the grains by the ImageJ application.*

![Figure 6. ImageJ I/O options window](https://raw.githubusercontent.com/marcoalopez/GrainSizeTools/master/FIGURES/Fig_ImageJ_IOoptions.png)  
*Figure 5. ImageJ I/O options window.*

### *List of useful references*

**Note**: This list of references is not intended to be exhaustive in any way. It simply reflects some works, webpages and books that I find interesting about the topic in question. My intention is to expand the list over time. Regarding the ImageJ program, there are extensive documentation and tutorials on the web, see for example [here](http://imagej.nih.gov/ij/docs/index.html) or [here](http://imagej.net/Category:Tutorials)

Heilbronner, R., 2000. Automatic grain boundary detection and grain size analysis using polarization micrographs or orientation images. J. Struct. Geol. 22, 969–981. doi:[10.1016/S0191-8141(00)00014-6](http://www.sciencedirect.com/science/article/pii/S0191814100000146)

> This paper explains a simple procedure for creating grain boundary maps from thin sections using a semi-automatic method called Lazy Grain Boundary (LGB) using the NIH Image, which is the predecessor of ImageJ (i.e. no longer under active development). The authors compare the results obtained using the LGB method and manual segmentation. The input digital images were obtained from a quartzite under light microscopy using different techniques including the CIP method.

Heilbronner, R., Barret, S., 2014. Image Analysis in Earth Sciences. Springer-Verlag Berlin Heidelberg. doi:[10.1007/978-3-642-10343-8](http://link.springer.com/book/10.1007%2F978-3-642-10343-8)

> This book on image analysis focuses on topics related with Earth Sciences, putting much emphasis on methods used in structural geology. The first two chapters, which deals with image processing and grain segmentation, uses the software Image SXM, which ultimately is similar to the ImageJ application (see [here](http://fiji.sc/ImageJ)).

Herwegh, M., 2000. A new technique to automatically quantify microstructures of fine grained carbonate mylonites: two-step etching combined with SEM imaging and image analysis. J. Struct. Geol. 22, 391-400. doi:[10.1016/S0191-8141(99)00165-0](http://www.sciencedirect.com/science/article/pii/S0191814199001650)

> This paper uses digital backscatter electron images on previously treated samples to distinguish between two mineral phases. The author uses the NIH Image and the LGB method for the grain segmentation.



[next section](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/references.md)

[table of contents](https://github.com/marcoalopez/GrainSizeTools/blob/master/DOCS/tableOfContents.md)