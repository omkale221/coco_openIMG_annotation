#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np

path = 'O:\\daaaCEMTREX\\openImgCSv\\v6\\labels\\filtered\\list\\train_rest_list.csv'
file = pd.read_csv(path)


# In[19]:


# file2 = file[(file['IsGroupOf']==0)]
file.head


# In[152]:


file3 = file[(file['LabelName']=='/m/01g317') | (file['LabelName']=='/m/0199g') | (file['LabelName']=='/m/0k4j')
             | (file['LabelName']=='/m/04_sv') | (file['LabelName']=='/m/01bjv') | (file['LabelName']=='/m/07r04')
             | (file['LabelName']=='/m/015qff') | (file['LabelName']=='/m/01940j') | (file['LabelName']=='/m/080hkjn')
             | (file['LabelName']=='/m/01s55n')]
print(file3.shape)


# In[153]:



file4 = file3[(file['IsGroupOf']==0)]

################# person filter, isoccluded
################# distinct list of image id
################# download by list

# file4.to_csv("O:\daaaCEMTREX\openImgCSv\\val_csv.csv",index = False)
print(file4.shape)


# In[140]:


# print(file3)
# file3 = file3[["ImageID", "LabelName" ,"XMin","XMax","YMin","YMax"]]
# file3.to_csv("O:\daaaCEMTREX\openImgCSv\\val2_csv.csv")
# is_person =  file2.concat([(file['LabelName']=='/m/01s55n'),(file['LabelName']=='/m/01g0g')])
# print(is_person)

# file_person = file[is_person]
# print(file_person.shape)
# print(file.head(100000000))
# df = pd.read_excel("O:\downloads\\validation-annotations-bbox.xlsx")


# In[154]:



file5 = file4[(file4['LabelName']=='/m/01g317')].drop_duplicates(subset=['ImageID'], keep='last')
file5.shape
# imlist = [file5['ImageID']]
# imlist
# file6 = file5.drop_duplicates(subset="LabelName")
# file6.shape
# file6 = file5.drop_duplicates(subset=['LabelName'], keep='last')
# file6.shape
# imlist = pd.DataFrame(imlist)


# In[155]:



unique_arr = file5["ImageID"].to_numpy()

unique_arr


# In[156]:


file6 = file4[file4['ImageID'].isin(unique_arr)]
file6.shape


# In[144]:


##################CONTAINING PERSON
# file6.to_csv("O:\\daaaCEMTREX\\openImgCSv\\v6\\filtered\\val_csv_containing_person_occ_mix.csv")


# In[145]:


#####################REST CLASS
file7 = file4
indexn = file7[file7['ImageID'].isin(unique_arr) ].index
file7.drop(indexn , inplace = True)
file7.shape
# file7.to_csv("O:\\daaaCEMTREX\\openImgCSv\\v6\\filtered\\val_csv_rest_classes.csv")


# In[146]:


############## occlusion remove
# idx = np.where((file6['IsOccluded']==0) & (file6['LabelName']=='/m/01g317'))/
file8 = file6[(file6['IsOccluded']==1) & (file6['LabelName']=='/m/01g317')].drop_duplicates(subset=['ImageID'], keep='last')
file8.shape


# In[147]:


unique_brr = file8["ImageID"].to_numpy()

len(unique_brr)


# In[137]:


#######################OCCLUSION = 1
file9 = file6[file6['ImageID'].isin(unique_brr)]
file9.shape
# file9.to_csv("O:\\daaaCEMTREX\\openImgCSv\\v6\\filtered\\train_csv_person_occ_present_classes.csv")


# In[148]:


##############OCCLUSION = 0

file10 = file6
indexn = file10[file10['ImageID'].isin(unique_brr) ].index
file10.drop(indexn , inplace = True)
file10.shape
# file10.to_csv("O:\\daaaCEMTREX\\openImgCSv\\v6\\filtered\\train_csv_occ_removed_classes.csv")


# In[149]:


file11 = file10
file11 = file10["ImageID"].drop_duplicates()
len(file11)
file11.to_csv("O:\\daaaCEMTREX\\openImgCSv\\v6\\filtered\\list\\train_occ_absent_list.csv")


# In[ ]:




