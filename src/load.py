import pandas as pd
import requests

# load data from API 
def get_json_data(url):
    print(f"--- Loading JSON Data---")
    try:
        df = pd.read_json(url)
        print(f"Data loaded: {len(df)} rows")
        return df
    except Exception as e:
        print(f"Error, could not get data from JSON: {e}")
        return None

# load data from web CSV
def get_csv_data(url):
    print(f"--- Loading CSV Data ---")
    try:
        # pandas can read a CSV directly from a URL
        df = pd.read_csv(url)
        print(f"Data loaded: {len(df)} rows")
        return df
    except Exception as e:
        print(f"Error loading data from Web CSV: {e}")
        return None
    

