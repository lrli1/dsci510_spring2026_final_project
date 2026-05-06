# include your tests here
from load import get_json_data, get_csv_data
from process import process_cdc_data, process_crime_data, process_census_data, merge_datasets
from config import CDC_URL, FBI_URL, CENSUS_URL, RESULTS_DIR, DATA_DIR
from analyze import plot_bar, plot_scatter, plot_heatmap, run_clustering

if __name__ == "__main__":
    
    # get CDC cleaned data
    cdc_raw = get_json_data(CDC_URL)
    cdc = process_cdc_data(cdc_raw)
    print(cdc.head())

    # check
    if cdc is None or len(cdc) == 0:
        print("FAIL: CDC DF returned no data")
    else:
        print(f"CDC DF returned {len(cdc)} rows")

    # get crime cleaned data
    fbi_raw = get_csv_data(FBI_URL)
    fbi = process_crime_data(fbi_raw)
    print(fbi.head())

    # check
    if fbi is None or len(fbi) == 0:
        print("FAIL: FBI DF returned no data")
    else:
        print(f"FBI DF returned {len(fbi)} rows")

    # get census cleaned data
    census_raw = get_csv_data(CENSUS_URL)
    census = process_census_data(census_raw)
    print(census.head())

    # check 
    if census is None or len(census) == 0:
        print("FAIL: Census DF returned no data")
    else:
        print(f"Census DF returned {len(census)} rows")

    # merge data
    merged = merge_datasets(cdc, fbi, census)
    print(merged.columns.tolist())
    print(merged.head())

    # check
    if merged is None or len(merged) == 0:
        print("FAIL: Merge returned no data")
    else:
        print(f"Merge returned {len(merged)} rows")


