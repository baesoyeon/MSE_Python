#!/usr/bin/env python
# coding: utf-8

# In[3]:


ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
total_profit = 0
for day_price in ohlc[1:]:
    profit = day_price[0] - day_price[3]
    total_profit += profit

print(total_profit)
#각 거래일의 수익금 = 시가 - 종가이다.
#[1:]은 1부터 끝까지라는 뜻으로 1일차부터 마지막차까지 for문을 돌린다는 뜻이다.
#total_profit += profit 은 total_profit = total_profit + profit을 간단히 나타낸 것이다.
#total_profit에 profit을 누적시켜 총 수익금을 구한다.


# In[ ]:




