#!/usr/bin/env python
# coding: utf-8

# # 17 과제

# In[1]:


#p296
import numpy as np
import pandas as pd
whisky = pd.read_csv("whiskies.txt")
print(whisky.head())


# In[2]:


#p297
whisky.columns


# In[3]:


whisky["Region"] = pd.read_csv("regions.txt")
print(whisky["Region"])


# In[4]:


#298
whisky.iloc[0:3]


# In[5]:


whisky.iloc[0:3,2:14]


# In[6]:


#299
flavors = whisky.iloc[:, 2:14]
print(flavors)


# In[7]:


corr_flavors = pd.DataFrame.corr(flavors)
print(corr_flavors)


# In[8]:


#p301
import matplotlib.pyplot as plt
plt.pcolor(corr_flavors)
plt.colorbar()
#plt.savefig("whiskey1")   # whiskey1.png 파일 생성


# In[9]:


corr_whisky = pd.DataFrame.corr(flavors.transpose())
print(corr_whisky)


# In[ ]:


corr_whisky = pd.DataFrame.corr(flavors.transpose())
plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)
plt.colorbar()


# In[ ]:


#p304
from sklearn.cluster.bicluster import SpectralCoclustering
model = SpectralCoclustering(n_clusters=6, random_state=0)
model.fit(corr_whisky)
print(model.rows_)


# In[ ]:


#p305
model.row_labels_


# In[ ]:


np.sum(model.rows_, axis=1)


# In[ ]:


print(whisky['Region'].value_counts())


# In[ ]:




