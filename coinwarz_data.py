import requests
import pandas as pd
from config import COINWARZ_API_KEY
from utils import save_with_history

def fetch_coinwarz_data():
    url = f'https://www.coinwarz.com/v1/api/coininformation/?apikey={COINWARZ_API_KEY}'
    response = requests.get(url)
    data = response.json()

    gpu_mineable = [coin for coin in data['Data'] if 'GPU' in coin['Algorithm']]
    df = pd.DataFrame(gpu_mineable, columns=['CoinName', 'Algorithm', 'Difficulty', 'NetHash', 'BlockReward', 'ExchangeRate'])
    save_with_history(df, 'coinwarz_mining_data.csv')

if __name__ == "__main__":
    fetch_coinwarz_data()
