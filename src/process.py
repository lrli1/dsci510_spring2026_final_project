from load import get_json_data, get_csv_data
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
        print(f"Could not clean CDC data: {e}")
        return pd.DataFrame()

# --- 2. CRIME DATA  ---
def process_crime_data(df):
    print("--- Processing Crime Data ---")
    try:
        import pandas as pd
        df = df.drop(range(0, 3))
        
        # keep only relevant columns (adjust index if needed)
        df = df.iloc[:, [1, 5]]  # State + Rate estimate
        df.columns = ["state_name", "rate_per_100k"]

        # convert to numeric & drop states without number
        df["rate_per_100k"] = pd.to_numeric(df["rate_per_100k"], errors="coerce")
        df = df.dropna(subset=["rate_per_100k"])
    
        print(f"Crime data processed: {len(df)} rows")
        return df
        
    except Exception as e:
        print(f"Could not clean Crime data: {e}")
        return pd.DataFrame()

# --- 3. CENSUS DATA  ---
def process_census_data(df):
    print("--- Processing Census Data ---")
    try:
        # keep relevant columns
        # Percent!!PERCENTAGE OF FAMILIES AND PEOPLE WHOSE INCOME IN THE PAST 12 MONTHS IS BELOW THE POVERTY LEVEL!!All people
        # Percent!!HEALTH INSURANCE COVERAGE!!Civilian noninstitutionalized population!!No health insurance coverage
        # Percent!!EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force!!Unemployed  
        df = df[['NAME','DP03_0128PE','DP03_0099PE','DP03_0005PE']].copy()
       
        # rename columnns
        df.columns = ['state_name','poverty_rate','no_insurance_pct','unemployment_rate']

        # clean columns
        df['poverty_rate'] = pd.to_numeric(df['poverty_rate'], errors='coerce')
        df['no_insurance_pct'] = pd.to_numeric(df['no_insurance_pct'], errors='coerce')
        df['unemployment_rate'] = pd.to_numeric(df['unemployment_rate'], errors='coerce')
        # drop missing values
        df = df.dropna()
        
        print(f"Census data processed: {len(df)} rows")
        return df
        
    except Exception as e:
        print(f"Could not clean Census data: {e}")
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

