import requests
import pandas as pd
from utils import save_with_history

def fetch_clore_rental_data():
    url = 'https://api.clore.ai/rental-prices'
    response = requests.get(url)
    data = response.json()

    df = pd.DataFrame(data, columns=['Algorithm', 'PricePerMH', 'Availability'])
    save_with_history(df, 'clore_rental_data.csv')

if __name__ == "__main__":
    fetch_clore_rental_data()
