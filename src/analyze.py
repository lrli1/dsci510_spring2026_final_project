import os
import matplotlib.pyplot as plt

# --- PLOT STATISTICS ---
def plot_statistics(df, dataset_name, result_dir="plots", notebook_plot=False):
    """
    Generates and saves basic plots for a given DataFrame.
    :param result_dir: where to place plots
    :param df: The pandas DataFrame
    :param dataset_name: A name for titling plots (e.g., 'Titanic')
    """
    print(f"--- Plotting statistics for {dataset_name} ---")

    # Ensure a directory for plots exists
    os.makedirs(result_dir, exist_ok=True)

    # Identify numerical and categorical columns for plotting
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns

    # # Plot 1: Histogram (for a numerical column)
    # if not numerical_cols.empty:
    #     col_to_plot = numerical_cols[0]
    #     plt.figure(figsize=(10, 6))
    #     df[col_to_plot].hist(bins=30, edgecolor='black')
    #     plt.title(f'Histogram of {col_to_plot} - {dataset_name}')
    #     plt.xlabel(col_to_plot)
    #     plt.ylabel('Frequency')
    #     plt.grid(axis='y')
    #     if not notebook_plot:
    #         plt.savefig(f'{result_dir}/{dataset_name}_histogram.png')
    #         print(f"Saved histogram for {col_to_plot}")
    #         plt.close()
    #     else:
    #         plt.plot()

    # Plot 2: Bar Chart (per state)
    if 'state_name' in df.columns and not numerical_cols.empty:
        col_to_plot = numerical_cols[0]
        df_sorted = df.sort_values(col_to_plot, ascending=False)
        plt.figure(figsize=(14, 6))
        plt.bar(df_sorted['state_name'], df_sorted[col_to_plot], edgecolor='black')
        plt.title(f'{col_to_plot} by State - {dataset_name}')
        plt.xlabel('State')
        plt.ylabel(col_to_plot)
        plt.xticks(rotation=90)
        plt.grid(axis='y')
        plt.tight_layout()
        if not notebook_plot:
            plt.savefig(f'{result_dir}/{dataset_name}_barchart.png')
            print(f"Saved bar chart for {col_to_plot} by state")
            plt.close()
        else:
            plt.plot()

    # Plot 3: Scatter Plot (for two numerical columns)
    if len(numerical_cols) >= 2:
        col1 = numerical_cols[0]
        col2 = numerical_cols[1]
        plt.figure(figsize=(10, 6))
        plt.scatter(df[col1], df[col2], alpha=0.5)
        plt.title(f'Scatter Plot: {col1} vs {col2} - {dataset_name}')
        plt.xlabel(col1)
        plt.ylabel(col2)
        plt.grid(True)
        if not notebook_plot:
            plt.savefig(f'{result_dir}/{dataset_name}_scatterplot.png')
            print(f"Saved scatter plot for {col1} vs {col2}")
            plt.close()
        else:
            plt.plot()


## check
# if __name__ == "__main__":
#     from config import CDC_API_URL, FBI_XLSX_PATH, CENSUS_CSV_PATH, RESULTS_DIR
#     from load import get_mental_health_data, get_crime_data, get_census_data
#     from process import process_cdc_data, process_crime_data, process_census_data, merge_datasets

#     cdc_df = process_cdc_data(get_mental_health_data(CDC_API_URL))
#     fbi_df = process_crime_data(get_crime_data(FBI_XLSX_PATH))
#     census_df = process_census_data(get_census_data(CENSUS_CSV_PATH))
#     merged = merge_datasets(cdc_df, fbi_df, census_df)

#     # bar graphs 
#     plot_statistics(merged[['state_name', 'mental_health_pct']], 'CDC_Mental_Health', result_dir=RESULTS_DIR)
#     plot_statistics(merged[['state_name', 'violent_crime']], 'FBI_Crime', result_dir=RESULTS_DIR)
#     plot_statistics(merged[['state_name', 'poverty_rate']], 'Census_Poverty', result_dir=RESULTS_DIR)
#     plot_statistics(merged[['state_name', 'no_insurance_pct']], 'Census_Insurance', result_dir=RESULTS_DIR)
#     plot_statistics(merged[['state_name', 'unemployment_rate']], 'Census_Unemployment', result_dir=RESULTS_DIR)

#     #scatter plots
#     plot_statistics(merged[['mental_health_pct', 'violent_crime']], 'MentalHealth_vs_Crime', result_dir=RESULTS_DIR)
#     # mental health vs census features
#     plot_statistics(merged[['mental_health_pct', 'poverty_rate']], 'MentalHealth_vs_Poverty', result_dir=RESULTS_DIR)
#     plot_statistics(merged[['mental_health_pct', 'unemployment_rate']], 'MentalHealth_vs_Unemployment', result_dir=RESULTS_DIR)
#     plot_statistics(merged[['mental_health_pct', 'no_insurance_pct']], 'MentalHealth_vs_Insurance', result_dir=RESULTS_DIR)
#     # crime vs census features
#     plot_statistics(merged[['violent_crime', 'poverty_rate']], 'Crime_vs_Poverty', result_dir=RESULTS_DIR)
#     plot_statistics(merged[['violent_crime', 'unemployment_rate']], 'Crime_vs_Unemployment', result_dir=RESULTS_DIR)
#     plot_statistics(merged[['violent_crime', 'no_insurance_pct']], 'Crime_vs_Insurance', result_dir=RESULTS_DIR)

