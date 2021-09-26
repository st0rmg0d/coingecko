import requests

headers = {
    "accept" : "application/json"
}

params = {
    'convert' : 'USD'
}

url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=9400&page=1&sparkline=false'

json = requests.get(url, params=params, headers=headers).json()

coins = json

print("\n Cryptocurrency by Market Cap: \n")


for x in coins:
    print(x['market_cap_rank'], x['name'], "$", x['market_cap'])


