#!/usr/bin/env python
# coding: utf-8

# In[ ]:


fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("좋아하는 과일은?")
if user in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")
#입력하는 value(과일)이 fruit 리스트에 있으면 if문이 실행되어 "정답입니다"가, 없으면 else문이 실행되어 "오답입니다"가 출력된다.
#기타연산자 in : x in 리스트/튜플/문자열에서 리스트/튜플/문자열에 x가 있으면 참이다.

