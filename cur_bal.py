import pyupbit
import time
import json

with open('api key.json') as json_file:
    api = json.load(json_file)

upbit = pyupbit.Upbit(api['Access'], api['Secret'])

LUNA = pyupbit.get_current_price(
    "KRW-BTC")*pyupbit.get_current_price("BTC-LUNA")*upbit.get_balance("BTC-LUNA")
XEM = pyupbit.get_current_price("KRW-XEM")*upbit.get_balance("KRW-XEM")

lunabuy = 997975
xembuy = 49001
xempercent = ((XEM-xembuy)/xembuy)*100
lunapercent = ((LUNA - lunabuy)/lunabuy)*100


print("XEM : %.2f / %.2f / %.2f" % (XEM, xempercent, XEM-xembuy))
print("LUNA : %.2f / %.2f / %.2f\n" % (LUNA, lunapercent, LUNA-lunabuy))


df = pyupbit.get_ohlcv("KRW-BTC")
ma5 = df['close'].rolling(window=5).mean()
last_ma5 = ma5[-2]

price = pyupbit.get_current_price("KRW-BTC")

if price > last_ma5:
    print("BTC Bull Market")
else:
    print("BTC Bearish Market")
