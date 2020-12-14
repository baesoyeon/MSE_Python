#!/usr/bin/env python
# coding: utf-8

# In[1]:


string = 'abcd'
string.replace('b', 'B')
print(string)
#문자열은 변경 불가능한 자료형이기 때문에 replace를 사용하면 원본은 그대로이다.
#대신 새로운 문자열 객체를 리턴해준다.

