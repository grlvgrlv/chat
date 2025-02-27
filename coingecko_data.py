import requests
import pandas as pd
from utils import save_with_history

def fetch_coingecko_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {'vs_currency': 'usd', 'order': 'market_cap_desc', 'per_page': 100, 'page': 1, 'sparkline': 'false'}
    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data, columns=['id', 'symbol', 'name', 'current_price', 'market_cap', 'total_volume'])
    save_with_history(df, 'coingecko_prices.csv')

if __name__ == "__main__":
    fetch_coingecko_data()
