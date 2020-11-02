#!/usr/bin/env python
# coding: utf-8

# # 12.3 Data Formatting
# ## 수치값을 카테고리값으로 변환하기

# In[1]:


#p189
import numpy as np
import pandas as pd
price = np.random.randint(100, size=8)*10000
cars = pd.DataFrame(price, columns=['price'])
cars


# In[2]:


group_names = ['저급', '중급', '고급']
cars['level'], mybin = pd.cut(cars['price'], 3, labels=group_names, retbins=True)
cars


# In[3]:


#p190
print(mybin)


# ## 카테고리값을 수치값으로 변환하기

# In[4]:


#p191
import pandas as pd
import numpy as np
ary = [[1, 1.1, '손'], [2, 2.2, '날개'], [3, 3.3, '손']]
data = pd.DataFrame(ary, columns=['수온', '상온', 'hand'])
pd.get_dummies(data['hand'])


# In[5]:


import pandas as pd
import numpy as np
ary = [[1, 1.1, '손'], [2, 2.2, '날개'], [3, 3.3, '손']]
data = pd.DataFrame(ary, columns=['수온', '상온', 'hand'])
data = pd.concat([data, pd.get_dummies(data['hand'])], axis=1, sort=False)
data


# In[6]:


data.drop(['hand'], axis=1, inplace=True)
data


# In[ ]:




