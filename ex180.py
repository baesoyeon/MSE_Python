#!/usr/bin/env python
# coding: utf-8

# In[2]:


low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(len(low_prices)) :
    volatility.append(high_prices[i] - low_prices[i])  
print(volatility)
#range함수를 통해 low_price의 길이 만큼 0-4의 숫자를 뽑아내고 append 메서드를 통해 원소를 추가해 결과를 출력한다
#append메서드는 원소를 추가하는 메서드이다.

