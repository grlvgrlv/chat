import pandas as pd
import joblib
import os
from config import DATA_DIR

def predict_real_time():
    model = joblib.load(os.path.join(DATA_DIR, 'crypto_mining_model.pkl'))
    df = pd.read_csv(os.path.join(DATA_DIR, 'combined_dataset.csv'))
    X = df.drop(columns=['Profitability'])

    predictions = model.predict(X)
    df['Predicted_Profitability'] = predictions
    df.to_csv(os.path.join(DATA_DIR, 'real_time_predictions.csv'), index=False)
    print("Real-time predictions saved.")

if __name__ == "__main__":
    predict_real_time()
