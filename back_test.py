import pyupbit
import time
import datetime
import numpy as np
import json

with open('api_key.json') as json_file:
    api = json.load(json_file)

upbit = pyupbit.Upbit(api['Access'], api['Secret'])

year = ' count 15'
coin = 'BTC'

df = pyupbit.get_ohlcv("KRW-"+coin, count=15)
#df = df.loc[year]
df['range'] = (df['high'] - df['low']) * 0.5
df['range_shift'] = df['range'].shift(1)
df['target'] = df['open'] + df['range'].shift(1)
df['ror'] = np.where(df['high'] > df['target'], df['close'] / df['target'], 1)
df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr'])/df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())

df.to_excel("C:\\Users\\user\\Naver MYBOX\\21-s\\bitcoin\\test_excels\\" +
            "trade"+year+"_"+coin+".xlsx")
