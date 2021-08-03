###2021/1/19##
#仅限Windows系统使用#

#本程序需要输入以下部分，请参考data下的文件例子#
#图像：包括测试集图像（需要求得坐标位置的图像），图谱集图像，图谱集对应mask图像。所有图像必须nii格式（可通过本程序将dicom预处理成nii）#
#坐标点：以世界坐标进行书写，例子如下，每行代表x,y,z坐标，用\t隔开，首行无注释，请务必注意世界坐标系的版本#
-8.3311	222.832	-47.3434
-7.8833	259.854	-137.6480
-7.5235	255.954	-147.4090
#列表：所有参与计算的图像和坐标点所在的地址均由txt进行记录#
比方说在list/atlas_imagelist.txt里
H:/MASthe_final/data/atlas/167/image_resample.nii.gz
H:/MASthe_final/data/atlas/169/image_resample.nii.gz
就是这两个图像文件构成图谱。
如果是dicom格式，可以写成：
H:/MASthe_final/data/atlas/167/
H:/MASthe_final/data/atlas/169/
#本程序包含两个部分#
#预处理阶段#
如果所有图像均为nii格式则跳过预处理部分
如果存在dicom,请输入list的地址 例如：H:/MASthe_final/data/list/atlas_imagelist.txt 
会生成对应的新list，并在dicom同一文件夹下的生成Nii文件。
#MAS阶段#
同时输入，空格隔开：
测试集样本list
图谱的list
图谱的mask的list
图谱的landmark的list
临时文件的存放地址
最终结果的存放地址
文件是否为需要重采样，请用T或F表示（推荐重采样,否则效率极低）"
label fusion是直接平均还是加权，请用T或F表示（T代表平均）"
label fusion如果是加权，请输入最终选择的图像个数（小于等于图谱数）"

运行例子：将对应文件位置修改后可直接运行
H:/MASthe_final/data/list/test_imagelist.txt H:/MASthe_final/data/list/atlas_imagelist.txt  H:/MASthe_final/data/list/atlas_masklist.txt H:/MASthe_final/data/list/atlas_landmarklist.txt H:/MASthe_final/data/linshi/ H:/MASthe_final/data/linshi/ F F 1 

