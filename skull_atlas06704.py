# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:07:39 2019

@author: TF
"""
#经验教训#
#landmark的排列顺序不一样#
import pandas as pd
import numpy as np
import os
#import nibabel as nib

#数据地址#
ads="H:/brainboneCT/"
#ads="//VBOXSVR/Newsmy/brainboneCT/"
#ads="G:/brainboneCT/"
address=ads+"20190912/processed_DICOM1/"

#调用程序地址前缀#
#address_pre="//VBOXSVR/Newsmy/brainboneCT/ZXHproj/"
address_pre="H:/brainboneCT/ZXHproj/"


#存储地址#
address2=address+"pre/"

list_wrong2=pd.read_csv(ads+"list_wrong.csv",header=None)
list_mask=[0,
 3,
 4,
 6,
 8,
 14,
 20,
 23,
 24,
 25,
 27,
 30,
 31,
 32,
 33,
 34,38,39,40,41,42,
 102,
 104,
 105,
 107,
 110,
 111,
 112,
 114,
 115,
 116,
 117,
 118,
 120,
 121,
 124,
 125,
 127,
 129,
 130,
 132,
 135,
 136,
 137,
 139,
 142,
 151,
 152,
 153,
 157]





#def computeMI(x, y):
#   sum_mi = 0.0
#   x_value_list = np.unique(x)
#   y_value_list = np.unique(y)
#   Px = np.array([ len(x[x==xval])/float(len(x)) for xval in x_value_list ]) #P(x)
#   Py = np.array([ len(y[y==yval])/float(len(y)) for yval in y_value_list ]) #P(y)
#   for i in range(len(x_value_list)):
#       if Px[i] ==0.:
#           continue
#       sy = y[x == x_value_list[i]]
#       if len(sy)== 0:
#           continue
#       pxy = np.array([len(sy[sy==yval])/float(len(y))  for yval in y_value_list]) #p(x,y)
#       t = pxy[Py>0.]/Py[Py>0.] /Px[i] # log(P(x,y)/( P(x)*P(y))
#       sum_mi += sum(pxy[t>0]*np.log2( t[t>0]) ) # sum ( P(x,y)* log(P(x,y)/( P(x)*P(y)) )
#   return sum_mi



for i in range(806):
    if i in list_wrong2[1].tolist():
        continue
    
    #if i in list_mask[1].tolist():
     #   continue
    image_path=address+str(i)+str("/image_resample.nii.gz")
    
    for j in list_mask:
        target_image_path=address+str(j)+str("/image_resample.nii.gz")      
                
        
##刚性变换##
#        os.system( r'%szxhreg.exe -target %s -source %s -o %s '
#                              r'-Reg 2 -sub 8 8 8 -sub 6 6 6 -steps 200 '
#                              r'-length 2 1 -pre 12 -notsaveimage' % (address_pre,
#                                                                      target_image_path,
#                                                                      image_path,
#                                                                      address+str(i)+str("/")+str(j)+str("_rig_atlas.AFF")
#                                                                                   )
#                                                                      )
#                              
###仿射变换##
#        os.system(r'%szxhregaff.exe -target %s -source %s -o %s '
#                              r'-Reg 2 -sub 7 7 7 -sub 5 5 5 -steps 200 '
#                              r'-length 2 1 -pre 0 %s' % (address_pre,
#                                                          target_image_path,
#                                                          image_path,
#                                                          address+str(i)+str("/")+str(j)+str("_affine_atlas"),
#                                                          address+str(i)+str("/")+str(j)+str("_rig_atlas.AFF")
#                                                          )
#                              )
#
####ddf##
#        os.system(r'%szxhregsemi0.exe -target %s -source %s -o %s -Reg 2 '
#                              r'-ffd 40 40 40 -ffd 20 20 20 -sub 8 8 8 -sub 6 6 6 '
#                              r'-steps -200 -100 -length 2 -bending 0.001' % (address_pre,
#                                                                              target_image_path,
#                                                                              address+str(i)+str("/")+str(j)+str("_affine_atlas.nii.gz"),
#                                                                              address+str(i)+str("/")+str(j)+str("_ffdt1_atlas")
#                                                                                           )
#                                                                              )
##mask的变换##3
# Buyong                           
#        os.system(r'%szxhtransform.exe %s %s -o %s -n 2 -t %s -t %s '
#                  r'-nearest' % (address_pre,
#                                 target_image_path.replace("image","mask"),
#                                             address+str(i)+str("/")+str(j)+str("_mask"),
#                                             address+str(i)+str("/")+str(j)+str("_atlas_mask"),
#                                             address+str(i)+str("/")+str(j)+str("_ffdt1_atlas.FFD"),
#                                             address+str(i)+str("/")+str(j)+str("_affine_atlas.AFF")
#                                                          )
#                                             )
#####最终的图像配准#######
#        os.system(r'%szxhregsemi0.exe -target %s -source %s -o %s -maskt %s -masktdi 20 -Reg 2 '
#                              r'-ffd 20 20 20 -ffd 10 10 10 -sub 5 5 5 -sub 4 4 4 -steps 100 50 '
#                              r'-length 1 -bending 0.0003 -pre 0 %s' % (address_pre,
#                                                                        target_image_path,
#                                                                        address+str(i)+str("/")+str(j)+str("_affine_atlas.nii.gz"),
#                                                                        address+str(i)+str("/")+str(j)+str("_ffdt2_atlas"),
#                                                                        address+str(j)+str("/")+str("mask_resample.nii.gz"),
#                                                                        address+str(i)+str("/")+str(j)+str("_ffdt1_atlas.FFD")
#                                                                        )
#                              )
                              
#landmark的配准###    
        
        os.system(r'%szxhTransformPointset.exe %s %s 2 '
                              r'%s %s' % (address_pre,
                                          "G:/doc_qian/landmark0703/train_landmark_v2/fusion/"+str(j)+".txt",
                                                         address+str(i)+str("/")+str(j)+str("_ffdt2_point.txt"),
                                                         address+str(i)+str("/")+str(j)+str("_ffdt2_atlas.FFD"),
                                                         address+str(i)+str("/")+str(j)+str("_affine_atlas.AFF")
                                                         )
                              )
                              
###计算互信息########

#    list_mutual_information=np.zeros((57))
#
#    count=0
#    for j in list_mask[1]:
#
#        target_address=address+str(i)+str("/")
#        after_reg_image= nib.load(target_address+str(j)+str("_ffdt2_atlas.nii.gz"))
#        after_reg_image_matrix=after_reg_image.get_fdata()
#        after_reshape=np.reshape(after_reg_image_matrix,-1)
##        after_reshape=(after_reshape-min(after_reshape))/max(after_reshape)
###        after_reshape[np.where(after_reshape>0.5)]=1
##        after_reshape[np.where(after_reshape<0.5)]=0
#        origin_image= nib.load(target_address+str("image_resample.nii.gz"))
#        origin_reg_image_matrix=after_reg_image.get_fdata()
#        origin_reshape=np.reshape(origin_reg_image_matrix,-1)
##        origin_reshape=(origin_reshape-min(origin_reshape))/max(origin_reshape)
##        origin_reshape[np.where(origin_reshape>0.5)]=1
##        origin_reshape[np.where(origin_reshape<0.5)]=0
#        list_mutual_information[count]=computeMI(origin_reshape,after_reshape)
#        count+=1
#    test=pd.DataFrame(data=list_mutual_information)
#    sav_path=address+str(i)+str("/")+str("mutual_infor_frist30.csv")
#    test.to_csv(sav_path,index=False,header=False,sep="\t")


##找到最大互信息序列#    
#    list_mutual_information=pd.read_csv(address+str(i)+str("/")+str("mutual_infor_frist30.csv"),header=None)
#    nums=list(list_mutual_information[0])
#    temp=[]    
#    Inf = 0    
#    for j in range(5):
#        temp.append(nums.index(max(nums)))
#        nums[nums.index(max(nums))]=Inf
##    te=t-30       
##保证最小的为最大的90%以上
#    max_mi=list_mutual_information[0][temp[0]]
#    while j<5:
#        min_mi=list_mutual_information[0][temp[j]]
#        if min_mi/max_mi<=0.95:
#            break
#        j+=1
#    temp_final=temp[:j]   
#    
#    
#    sum_matrix=np.zeros((57,21,3))
#    
#    
##计算最终结果#    
#    count=0
#    for j in list_mask[1]:
#        image_path=address+str(i)+str("/")+str(j)+str("_ffdt2_point.txt")       
#   # weights=np.exp(list_mutual_information[temp_final,te])    
#        sum_matrix[count,:,:]=pd.read_csv(image_path,header=None,sep="\t",skiprows=[0])
#        count+=1
#    slecet_sum_matrix=sum_matrix[temp_final,:,:]        
#    final_result=np.average(slecet_sum_matrix,axis=0)
#    
#    df = pd.DataFrame(final_result)
#    df.to_csv(address2+str(i)+str("_predict.csv"),header=0,sep="\t",index=0)
    
##删除中间产物##
#    def del_files(path,dname):
#        for root,dirs,files in os.walk(path):#（使用 os.walk ,这个方法返回的是一个三元tupple(dirpath(string), dirnames(list), filenames(list)), 其中第一个为起始路径， 第二个为起始路径下的文件夹, 第三个是起始路径下的文件.）
#
#                for name in files:
#                    if dname in name:#判断某一字符串是否具有某一字串，可以使用in语句
#                        os.remove(os.path.join(root,name))##os.move语句为删除文件语句
#
#                        print('Delete files:',os.path.join(root,name))   
#    if __name__=='__main__':
#        path=address+str(i)+str("/")#此为需要删除的路径
#        del_files(path,"atlas.nii")#调用函数
#        del_files(path,"rig")
  
#for i in range(0,200):
#    path = "/media/zibin112/Newsmy/brainboneCT/20190912/processed_DICOM1/" + str(i) + str("/")
#    del_files(path, "rig")
