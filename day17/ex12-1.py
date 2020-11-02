#!/usr/bin/env python
# coding: utf-8

# # 12.1 빅데이터의 가공
# ## 존재하지 않는 값 처리

# In[1]:
import pandas as pd
accident = pd.read_csv('acci.csv',engine='python',encoding='euc-kr')
print(accident.head())


#p183
import pandas as pd
#robots = [[24, 23680], [35, NaN], [46, 47350], [27, NaN]]


# In[2]:


#p184
import pandas as pd
from numpy import NaN
robots = [[24, 23680], [35, NaN], [46, 47350], [27, NaN]]
print(robots)


# In[3]:

print('----------------------')
import pandas as pd
from numpy import NaN
robots = [[24, 23680], [35, NaN], [46, 47350], [27, NaN]]
data = pd.DataFrame(robots, columns=['max_speed', 'price'])
print(data)

print('-----------------------')
# In[4]:


data.dropna(subset=['price'], axis=0, inplace=True)
print(data)
print('-----------------------')

# In[5]:


#p185
import pandas as pd
from numpy import NaN
robots = [[24, 23680], [35, NaN], [46, 47350], [27, NaN]]
data = pd.DataFrame(robots, columns=['max_speed', 'price'])
mean = data['price'].mean()
data.replace(NaN, mean)
print(data)

print('-----------------------')
# In[6]:


data = data.replace(NaN, mean)
# 또는
# data.replace(NaN, mean, inplace=True)
print(data)
print('-----------------------')

# In[ ]:




