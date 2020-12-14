#!/usr/bin/env python
# coding: utf-8

# In[1]:


if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")
#참이면 if문, 거짓이면 else문이 수행된다. 조건이 참이기 때문에 if문이 수행된다. 
#if문 안에 또 다른 if-else문이 있는데 참이므로 if문이 수행되지 않고 else문이 수행된다.
#남은 문장 print("5")가 출력된다.
#if문에 속하는 모든 문장은 들여쓰기 한다.(공백 4개 또는 탭) 조건문 다음엔 :

