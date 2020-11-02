#!/usr/bin/env python
# coding: utf-8

# # 6.6 빈도수

# In[1]:


#p120
text = "AI! 나는 인공지능 로봇 입니다. 나는 'AI 로봇' 입니다."
def max_counts(text):
    counts = {}
    for i in text.split(' '):
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts
max_counts(text)


# In[2]:


#p121
people = ['홍', '이', '김', '이', '이', '김']
def max_count(people):
    counts = {}
    for i in people:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts
counts = max_count(people)
print(counts)


# In[3]:


#p122
max(counts)


# In[4]:


max(counts, key=counts.get)


# In[5]:


#p124
nums = [1, 1, 1, 2, 2, 3, 2, 3, 3, 3, 1]
def max_counts(nums):
    counts = {}
    for i in nums:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts
counts = max_counts(nums)
first = []
max_num = max(counts.values())
first = []
max_num = max(counts.values())
for name, count in counts.items():
    print(name, ':', count,'번')
    if count == max_num:
        first.append(name)
print('1등:', first)


# In[6]:


people = ['홍', '홍', '김', '이', '홍', '김']
import scipy.stats as ss
mode, count = ss.mstats.mode(people)
print(mode, count)


# In[7]:


#p125
nums = [1, 1, 1, 2, 2, 3, 2, 3, 3, 3, 3, 1]
import scipy.stats as ss
mode, count = ss.mstats.mode(nums)
print(mode, count)


# In[ ]:




