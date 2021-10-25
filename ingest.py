import json
import requests
import configparser

config = configparser.ConfigParser()
config.read('config.env')

API_KEY = config.get('CONFIG','API_KEY')


#Get basic Stock info
def get_stock_info(ticker,api):
	url = "https://api.twelvedata.com/profile?symbol=" + ticker + "&apikey=" + api
	response = requests.get(url).json()
	print(json.dumps(response,sort_keys = True, indent =4))


def get_stock_current_price(ticker,api):
	url = "https://api.twelvedata.com/price?symbol=" + ticker + "&apikey=" + api
	response = requests.get(url).json()
	print(response)


#main
get_stock_info("AAPL", API_KEY)
get_stock_current_price("AAPL",API_KEY)

