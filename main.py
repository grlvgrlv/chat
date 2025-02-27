### main.py
```python
# main.py
import coingecko_data
import coinwarz_data
import coinapi_data
import miningpoolstats_data
import clore_rental_data
import sentiment_analysis
import combine_data
import preprocess_data
import train_model
import predict_real_time
import clean_old_data

if __name__ == "__main__":
    try:
        coingecko_data.fetch_coingecko_data()
        coinwarz_data.fetch_coinwarz_data()
        coinapi_data.fetch_coinapi_data()
        miningpoolstats_data.fetch_miningpoolstats_data()
        clore_rental_data.fetch_clore_rental_data()
        sentiment_analysis.main()
        combine_data.combine_data()
        preprocess_data.preprocess_data()
        clean_old_data.clean_old_data()
        train_model.train_model()
        predict_real_time.predict_real_time()
    except Exception as e:
        print(f"Σφάλμα κατά την εκτέλεση του main.py: {e}")

