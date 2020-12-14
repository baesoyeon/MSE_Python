#!/usr/bin/env python
# coding: utf-8

# In[1]:


class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()
#super를 통해 부모 class에 접근해 생산자를 호출할 수 있다.

