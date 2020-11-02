#!/usr/bin/env python
# coding: utf-8

# # 5.2 배열의 종류
# ## 리스트

# In[1]:


#p77
price = [1020, 870, 3160, 2650]
fruits = ['사과', '오렌지', '포도', '복숭아']
print(price)
print(fruits)


# In[2]:


#p78
price = [1020, 870, 3160, 2650]
fruits = ['사과', '오렌지', '포도', '복숭아']
print(price[1])
print(fruits[-1])


# In[3]:


fruits = ['사과', '오렌지', '사과', '복숭아']
fruitstag = ['사과', 1020, '오렌지', 870, '복숭아', 2650]


# In[4]:


a = [3, 5, 7]
b = a
b[0] = b[0] - 2
print('a=', a, 'b=', b)


# ### 슬라이싱

# In[5]:


#p79
price = [1020, 870, 3160, 365, 731]
print(price[0:2])
print(price[0:4:2])
print(price[1::2])


# ### 리스트에서의 병합 및 삽입
# #### 복수 개 변수의 병합

# In[6]:


#p80
x = 12.23
y = 23.34
packing = [x, y]          # packing!
type(packing)
print('Packing:', packing)
[c1, c2] = packing        # unpacking!
print('Unpacking:\nc1:', c1)
print('c2:', c2)


# #### 복수 개 리스트의 병합

# In[7]:


#p81
fruits1 = ['사과', '오렌지', '포도']
fruits2 = ['복숭아', '키위']
allfruits = fruits1 + fruits2
print(allfruits)


# #### 리스트에 원소 삽입
# ##### append() 메소드

# In[8]:


prime = [2, 3, 5]
prime.append(7)
print(prime)


# In[9]:


#p82
a = list()            # list()는 빈 리스트 생성, a = []와 동일
for i in range(5):
    a.append(i)
    print(a[i])


# In[10]:


fruits = ['사과', '귤', '포도']
fruits.append('수박')
print(fruits)


# ##### insert() 메소드

# In[11]:


#p83
fruits = ['사과', '오렌지', '포도']
fruits.insert(1, '키위')
print(fruits)


# ##### 리스트의 함축

# In[12]:


#p84
mylist = [3, 5, 4, 9, 1, 8, 2, 1]
newlist = [i for i in mylist if (i%2)==0]
print(newlist)


# ### 리스트의 항목 삭제
# #### del 명령문으로 삭제

# In[13]:


#p85
nums = [0, 1, 2, 3, 4, 5]
del nums[1]
print(nums)


# In[14]:


nums = [0, 1, 2, 3, 4, 5]
del nums[1:5]
print(nums)


# #### pop() 함수로 삭제

# In[15]:


#p86
nums = [1, 3, 5, 7, 9]
nums.pop()         # 9가 삭제되어 [1, 3, 5, 7]로 변경됨
nums.pop()         # 7이 삭제되어 [1, 3, 5]로 변경됨
print(nums)        # 결과를 출력


# In[16]:


nums = [1, 3, 5, 7, 9]
nums.pop(2)
print(nums)


# #### 빈 리스트로 삭제

# In[17]:


nums = [0, 1, 2, 3, 4, 5]
nums[1:2] = []
print(nums)


# ### 존재여부

# In[18]:


word = 'orange'
print('r' in word)


# In[19]:


#p87
fruits = ['사과', '오렌지', '포도']
print('포도' not in fruits)


# ### 원소의 반복

# In[20]:


a = [1, 2, 3]
b = a * 2
print(b)


# In[21]:


a = [1, 2, 3]
for i in a:
    print(i * 2)


# ### 원소의 개수 측정

# In[22]:


#p88
fruits = ['사과', '오렌지', '포도']
print(len(fruits))


# ### 검색 기능
# #### 빈도수 검사

# In[23]:


nums = [5, 7, 1, 3, 5, 7, 1, 3, 3, 5, 7, 9]
print(nums.count(5))


# #### 인덱스번호 찾기

# In[24]:


#p89
nums = [1, 2, 3, 4, 5, 3]
print(nums.index(3))


# ### 정렬

# In[25]:


nums = [3, 5, 2, 1, 5, 3]
nums.sort()
print(nums)


# In[26]:


fruits = ['사과', '오렌지', '포도', '복숭아']
fruits.reverse()
print(fruits)


# ### 2차원 리스트

# In[27]:


fruits = ['apple', 'orange', 'grape', 'orange']
fruitdb = [['apple', 1020], ['orange', 880], ['grape', 3160]]


# In[28]:


#p90
fruitdb = [['사과', 1020], ['오렌지', 880], ['포도', 3160]]
print(fruitdb[1])
print(fruitdb[1][0])


# In[29]:


record = [
    [1, 2, 3],
    [10, 20, 30],
    [100, 200, 300]]
index = [ary[1] for ary in record]
print(index)


# In[30]:


mylist = [[1, 2], [3, 4, 5], [6, 7]]
newlist = [x for x in mylist if len(x)==2]
print(newlist)


# In[31]:


#p92
def times2(a):
    a = a * 2
    print(a)
nums = [1, 2, 3]
times2(nums)


# In[ ]:




