# Understanding the Relationship Between Mental Health and Crime Rates Using Socioeconomic Factors
This project aims to explore the relationship between mental health status and crime rates at the state level using bar charts, correlation calculations, and clustering analysis. Poor untreated mental health can often lead to violence, confusion, and impulsive behavior. Therefore, it is important to address the potential patterns and correlations that may exist. That way, we can implement policy programs, health insurance, mental health shelters, etc., to help solve crime from the ground up rather than top-down. There are many confounders to crime rates as well, so CDC economic data, including health insurance rates, unemployment rates, and poverty rates, are analyzed as well. Mental health is analyzed via a survey on happiness/emotion, and violent crime is measured based on the number of homicides, aggravated assaults, robberies, and rape cases per 100,000 people. 

# Data sources
Dataset 1: CDC (Center for Disease Control and Prevention)'s Behavioral Risk Factor Surveillance System (BRFSS) - Mental Health Indicators, API Datatype; API URL: https://data.cdc.gov/resource/5eh7-pjx8.json?$limit=50000; Website URL: https://data.cdc.gov/Mental-Health/Behavioral-Risk-Factor-Surveillance-System-BRFSS-M/5eh7-pjx8/about_data; Description: Mental Health Data by state; Important Features: area, area_name, question, percent; Question: 'Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good?'; Format: JSON, Num data points: XXXXXX

Dataset 2: Bureau of Justice Statistics: Crime Known to Law Enforcement 2024; Datatype: Web Page; URL: https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/downloads; Description: Estimates and RMSE for rate of violent victimization by state 2024, Important Features: state, rate per 100000 estimate; Format: CSV

United States Census Bureau: ACS 5-year Estimates (2020-2025) Selected Economic Characteristics All States in the United States, Datatype: CSV, Website Link: https://data.census.gov/table/ACSDP5YSPT2021.DP03?g=010XX00US$0400000&d=ACS+5-Year+Estimates+Selected+Population+Data+Profiles, Description: 
Economic demographic data for states in the US, 

# Results 
West Virginia has the highest percentage of the population who are depressed per month (over 20 days out of the month).
California has the highest amount of violent crime.
Mississippi faces the highest poverty rates.
Texas populations have the most people with no health insurance. 
Nevada has the highest unemployment rate.

Mental health and violent crime are not strongly positively correlated.
Mental health and poverty are moderately positively correlated.
Mental health and unemployment rate are slightly positively correlated. 
Mental health and insurance rates are moderately positively correlated.

Violent crime and poverty are not strongly correlated.
Violent crime and unemployment are not strongly correlated.
Violent crime and insurance rates are not strongly correlated.

# Installation
API endpoint is public and stored in the config.py file.
CSV files are public via a web CSV URL, which is stored in the config.py file.
No further user action is needed to run project.
Libraries used include numpy, pandas (for data cleaning), matplotlib (for visualization), sklearn.preprocessing (for cluster scaling), and sklearn.cluster (for cluster analysis).

# Running analysis 
From 'src/' directory, run 'python3 main.py'. Results will output in both the terminal and in the `results/` directory. Optionally, run 'python3 results.ipynb'. 
