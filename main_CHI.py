# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 12:42:00 2021

@author: TF
"""
#20210118组装完工#
#可能需要考虑一下mask的01问题#
#20210117万开文#
#基本完成，明天组装一下#
#程序分为几个部分#
##############输入环节#############3
#输入本文件所在目录#
#输入测试样本list#
#输入atlas的list# 
#输入mask的list#
#atlas landmark list#
#输入临时文件（会非常之大）的存放地址#
import sys
import os
#print(os.path.abspath(__file__))
f_a_full=os.path.abspath(__file__)
f_a=f_a_full.replace("main.py","")
from pre.dicom2nii import *
from MAS import *
from pre.resample import *
from after.mutual_information import *

print("本程序为MAS(多图谱分割)算法在landmark标记中的应用")

don = "F"
while don == "F":
    print("你使用的测试集，图谱，图谱landmark文件均为nii格式吗？如果存在dicom格式请输入F")
    don=input("请输入：")
    if don != "T":
        print("所有文件必须转化为nii格式请输入")
        print("请输入要转化成nii的list,输出文件会在输入文件目录下以_nii.txt命名,多个List请用空格隔开")
        list_dicom=(input("请输入：").split())
        for i in range(len(list_dicom)):
            dicom2nii(list_dicom[i])
        print("转换完毕")

   
print("请分别输入以下内容，用空格隔开,地址用/分割")
print("输入测试集样本list")
print("输入图谱的list")
print("输入图谱的mask的list")
print("输入图谱的landmark的list")
print("输入临时文件（会非常之大）的存放地址")
print("输入最终结果的存放地址")
print("文件是否为需要重采样，请用T或F表示（推荐重采样,否则效率极低）")
print("label fusion是直接平均还是加权，请用T或F表示（T代表平均）")
print("label fusion如果是加权，请输入最终选择的图像个数（小于等于图谱数）")
print("程序附带使用案例")

#H:/MASthe_final/data/list/test_imagelist.txt H:/MASthe_final/data/list/atlas_imagelist.txt  H:/MASthe_final/data/list/atlas_masklist.txt H:/MASthe_final/data/list/atlas_landmarklist.txt H:/MASthe_final/data/linshi/ H:/MASthe_final/data/linshi/ F F 1 

def FINAL(file_address,testlist,atlaslist,masklist,landmarklist,linshiaddress,saveaddress,resample_or_not,average_or_not,maxnum):

##########预处理###########
#如果是DICOM，转化为nifti#      
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
print("完毕")      
 
    
    



