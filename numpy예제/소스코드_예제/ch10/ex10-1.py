#!/usr/bin/env python
# coding: utf-8

# # 10.1 Matplot의 기초
# ## 직선 그래프

# In[1]:


#p160
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
y = [1, 2, 3, 4, 5]
plt.plot(y)
plt.show()


# In[2]:


import matplotlib.pyplot as plt
y = [13, 16, 15, 18, 16, 17, 16]
plt.plot(y)


# In[3]:


#p161
y = [13, 16, 15, 18, 16, 17, 16]
plt.plot(range(len(y)), y);


# In[4]:


x = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
y = [13, 16, 15, 18, 16, 17, 16]
plt.plot(x, y);


# In[5]:


#p162
x = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
y = [13, 16, 15, 18, 16, 17, 16]
plt.plot(x, y);
plt.xlabel('Daily')
plt.ylabel('No. of Books Sold');


# In[6]:


x = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
y1 = [13, 16, 15, 18, 16, 17, 16]
y2 = [17, 14, 17, 16, 15, 15, 14]
plt.plot(x, y1)
plt.plot(x, y2)
plt.xlabel('Daily')
plt.ylabel('No. of Books Sold');


# In[7]:


#p163
x = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
y1 = [13, 16, 15, 18, 16, 17, 16]
y2 = [17, 14, 17, 16, 15, 15, 14]
plt.plot(x, y1, label='Sold')
plt.plot(x, y2, label='On Shelves')
plt.xlabel('Daily')
plt.ylabel('No. of Books Sold')
plt.legend(loc="upper left")


# In[8]:


x = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
y1 = [13, 16, 15, 18, 16, 17, 16]
y2 = [17, 14, 17, 16, 15, 15, 14]
plt.plot(x, y1, label='Sold')
plt.plot(x, y2, label='On Shelves')
plt.xlabel('Daily')
plt.ylabel('No. of Books Sold')
plt.legend(loc="upper left")
plt.title('Le Petit Prince: Sold & Left')


# ## 점선 그래프

# In[9]:


#p164
x = [1, 2, 3, 4, 5]
y = [1, 4, 6, 16, 25]
plt.plot(x, y, 'bo')
plt.show()


# In[10]:


x = [1, 2, 3, 4, 5]
y = [1, 4, 6, 16, 25]
plt.plot(x, y, 'bo')
plt.axis([0, 6, 0, 30])
plt.show()


# In[ ]:




