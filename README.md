# Automated Localization of Skull and Face Landmarks (ALoSFL v1.0)

### Introduction

**ALoSFL** is a Python-based command line tool for localization of both facial and cranial landmarks from head CT images by implementing the multi-atlas registration (MAS) and label fusion algorithms (Zhuang, Arridge et al. 2011). The pipeline is described in our recent paper shown in **Citation** below.

The current version of the software is only available for Windows! The Linux version will be launched in the near future.

### Get Started
To run ALoSFL, you will need to have Python 3.6 installed with the following packages:
- `numpy (>=1.17.0)`
- `pandas (>=0.23.0)`
- `SimpleITK`
- `nibabel 2.3.3 `
- `argparse 1.1`

ALoSFL can be downloaded by cloning the github repository:

`git clone https://github.com/kevinwolcano/ALoSFL.git`

`cd ALoSFL`

To test that the tool has been successfully installed, simply run:

`python ./main.py -h`

To run the software, simply run:

`python ./main.py --list_test_images [path] --list_atlas_images [path] --list_landmarks [path] --tmp [path] --output [path]`

More options:

If you just want to resample the test image and average the results of the top 10 atlas proposed when doing label fusion,
then you can run:

`python ./main.py --resample test --fusion 2 --top_n 10`

We have provided an example of toy data to help you walk through the use of ALoSFL. 
To play with the example, you can simply run:

`python ./main.py `

More details can be found in the help list by typing:

`python ./main.py -h`


### Data Preparation
Before running the software, please prepare all the data and configure files as follows. The example data is for your reference.

##### Data folder
- Atlas images that are reference images used for registration
- Test images that are required to localize facial and cranial landmarks
- Landmark files contain the coordinates of landmarks for each atlas image

***To be noted*** - DICOM and Nifti encode space differently. Our software requires the coordinate system of landmark inputs in **Nifti** format. Please make sure before running the software. 
More information can be found [here](https://www.nitrc.org/plugins/mwiki/index.php/dcm2nii:MainPage#Spatial_Coordinates).


##### Configure folder
- List of atlas image path
- List of test image path
- List of landmark path


### Citation
If you use the ALoSFL software, please cite:

*Qian et al., Genetic evidence for facial variation being a composite phenotype of cranial variation and facial soft tissue thickness. Journal of Genetics and Genomics (under revision)*


### Support
We will help address the problems that you may encounter when using ALoSFL. Please feel free to contact us if you have any question. 

Email: 18110980009@fudan.edu.cn; qianwei@picb.ac.cn
