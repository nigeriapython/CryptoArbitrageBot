# import requests

# url = "https://coingecko.p.rapidapi.com/simple/supported_vs_currencies"

# headers = {
# 	"X-RapidAPI-Key": "a799389df0msh028b3b04e376424p1955dajsn86808412f2e0",
# 	"X-RapidAPI-Host": "coingecko.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers)

# print(response.text)


# c_lists=["btc","eth","ltc","bch","bnb","eos","xrp","xlm","link","dot","yfi","usd","aed","ars","aud","bdt","bhd","bmd","brl","cad","chf","clp","cny","czk","dkk","eur","gbp","hkd","huf","idr","ils","inr","jpy","krw","kwd","lkr","mmk","mxn","myr","ngn","nok","nzd","php","pkr","pln","rub","sar","sek","sgd","thb","try","twd","uah","vef","vnd","zar","xdr","xag","xau","bits","sats"]

# print(count(c_lists))


import requests
import time

url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
headers = {'X-CoinAPI-Key' : '73034021-THIS-IS-SAMPLE-KEY'}
response = requests.get(url, headers=headers)


for x in range(3):
	print(response.text)
	time.sleep(2)



