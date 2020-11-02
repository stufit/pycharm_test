#!/usr/bin/env python
# coding: utf-8

# # 6.2 클래스로 객체 만들기

# In[1]:


#p114
# 클래스 선언
class You:
    name = ''      # 멤버변수(속성) 정의
    def setname(self, n):
        self.name = n
    def show(self):
        print('이름:', self.name)

# main 부분
my = You()         # 클래스 You로 객체 my를 생성!
my.setname('준서')
my.show()


# In[2]:


class You:
    def setname(self, n):
        self.name = n
    def show(self):
        print('이름:', self.name)
my = You()
my.setname('준서')
my.show()


# In[ ]:




