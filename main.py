import requests
import json
from user_agent import generate_user_agent, generate_navigator
class currencyconverter:
	def __init__(self):
		pass
	def rates(self):
		headers = {
		'User-Agent': str(generate_user_agent()),
		'Accept': '*/*',
		'Accept-Language': 'tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3',
		'Referer': 'https://www.xe.com/',
		'authorization': 'Basic bG9kZXN0YXI6QlQ4bUdGYmtPSjJnQ0p5TmlFeVd4Z2NEZlBTVHYyTEc=',
		'Connection': 'keep-alive',
		}

		response = requests.get('https://www.xe.com/api/protected/midmarket-converter/', headers=headers).text
		print(response,flush=True)
		jsonData=json.loads(response)
		print(jsonData,flush=True)
		return jsonData
	def chart(self,From,To):
		#agent=ua.random
		headers = {
			'sec-ch-ua': '^\\^',
			'User-Agent': str(generate_user_agent()),
			'Referer': 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=EUR',
			'sec-ch-ua-mobile': '?0',
			'authorization': 'Basic bG9kZXN0YXI6QlQ4bUdGYmtPSjJnQ0p5TmlFeVd4Z2NEZlBTVHYyTEc=',
		}
		
		params = (
			('fromCurrency', From),
			('toCurrency', To),
		)
		
		response = requests.get('https://www.xe.com/api/protected/charting-rates/', headers=headers, params=params).text
		jsonData=json.loads(response)
		print(jsonData,flush=True)
		return jsonData
	def statistics(self,From,To):
		headers = {
			'sec-ch-ua': '^\\^',
			'User-Agent': str(generate_user_agent()),
			'Referer': 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=EUR',
			'sec-ch-ua-mobile': '?0',
			'authorization': 'Basic bG9kZXN0YXI6QlQ4bUdGYmtPSjJnQ0p5TmlFeVd4Z2NEZlBTVHYyTEc=',
		}
		params = (
			('from', From),
			('to', To),
		)
		response = requests.get('https://www.xe.com/api/protected/statistics/', headers=headers, params=params).text
		jsonData=json.loads(response)
		print(jsonData,flush=True)
		return jsonData