# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 13:58:09 2021

@author: TF
"""

#MASK的01化#    
for i in list_brain_new[0]:
    templete= nib.load(address_mask+p.get_pinyin(i, '')+str("/mask.nii.gz"))  
    templete_data=templete.get_fdata()
    templete_data[templete_data<2000]=0
    templete_data[templete_data>2000]=1     
    img_save= nib.Nifti1Image(templete_data, templete.affine )
    nib.save(img_save, address_mask+p.get_pinyin(i, '')+str("/mask.nii.gz"))