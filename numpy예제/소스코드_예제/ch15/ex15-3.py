#!/usr/bin/env python
# coding: utf-8

# # 15.3 지도학습 모델의 종류
# ## 결정트리
# ### 데이터 분석 및 준비

# In[1]:


#p254
from sklearn.datasets import load_iris  # iris 데이터 세트 가져오기
iris = load_iris()                      # iris 토이 데이터세트를 iris 변수에 저장
print(iris.feature_names)               # 특징(feature)들을 출력
print(iris.target_names)                # 학습 라벨에 해당하는 target을 출력
print(iris.data[0])                     # 첫 번째 데이터에 저장된 feature값 출력
print(iris.target[0])                   # 첫 번째 데이터에 저장된 target값 출력


# In[2]:


#p255
from sklearn.datasets import load_iris
iris = load_iris()
for i in range(len(iris.target)):
    print("Example %d: label %s, features %s" % (i, iris.target[i], iris.data[i]))


# In[3]:


import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
test = [0,50,100]

# training data 준비과정!
train_data = np.delete(iris.data, test, axis=0)   # 세 개의 데이터들을 데이터변수에서 제거
train_target = np.delete(iris.target, test)       # 세 개의 데이터들을 타깃변수에서 제거

# testing data 준비과정!
test_data = iris.data[test]
test_target = iris.target[test]

# 결정트리 생성!
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

# 출력
print(test_target)
print(clf.predict(test_data))


# #### Flatten

# In[4]:


#p257
a = np.array([[1,2], [3,4]])
print(a.flatten())                     # 또는 print(a.flatten('C'))


# In[5]:


print(a.flatten('F'))


# In[6]:


import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
test_idx = [0,50,100]
train_data = np.delete(iris.data, test_idx, axis=0)
print(train_data.shape)
print(train_data)


# In[7]:


import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
test_idx = [0,50,100]
train_data = np.delete(iris.data, test_idx, axis=1)
print(train_data.shape)
print(train_data)


# In[8]:


#p258
import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree                           # 구분자 훈련을 위한 import
iris = load_iris()
test_idx = [0,50,100]           # 3종류의 꽃 리스트에서 가장 앞에 있는 1개씩의 데이터 3개!
train_target = np.delete(iris.target, test_idx)     # 세 개의 요소들을 타깃변수에서 제거
train_data = np.delete(iris.data, test_idx) # 세 개의 요소들을 데이터변수에서 제거
print(train_data.shape)
for i in range(len(train_data)):
    print("%dth, %s" % (i, train_data[i]))


# In[9]:


#p259
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
iris = load_iris()
sepal = iris.data[:, 0:2]
kind = iris.target
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.plot(sepal[kind==0][:,0], sepal[kind==0][:,1], "ro", label='Setosa')
plt.plot(sepal[kind==1][:,0], sepal[kind==1][:,1], "bo", label='Versicolor')
plt.plot(sepal[kind==2][:,0], sepal[kind==2][:,1], "yo", label='Virginica')
plt.legend()


# In[10]:


#260
import graphviz
dot_data = tree.export_graphviz(clf, out_file=None)
graph = graphviz.Source(dot_data)
graph.render("iris")
dot_data = tree.export_graphviz(clf, out_file=None,
                               feature_names=iris.feature_names,
                               class_names=iris.target_names,
                               filled=True, rounded=True,
                               special_characters=True)
graph = graphviz.Source(dot_data)
graph


# In[11]:


#p261
from sklearn.externals.six import StringIO
import graphviz
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data,
                    feature_names=iris.feature_names,
                    class_names=iris.target_names,
                    filled=True, rounded=True,
                    impurity=False)
graph = graphviz.Source(dot_data.getvalue())
graph.render("iris", view=True)


# In[12]:


#p262
print(test_data[1], test_target[1])
print(iris.feature_names, iris.target_names)


# In[13]:


import numpy as np
from sklearn.model_selection import train_test_split
y = range(6)
print(list(y))
print(train_test_split(y))


# In[14]:


#p263
import numpy as np
from sklearn.model_selection import train_test_split
y = range(6)
print(list(y))
print(train_test_split(y, test_size=0.5))


# In[15]:


import numpy as np
from sklearn.model_selection import train_test_split
X = np.arange(12).reshape((6, 2))
y = range(6)
print(X)
print(list(y))


# In[16]:


import numpy as np
from sklearn.model_selection import train_test_split
X = np.arange(12).reshape((6, 2))
y = range(6)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)
print(X_train)
print(y_train)
print(X_test)
print(y_test)


# ### 학습 및 예측

# In[17]:


#p264
from sklearn import datasets
iris = datasets.load_iris()
X = iris.data
y = iris.target
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5)
from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
print('예측:\n', predictions)
print('정답(y_test):\n', y_test)


# ### 테스트

# In[18]:


#p265
from sklearn.metrics import accuracy_score
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [1, 2, 4, 4, 5, 6, 7, 8, 9, 10]
print(accuracy_score(a, b))


# In[19]:


from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))


# ## 최근접 이웃 탐색 모델
# ### K-최근접이웃 모델

# In[20]:


#p266
X = [[0], [1], [2], [3], [4], [5]]
y = [0, 0, 0, 1, 1, 1]
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y)


# In[21]:


#p267
print(neigh.predict([[2.8]]))
print(neigh.predict_proba([[2.8]]))


# In[22]:


print(neigh.predict([[2.3]]))
print(neigh.predict_proba([[2.3]]))


# In[23]:


from sklearn import datasets
iris = datasets.load_iris()
X = iris.data
y = iris.target
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5)
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier()
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
print('예측:\n', predictions)
print('정답(y_test):\n', y_test)


# In[24]:


#p268
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))


# ### 나만의 분류자 모델

# In[25]:


#p269
import random
class myKNN():
    def fit(self, X_train, y_train):
        self.X_train = X_train      # X_train 데이터를 그대로 저장!
        self.y_train = y_train      # y_train 데이터를 그대로 저장!
    def predict(self, X_test):
        predictions = []
        for row in X_test:
            label = random.choice(self.y_train)
            predictions.append(label)
        return predictions

from sklearn import datasets
iris = datasets.load_iris()
X = iris.data
y = iris.target
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5)

# from sklearn.neighbors import KNeighborsClassfier 사용하지 않고
clf = myKNN()                            # 나만의 분류자를 사용!
clf.fit(X_train, y_train)
preidctions = clf.predict(X_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))


# ### 유클리디어 방식의 분류자 모델
# #### 요약 문제

# In[26]:


#p270
import numpy as np
def euc(p1, p2):
    return np.sqrt(np.sum(np.power(p2-p1, 2)))
p1 = np.array([1, 1])
p2 = np.array([4, 4])
euc(p1, p2)


# In[27]:


from scipy.spatial import distance
def euc(a, b) :
    return distance.euclidean(a, b)
p1 = np.array([1, 1])
p2 = np.array([4, 4])
euc(p1, p2)


# In[28]:


from scipy.spatial import distance
def euc(a, b) :
    return distance.euclidean(a, b)
p1 = np.array([1, 1, 3, 3])
p2 = np.array([4, 4, 5, 5])
euc(p1, p2)


# In[29]:


#p271
from scipy.spatial import distance
def euc(a,b) :
    return distance.euclidean(a, b)
class eucKNN():
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train
    def predict(self, X_test):
        predictions = []
        for row in X_test:
            label = self.closest(row)
            predictions.append(label)
        return predictions
    def closest(self, row):
        best_dist = euc(row, self.X_train[0])
        best_index = 0
        for i in range(1, len(self.X_train)):
            dist = euc(row, self.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = 1
        return self.y_train[best_index]
from sklearn import datasets
iris = datasets.load_iris()
X = iris.data
y = iris.target
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5)
clf = eucKNN()
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))


# ## 서포트 벡터 머신

# In[30]:


#p272
from sklearn import datasets
iris = datasets.load_iris()
X = iris.data
y = iris.target
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5)

from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)
print(y_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))


# ### [참고]

# In[31]:


#p274
import numpy as np
points = 500
vectors = []
for i in range(points):
    x1= np.random.normal(0.0, 0.5)
    y1= x1 * 0.3 + 0.5 + np.random.normal(0.0, 0.05)
    vectors.append([x1, y1])
x_data = [v[0] for v in vectors]
y_data = [v[1] for v in vectors]

import matplotlib.pyplot as plt
plt.plot(x_data, y_data, 'bo', label='Data')
plt.legend()
plt.show();


# In[32]:


#p275
import matplotlib.pyplot as plt
import numpy as np
points = 500
vectors = []
for i in range(points):
    x1= np.random.normal(0.0, 0.5)
    y1= x1 * 0.3 + 0.5 + np.random.normal(0.0, 0.05)
    vectors.append([x1, y1])
x_data = [v[0] for v in vectors]
y_data = [v[1] for v in vectors]

import tensorflow as tf
a = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))
y = a * x_data + b
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
get_ipython().run_line_magic('matplotlib', 'inline')
for step in range(10):
    sess.run(train)
    plt.plot(x_data, y_data, 'bo')
    plt.plot(x_data, sess.run(a) * x_data + sess.run(b))
plt.show()


# In[ ]:




