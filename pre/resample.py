# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 14:42:48 2021

@author: TF
"""

#重采样 距离2,2,2#
#输入需要重采样的List，以及工程文件所在地址的前缀#
#必须在windos系统下运行#
import os
import pandas as pd
import numpy as np
def resample(input_address,pre_adress):
    if pre_adress[-1]!="/":
            pre_adress=pre_adress+"/"
    else:
        1
    savelist=[]
    imagelist = pd.read_csv(input_address,header=None)
    imagelist = np.array(imagelist)
    for i in range(len(imagelist)):  
        image_address=imagelist[i][0]                  
        os.system(r'%szxhproj\zxhtransform.exe %s -o %s -resave -spacing 2 2 2 -linear' % (pre_adress,image_address,
                                                                                           image_address.replace(".nii","_resample.nii")))
    
        savelist.append(image_address.replace(".nii","_resample.nii"))
    df = pd.DataFrame(savelist, columns=['x'])
    df.to_csv(input_address.replace(".txt","_resample.txt"), sep=',', header=False, index=False)
                                                                               
 