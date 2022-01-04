# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 12:42:00 2021
@author: TF
"""
#20220104#
#Enligsh version#
##############WHAT SHOULD BE INPUTTED#############3
#intput the address of this file#
#inut list of test image#
#input list of atlas image# 
#input list of mask image#
#input list of atlas landmark#
#input storage address of temporary documents(could be very large)#
import sys
import os
#print(os.path.abspath(__file__))
f_a_full=os.path.abspath(__file__)
f_a=f_a_full.replace("main.py","")
from pre.dicom2nii import *
from MAS import *
from pre.resample import *
from after.mutual_information import *

print("This is a landmark detection algorithm based on Multi-Atlas regiatration")

don = "F"
while don == "F":
    print("All your test images,atlas images are in nii format or not?Please input F if DICOM exists")
    don=input("Input：")
    if don != "T":
        print("All images should be converted to nii")
        print("Please input the image list you need to transform to nii,the output images will be named as _nii.txt in the same file with the input images.the list names should be separated by spaces if more than one")
        list_dicom=(input("Input：").split())
        for i in range(len(list_dicom)):
            dicom2nii(list_dicom[i])
        print("convert finished")

   
print("Input at the same time, separated by spaces,use / in the address")
print("Input list of test images")
print("Input list of atlas images")
print("Input list of mask for atlas images")
print("Input list of landmarks of atlas")
print("Storage address of temporary documents(it could be quite large)")
print("Storage address of final results")
print("Whether the file needs resampling ? please use T or F (resampling is recommended, otherwise the efficiency is quite low)")
print("Whether label fusion is average or weighted, please use T or F (T represents average)")
print("If label fusion is weighted, please enter the number of images finally selected (less than or equal to the number of atlas)")
print("this code contains an example")

#H:/MASthe_final/data/list/test_imagelist.txt H:/MASthe_final/data/list/atlas_imagelist.txt  H:/MASthe_final/data/list/atlas_masklist.txt H:/MASthe_final/data/list/atlas_landmarklist.txt H:/MASthe_final/data/linshi/ H:/MASthe_final/data/linshi/ F F 1 

def FINAL(file_address,testlist,atlaslist,masklist,landmarklist,linshiaddress,saveaddress,resample_or_not,average_or_not,maxnum):

##########PREPROCESS###########
#If DICOM，convert to nifti#      
    if  resample_or_not=="T":
        resample(testlist,file_address)
        resample(atlaslist,file_address)
        resample(masklist,file_address)
            
        MAS(testlist.replace(".txt","_resample.txt"),
            atlaslist.replace(".txt","_resample.txt"),
            masklist.replace(".txt","_resample.txt"),
            landmarklist,
            file_address,
            linshiaddress)
        
        MI(testlist.replace(".txt","_resample.txt"),
           atlaslist.replace(".txt","_resample.txt"),
           linshiaddress,
           saveaddress,
           average_or_not,maxnum)
        
    elif resample_or_not=="F":
            
        MAS(testlist,
            atlaslist,
            masklist,
            landmarklist,
            file_address,
            linshiaddress)
        
        MI(testlist,
           atlaslist,
           linshiaddress,
           saveaddress,
           average_or_not,maxnum)
  
te_list,at_list,ma_list,ld_list,ls_ad,sv_ad,reon,avon,mn = (input("请输入：").split())
#print(f_a,te_list,at_list,ma_list,ld_list,ls_ad,sv_ad,reon,avon,mn)
FINAL(f_a,te_list,at_list,ma_list,ld_list,ls_ad,sv_ad,reon,avon,int(mn))
print("finished")      
