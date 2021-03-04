'''
(int) start - return results from rank [start] and above (default is 1)
(int) limit - return a maximum of [limit] results (default is 100; max is 100)
(string) convert - return pricing info in terms of another currency. Valid fiat
currency values are: "AUD", "BRL", "CAD", "CHF", "CLP", "CNY", "CZK", "DKK", "EUR",
"GBP", "HKD", "HUF", "IDR", "ILS", "INR", "JPY", "KRW", "MXN", "MYR", "NOK", "NZD", 
"PHP", "PKR", "PLN", "RUB", "SEK", "SGD", "THB", "TRY", "TWD", "ZAR" 
Valid cryptocurrency values are: "BTC", "ETH" "XRP", "LTC", and "BCH"
'''

from coinmarketcap import Market

coinmarketcap = Market()

all_coin_list = coinmarketcap.listings()

coin_data = coinmarketcap.ticker(start=0, limit=200, convert='INR')

print(coin_data)