#!/usr/bin/env python
# coding: utf-8

# In[2]:


def print_max(a, b, c) :
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    else:
        print(c)
# 논리연산자 and는 두 값 모두 True여야 True다. 
# a>b와 a>c가 모두 True일 때 a값이 출력된다.
# 그렇지 않다면 b>a와 b>c가 모두 True일 때 b값이 출력된다.
# 그렇지 않다면 c값이 출력된다.

