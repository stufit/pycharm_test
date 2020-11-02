#!/usr/bin/env python
# coding: utf-8

# # 16.1 텐서플로우를 이용한 필기 숫자 데이터 세트 학습

# In[1]:


#p284
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
learn = tf.contrib.learn                                       #TF.Learn을 이용하여 구분자를 훈련!
mnist = learn.datasets.load_dataset('mnist')                   # mnist 데이터셋 다운로드
train_data = mnist.train.images                                # 학습이미지 데이터
train_labels = np.asarray(mnist.train.labels, dtype=np.int32)  # 학습라벨 데이터
test_data = mnist.test.images                                  # 테스트 이미지 데이터
test_labels = np.asarray(mnist.test.labels, dtype=np.int32)    # 테스트 학습 데이터
print(test_labels)


# In[2]:


tf.logging.set_verbosity(tf.logging.ERROR)


# In[3]:


max_examples = 10000
data = train_data[:max_examples]
labels = train_labels[:max_examples]
plt.imshow(test_data[0].reshape((28, 28)), cmap=plt.cm.YlOrBr)
print('Index %d: Label %d' % (0, test_labels[0]))


# In[4]:


#p285
print(data[0].shape)


# In[5]:


#p286
print(test_data[0])


# In[8]:


#p287
input_features = learn.infer_real_valued_columns_from_input(data)
classifier = learn.LinearClassifier(feature_columns=input_features, n_classes=10)
classifier.fit(data, labels, batch_size=100, steps=1000)
classifier.evaluate(test_data, test_labels)
print(classifier.evaluate(test_data, test_labels)['accuracy'])
print(classifier.predict(np.array([test_data[0]], dtype=float), as_iterable=False))
print(test_labels[0])


# ## 필기 숫자 데이터 세트를 기계학습 모델에 적용

# In[9]:


#p289
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
learn = tf.contrib.learn                           # TF.Learn을 이용하여 구분자를 훈련!
tf.logging.set_verbosity(tf.logging.ERROR)
mnist = learn.datasets.load_dataset('mnist')                  # mnist 데이터셋 다운로드
train_data = mnist.train.images                               # 학습이미지 데이터
train_labels = np.asarray(mnist.train.labels, dtype=np.int32) # 학습라벨 데이터
test_data = mnist.test.images                                 # 테스트 이미지 데이터
test_labels = np.asarray(mnist.test.labels, dtype=np.int32)
max_examples = 10000
data = train_data[:max_examples]
labels = train_labels[:max_examples]


# ### 결정트리를 이용한 경우

# In[11]:


from sklearn import datasets, tree
clf = tree.DecisionTreeClassifier()
clf.fit(data, labels)
predictions = clf.predict(test_data)
from sklearn.metrics import accuracy_score
print(accuracy_score(test_labels, predictions))


# ### KNeighborsClassifier를 이용한 경우

# In[12]:


from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
digits = datasets.load_digits()
clf = KNeighborsClassifier()
clf.fit(data, labels)
predictions = clf.predict(test_data)
from sklearn.metrics import accuracy_score
print(accuracy_score(test_labels, predictions))


# ### 직접 작성한 무작위 분류 방식을 이용한 경우

# In[13]:


#p290
from sklearn import datasets
digits = datasets.load_digits()
import random
class myKNN():
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train
    def predict(self, X_test):
        predictions = []
        for row in X_test:
            label = random.choice(self.y_train)
            predictions.append(label)
        return predictions
clf = myKNN()              # 나만의 구분자를 사용!
clf.fit(data, labels)
predictions = clf.predict(test_data)
from sklearn.metrics import accuracy_score
print(accuracy_score(test_labels, predictions))


# ### 직접 작성한 유클리디언 분류 방식을 이용한 경우

# In[15]:


from scipy.spatial import distance
def euc(a, b) :
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
                best_index = i
        return self.y_train[best_index]
clf = eucKNN()
clf.fit(data, labels)
predictions = clf.predict(test_data)
from sklearn.metrics import accuracy_score
print(accuracy_score(test_labels, predictions))


# In[17]:


#p291
from sklearn import datasets
digits = datasets.load_digits()
print(len(digits.data), len(digits.target))


# In[19]:


from sklearn import datasets
digits = datasets.load_digits()
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
                best_index = i
        return self.y_train[best_index]
clf = eucKNN()
clf.fit(digits.data[:-500], digits.target[:-500])
predictions = clf.predict(digits.data[-500:])
from sklearn.metrics import accuracy_score
print(accuracy_score(digits.target[-500:], predictions))


# ### 서포트 벡터머신을 이용한 경우

# In[20]:


#p292
from sklearn import svm, datasets
digits = datasets.load_digits()
clf = svm.SVC(gamma=0.001, C=100.)
clf.fit(data, labels)
predictions = clf.predict(test_data)
from sklearn.metrics import accuracy_score
print(accuracy_score(test_labels, predictions))


# In[ ]:




