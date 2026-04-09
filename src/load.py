import pandas as pd
import requests

# --- 1. DOWNLOAD DATA FROM API ---
def get_mental_health_data(url):
    print(f"--- Loading CDC Mental Health Data from API: {url} ---")
    try:
        df = pd.read_json(url)
        print(f"Mental Health data loaded: {len(df)} rows")
        return df
    except Exception as e:
        print(f"Error, could not get data from API: {e}")
        return None


# --- 2. DOWNLOAD DATA FROM XLSX ---
def get_crime_data(filepath):
    print(f"--- Loading Crime Data from {filepath} ---")
    try:
        df = pd.read_excel(filepath, skiprows=4, header=0)
        print(f"FBI data loaded: {len(df)} rows")
        return df
    except Exception as e:
        print(f"Error, could not get data from file:{e}")
        return None


# --- 3. DOWNLOAD DATA FROM CSV ---
def get_census_data(filepath):
    print(f"--- Loading Census Data from {filepath} ---")
    try:
        df = pd.read_csv(filepath, skiprows=1, header=0)
        print(f"Census data loaded: {len(df)} rows")
        return df
    except Exception as e:
        print(f"Error, could not get data from file:{e}")
        return None

## check 
# if __name__ == "__main__":
#     from config import CDC_API_URL, FBI_XLSX_PATH, CENSUS_CSV_PATH

#     cdc = get_mental_health_data(CDC_API_URL)
#     print(cdc.head())

#     fbi = get_crime_data(FBI_XLSX_PATH)
#     print(fbi.head())

#     census = get_census_data(CENSUS_CSV_PATH)
#     print(census.head())

