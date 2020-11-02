#!/usr/bin/env python
# coding: utf-8

# # 5.2 배열의 종류
# ## 사전
# ### 사전의 생성 및 삽입

# In[1]:


#p102
student = {}         # 빈 사전을 생성함. 또는 student = dict()
student['지훈'] = 1234
print(student)


# In[2]:


student = { }
student['지훈'] = 1234
student['수민'] = 2345
print(student)


# In[3]:


#p103
fruitdb = {'사과':1020, '오렌지':880, '포도':3160}
print(fruitdb)


# In[4]:


fruitdb = {'사과':1020, '오렌지':880, '포도':3160}
print(fruitdb[1])


# In[5]:


print(fruitdb[1:2])


# ### 사전 항목 삭제

# In[6]:


#p104
fruitdb = {'사과':1020, '오렌지':880, '포도':3160}
del fruitdb['사과']
print(fruitdb)


# ### 사전 항목 검색

# In[7]:


student = {'현준': 1234, '민지': 2345}
print('SeJong' in student)
print(student.get('현준'))
print(student.get('민지'))
print(student.keys())
print(student.values())
print(student.items())


# ### 사전 병합

# In[8]:


#p105
student = {'현준': 1234, '민지': 2345}
newstd = {'승민': 3456, '유진': 4567}
student.update(newstd)
print(student)


# ### 다른 배열로 사전만들기

# In[9]:


student = dict([['현준', 1234], ['민지', 2345]])
print(student)
student = dict([('현준', 1234), ('민지', 2345)])
print(student)
student = dict((('현준', 1234), ('민지', 2345)))
print(student)


# In[10]:


student = dict(현준=1234, 민지=2345)
print(student)


# ### [참고] 사전 포매팅

# In[11]:


person = {'name':'준혁', 'age':21, 'height':172.5}
print('이름:{0[name]}, 나이:{0[age]}, 키:{0[height]}'.format(person))


# In[ ]:




