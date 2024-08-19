import pandas as pd

def load(data):
    data = pd.read_csv(data)
    data.to_parquet('data.parquet')