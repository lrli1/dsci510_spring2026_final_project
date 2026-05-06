import os
import matplotlib.pyplot as plt
from config import CDC_URL, FBI_URL, CENSUS_URL, RESULTS_DIR, DATA_DIR
from load import get_json_data, get_csv_data
from process import process_cdc_data, process_crime_data, process_census_data, merge_datasets
from analyze import plot_bar, plot_scatter, plot_heatmap, run_clustering, run_clustering_confound
        
if __name__ == "__main__":
    # Create a data directory
    os.makedirs(DATA_DIR, exist_ok=True)

    # --- Load Data-- 
    print("----- LOADING DATA ----- ")
    cdc_raw = get_json_data(CDC_URL)
    fbi_raw = get_csv_data(FBI_URL)
    census_raw = get_csv_data(CENSUS_URL)

    # --- Process Data -- 
    print("----- PROCESSING DATA ----- ")
    cdc_df = process_cdc_data(cdc_raw)
    fbi_df = process_crime_data(fbi_raw)
    census_df = process_census_data(census_raw)
    merged = merge_datasets(cdc_df, fbi_df, census_df)
    
    # -- Visualize Bar Plots-- 
    plot_bar(merged, 'mental_health_pct', 'Poor Mental Health (%) – Past 30 Days', 'Poor Mental Health % by State', RESULTS_DIR)
    plot_bar(merged, 'rate_per_100k', 'Violent Crime Rate (per 100k ppl)','Violent Crime Rate by State', RESULTS_DIR)
    plot_bar(merged, 'poverty_rate', 'Poverty Rate', 'Poverty Rate by State', RESULTS_DIR)
    plot_bar(merged, 'unemployment_rate', 'Unemployment Rate','Unemployment Rate by State', RESULTS_DIR)
    plot_bar(merged, 'no_insurance_pct', '% with No Insurance','% No Insurance Rate by State', RESULTS_DIR)

    # -- Visualize Scatter Plot-- 
    plot_scatter(merged, 'mental_health_pct','rate_per_100k', 'Poor Mental Health (%) – Past 30 Days', 'Violent Crime Rate (per 100k ppl)', 'Mental Health x Crime Scatter Plot',RESULTS_DIR)

    # -- Visualize Heat Map-- 
    plot_heatmap(merged,RESULTS_DIR)

    # -- Clustering Analysis (no confounders)--
    print("----- Clustering (no confounders) ----- ")
    run_clustering(merged,RESULTS_DIR)
        
    # -- Clustering Analysis (with confounders)-- 
    print("----- Clustering (with confounders) ----- ")
    run_clustering_confound(merged,RESULTS_DIR)

    
    print("\n--- Data collection and plotting complete. Check the 'results' directory. ---")