import pandas as pd
import os
from config import DATA_DIR

def combine_data():
    files = ['coingecko_prices.csv', 'coinwarz_mining_data.csv', 'coinapi_new_coins.csv',
             'miningpoolstats_data.csv', 'clore_rental_data.csv', 'bitcointalk_sentiment.csv', 'discord_sentiment.csv']

    dfs = [pd.read_csv(os.path.join(DATA_DIR, file)) for file in files]
    combined_df = pd.concat(dfs, axis=1)

    combined_df.to_csv(os.path.join(DATA_DIR, 'combined_dataset.csv'), index=False)
    print("Combined dataset saved.")

if __name__ == "__main__":
    combine_data()
