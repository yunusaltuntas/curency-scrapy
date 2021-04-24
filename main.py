from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
class currencyconverter:
	def __init__(self):
		chrome_options = Options()
		chrome_options.add_argument('--headless')
		chrome_options.add_argument("start-maximized")
		chrome_options.add_argument("disable-infobars")
		chrome_options.add_argument("--disable-extensions")
		chrome_options.add_argument("--disable-gpu")
		chrome_options.add_argument("--disable-dev-shm-usage")
		chrome_options.add_argument("--no-sandbox")
		self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver',options=chrome_options)
	def convert(self,From,To,Amount="1"):
		self.driver.get("https://www.xe.com/currencyconverter/convert/?Amount="+Amount+"&From="+From+"&To="+To)
		r=self.driver.page_source
		elms=bs(r,'lxml')
		text=str(elms.findAll('p',attrs={'class':'sc-AxjAm ConvertedSubText-fcQdYJ efOulh'}))
		starting=0
		for i in range(0,len(text)):
			if text[i]==">":
				starting=i
			elif text[i]=="<" and starting!=0:
				b=text[starting+1:i]
				break
		return b
if __name__=="__main__":
	converter=currencyconverter()
	Amount="1"
	From="USD"
	To="GBP"
	print(converter.convert(From,To,Amount))
