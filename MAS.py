# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 12:42:00 2021

@author: TF
"""
#20210117万开文#
#程序分为几个部分#

#MAS的主体部分#

#这里是测试集#
#测试集序列，atlas序列，atlasmask序列,atlaslandmark序列，调用程序前缀，临时文件存放地址#
import os
import pandas as pd
import numpy as np
def MAS(testlist,atlas,mask,landmark,pre_adress,linshi_address):
    imagelist = pd.read_csv(testlist,header=None)
    imagelist = np.array(imagelist)
    
    atlaslist = pd.read_csv(atlas,header=None)
    atlaslist = np.array(atlaslist)
    
    masklist = pd.read_csv(mask,header=None)
    masklist = np.array(masklist)
    
    landmarklist = pd.read_csv(landmark,header=None)
    landmarklist = np.array(landmarklist)
    
    if pre_adress[-1]!="/":
            pre_adress=pre_adress+"/"
    else:
        1
        
    if linshi_address[-1]!="/":
            linshi_address=linshi_address+"/"
    else:
        1
        
   ###本段引用自https://www.cnblogs.com/guohu/p/11320008.html### 
    def mkdir(path):    
    # 去除首位空格
        path=path.strip()
    # 去除尾部 \ 符号
        path=path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
        isExists=os.path.exists(path)
    # 判断结果
        if not isExists:
        # 如果不存在则创建目录
            os.makedirs(path)
            return True
        else:
        # 如果目录存在则不创建，并提示目录已存在
            1
            return False
  

    for i in range(len(imagelist)):  
               
        image_path=imagelist[i][0]
        # 定义要创建的目录
        mkpath=linshi_address+str(i)+"/"
        mkdir(mkpath)
    #这里是atlas#
        for j in range(len(atlaslist)):
            target_image_path=atlaslist[j][0]
                       
##刚性变换##
            os.system( r'%szxhproj\zxhreg.exe -target %s -source %s -o %s '
                              r'-Reg 2 -sub 8 8 8 -sub 6 6 6 -steps 200 '
                              r'-length 2 1 -pre 12 -notsaveimage -v 0 ' % (pre_adress,
                                                                      target_image_path,
                                                                      image_path,
                                                                      mkpath+str(j)+str("_rig_atlas.AFF")
                                                                                   )
                                                                      )
                              
##仿射变换##
            os.system(r'%szxhproj\zxhregaff.exe -target %s -source %s -o %s '
                              r'-Reg 2 -sub 7 7 7 -sub 5 5 5 -steps 200 '
                              r'-length 2 1 -pre 0 %s -v 0 ' % (pre_adress,
                                                          target_image_path,
                                                          image_path,
                                                          mkpath+str(j)+str("_affine_atlas"),
                                                          mkpath+str(j)+str("_rig_atlas.AFF")
                                                          )
                              )

###ddf##
            os.system(r'%szxhproj\zxhregsemi0.exe -target %s -source %s -o %s -Reg 2 '
                              r'-ffd 40 40 40 -ffd 20 20 20 -sub 8 8 8 -sub 6 6 6 '
                              r'-steps -200 -100 -length 2 -bending 0.001 -v 0 ' % (pre_adress,
                                                                              target_image_path,
                                                                              mkpath+str(j)+str("_affine_atlas.nii.gz"),
                                                                              mkpath+str(j)+str("_ffdt1_atlas")
                                                                                           )
                                                                              )
#####最终的图像配准#######
            os.system(r'%szxhproj\zxhregsemi0.exe -target %s -source %s -o %s -maskt %s -masktdi 20 -Reg 2 '
                              r'-ffd 20 20 20 -ffd 10 10 10 -sub 5 5 5 -sub 4 4 4 -steps 100 50 '
                              r'-length 1 -bending 0.0003 -pre 0 %s -v 0 ' % (pre_adress,
                                                                        target_image_path,
                                                                        mkpath+str(j)+str("_affine_atlas.nii.gz"),
                                                                        mkpath+str(j)+str("_ffdt2_atlas"),
                                                                        masklist[j][0],
                                                                        mkpath+str(j)+str("_ffdt1_atlas.FFD")
                                                                        )
                              )
                              
##landmark的配准###    
        
            os.system(r'%szxhproj\zxhTransformPointset.exe %s %s 2 '
                              r'%s %s' % (pre_adress,
                                          landmarklist[j][0],
                                                         mkpath+str(j)+str("_ffdt2_point.txt"),
                                                         mkpath+str(j)+str("_ffdt2_atlas.FFD"),
                                                         mkpath+str(j)+str("_affine_atlas.AFF")
                                                         )
                              )