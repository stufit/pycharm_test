#!/usr/bin/env python
# coding: utf-8

# # 5.1 문자열

# In[1]:


#p65
print("hello")         # 'hello'를 출력!
print('hello')         # 'hello'를 출력!


# In[2]:


print('My friend's house.')


# In[3]:


print("My friend's house.")


# In[4]:


print("그녀가 말했다. "안녕!".")


# In[5]:


print('그녀가 말했다. "안녕!".')


# ## 문자열 읽어오기

# In[6]:


#p66
animal = 'frog'
print(animal[3])


# In[7]:


animal = 'frog'
print(animal[-2])


# In[8]:


#p67
animal = '진돗개'
print(animal[0])
print(animal[-2])


# ### [TIP] 문자열 슬라이싱

# In[9]:


#p68
animal = 'frog'
print(animal[1])


# In[10]:


animal = 'frog'
print(animal[1:3])


# In[11]:


animal = 'frog'
print(animal[0:3:2])


# In[12]:


#p69
animal = 'frog'
print(animal[:])
print(animal[1:])
print(animal[:2])


# In[13]:


animal = 'elephant'
print(animal[::2])
print(animal[::-2])


# ## 문자열의 병합

# In[14]:


#p71
dog = '개'
animal = '진돗' + dog
print(animal)


# ## 문자열 함수(메소드)

# In[15]:


animal = 'elephant'
print(len(animal))


# ### 정보 수집

# In[16]:


#p72
animal = 'elephant'
print('총 개수:', animal.count('e'))


# In[17]:


animal = 'elephant'
print('앞쪽 찾기:', animal.find('e'))
print('ep 찾기:', animal.find('ep'))
print('뒤쪽 찾기:', animal.rfind('e'))
print('위치:', animal.index('e'))
print('el 시작:', animal.startswith('el'))


# In[18]:


animal = 'elephant'
print('n이 있다.:', 'n' in animal)
print('an이 있다.:', 'an' in animal)
print('an이 없다.:', 'an' not in animal)


# ### 정보 수정

# In[19]:


#p73
ai = 'python program'
print('선택수정:', ai.replace('p', 'P'))
print('소문자:', ai.lower())
print('대문자:', ai.upper())
print('swap대소문자:', ai.swapcase())
print('첫문자만 대문자:', ai.capitalize())


# In[20]:


animal = 'Elephant'
animal = animal.upper()
print(animal)


# ### 정보 분할

# In[21]:


animal = ' elephant '
print('왼쪽 벗겨내기:', animal.lstrip())
print('오른쪽 벗겨내기:', animal.rstrip())
print('좌우 벗겨내기:', animal.strip())


# ## [TIP] Random 모듈

# In[22]:


#p74
import random
random.random()


# In[23]:


import random
print(random.randrange(1, 6))


# In[24]:


import random
chars = '한글우수'
print(random.choice(chars))


# In[25]:


#p75
import random
chars = ['한', '글', '우', '수']
print(random.choice(chars))


# In[26]:


import random
chars = ['한', '글', '우', '수']
random.shuffle(chars)
print(chars)


# In[ ]:




