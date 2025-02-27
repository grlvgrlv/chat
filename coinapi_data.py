import requests
import pandas as pd
from config import COINAPI_API_KEY
from utils import save_with_history

def fetch_coinapi_data():
    url = 'https://rest.coinapi.io/v1/assets'
    headers = {'X-CoinAPI-Key': COINAPI_API_KEY}
    response = requests.get(url, headers=headers)
    data = response.json()

    unlisted_coins = [asset for asset in data if not asset['data_end']]
    df = pd.DataFrame(unlisted_coins, columns=['asset_id', 'name', 'type_is_crypto'])
    save_with_history(df, 'coinapi_new_coins.csv')

if __name__ == "__main__":
    fetch_coinapi_data()
