#!/usr/bin/env python
# coding: utf-8

# # 6.3 생성자

# In[1]:


#p115
class You:
    def __init__(self, n, a) :
        self.name = n
        self.age = a
    def show(self) :
        print('이름:', self.name, '나이:', self.age)
my = You('준서', 21)    # 객체가 생성될 때 __init__() 생성자 자동실행!
my.show()


# In[ ]:





# In[ ]:




