#!/usr/bin/env python
# coding: utf-8

# In[1]:


def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) : #0,1,2
        message2()
        print("C")
    message1()

message3()
#def는 함수를 정의할 때 사용하는 예약어이다. def함수이름(매개변수)
#i=0일 때 message2를 호출하고 C를 출력한다. i가 1,2일 때도 이것이 반복되고 for문이 종료된다.
#message1이 호출되면 A가 출력된다.

