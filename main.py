import requests
import json
#from fake_useragent import UserAgent

class currencyconverter:
	def __init__(self):
		#self.ua = UserAgent()
		pass
	def rates(self):
		headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
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
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
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
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
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