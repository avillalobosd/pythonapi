from flask import Flask, jsonify, request
import requests
import json
from flask_cors import CORS



app = Flask(__name__)
CORS(app)


@app.route('/coinapi')
def getCoin():
    # url = 'https://rest.coinapi.io/v1/exchanges'
    url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD?time=2020-05-19T12:00:01.0000000Z'
    headers = {'X-CoinAPI-Key' : '39F7513A-39B9-416C-BD6B-DEADFAC894E7'}
    response = requests.get(url, headers=headers)
    content= response.content
    decoded = content.decode('utf8')
    loads = jsonify(json.loads(content))
    # tojson= json.dumps(decoded)
    print (loads)
    return  loads



if __name__ == '__main__':
    app.run(debug=True, port=4000)