#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np


# In[76]:


path = "O:\\daaaCEMTREX\\openImgCSv\\v6\\labels\\oidv6-train-annotations-bbox.csv"

file = pd.read_csv(path)


# In[77]:


file.shape


# In[78]:


file1 = file[(file['LabelName']=='/m/015qff')]
file1
filex = file1[["ImageID", "LabelName" , "XMin" , "XMax" ,"YMin","YMax"]]
filex
filex.to_csv("O:\\daaaCEMTREX\\openImgCSv\\v6\\labels\\traffic\\train_traffic_annotations.csv" , index = False)


# In[79]:


file2 = file1[["ImageID"]].drop_duplicates(subset=['ImageID'], keep='last')
file2.to_csv("O:\\daaaCEMTREX\\openImgCSv\\v6\\labels\\traffic\\train_traffic_ImageID_list.csv" , index = False)


# In[ ]:




