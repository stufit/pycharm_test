#!/usr/bin/env python
# coding: utf-8

# # 11.1 Pandas의 기초
# ## Pandas의 데이터 형식
# ### Series 형식

# In[1]:


#p173
import pandas as pd
pd.Series([7, 3, 5, 8])


# #### index

# In[2]:


x = pd.Series([7, 3, 5, 8], index=['서울', '대구', '부산', '광주'])
print(x)
x['서울']


# In[3]:


x[['서울', '대구']]


# In[4]:


#p174
x.index


# #### sorted()

# In[5]:


print(sorted(x.index))


# In[6]:


sorted(x.values)


# In[7]:


x.reindex(sorted(x.index))


# #### 인덱스별로 저장된 값들의 합을 구하기

# In[8]:


x = pd.Series([3, 8, 5, 9], index=['서울', '대구', '부산', '광주'])
y = pd.Series([2, 4, 5, 1], index=['대구', '부산', '서울', '대전'])
x+y


# #### unique()

# In[9]:


#p175
medal = [1, 3, 2, 4, 2, 3]
x = pd.Series(medal)
print(pd.unique(x))


# In[10]:


medal = ['민준', '현우', '서연', '동현', '서연', '현우']
x = pd.Series(medal)
print(pd.unique(x))


# #### 사전 형식의 데이터를 Pandas의 Series 형식으로 변환

# In[11]:


age = {'민준':23, '현우':43, '서연':12, '동현':45}
x = pd.Series(age)
x


# In[12]:


names = ['민준', '서연', '현우', '민서', '동현', '수빈']
pdata = pd.Series(names)
print(pdata)


# In[13]:


a = pdata[3:6]
print(a.values)


# #### 요약

# In[1]:


#p176
print(a[2])


# In[15]:


print(a)


# ### 데이터프레임

# In[16]:


#p177
data = {'age' : [23, 43, 12, 45],
       'name' : ['민준', '현우', '서연', '동현'],
       'height' : [175.3, 180.3, 165.8, 172.7]}
x = pd.DataFrame(data, columns = ['name', 'age', 'height'])
x


# #### name 컬럼의 내용만 출력

# In[17]:


x.name


# #### iloc()

# In[18]:


ary = [[1, 2], [3, 4], [5, 6]]
data = pd.DataFrame(ary, columns=['First', 'Second'])
data


# In[19]:


data.iloc[1]


# In[20]:


#p178
data.iloc[:, -1]


# #### head()와 tail()

# In[21]:


ary = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
data = pd.DataFrame(ary, columns=['First', 'Second'])
data.head(3)


# In[22]:


data.tail(3)


# #### 특정 항목만 선택

# In[23]:


bools = [False, True, True, False, True]
data.Second[bools]


# In[24]:


#p179
print(x.mean(axis=0))


# #### [참고] 부울형 리스트를 인덱스 값으로 입력

# In[25]:


data = {'age' : [23, 43, 12, 45],
       'name' : ['민준', '현우', '서연', '동현'],
       'height' : [175.3, 180.3, 165.8, 172.7]}
x = pd.DataFrame(data, columns = ['name', 'age', 'height'])
index = [True, False, True, False]
print(x[index])


# ## Pandas 데이터의 형변환

# In[26]:


#p180
import pandas as pd
#import numpy as np
ary = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
data = pd.DataFrame(ary, columns=['First', 'Second'])
data


# In[27]:


data['First'] = data['First'].astype('float')
data


# ### Pandas에 파일 가져오기

# In[28]:


#p181
import pandas as pd
food = pd.read_csv('food.csv')
food.head()


# In[29]:


import pandas as pd
accident = pd.read_csv('acci.csv')
accident


# In[30]:


import pandas as pd
accident = pd.read_csv('acci.csv', engine='python')
accident.head()


# In[ ]:




