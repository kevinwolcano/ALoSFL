# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 12:42:00 2021

@author: TF
"""
import os
import pandas as pd
import numpy as np
import nibabel as nib
from tools.delete import *
def mkdir(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        1
        return False

def computeMI(x, y):
    sum_mi = 0.0
    x_value_list = np.unique(x)
    y_value_list = np.unique(y)
    Px = np.array([ len(x[x==xval])/float(len(x)) for xval in x_value_list ]) #P(x)
    Py = np.array([ len(y[y==yval])/float(len(y)) for yval in y_value_list ]) #P(y)
    for i in range(len(x_value_list)):
        if Px[i] ==0.:
            continue
        sy = y[x == x_value_list[i]]
        if len(sy)== 0:
            continue
        pxy = np.array([len(sy[sy==yval])/float(len(y))  for yval in y_value_list]) #p(x,y)
        t = pxy[Py>0.]/Py[Py>0.] /Px[i] # log(P(x,y)/( P(x)*P(y))
        sum_mi += sum(pxy[t>0]*np.log2( t[t>0]) ) # sum ( P(x,y)* log(P(x,y)/( P(x)*P(y)) )
    return sum_mi


def MAS(testlist,atlas,landmark,linshi_address,pre_address,final_address,average_or_not,maxnum,delornot):
    imagelist = pd.read_csv(testlist,header=None)
    imagelist = np.array(imagelist)
    
    atlaslist = pd.read_csv(atlas,header=None)
    atlaslist = np.array(atlaslist)
        
    landmarklist = pd.read_csv(landmark,header=None)
    landmarklist = np.array(landmarklist)
        
    if pre_address[-1]!="/":
            pre_address=pre_address+"/"
    else:
        1
    
    if linshi_address[-1]!="/":
            linshi_address=linshi_address+"/"
    else:
        1
    if final_address[-1]!="/":
            final_address=final_address+"/"
    else:
        1
        
    count=0
    for i in range(len(imagelist)):
        image_path=imagelist[i][0]
        mkpath=linshi_address+str(i)+"/"
        mkdir(mkpath)

        for j in range(len(atlaslist)):
            target_image_path=atlaslist[j][0]
        # rigid transformation
            os.system( r'%sMAS/zxhreg.exe -target %s -source %s -o %s '
                          r'-Reg 2 -sub 8 8 8 -sub 6 6 6 -steps 200 '
                          r'-length 2 1 -pre 12 -notsaveimage -v 0 ' % (pre_address,
                                                                  target_image_path,
                                                                  image_path,
                                                                  mkpath+str(j)+str("_rig_atlas.AFF")
                                                                               )
                                                                  )

        # affine transformation
            os.system(r'%sMAS/zxhregaff.exe -target %s -source %s -o %s '
                          r'-Reg 2 -sub 7 7 7 -sub 5 5 5 -steps 200 '
                          r'-length 2 1 -pre 0 %s -v 0 ' % (pre_address,
                                                      target_image_path,
                                                      image_path,
                                                      mkpath+str(j)+str("_affine_atlas"),
                                                      mkpath+str(j)+str("_rig_atlas.AFF")
                                                      )
                          )
        # ddf
            os.system(r'%sMAS/zxhregsemi0.exe -target %s -source %s -o %s -Reg 2 '
                          r'-ffd 40 40 40 -ffd 20 20 20 -sub 8 8 8 -sub 6 6 6 '
                          r'-steps -200 -100 -length 2 -bending 0.001 -v 0 -notsaveimage' % (pre_address,
                                                                          target_image_path,
                                                                          mkpath+str(j)+str("_affine_atlas.nii.gz"),
                                                                          mkpath+str(j)+str("_ffdt1_atlas")
                                                                                       )
                                                                          )
        # registration
            os.system(r'%sMAS/zxhregsemi0.exe -target %s -source %s -o %s  -Reg 2 '
                          r'-ffd 20 20 20 -ffd 10 10 10 -sub 5 5 5 -sub 4 4 4 -steps 100 50 '
                          r'-length 1 -bending 0.0003 -pre 0 %s -v 0 ' % (pre_address,
                                                                    target_image_path,
                                                                    mkpath+str(j)+str("_affine_atlas.nii.gz"),
                                                                    mkpath+str(j)+str("_ffdt2_atlas"),
                                                                    mkpath+str(j)+str("_ffdt1_atlas.FFD")
                                                                    )
                          )
        # landmark projection
            os.system(r'%sMAS/zxhTransformPointset.exe %s %s 2 '
                          r'%s %s' % (pre_address,
                                      landmarklist[j][0],
                                                     mkpath+str(j)+str("_ffdt2_point.txt"),
                                                     mkpath+str(j)+str("_ffdt2_atlas.FFD"),
                                                     mkpath+str(j)+str("_affine_atlas.AFF")
                                                     )
                          )
            if delornot =="T":              
                os.remove(mkpath+str(j)+str("_affine_atlas.nii.gz"))
            
            if count ==0:
                sss=pd.read_csv(linshi_address+str("0/0_ffdt2_point.txt"),header=None,sep="\t",skiprows=[0])
                sum_matrix=np.zeros((len(atlaslist),len(sss),3))  
                sum_matrix_final=np.zeros((len(sss),3))  
                count+=1 
            sum_matrix[j,:,:]=pd.read_csv(mkpath+str(j)+str("_ffdt2_point.txt"),header=None,sep="\t",skiprows=[0])
                            
        if average_or_not == "2" or average_or_not == "3":           

            list_mutual_information=np.zeros((len(atlaslist)))
 
            for j in range(len(atlaslist)):
                after_reg_image= nib.load(mkpath+str(j)+str("_ffdt2_atlas.nii.gz"))
                after_reg_image_matrix=after_reg_image.get_fdata()
                after_reshape=np.reshape(after_reg_image_matrix,-1)

                origin_image= nib.load(atlaslist[j][0])
                origin_reg_image_matrix=origin_image.get_fdata()
                origin_reshape=np.reshape(origin_reg_image_matrix,-1)

                list_mutual_information[j]=computeMI(origin_reshape,after_reshape)

            test=pd.DataFrame(data=list_mutual_information)
            sav_path=mkpath+str("mutual_infor.csv")
            test.to_csv(sav_path,index=False,header=False,sep="\t")
    
            list_mutual_information=pd.read_csv(sav_path,header=None)
            nums=list(list_mutual_information[0])
            if maxnum>=len(atlaslist):
                maxnum = len(atlaslist)
    
            temp=[]    
            Inf = 0 
            for j in range(maxnum):
                temp.append(nums.index(max(nums)))
                nums[nums.index(max(nums))]=Inf

            max_mi=list_mutual_information[0][temp[0]]
            j=0    
            while j<maxnum:
                min_mi=list_mutual_information[0][temp[j]]
                if min_mi/max_mi<=0.95:
                    break
                j+=1
                temp_final=temp[:j]   
        
        if average_or_not == "1" or average_or_not =="3":
            final_result=np.average(sum_matrix,axis=0)
            df = pd.DataFrame(final_result)
            df.to_csv(final_address+str(i)+str("_predict_average.txt"),header=0,sep="\t",index=0)

        if average_or_not == "2" or average_or_not =="3":
                  
            slecet_sum_matrix=sum_matrix[temp_final,:,:]        
            final_result=np.average(slecet_sum_matrix,axis=0)
            df = pd.DataFrame(final_result)
            df.to_csv(final_address+str(i)+str("_predict_weight.txt"),header=0,sep="\t",index=0)
            
        if average_or_not == "4":   
            #from sklearn.datasets.samples_generator import make_blobs
            from sklearn.cluster import MeanShift, estimate_bandwidth
    
            for j in range(len(sss)):
                bandwidth = estimate_bandwidth(sum_matrix[:,j,:])

                ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)

                ms.fit(sum_matrix[:,j,:])

                cluster_centers = ms.cluster_centers_
                sum_matrix_final[j,:]=cluster_centers[0]
            df = pd.DataFrame(sum_matrix_final)
            df.to_csv(final_address+str(i)+str("_predict_cluster.txt"),header=0,sep="\t",index=0)
        
        if delornot =="T":
            del_files(linshi_address, "")

