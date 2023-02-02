from flask import Flask, render_template
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
    f'https://api.coingecko.com/api/v3/coins/{crypto}').json()

    return coin

if __name__ == "__main__":
    app.run()
