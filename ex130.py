#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")
#실수의 사칙연산을 할 수 있게 하기 위해 float을 사용한다.
#비교연산자 > (x > y : x가 y보다 크다)를 사용해 만약 참이면 if문이 실행되고 아니면 else문이 실행되게 만들었다.

