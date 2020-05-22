import requests
from flask import Flask, request
import jsonify

url = 'https://rest.coinapi.io/v1/exchanges'
# url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
headers = {'X-CoinAPI-Key' : '39F7513A-39B9-416C-BD6B-DEADFAC894E7'}
response = requests.get(url, headers=headers)

print(response.content)
# print jsonify({'products': response.content})
