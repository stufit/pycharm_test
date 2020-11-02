#!/usr/bin/env python
# coding: utf-8

# # 5.2 배열의 종류
# ## 튜플

# In[1]:


#p94
empty = ()         # 빈 튜플을 생성! 또는 empty = tuple()
animals = ('토끼', '사자', '원숭이')
fruits = '사과', '오렌지', 1020, 880
start = '하나', '둘'
print(fruits)


# In[2]:


#p95
print(fruits[1])     # 인덱싱 가능
print(fruits[1:3])   # 슬라이싱 가능


# In[3]:


fruits[1] = '키위'


# In[4]:


animals = ('토끼', '사자', '원숭이')
fruits = '사과', '오렌지', 1020, 88,
things = animals, fruits
print(things)


# In[5]:


#p96
fruits = (['포도', '망고'], ['사과', '키위'])
print(fruits[1])


# In[6]:


fruits = (['포도', '망고'], ['사과', '키위'])
newfruits = ['수박', '참외']
fruits[1] = newfruits


# In[7]:


fruits = [('포도', '망고'), ('사과', '키위')]
fruits[0] = ('수박', '참외')
print(fruits)


# In[8]:


fruits = (['포도', '망고'], ['사과', '키위'])
fruits[1][0] = '수박'
print(fruits)


# ### 리스트와 비교한 튜플의 기능들
# #### 슬라이싱

# In[9]:


#p97
dice = (3, 2, 5, 3, 4)
dice[2:4]


# #### 병합

# In[10]:


x = 12.23
y = 23.34
packing = (x, y)      # packing!
type(packing)
print('packing:', packing)
(c1, c2) = packing    # unpacking!
print('c1:', c1)
print('c2:', c2)


# In[11]:


dice1 = (3, 2, 5, 3, 4)
dice2 = (6, 1, 4, 2, 3)
dice3 = (dice1 + dice2)
print(dice3)


# #### 존재여부

# In[12]:


#p98
dice = (3, 2, 5, 3, 4)
print(2 in dice)
print(2 not in dice)


# #### 반복

# In[13]:


a = (1, 2, 3)
b = a * 2
print(b)


# #### 원소의 개수 측정

# In[14]:


dice = (1, 2, 3)
print(len(dice))


# #### 검색 기능
# ##### 빈도수 검사

# In[15]:


#p99
dice = (5, 3, 1, 2, 3, 6)
print(dice.count(3))


# ##### 인덱스번호 찾기

# In[16]:


dice = (5, 3, 1, 2, 3, 6)
print(dice.index(3))


# ### 2차원 튜플

# In[17]:


dice1 = (6, 1, 4)
dice2 = (5, 2, 1)
result = (dice1, dice2)
print(result)
print(result[1][1])


# #### [참고] 튜플 포매팅

# In[18]:


#p100
name = '홍길동'
age = 21
height = 172.5
print('이름: {} 나이: {} 키: {}'.format(name, age, height))


# In[19]:


print('이름: {0:3s} 나이:{1:3} 키:{2:6.1f}'.format(name, age, height))


# ### 요약 문제

# In[20]:


#p101
import turtle
import random
for i in range(10):
    for j in range(5):
        col = random.randint(0, 4)
        coltype = ('yellow', 'blue', 'red', 'purple', 'green')
        col = random.randint(0, 4)
        turtle.color(coltype[col])
        sel = random.randint(0, 4)
        if (0 == sel):
            turtle.forward(random.randint(50, 100))
        elif (1 == sel):
            turtle.right(random.randint(90, 360))
        elif (2 == sel):
            turtle.begin_fill()
            turtle.circle(random.randint(-100, -20))
            turtle.end_fill()
        elif (3 == sel):
            turtle.forward(random.randint(30, 50))
        elif (4 == sel):
            turtle.circle(random.randint(20, 100))
    a = float(random.randint(-300, 300))
    b = float(random.randint(-300, 300))
    turtle.goto(a, b)


# In[ ]:




