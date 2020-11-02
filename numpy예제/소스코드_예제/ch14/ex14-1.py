
# coding: utf-8

# # 14.1 기계학습의 단계

# In[1]:


#p242
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import matplotlib.pyplot as plt
dogs = 1000                        # 1000마리
cats = 1000
dog_height = 35 + (5 * np.random.randn(dogs))
cat_height = 30 + (5 * np.random.randn(cats))
plt.xlabel('Height')
plt.ylabel('Number of Species')
plt.hist([dog_height, cat_height], label=['Dogs', 'Cats'], stacked=True, color=['r', 'y'])
plt.legend()
plt.show()


# ## 훈련 데이터 수집

# In[2]:


#p244
features = [[270, "울퉁불퉁"], [250, "울퉁불퉁"], [220, "매끈"], [240, "매끈"]]
labels = ["오렌지", "오렌지", "사과", "사과"]


# ## 입력 데이터 준비 및 분석

# In[3]:


#p245
features = [[270, 0], [250, 0], [220, 1], [240, 1]]
labels = [0, 0, 1, 1]


# ## 학습

# In[4]:


from sklearn import tree
features = [[270, 0], [250, 0], [220, 1], [240, 1]]
labels = [0, 0, 1, 1]        # 오렌지(0), 사과(1)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)


# ## 예측 및 테스트

# In[5]:


#p246
print(clf.predict([[245, 1]]))

