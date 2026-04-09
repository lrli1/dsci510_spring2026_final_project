import os
from config import CDC_API_URL, FBI_XLSX_PATH, CENSUS_CSV_PATH, RESULTS_DIR, DATA_DIR
from load import get_mental_health_data, get_crime_data, get_census_data
from process import process_cdc_data, process_crime_data, process_census_data, merge_datasets
from analyze import plot_statistics

    
if __name__ == "__main__":
    # Create a data directory
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(RESULTS_DIR, exist_ok=True)

    # --- Load Data
    print("----- LOADING DATA ----- ")
    cdc_raw = get_mental_health_data(CDC_API_URL)
    fbi_raw = get_crime_data(FBI_XLSX_PATH)
    census_raw = get_census_data(CENSUS_CSV_PATH)

    # --- Process Data 
    print("----- PROCESSING DATA ----- ")
    cdc_df = process_cdc_data(cdc_raw)
    fbi_df = process_crime_data(fbi_raw)
    census_df = process_census_data(census_raw)
    merged = merge_datasets(cdc_df, fbi_df, census_df)
    
    # -- Analyze Data
    print("----- ANALYZING DATA ----- ")
    plot_statistics(merged[['state_name', 'mental_health_pct']], 'CDC_Mental_Health', result_dir=RESULTS_DIR)
    plot_statistics(merged[['state_name', 'violent_crime']], 'FBI_Crime', result_dir=RESULTS_DIR)
    plot_statistics(merged[['state_name', 'poverty_rate']], 'Census_Poverty', result_dir=RESULTS_DIR)
    plot_statistics(merged[['state_name', 'no_insurance_pct']], 'Census_Insurance', result_dir=RESULTS_DIR)
    plot_statistics(merged[['state_name', 'unemployment_rate']], 'Census_Unemployment', result_dir=RESULTS_DIR)

    #scatter plots
    plot_statistics(merged[['mental_health_pct', 'violent_crime']], 'MentalHealth_vs_Crime', result_dir=RESULTS_DIR)
    # mental health vs census features
    plot_statistics(merged[['mental_health_pct', 'poverty_rate']], 'MentalHealth_vs_Poverty', result_dir=RESULTS_DIR)
    plot_statistics(merged[['mental_health_pct', 'unemployment_rate']], 'MentalHealth_vs_Unemployment', result_dir=RESULTS_DIR)
    plot_statistics(merged[['mental_health_pct', 'no_insurance_pct']], 'MentalHealth_vs_Insurance', result_dir=RESULTS_DIR)
    # crime vs census features
    plot_statistics(merged[['violent_crime', 'poverty_rate']], 'Crime_vs_Poverty', result_dir=RESULTS_DIR)
    plot_statistics(merged[['violent_crime', 'unemployment_rate']], 'Crime_vs_Unemployment', result_dir=RESULTS_DIR)
    plot_statistics(merged[['violent_crime', 'no_insurance_pct']], 'Crime_vs_Insurance', result_dir=RESULTS_DIR)

    print("\n--- Data collection and plotting complete. Check the 'results' directory. ---")
