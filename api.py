from flask import Flask, request, jsonify
from  main import currencyconverter 
from flask import request
app = Flask(__name__)
app.config["DEBUG"] = True
converter=currencyconverter()
@app.route('/', methods=['GET'])
def home():
	json=converter.rates()
	return jsonify(json)
@app.route('/chart', methods=['GET'])
def chart():
	args = request.args
	From = args['From']
	To = args['To']
	json=converter.chart(From,To)
	return jsonify(json)
@app.route('/statistics', methods=['GET'])
def statistic():
	args = request.args
	From = args['From']
	To = args['To']
	json=converter.statistics(From,To)
	return jsonify(json)	
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3003)