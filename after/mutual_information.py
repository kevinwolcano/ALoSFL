# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 18:52:51 2021

@author: TF
"""
#互信息值计算#
#label fusion部分#
import pandas as pd
import numpy as np
import nibabel as nib
#测试序列，图谱序列，临时存放地址,最终存放地址,是否平均，最大值取数#
def MI(testlist,atlas,linshi_address,final_address,average_or_not,maxnum):
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
    
    imagelist = pd.read_csv(testlist,header=None)
    imagelist = np.array(imagelist)
    
    atlaslist = pd.read_csv(atlas,header=None)
    atlaslist = np.array(atlaslist)
    
    if linshi_address[-1]!="/":
        linshi_address=linshi_address+"/"
    else:
        1
    if final_address[-1]!="/":
        final_address=final_address+"/"
    else:
        1
    
    if average_or_not == "T":
        image_path=linshi_address+str("0/0_ffdt2_point.txt")
        sss=pd.read_csv(image_path,header=None,sep="\t",skiprows=[0])
        sum_matrix=np.zeros((len(atlaslist),len(sss),3))
        for i in range(len(imagelist)):
            target_address=linshi_address+str(i)+str("/") 
            for j in range(len(atlaslist)):
                image_path=target_address+str(j)+str("_ffdt2_point.txt")          
                sum_matrix[j,:,:]=pd.read_csv(image_path,header=None,sep="\t",skiprows=[0])
                    
            final_result=np.average(sum_matrix,axis=0)
            df = pd.DataFrame(final_result)
            df.to_csv(final_address+str(i)+str("_predict.txt"),header=0,sep="\t",index=0)
        
    
    else:
        list_mutual_information=np.zeros((len(atlaslist)))
   
        for i in range(len(imagelist)):
            target_address=linshi_address+str(i)+str("/")   
            for j in range(len(atlaslist)):
                after_reg_image= nib.load(target_address+str(j)+str("_ffdt2_atlas.nii.gz"))
                after_reg_image_matrix=after_reg_image.get_fdata()
                after_reshape=np.reshape(after_reg_image_matrix,-1)

                origin_image= nib.load(atlaslist[j][0])
                origin_reg_image_matrix=origin_image.get_fdata()
                origin_reshape=np.reshape(origin_reg_image_matrix,-1)

                list_mutual_information[j]=computeMI(origin_reshape,after_reshape)

            test=pd.DataFrame(data=list_mutual_information)
            sav_path=target_address+str("mutual_infor.csv")
            test.to_csv(sav_path,index=False,header=False,sep="\t")
    
    
#找到最大互信息序列#    
            list_mutual_information=pd.read_csv(sav_path,header=None)
            nums=list(list_mutual_information[0])
            if maxnum>=len(atlaslist):
                print("最大选取数应小于图谱个数")
            
            else:
                temp=[]    
                Inf = 0 
                for j in range(maxnum):
                    temp.append(nums.index(max(nums)))
                    nums[nums.index(max(nums))]=Inf
#    te=t-30       
#保证最小的为最大的95%以上
                max_mi=list_mutual_information[0][temp[0]]
                j=0    
                while j<maxnum:
                    min_mi=list_mutual_information[0][temp[j]]
                    if min_mi/max_mi<=0.95:
                        break
                    j+=1
                    temp_final=temp[:j]   
    #随便挑一个确定一下Landmark个数#
            image_path=linshi_address+str("0/0_ffdt2_point.txt")
            sss=pd.read_csv(image_path,header=None,sep="\t",skiprows=[0])
            sum_matrix=np.zeros((len(atlaslist),len(sss),3))
        
#计算最终结果#    
            for j in range(len(atlaslist)):
                image_path=target_address+str(j)+str("_ffdt2_point.txt")          
                sum_matrix[j,:,:]=pd.read_csv(image_path,header=None,sep="\t",skiprows=[0])
            
            slecet_sum_matrix=sum_matrix[temp_final,:,:]        
            final_result=np.average(slecet_sum_matrix,axis=0)
    
            df = pd.DataFrame(final_result)
            df.to_csv(final_address+str(i)+str("_predict.txt"),header=0,sep="\t",index=0)
    
   