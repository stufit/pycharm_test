#!/usr/bin/env python
# coding: utf-8

# # 15.4 비지도학습의 구조
# ## 개요

# In[1]:


#p277
from sklearn import cluster, datasets
import matplotlib.pyplot as plt
iris = datasets.load_iris()
X = iris.data[:, 2:]
y = iris.target
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.axis([0, X[:, 0].max()+0.2, 0, X[:, 1].max()+0.2])
plt.plot(X[:, 0], X[:, 1], 'bo')


# In[2]:


#p278
from sklearn import cluster, datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()
X = iris.data[:, 2:]
y = iris.target
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolor='k')

plt.xlabel('Petal Length')
plt.ylabel('Petal width')
plt.axis([0, X[:, 0].max()+0.2, 0, X[:, 1].max()+0.2])

plt.show()


# ### K-평균 방식

# In[3]:


#p278
from sklearn.cluster import KMeans
import numpy as np
X = np.array([[1, 5], [3, 4], [2, 3], [5, 3], [6, 2], [5, 1]])
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
print(kmeans.labels_)
print(kmeans.cluster_centers_)


# In[4]:


#p279
import matplotlib.pyplot as plt
y = kmeans.labels_
ycenter = kmeans.cluster_centers_
plt.scatter(X[:,0], X[:,1], c=y, cmap='viridis', edgecolor='k')
plt.scatter(ycenter[:,0], ycenter[:,1], c=[0,1], cmap='viridis', s=200, edgecolor='k')


# In[5]:


from sklearn.cluster import KMeans
import numpy as np
X = np.array([[1, 5], [3, 4], [2, 3], [5, 3], [6, 2], [5, 1]])
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
x = np.array([[1, 4], [4, 2]])
y = kmeans.labels_
y_pred = kmeans.predict(x)
print(y_pred)
plt.scatter(X[:,0], X[:,1], c=y, cmap='viridis', edgecolor='k')
plt.scatter(x[:,0], x[:,1], c=y_pred, cmap='magma', marker='^', s=200, edgecolor='k')


# #### 참고

# In[6]:


#p281
from sklearn.cluster import KMeans
import numpy as np
X = np.array([[1, 5], [3, 8], [3, 5],
             [10, 13], [9, 12], [11, 14],
             [5, 3], [7, 2], [5, 1]])
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
#kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
y = kmeans.labels_
print(kmeans.labels_)
print(kmeans.cluster_centers_)
x = np.array([[1, 4], [6, 5], [8, 10]])
y_pred = kmeans.predict(x)
import matplotlib.pyplot as plt
plt.scatter(X[:,0], X[:,1], c=y, cmap='viridis', edgecolor='K')
plt.scatter(x[:,0], x[:,1], c=y_pred, cmap='viridis', marker='^', s=200, edgecolor='k')
plt.axis([0, 12, 0, 15])
plt.show()


# #### 실제 데이터에 K-평균 모델 적용

# In[7]:


#p282
from sklearn.cluster import KMeans
iris = datasets.load_iris()
X_iris = iris.data
y_iris = iris.target
k_means = cluster.KMeans(n_clusters=3)
k_means.fit(X_iris)
print(k_means.labels_[::10])
print(y_iris[::10])


# In[8]:


from sklearn import cluster, datasets
import matplotlib.pyplot as plt
iris = datasets.load_iris()
X = iris.data[:, 2:]
y = iris.target
X1 = iris.data[[1, 50, 100], 2:]
y1 = iris.target[[1, 50, 100]]
k_means = cluster.KMeans(n_clusters=3).fit(X)
y_pred = k_means.predict(X1)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolor='k')
plt.scatter(X1[:,0], X1[:, 1], c=y_pred, cmap='viridis', marker='^', s=200, edgecolor='k')
plt.xlabel('Petal Length')
plt.ylabel('Petal width')
plt.axis([0, 8, -0.5, 3.5])
plt.show()


# In[ ]:




