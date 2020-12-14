#!/usr/bin/env python
# coding: utf-8

# In[3]:


date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
print(dict(zip(date, close_price)))
#zip함수는 동일한 개수로 이루어진 자료형을 묶어준다. date list와 close_price list를 묶어주고 dict함수에 넣어주어 프린트한다.

