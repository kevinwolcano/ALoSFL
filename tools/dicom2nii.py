# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 11:31:56 2019

@author: TF
"""
import SimpleITK as sitk
import pandas as pd
import numpy as np


def dicom2nii(input_address):
    savelist=[]
    imagelist = pd.read_csv(input_address,header=None)
    imagelist = np.array(imagelist)
    for i in range(len(imagelist)):    
        reader = sitk.ImageSeriesReader()
        if imagelist[i][0][-1]!="/":
            image_address=imagelist[i][0]+"/"
        else:
            image_address=imagelist[i][0]
                      
        ids=sitk.ImageSeriesReader.GetGDCMSeriesIDs(image_address)
  
        number_of_dicom=0
        for j in range(len(ids)):
            dicom_names = reader.GetGDCMSeriesFileNames(image_address,ids[j])
            if len(dicom_names)>number_of_dicom:
                number_of_dicom=len(dicom_names)
                dicom_final_names=dicom_names
                    
        reader.SetFileNames(dicom_final_names)
        image2 = reader.Execute()
        sitk.WriteImage(image2,image_address+"image.nii.gz")
        savelist.append(image_address+"image.nii.gz")
        df = pd.DataFrame(savelist, columns=['x'])
        df.to_csv(input_address.replace(".txt","_nii.txt"), sep=',', header=False, index=False)