import requests
import pandas as pd
from bs4 import BeautifulSoup
from utils import save_with_history

def fetch_miningpoolstats_data():
    url = 'https://miningpoolstats.stream/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    coins = []
    for row in soup.find_all('tr'):
        columns = row.find_all('td')
        if columns and 'GPU' in columns[2].text:
            coin = {'CoinName': columns[0].text.strip(), 'Algorithm': columns[2].text.strip(),
                    'Difficulty': columns[4].text.strip(), 'NetHash': columns[5].text.strip()}
            coins.append(coin)

    df = pd.DataFrame(coins)
    save_with_history(df, 'miningpoolstats_data.csv')

if __name__ == "__main__":
    fetch_miningpoolstats_data()
