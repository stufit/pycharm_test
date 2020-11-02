#!/usr/bin/env python
# coding: utf-8

# # 5.2 배열의 종류
# ## 집합

# In[1]:


#p107
dict = { }                 # 빈 사전을 생성 또는 dict = set()
dict = {3, 2, 3, 1}       # 중복된 원소를 포함한 데이터 입력
print(dict)


# In[2]:


fruits = ['사과', '오렌지', '포도', '오렌지']
fruits = set(fruits)
print(fruits)


# ### 추가 및 삭제

# In[3]:


fruits = {'사과', '오렌지', '포도'}
fruits.add('키위')
print(fruits)         


# In[4]:


fruits = {'사과', '오렌지', '포도'}
fruits.update({'수박', '배'})
print(fruits)


# In[5]:


#p108
fruits = {'사과', '오렌지', '포도', '수박'}
fruits.remove('오렌지')
print(fruits)
fruits.pop()
print(fruits)
fruits.clear()
print(fruits)


# ### 존재여부

# In[6]:


fruits = {'사과', '오렌지', '포도'}
print('사과' in fruits)
print('키위' not in fruits)


# ### 집합의 연산

# In[7]:


#p109
one = {1, 3, 5, 7, 8}
two = {1, 3, 5, 6, 8}
print('one | two:', one | two)
print('one & two:', one & two)
print('one - two:', one - two)
print('one ^ two:', one ^ two)


# In[8]:


#p110
one = {1, 3, 5, 8}
two = {1, 3, 5, 8}
print('one <= two:', one <= two)
print('one < two:', one < two)
print('one >= two:', one >= two)
print('one > two:', one > two)


# ### 인공지능을 위한 빅데이터 분석의 예제

# In[9]:


training_data = [['연두', 3, '사과'],
                ['노랑', 3, '사과'],
                ['빨강', 2, '포도'],
                ['빨강', 1, '포도'],
                ['노랑', 3, '레몬']]
def fruit_counts(data):
    counts = {}
    for row in data:
        label = row[-1]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts
result = fruit_counts(training_data)
print(result)


# In[ ]:




