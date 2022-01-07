# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 19:10:59 2021

@author: TF
"""

import os 
def del_files(path,dname):
    for root,dirs,files in os.walk(path):
        for name in files:
            if dname in name:
                os.remove(os.path.join(root,name))
                print('Delete files:',os.path.join(root,name))


