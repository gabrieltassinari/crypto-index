from flask import Flask, render_template
from datetime import datetime

import matplotlib.pyplot as plt
import requests

app = Flask(__name__)

@app.route('/')
def get_coin():
    coin_list = requests.get(
        'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd').json()

    return render_template('main.html', coin=coin_list)

@app.route('/coin/<crypto>')
def info_coin(crypto):
    
    coin = requests.get(
        f'https://api.coingecko.com/api/v3/coins/{crypto}/market_chart?vs_currency=usd&days=30&interval=daily').json()
    
    coin_date = []
    coin_price = []

    for i in range(len(coin['prices'])):

        dt = datetime.fromtimestamp(coin['prices'][i][0] / 1000)
        formated = dt.strftime('%d-%m')

        coin_date.append(formated)
        coin_price.append(coin['prices'][i][1])

    x = coin_date
    y = coin_price
    
    plt.plot(x, y, label='Price')
    plt.xticks(x[::2], rotation=45)
    plt.legend()

    plt.savefig('static/new_plot.png')
    plt.clf()

    return render_template('coin.html', crypto=crypto, coin_date=coin_date, coin_price=coin_price)

if __name__ == "__main__":
    app.run()
