#!/usr/bin/env python
# coding: utf-8

# # 10.2 Numpy를 이용한 plot 기능

# In[1]:


#p164
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
points = np.array([[1,1], [1,2], [1,3], [2,1], [2,2], [2,3], [3,1], [3,2], [3,3]])
p = np.array([2.5, 2])
import matplotlib.pyplot as plt
plt.plot(points[:,0], points[:,1], "ro")
plt.plot(p[0], p[1], "bo")


# In[2]:


import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 5, 10)
y = x**2
plt.plot(x, y);


# In[3]:


#p166
x = np.linspace(0, 10, 20)
y = x**2.0
plt.plot(x, y, "bo-", linewidth=3, markersize=5);


# In[4]:


plt.plot(x, y, "gs-", linewidth=1, markersize=3);


# In[5]:


#p167
x = np.linspace(0, 10, 20)
y1 = x**2.0
y2 = x**1.5
plt.plot(x, y1, "bo-", linewidth=2, markersize=12, label="First")
plt.plot(x, y2, "gs-", linewidth=2, markersize=12, label="Second")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis([-0.5, 10.5, -5, 105])
plt.legend(loc="upper left")
plt.savefig("mplot.pdf")


# In[6]:


x = np.logspace(-1, 1, 20)
y1 = x**2.0
y2 = x**1.5
plt.plot(x, y1, "bo-", linewidth=2, markersize=5, label="First")
plt.plot(x, y2, "gs-", linewidth=2, markersize=5, label="Second")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis([-0.5, 10.5, -5, 105])
plt.legend(loc="upper left")
plt.savefig("mplot.pdf")


# In[7]:


#p169
import matplotlib.pyplot as plt
import numpy as np
x = np.random.standard_normal(size=1000)
plt.hist(x)


# In[8]:


plt.hist(x, density=True)


# In[9]:


#p170
import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(1000)
plt.hist(x)


# In[10]:


import numpy as np
import matplotlib.pyplot as plt
x = np.random.rand(30)
y = np.random.rand(30)
colors = np.random.rand(30)
shape = np.pi * (np.random.rand(30)*20) **2
plt.scatter(x, y, s=shape, c = colors, marker='*', alpha=0.7)
plt.show()


# In[ ]:




