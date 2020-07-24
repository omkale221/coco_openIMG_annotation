#!/usr/bin/env python
# coding: utf-8

# In[42]:


import pandas as pd
import numpy as np


# In[43]:


val_url = 'O:\\daaaCEMTREX\\openImgCSv\\v6\\imageid-url\\validation-images-with-rotation.csv'
val_list = 'O:\\daaaCEMTREX\\openImgCSv\\v6\\labels\\filtered\\list'
val_r = 'val_rest_list.csv'
val_p = 'val_occ_present_list.csv'
val_a = 'val_occ_absent_list.csv'


# In[44]:


test_url = 'O:\\daaaCEMTREX\\openImgCSv\\v6\\imageid-url\\test-images-with-rotation.csv'
test_list = 'O:\\daaaCEMTREX\\openImgCSv\\v6\\labels\\filtered\\list'
test_r = 'test_rest_list.csv'
test_p = 'test_occ_present_list.csv'
test_a = 'test_occ_absent_list.csv'


# In[45]:


train_url = 'O:\\daaaCEMTREX\\openImgCSv\\v6\\imageid-url\\train-images-boxable-with-rotation.csv'
train_list = 'O:\\daaaCEMTREX\\openImgCSv\\v6\\labels\\filtered\\list'
train_r = 'train_rest_list.csv'
train_p = 'train_occ_present_list.csv'
train_a = 'train_occ_absent_list.csv'


# In[46]:


val_u_df = pd.read_csv(val_url)
val_r_df = pd.read_csv(val_list + '\\' + val_r)
val_p_df = pd.read_csv(val_list + '\\' + val_p)
val_a_df = pd.read_csv(val_list + '\\' + val_a)


# In[47]:


test_u_df = pd.read_csv(test_url)
test_r_df = pd.read_csv(test_list + '\\' + test_r)
test_p_df = pd.read_csv(test_list + '\\' + test_p)
test_a_df = pd.read_csv(test_list + '\\' + test_a)


# In[48]:


train_u_df = pd.read_csv(train_url)
train_r_df = pd.read_csv(train_list + '\\' + train_r)
train_p_df = pd.read_csv(train_list + '\\' + train_p)
train_a_df = pd.read_csv(train_list + '\\' + train_a)


# In[59]:


val_array_r =val_r_df["ImageID"].to_numpy()
len(val_array_r)
val_array_p =val_p_df["ImageID"].to_numpy()
len(val_array_p)
val_array_a =val_a_df["ImageID"].to_numpy()
len(val_array_a)


# In[78]:


test_array_r =test_r_df["ImageID"].to_numpy()
len(test_array_r)
test_array_p =test_p_df["ImageID"].to_numpy()
len(test_array_p)
test_array_a =test_a_df["ImageID"].to_numpy()
len(test_array_a)


# In[61]:


tr_array_r =train_r_df["ImageID"].to_numpy()
len(tr_array_r)
tr_array_p =train_p_df["ImageID"].to_numpy()
len(tr_array_p)
tr_array_a =train_a_df["ImageID"].to_numpy()
len(tr_array_a)


# In[71]:


r_val = val_u_df[val_u_df['ImageID'].isin(val_array_r)]
r_val = r_val[['ImageID','OriginalURL']]
r_val.to_csv('O:\\daaaCEMTREX\\openImgCSv\\v6\\imageid-url\\req_url' + '\\' + val_r)


# In[73]:


p_val = val_u_df[val_u_df['ImageID'].isin(val_array_p)]
p_val = p_val[['ImageID','OriginalURL']]
p_val.to_csv('O:\\daaaCEMTREX\\openImgCSv\\v6\\imageid-url\\req_url' + '\\' + val_p)


# In[74]:


a_val = val_u_df[val_u_df['ImageID'].isin(val_array_a)]
a_val = a_val[['ImageID','OriginalURL']]
a_val.to_csv('O:\\daaaCEMTREX\\openImgCSv\\v6\\imageid-url\\req_url' + '\\' + val_a)


# In[79]:


r_test = test_u_df[test_u_df['ImageID'].isin(test_array_r)]
r_test = r_test[['ImageID','OriginalURL']]
r_test.to_csv('O:\\daaaCEMTREX\\openImgCSv\\v6\\imageid-url\\req_url' + '\\' + test_r)


# In[80]:


a_test = test_u_df[test_u_df['ImageID'].isin(test_array_a)]
a_test = a_test[['ImageID','OriginalURL']]
a_test.to_csv('O:\\daaaCEMTREX\\openImgCSv\\v6\\imageid-url\\req_url' + '\\' + test_a)


# In[81]:


p_test = test_u_df[test_u_df['ImageID'].isin(test_array_p)]
p_test = p_test[['ImageID','OriginalURL']]
p_test.to_csv('O:\\daaaCEMTREX\\openImgCSv\\v6\\imageid-url\\req_url' + '\\' + test_p)


# In[82]:


r_train = train_u_df[train_u_df['ImageID'].isin(tr_array_r)]
r_train = r_train[['ImageID','OriginalURL']]
r_train.to_csv('O:\\daaaCEMTREX\\openImgCSv\\v6\\imageid-url\\req_url' + '\\' + train_r)


# In[83]:


a_train = train_u_df[train_u_df['ImageID'].isin(tr_array_a)]
a_train = a_train[['ImageID','OriginalURL']]
a_train.to_csv('O:\\daaaCEMTREX\\openImgCSv\\v6\\imageid-url\\req_url' + '\\' + train_a)


# In[84]:


p_train = train_u_df[train_u_df['ImageID'].isin(tr_array_p)]
p_train = p_train[['ImageID','OriginalURL']]
p_train.to_csv('O:\\daaaCEMTREX\\openImgCSv\\v6\\imageid-url\\req_url' + '\\' + train_p)


# In[ ]:




