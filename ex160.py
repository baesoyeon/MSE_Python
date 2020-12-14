#!/usr/bin/env python
# coding: utf-8

# In[1]:


리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트:
  split = 변수.split(".")
  if (split[1] == "h") or (split[1] == "c"):
    print(변수)
#split함수는 인자 안의 값으로 구분하여 문자열을 나누어 준다. 
#논리연산자 or : x or y == x와 y 둘 중에 하나만 참이면 참이다
#split 함수를 이용해 .을 구분점으로 문자열을 나눠주고 or연산자를 이용해 h 혹은 c일 경우 변수를 출력하도록 설계했다.

