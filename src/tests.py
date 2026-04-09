# include your tests here
from load import get_mental_health_data, get_crime_data, get_census_data
from process import process_cdc_data, process_crime_data, process_census_data, merge_datasets
from config import CDC_API_URL, FBI_XLSX_PATH, CENSUS_CSV_PATH

def test_cdc_api_returns_data():
    df = get_mental_health_data(CDC_API_URL)
    if df is None or len(df) == 0:
        print("FAIL: CDC API returned no data")
    else:
        print(f"PASS: CDC API returned {len(df)} rows")

def test_cdc_api_has_expected_columns():
    df = get_mental_health_data(CDC_API_URL)
    if 'area' not in df.columns:
        print("FAIL: Missing 'area' column")
    elif 'percent' not in df.columns:
        print("FAIL: Missing 'percent' column")
    else:
        print("PASS: CDC API has expected columns")

def test_crime_data_loads():
    df = get_crime_data(FBI_XLSX_PATH)
    if df is None or len(df) == 0:
        print("FAIL: Crime data returned no data")
    else:
        print(f"PASS: FBI crime data loaded {len(df)} rows")

def test_census_data_loads():
    df = get_census_data(CENSUS_CSV_PATH)
    if df is None or len(df) == 0:
        print("FAIL: Census data returned no data")
    else:
        print(f"PASS: Census data loaded {len(df)} rows")

def test_cdc_processing():
    raw = get_mental_health_data(CDC_API_URL)
    df = process_cdc_data(raw)
    if len(df) == 0:
        print("FAIL: CDC processed data is empty")
    elif 'mental_health_pct' not in df.columns:
        print("FAIL: Missing mental_health_pct column")
    else:
        print(f"PASS: CDC data processed into {len(df)} states")

def test_merge_datasets():
    cdc = process_cdc_data(get_mental_health_data(CDC_API_URL))
    fbi = process_crime_data(get_crime_data(FBI_XLSX_PATH))
    census = process_census_data(get_census_data(CENSUS_CSV_PATH))
    merged = merge_datasets(cdc, fbi, census)
    if len(merged) == 0:
        print("FAIL: Merged dataset is empty")
    elif 'mental_health_pct' not in merged.columns:
        print("FAIL: Missing mental_health_pct column")
    elif 'violent_crime' not in merged.columns:
        print("FAIL: Missing violent_crime column")
    else:
        print(f"PASS: Datasets merged into {len(merged)} rows")

if __name__ == "__main__":
    test_cdc_api_returns_data()
    test_cdc_api_has_expected_columns()
    test_crime_data_loads()
    test_census_data_loads()
    test_cdc_processing()
    test_merge_datasets()
    print("\nTests complete")