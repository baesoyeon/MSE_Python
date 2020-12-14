#!/usr/bin/env python
# coding: utf-8

# In[ ]:


종목 = []

삼성전자 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)

종목.append(삼성전자)
종목.append(현대차)
종목.append(LG전자)

for i in 종목:
    print(i.code, i.per)        # i-> Stock 클래스의 객체를 바인딩하기 때문
#Stock함수를 이용하여 3 종목에 대한 객체를 생성한다.
#append함수를 이용하여 종목 list에 삼성전자, 현대차, LG전자를 추가한다.
#i가 Stock 클래스의 객체를 바인딩하기 때문에 i에서 코드와 PER을 불러온다.

