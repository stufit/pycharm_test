#!/usr/bin/env python
# coding: utf-8

# # 2.3 입출력 함수
# ## 출력함수
# ### 다양한 데이터형 출력
# #### 문자열 출력

# In[1]:


#p21
print('안녕하세요!')


# #### 정수형, 실수형 부울형 데이터값 출력

# In[2]:


print(3)


# In[3]:


print(3.5)


# In[4]:


print(True)


# In[5]:


print(3+5)


# #### 변수에 저장된 내용 출력

# In[6]:


#p22
a = 3
b = 3.5
c = True
print(a)
print(b)
print(c)


# In[7]:


a = 3
b = 3.5
print(a+b)


# In[8]:


#p23
print(3.5)


# In[9]:


two = 0b11    # 2진수는 0b를 사용! [영(0)과 binary를 나타내는 b]
print(two)


# In[10]:


eight = 0o11    # 8진수는 0o를 사용! [영(0)과 octet를 나타내는 o]
print(eight)


# In[11]:


a = 0x11    # 16진수는 0x를 사용! [영(0)과 hex를 나타내는 x]
print(a)


# ### 다수의 데이터형 출력

# In[12]:


age = 21
print('나이: ', age)


# In[13]:


name = '홍길동'
print('나는', name, '입니다.')


# In[14]:


#p24
a = 3
b = 3.5
print(a, '*', b, '=', a*b)


# ### C언어 유사 형태 출력 형식

# In[15]:


#p25
print("%d" % 3)


# In[16]:


print("%f" % 3.5)


# In[17]:


a = 3
b = 3.5
print("%d" % a)
print("%f" % b)


# ## 입력 함수

# ### 문자열형 데이터값 입력

# In[18]:


#p26
name = input()


# In[19]:


#p26
print(name)


# In[20]:


name = input('이름: ')


# In[21]:


print(name)


# ### 정수형 데이터값 입력

# In[22]:


age = input('나이 : ')


# In[23]:


print(age)


# In[24]:


age = input('나이 : ')


# In[25]:


after = input('몇 년 후? ')


# In[26]:


print(age + after)


# In[27]:


#p27
age = input('나이 : ')


# In[28]:


after = input('몇 년 후? ')


# In[29]:


print(int(age) + int(after))


# In[30]:


print('나이: ' + 21)


# In[31]:


print('나이: ' + str(21))


# In[32]:


#p29
age = input('나이 : ')


# In[33]:


print(int(age) + 10)


# In[34]:


old = age + 10


# In[35]:


print(old)


# In[36]:


type(age)


# In[37]:


age = int(age)
type(age)


# ### 실수형 데이터값 입력

# In[38]:


#p30
height = input('키 : ')


# In[39]:


print(height)


# In[40]:


type(height)


# In[41]:


height = input('키 : ')


# In[42]:


print(float(height) + 1.5, 'cm')


# In[43]:


#p31
num = 5.5
print(int(num))


# In[44]:


a = '5'
print(int(a))


# In[45]:


b = '5.5'
print(int(b))


# ### 부울형 데이터값 입력

# In[46]:


#p32
a = input('참(True)/거짓(False): ')


# In[47]:


a


# In[48]:


type(a)


# In[49]:


a = input('참(True)/거짓(False): ')


# In[50]:


print(bool(a))


# In[51]:


#p33
a = input('참(1)/거짓(0): ')


# In[52]:


a = int(a)
print(bool(a))


# ## [참고]

# In[53]:


input('당신은 성인입니까?\n')


# In[ ]:




