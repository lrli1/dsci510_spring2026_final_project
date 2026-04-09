# Sample Project <Mental Health and Crime Rates, with Socioeconomic Factors>
This project aims to explore the relationship between mental health status and crime rates at the state level. Poor untreated mental health can often lead to violence, confusion, and impulsive behavior. Therefore, it is important to address the potential patterns and correlations that may exist. That way, we can implement policy programs, health insurance, mental health shelters, etc. to help solve crime from the ground-up rather than top-down. There are many confounders to crime rates as well, so CDC economic data including health insurance rates, unemployment rates, and poverty rates are analyzed as well.

# Data sources
CDC (Center for Disease Control and Prevention): Behavioral Risk Factor Surveillance System (BRFSS) - Mental Health Indicators, Datatype: API, API URL: https://data.cdc.gov/resource/5eh7-pjx8.json?$limit=50000, Website URL: https://data.cdc.gov/Mental-Health/Behavioral-Risk-Factor-Surveillance-System-BRFSS-M/5eh7-pjx8/about_data, Description: Mental Health Data, Feature analyzed: 'Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good?' 

FBI’s Crime Data Explorer: Crime in the United States Annual Reports - 2024, Offenses Known to Law Enforcement, Datatype: XLSX, URL: https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/downloads, Description: Crime Data, Table: ‘CIUS_Table_10_Offenses_Known_to_Law_Enforcement_by_State_by_Metropolitan_and_Nonmetropolitan_Counties_2024.xlsx', Feature Analyzed: Violent Crime

United States Census Bureau: ACS 5-year Estimates (2020-2025) Selected Economic Characteristics All States in te United States, Datatype: CSV, Website Link: https://data.census.gov/table/ACSDP5YSPT2021.DP03?g=010XX00US$0400000&d=ACS+5-Year+Estimates+Selected+Population+Data+Profiles, Description: 
Economic demographic data for states in the US, 

# Results 
West Virginia has the highest percentage of population who is depressed per month (over 20 days out of the month)
California has the highest amount of violent crime 
Mississippi faces the highets poverty rates 
Texas populations have the most people with no health insurance 
Nevada has the highest unemployment rate

Mental health and violent crime are not strongly positively correlated
Mental health and poverty are moderately positively correlated 
Mental health and unemployment rate are slightly positively correlated 
Mental health and insurance rate are moderately positively correlated 

Violent crime and poverty are not strongly correlated
Violent crime and unemployment are not strongly correlated
Violent crime and insurance rate are not strongly correlated

# Installation
API keys are public and stored in the config.py file 
In order to run analysis, processing, loading, user MUST manually download data via instructions in Lara_Li_progres_report

numpy
pandas (for data cleaning)
matplotlib (for analysis) 

# Running analysis 
After manually importing data into 'data/' directory via instructions in 'Lara_Li_progress_report': 

from 'src/' directory run 
run 'python3 tests.py'
run 'python3 main.py' 
run 'python3 results.ipynb'

Results will appear in `results/` directory