import pandas as pd
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
import os
from config import DATA_DIR

def preprocess_data():
    """Προεπεξεργασία του combined_dataset.csv και αποθήκευση του αποτελέσματος σε final_dataset.csv"""
    input_path = os.path.join(DATA_DIR, 'combined_dataset.csv')
    output_path = os.path.join(DATA_DIR, 'final_dataset.csv')

    df = pd.read_csv(input_path)
    df = df.dropna()  # Αφαίρεση γραμμών με κενές τιμές
    df = df.drop_duplicates()  # Αφαίρεση διπλότυπων

    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    scaler = MinMaxScaler()
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

    categorical_columns = df.select_dtypes(include=['object']).columns
    if len(categorical_columns) > 0:
        encoder = OneHotEncoder(sparse=False, drop='first')
        encoded_data = encoder.fit_transform(df[categorical_columns])
        encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(categorical_columns))
        df = pd.concat([df.drop(columns=categorical_columns), encoded_df], axis=1)

    df.to_csv(output_path, index=False)
    print(f"Τα δεδομένα προεπεξεργάστηκαν και αποθηκεύτηκαν στο: {output_path}")

if __name__ == "__main__":
    preprocess_data()
