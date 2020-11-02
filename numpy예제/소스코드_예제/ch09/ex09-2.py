#!/usr/bin/env python
# coding: utf-8

# # 9.2 Numpy의 기초
# ## Numpy 배열

# In[1]:


#p144
x = [1, 3, 5]
x.mean()


# In[2]:


import numpy as np
x = np.array([1, 3, 5])
print(x.mean())


# In[3]:


print(x.shape)


# In[4]:


#p145
a = np.array([[1, 2, 3], [2, 3, 4]])


# In[5]:


x = np.array([1, 3, 5])
x = np.array(1, 3, 5)


# In[6]:


x = np.array([1, 3, 5, 7, 9, 11]).reshape(3, 2)
print(x)


# In[7]:


y = np.ones([3, 4])
print(y)


# In[8]:


#p146
x = np.array([[1, 3, 5], [2, 4, 6]])
print(x[1])          # [2 4 6] 출력
print(x[1].mean())   # 4.0 출력
print(x.mean())      # 3.5 출력
print(x.shape)       # (2, 3) 출력


# ## Numpy 배열의 슬라이싱

# In[9]:


list1 = [[1, 11], [2, 12], [3, 13]]
print(list1[:][1])


# In[10]:


print(list1[:, 1])  # Error 발생


# In[11]:


#p147
import numpy as np
list1 = [[1, 11], [2, 12], [3, 13]]
np_ary = np.array(list1)
print(np_ary[:, 1])


# In[12]:


import numpy as np
list1 = [[1, 11], [2, 12], [3, 13]]
print(np.array(list1[:, 1]))


# In[13]:


import numpy as np
list1 = np.array([[1, 11], [2, 12], [3, 13]])
print(list1[:, 1])


# In[14]:


import numpy as np
list1 = [[1, 11], [2, 12], [3, 13]]
print(np.array(list1[:, 1]))


# ## Numpy를 이용한 연산

# In[15]:


#p148
import math
math.sqrt(2)


# In[16]:


math.sqrt([2, 3, 4])


# In[17]:


import numpy as np
np.sqrt([2, 3, 4])


# In[18]:


#p149
math.sqrt([2, 3, 4])


# In[19]:


import numpy as np
a = np.arange(15)
print(a)


# In[20]:


import numpy as np
a = np.arange(15).reshape(3, 5)
print(a)


# ## 제로 벡터와 제로 행렬

# In[21]:


#p150
import numpy as np
zero_vector = np.zeros(3)
print(zero_vector)


# In[22]:


zero_matrix = np.zeros((4, 3))
print(zero_matrix)


# In[23]:


zero_vector = np.zeros(5)
zero_vector


# In[24]:


zero_matrix = np.zeros((5, 3))
zero_matrix


# In[25]:


import numpy as np
my_array = np.zeros(15).reshape(3,5)
my_array += 4
my_array


# ## 전치행렬

# In[26]:


#p151
ary = [[1,2], [3,4]]
print(ary.transpose())


# In[27]:


import numpy as np
ary = np.array([[1, 2], [3, 4]])
print(ary.transpose())


# In[28]:


#p152
import numpy as np
x = np.array([1,2,3])
y = np.array([4,5,6])
z = x * y
print(z)


# In[29]:


s = [1, 2, 3]
t = s + 1
print(t)


# In[30]:


s = np.array([1, 2, 3])
t = s + 1
print(t)


# In[31]:


#p153
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(X[1])
print(X[:, 1])


# In[32]:


X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
Y = np.array([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
print(X[:,1]+Y[:,1])


# In[33]:


#p154
a = np.array([10, 20, 30, 40, 50, 60, 70])
i = [1, 3, 5]
print(a[i])


# In[34]:


#p155
import numpy as np
a = np.array([10, 20, 30, 40, 50, 60, 70])
b = np.array(a[1:6:2])
print('b:', b)
b[1] = 10
print('b:', b)
print('a:', a)
type(b)


# ## 불리언

# In[35]:


a = np.array([10, 20, 30, 40, 50, 60, 70])
b = a > 50
print(b)


# In[36]:


ary = np.random.random(5)
print(ary)
print(np.all(ary >= 0.3))
print(np.any(ary > 0.7))


# ## 등간격 나누기

# In[37]:


#p157
np.linspace(0, 12, 4)


# In[38]:


np.linspace(0, 12, 4, retstep=True)


# In[39]:


np.linspace(0, 12, 4, endpoint=False)


# In[40]:


np.logspace(np.log10(10), np.log10(100), 5)


# In[41]:


np.logspace(1, 2, 5)


# In[ ]:




