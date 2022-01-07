# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 12:42:00 2021

@author: TF
"""
import sys
import os
import argparse
import pandas as pd
import numpy as np

os.chdir('I:/Skull_program/ALoSFL_v2/')
#sys.path.append(os.getcwd())
from tools.dicom2nii import *
from tools.MAS import *
from tools.resample import *


def FINAL(donot,testlist, atlaslist, landmarklist, linshiaddress, saveaddress, resample_or_not, average_or_not, maxnum,delo):
    preaddress=os.getcwd()

       
#    if  donot == "both" or donot == "atlas":
#        dicom2nii(atlaslist)
#        atlaslist=atlaslist.replace(".txt","_nii.txt")
#    
#    if  donot == "both" or donot == "test":
#        dicom2nii(testlist)
#        testlist=testlist.replace(".txt","_nii.txt")
        
    """preprocessing: dicom to nifti"""
    if  resample_or_not=="both" or resample_or_not=="test":
        resample(testlist,preaddress)
        testlist=testlist.replace(".txt","_resample.txt")
        
    if  resample_or_not=="both" or resample_or_not=="atlas":   
        resample(atlaslist,preaddress)
        atlaslist=atlaslist.replace(".txt","_resample.txt")
            
    MAS(testlist,
            atlaslist,
            landmarklist,
            linshiaddress,preaddress,saveaddress,
           average_or_not,maxnum,delo)
    #delete resample file if you have done resampling before
    if  resample_or_not=="both" or resample_or_not=="test":
        imagelist = pd.read_csv(testlist,header=None)
        imagelist = np.array(imagelist)
        for i in range(len(imagelist)):  
            image_address=imagelist[i][0]  
        
            os.remove(image_address)
        os.remove(testlist)
        
    if  resample_or_not=="both" or resample_or_not=="atlas":
        imagelist = pd.read_csv(atlaslist,header=None)
        imagelist = np.array(imagelist)
        for i in range(len(imagelist)):  
            image_address=imagelist[i][0]          
            os.remove(image_address)
        os.remove(atlaslist)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--dicom2nii', help='Whether to convert Dicom data to Nifti format. Default is none supposing all the input images are in Nifti format.',
                        choices=['atlas', 'test', 'both', 'none'], default='none')
    parser.add_argument('--resample', help='Whether to resample images.', choices=['atlas', 'test', 'both', 'none'], default='both')
    parser.add_argument('--list_atlas_images', help='Input the configure file of atlas image path', default='configure/atlas_image_list.txt')
    parser.add_argument('--list_landmarks', help='Input the configure file of atlas landmark path', default='configure/landmark_list.txt')
    parser.add_argument('--list_test_images', help='Input the configure file of test image path', default='configure/test_image_list.txt')
    parser.add_argument('--fusion', help='Select label fusion methods:'
                                         '1. average all the atlas; '
                                         '2. average the top n atlas via mutual information; '
                                         '3. output results of both 1 and 2;'
                                         '4. average the selected atlas by clustering.',
                        choices=['1', '2', '3', '4'], default='3')
    parser.add_argument('--output', help='Input the path for final results.', default='example/result')
    parser.add_argument('--tmp', help='Input the path for temporary files.', default='example/tmp')
    parser.add_argument('--top_n', help='Input the number of selected top atlas. The number should be no more than the number of atlas images.', default=5)
    parser.add_argument('--delete', help='Whether to delete all the temporary files', choices=['T', 'F'], default='T')

    args = parser.parse_args()
    
    dicomonot = args.dicom2nii
    at_list = args.list_atlas_images
    ld_list = args.list_landmarks
    te_list = args.list_test_images
    ls_ad = args.tmp
    sv_ad = args.output
    
    isExists = os.path.exists(ls_ad)
    if not isExists:
        os.makedirs(ls_ad) 

    isExists = os.path.exists(sv_ad)
    if not isExists:
        os.makedirs(sv_ad)  
        
    reon = args.resample
    avon = args.fusion
    mn = args.top_n
    delo = args.delete

    FINAL(dicomonot,te_list, at_list, ld_list, ls_ad, sv_ad, reon, avon, int(mn),delo)
    print("Finish!")



