#Only for Windows systems#

# The following parts are needed to input, please refer to the example in file'data'#

#Image: including the test image (the image that landmarks need to detect),the atlas set image,and the mask image corresponding to the atlas set. 
All images must be in NII format (DICOM can be preprocessed into NII through this program)#

#Coordinate points: write in world coordinates. 
For example, each line represents x, y and Z coordinates, separated by \t, and there should be no comment on the first line. 
Please pay attention to the version of world coordinate system(NIFTI√ ITK×)#

-8.3311	222.832	-47.3434
-7.8833	259.854	-137.6480
-7.5235	255.954	-147.4090

#List: The address of images and coordinate points involved in the calculation are recorded in .txt#

For example, in file 'list/atlas_imagelist.txt':

H:/MASthe_final/data/atlas/167/image_resample.nii.gz
H:/MASthe_final/data/atlas/169/image_resample.nii.gz

The atlas consisists of these two image files.

If the image is in DICOM format, it can be written as:

H:/MASthe_ final/data/atlas/167/
H:/MASthe_ final/data/atlas/169/

#This procedure consists of two parts#

#Preprocessing#

If all images are in NII format, please skip the preprocessing section
If DICOM exists, input the address of the list, for example: H:/MASthe_final/data/list/atlas_imagelist.txt 

The corresponding new list will be generated and the NII file will be generated in the same folder of DICOM.

#MAS#

Enter at the same time, separated by spaces:

List of test sample
List of atlas
List of atlas mask
List of landmarks of atlas
Storage address of temporary documents
Storage address of final results

Whether the file needs resampling, please use t or F (resampling is recommended, otherwise the efficiency is quite low)“
Whether label fusion is direct average or weighted, please use t or F (T represents average)“
If label fusion is weighted, please enter the number of images finally selected (less than or equal to the number of atlas)“



Running example: you can run directly after modifying the corresponding file location

H:/MASthe_final/data/list/test_imagelist.txt H:/MASthe_final/data/list/atlas_imagelist.txt  H:/MASthe_final/data/list/atlas_masklist.txt H:/MASthe_final/data/list/atlas_landmarklist.txt H:/MASthe_final/data/linshi/ H:/MASthe_final/data/linshi/ F F 1 
