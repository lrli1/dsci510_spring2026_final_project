from load import get_mental_health_data, get_crime_data, get_census_data
import pandas as pd

# --- 1. CDC DATA  ---
def process_cdc_data(df):
    # print("CDC Data Head:")
    # print(df.head())
    
    print("--- Processing CDC Mental Health Data ---")
    # Clean and filter CDC mental health data 
    try: 
        # filter for specific question
        df = df[df['question'] == 'Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good?'].copy()
        
        # convert to numeric 
        df['percent'] = pd.to_numeric(df['percent'], errors='coerce') # % of days in past 30 days with poor mental health 
        df = df.dropna(subset=['percent'])
        
        # average mental health % per state
        grouped = df.groupby(['area_abbr', 'area'])['percent'].mean().reset_index()
        
        plot_df = pd.DataFrame({
            'state': grouped['area_abbr'],
            'state_name': grouped['area'],
            'mental_health_pct': grouped['percent']
        })
        print(f"CDC data processed: {len(plot_df)} rows")
        return plot_df
        
    except Exception as e:
        print(f"Could not clean/plot CDC data: {e}")
        return pd.DataFrame()

# --- 2. CRIME DATA  ---
def process_crime_data(df):
    print("--- Processing Crime Data ---")
    try:
        df = df.dropna(subset=['State'])
        df = df.dropna(subset=['Violent\ncrime'])
        df['Violent\ncrime'] = pd.to_numeric(df['Violent\ncrime'], errors='coerce')

        #clean data values 
        df['State'] = df['State'].str.strip() #remove whitespace
        df['State'] = df['State'].str.replace(r'\d+', '', regex=True).str.strip() #remove numbers

        # add all violent crimes per state
        grouped = df.groupby('State')['Violent\ncrime'].sum().reset_index()
        plot_df = pd.DataFrame({
            'state_name': grouped['State'].str.title(),
            'violent_crime': grouped['Violent\ncrime']
        })
        
        # see row change 
        print(f"Crime data processed: {len(plot_df)} rows")
        return plot_df
        
    except Exception as e:
        print(f"Could not clean/plot Crime data: {e}")
        return pd.DataFrame()

# --- 3. CENSUS DATA  ---
def process_census_data(df):
    print("--- Processing Census Data ---")
    try:
        # keep relevant columns
        df = df[['Geographic Area Name',
            'Percent!!PERCENTAGE OF FAMILIES AND PEOPLE WHOSE INCOME IN THE PAST 12 MONTHS IS BELOW THE POVERTY LEVEL!!All people',
            'Percent!!HEALTH INSURANCE COVERAGE!!Civilian noninstitutionalized population!!No health insurance coverage',
            'Percent!!EMPLOYMENT STATUS!!Civilian labor force!!Unemployment Rate'
        ]].copy()

        # rename columnns
        df.rename(columns={
            'Geographic Area Name': 'state_name',
            'Percent!!PERCENTAGE OF FAMILIES AND PEOPLE WHOSE INCOME IN THE PAST 12 MONTHS IS BELOW THE POVERTY LEVEL!!All people': 'poverty_rate',
            'Percent!!HEALTH INSURANCE COVERAGE!!Civilian noninstitutionalized population!!No health insurance coverage': 'no_insurance_pct',
            'Percent!!EMPLOYMENT STATUS!!Civilian labor force!!Unemployment Rate': 'unemployment_rate'
        }, inplace=True)

        # clean columns
        df['poverty_rate'] = pd.to_numeric(df['poverty_rate'], errors='coerce')
        df['no_insurance_pct'] = pd.to_numeric(df['no_insurance_pct'], errors='coerce')
        df['unemployment_rate'] = pd.to_numeric(df['unemployment_rate'], errors='coerce')
        df = df.dropna()

        # new, cleaner plot 
        plot_df = pd.DataFrame({
            'state_name': df['state_name'],
            'poverty_rate': df['poverty_rate'],
            'no_insurance_pct': df['no_insurance_pct'],
            'unemployment_rate': df['unemployment_rate']
        })

        print(f"Census data processed: {len(plot_df)} rows")
        return plot_df
        
    except Exception as e:
        print(f"Could not clean/plot Census data: {e}")
        return pd.DataFrame()

def merge_datasets(cdc_df, fbi_df, census_df):
    print("--- Merging Datasets ---")
    try:
        # merge CDC and Crime
        merged = pd.merge(cdc_df, fbi_df, on='state_name', how='inner')

        # merge with Census 
        merged = pd.merge(merged, census_df, on='state_name', how='inner')
        
        print(f"Merged dataset: {len(merged)} rows, {len(merged.columns)} columns")
        # print(merged.head())
        return merged
        
    except Exception as e:
        print(f"Could not merge data: {e}")
        return pd.DataFrame()

## check 
# if __name__ == "__main__":
#     from config import CDC_API_URL, FBI_XLSX_PATH, CENSUS_CSV_PATH
#     from load import get_mental_health_data, get_crime_data, get_census_data

#     cdc_raw = get_mental_health_data(CDC_API_URL)
#     cdc = process_cdc_data(cdc_raw)
#     print(cdc.head())

#     fbi_raw = get_crime_data(FBI_XLSX_PATH)
#     fbi = process_crime_data(fbi_raw)
#     print(fbi.head())

#     census_raw = get_census_data(CENSUS_CSV_PATH)
#     census = process_census_data(census_raw)
#     print(census.head())

    merged = merge_datasets(cdc, fbi, census)
    print(merged.columns.tolist())