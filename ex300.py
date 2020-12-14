#!/usr/bin/env python
# coding: utf-8

# In[1]:


per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print("clean data")
    finally:
        print("변환 완료")
#try는 실행코드이다.
#except는 예외가 있을 경우 수행할 코드이다.
#else는 예외가 없을 경우 수행할 코드이다.
#finally는 예외와 상관없이 항상 수행할 코드이다.
#먼저 try를 실행하면 "10.31"과 "8.00"은 float이므로 그대로 출력한다.
#예외가 없기 때문에 else 코드가 실행되어 clean data를 출력한다.
#""은 실수 변환이 안되는 예외이므로 except가 실행되어 0을 출력한다.
#예외와 상관없는 finally 코드가 실행되어 변환완료를 출력한다.

