#!/usr/bin/env python
# coding: utf-8

# # 12.2 Binning/Normalization
# ## Binning

# In[1]:


#p186
#get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(1000)
plt.hist(x, density=True, bins=np.linspace(-5, 5, 21))
plt.show()

# ## Normalization

# In[2]:


#p187
import pandas as pd
ary = [[2, 2], [4, 4], [6, 6], [8, 8], [10, 10]]
data = pd.DataFrame(ary, columns=['수온', '상온'])
data['수온'] = data['수온']/data['수온'].max()
data['상온'] = data['상온']/data['상온'].max()
data



# In[3]:


#p188
import pandas as pd
ary = [[2, 2], [4, 4], [6, 6], [8, 8], [10, 10]]
data = pd.DataFrame(ary, columns=['수온', '상온'])
data['수온'] = (data['수온']-data['수온'].min())/(data['수온'].max()-data['수온'].min())
data['상온'] = data['상온']/data['상온'].max()
data


# In[ ]:




