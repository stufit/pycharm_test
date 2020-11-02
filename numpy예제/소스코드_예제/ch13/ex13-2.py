
# coding: utf-8

# # 13.2 GPS를 이용한 철새 이동
# ## 시간측정 기능 소개

# In[1]:


#p220
import pandas as pd
birdata = pd.read_csv('bird_tracking.csv')
birdata.columns


# In[2]:


#p221
birdata.date_time[0:3]


# ### 시간 출력

# In[3]:


import datetime as dt
dt.datetime.today()


# ### 시간 측정

# In[4]:


#p222
time1 = dt.datetime.today()


# In[5]:


time2 = dt.datetime.today()
time2 - time1


# In[6]:


import pandas as pd
birdata = pd.read_csv('bird_tracking.csv')
import datetime as dt
date_str = birdata.date_time[0]
print(date_str)


# In[7]:


date_str[:-3]


# In[8]:


dt.datetime.strptime(date_str[:-3], '%Y-%m-%d %H:%M:%S')


# In[9]:


#p223
a = dt.datetime.strptime(date_str[:-3], '%Y-%m-%d %H:%M:%S')
print(a)


# In[10]:


timestamps = []
for k in range(len(birdata)):
    timestamps.append(dt.datetime.strptime(birdata.date_time.iloc[k][:-3], '%Y-%m-%d %H:%M:%S'))
timestamps


# In[11]:


timestamps[1] - timestamps[0]


# In[12]:


a = timestamps[1] - timestamps[0]
print(a)


# In[13]:


birdata.index


# In[14]:


birdata['timestamp'] = pd.Series(timestamps, index=birdata.index)
birdata.head()


# #### 새의 이름 출력

# In[15]:


#p224
import pandas as pd
birdata = pd.read_csv('bird_tracking.csv')
bird_names = pd.unique(birdata.bird_name)
print(bird_names)


# ### 누적측정시간

# In[16]:


import pandas as pd
birdata = pd.read_csv('bird_tracking.csv')
import datetime as dt
timestamps = []
for k in range(len(birdata)):
    timestamps.append(dt.datetime.strptime(birdata.date_time.iloc[k][:-3], '%Y-%m-%d %H:%M:%S'))
birdata['timestamp'] = pd.Series(timestamps, index=birdata.index)
times = birdata.timestamp[birdata.bird_name == 'Eric']
elapsed = [time - times[0] for time in times]
elapsed


# In[17]:


#p225
print(elapsed[0])
print(elapsed[1])
print(elapsed[100])


# In[18]:


elapsed[100] / dt.timedelta(days=1)


# In[19]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
plt.plot(np.array(elapsed) / dt.timedelta(days=1))
plt.xlabel('Observation')
plt.ylabel('Elapsed(days)')


# #### 비행속도 추적

# In[20]:


#226
import pandas as pd
birdata = pd.read_csv('bird_tracking.csv')
ix = birdata.bird_name == "Eric"
speed = birdata.speed_2d[ix]
print(speed.head())


# In[21]:


import pandas as pd
import matplotlib.pyplot as plt
plt.plot(range(50), speed[:50]);
plt.xlabel('Observation')
plt.ylabel('Flying Speed')


# #### 비행 경로

# In[22]:


#p227
import pandas as pd
birdata = pd.read_csv('bird_tracking.csv')
speed = birdata.speed_2d[birdata.bird_name == "Eric"]
speed[218]


# In[23]:


speed[219]


# In[24]:


#p228
import pandas as pd
birdata = pd.read_csv('bird_tracking.csv')
speed = birdata.speed_2d[birdata.bird_name == "Eric"]
import numpy as np
speed = np.array(speed)
speed = np.isnan(speed)
print(np.isnan(speed))


# In[25]:


np.isnan(speed).any()


# In[26]:


import pandas as pd
birdata = pd.read_csv('bird_tracking.csv')
speed = birdata.speed_2d[birdata.bird_name == "Eric"]
import numpy as np
speed = np.array(speed)
def getnan(s):
    for i, n in enumerate(s):
        if np.isnan(n):
            return i
ind = getnan(speed)
print(ind)


# In[27]:


#p229
len(np.isnan(speed))


# In[28]:


#p230
import cartopy.crs as ccrs
import cartopy.feature as cfeature
proj = ccrs.Mercator()
plt.figure(figsize=(10,10))
ax = plt.axes(projection=proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':');


# In[29]:


#p231
import cartopy.crs as ccrs
import cartopy.feature as cfeature
proj = ccrs.Mercator()
plt.figure(figsize=(10,10))
ax = plt.axes(projection=proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':');
for name in bird_names:
    ix = birdata['bird_name'] == name
    x, y = birdata.longitude[ix], birdata.latitude[ix]
    ax.plot(x, y, '.', transform=ccrs.Geodetic(), label=name)
plt.legend(loc='upper left')


# In[30]:


#p232
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
birdata = pd.read_csv('bird_tracking.csv')
x, y = birdata.longitude, birdata.latitude
plt.figure(figsize=(7,7))
plt.plot(x, y, '.');


# In[31]:


import pandas as pd
birdata = pd.read_csv('bird_tracking.csv')
import matplotlib.pyplot as plt
import numpy as np
ix = birdata.bird_name == "Eric"
x, y = birdata.longitude[ix], birdata.latitude[ix]
plt.figure(figsize=(7,7))
plt.plot(x, y, '.');


# In[32]:


#p233
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import distance
import cartopy.crs as ccrs
import cartopy.feature as cfeature
proj = ccrs.Mercator()
plt.figure(figsize=(10,10))
ax = plt.axes(projection=proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':');
birdata = pd.read_csv('bird_tracking.csv')
bird_names = pd.unique(birdata.bird_name)
ix = birdata.bird_name == "Eric"
x, y = birdata.longitude[ix], birdata.latitude[ix]
ax.plot(x[0:17000], y[0:17000], '.', transform=ccrs.Geodetic());
ax.plot(x[17101:18600], y[17101:18600], '.', transform=ccrs.Geodetic());


# ### 요약 문제

# In[33]:


#p234
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import distance
import cartopy.crs as ccrs
import cartopy.feature as cfeature
proj = ccrs.Mercator()
plt.figure(figsize=(10,10))
ax = plt.axes(projection=proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':');
def euc(a,b) :
    return distance.euclidean(a, b)
birdata = pd.read_csv('bird_tracking.csv')
bird_names = pd.unique(birdata.bird_name)
sindex = 2500                           # start index
eindex = 7500                           # end index
ix = birdata.bird_name == "Eric"
x, y = birdata.longitude[ix], birdata.latitude[ix]
i = [x[sindex], y[sindex]]
j = [x[eindex], y[eindex]]
ax.plot(x[sindex:eindex], y[sindex:eindex], '.', transform=ccrs.Geodetic());
print('Eric', euc(i, j))
ix = birdata['bird_name'] == 'Nico'
x, y = birdata.longitude[ix], birdata.latitude[ix]
start = len(x)
dest = len(y)
i = [x[start+sindex], y[start+sindex]]
j = [x[dest+eindex], y[dest+eindex]]
ax.plot(x[sindex:eindex], y[sindex:eindex], '.', transform=ccrs.Geodetic());
print('Nico', euc(i, j))
ix = birdata['bird_name'] == 'Sanne'
x, y = birdata.longitude[ix], birdata.latitude[ix]
#print(x.get_value[40920])
start = start + len(x)
dest = dest + len(x)
i = [x[start+sindex], y[start+sindex]]
j = [x[dest+eindex], y[dest+eindex]]
ax.plot(x[sindex:eindex], y[sindex:eindex], '.', transform=ccrs.Geodetic());
print('Sanne', euc(i,j))


# In[34]:


#p236
longest = 0
distlist = []
def euc(a, b) :
    return distance.euclidean(a, b)
ix = birdata['bird_name'] == 'Eric'
x, y = birdata.longitude[ix], birdata.latitude[ix]
i = [x[0], y[0]]
for ind in range(len(x)-1):
    j = [x[ind+1], y[ind+1]]
    newlength = euc(i, j)
    distlist.append(newlength)
    if (euc(i, j) > longest):
        longest = newlength
print('Longest=', longest)


# In[35]:


bird_name = pd.unique(birdata.bird_name)
bird_dist = {}
def euc(a, b) :
    return distance.euclidean(a, b)
start = 0
end = 0
count = 0
for bird_name in bird_names:
    ix = birdata['bird_name'] == bird_name
    x, y = birdata.longitude[ix], birdata.latitude[ix]
    longest = 0
    i = [x[start], y[start]]
    for ind in range(len(x)-1):
        j = [x[start+ind+1], y[start+ind+1]]
        newlength = euc(i, j)
        distlist.append(newlength)
        if (euc(i, j) > longest):
            longest = newlength
    bird_dist[bird_names[count]] = longest
    count = count + 1
    start = start + len(x)
    dest = dest + len(x)
print(bird_dist)

