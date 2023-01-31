from flask import Flask, render_template
import requests

app = Flask(__name__)

coins = requests.get(
    'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd').json()

@app.route('/')
def get_coin():
    return render_template('main.html', coin=coins)

app.run()
