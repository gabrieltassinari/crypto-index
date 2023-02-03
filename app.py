from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def get_coin():
    coin_list = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd').json()

    return render_template('main.html', coin=coin_list)

@app.route('/coin/<crypto>')
def info_coin(crypto):

    now = int(datetime.now().timestamp())

    coin = requests.get(
    f'https://api.coingecko.com/api/v3/coins/{crypto}').json()

    price = requests.get(
        f'https://api.coingecko.com/api/v3/coins/{crypto}/market_chart/range?vs_currency=usd&from={now - 604800}&to={now}').json()

    return render_template('coin.html', coin=coin, price=price)

@app.template_filter('ctime')
def convert_time(t):
    return datetime.fromtimestamp(t / 1000)


if __name__ == "__main__":
    app.run()
