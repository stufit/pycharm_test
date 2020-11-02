#!/usr/bin/env python
# coding: utf-8

# # 3.1 조건문
# ## 단일 if문
# ### 단일 if 구문 형식

# In[1]:


#p36
grade = 82
if (grade >= 80):
    print('합격입니다.\n')


# ### 단일 if-else 구문 형식

# In[2]:


#p37
age = 20
if (age >= 19):
    print('당신은 성인입니다.\n')
else :
    print('당신은 미성년자입니다.\n')


# In[3]:


age = 18
if (age >= 19):
    print('당신은 성인입니다.')
    print(age-19, '살 넘음.')
else :
    print('당신은 미성년자입니다.')
    print(19-age, '살이 부족함.')


# ## 중첩 if문

# In[4]:


#p38
num = -1
if (num > 0):
    print('양수!\n')
elif (num < 0):
    print('음수\n')
else :
    print('0\n')


# In[ ]:




