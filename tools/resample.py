# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 14:42:48 2021

@author: TF
"""
import os
import pandas as pd
import numpy as np


def resample(input_address,pre_address):
    """resample the image to 2*2*2 scale"""
    if pre_address[-1]!="/":
            pre_address=pre_address+"/"
    else:
        1
    savelist=[]
    imagelist = pd.read_csv(input_address,header=None)
    imagelist = np.array(imagelist)
    for i in range(len(imagelist)):  
        image_address=imagelist[i][0]                  
        os.system(r'%sMAS/zxhtransform.exe %s -o %s -resave -spacing 2 2 2 -linear' % (pre_address,image_address,
                                                                                           image_address.replace(".nii","_resample.nii")))
    
        savelist.append(image_address.replace(".nii","_resample.nii"))
    df = pd.DataFrame(savelist, columns=['x'])
    df.to_csv(input_address.replace(".txt","_resample.txt"), sep=',', header=False, index=False)
                                                                               
 