#!/usr/bin/env python
# coding: utf-8

# In[1]:


def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)
#return을 사용하면 값을 함수 바깥으로 반환한다.
#함수2를 호출해 num에 지정된 값 2를 넣어주면 num = 2 + 10 이므로 num = 12가 된다.
#return으로 num = 12를 함수 바깥으로 반환하고 함수1을 호출해 num + 2를 하면 14가 된다.
#return으로 num = 14를 함수 바깥으로 반환하고 함수0을 호출해 num = 14일 때 num * 2를 하면 28이 된다.

