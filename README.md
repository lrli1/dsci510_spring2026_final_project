# Understanding the Relationship Between Mental Health and Crime Rates Using Socioeconomic Factors
This project aims to explore the relationship between mental health status and crime rates at the state level using bar charts, correlation calculations, and clustering analyses. Poor untreated mental health can often lead to violence, confusion, and impulsive behavior. Therefore, it is important to address potential patterns and correlations. That way, we can implement policy programs, health insurance, mental health shelters, etc., to help solve crime from the ground up rather than top-down. There are many confounders to crime rates, so CDC economic data, including health insurance rates, unemployment rates, and poverty rates, are analyzed as well. Mental health is measured as a percentage of survey responses on happiness/emotion, and violent crime is measured based on the number of homicides, aggravated assaults, robberies, and rape cases per 100,000 people. 

# Data sources
Dataset 1: 
- _Name_: CDC (Center for Disease Control and Prevention)'s Behavioral Risk Factor Surveillance System (BRFSS) Mental Health Indicators
- _Datatype_: API
- _API URL_: https://data.cdc.gov/resource/5eh7-pjx8.json?$limit=50000
- _Website URL_: https://data.cdc.gov/Mental-Health/Behavioral-Risk-Factor-Surveillance-System-BRFSS-M/5eh7-pjx8/about_data
- _Description_: Mental Health Data by state
- _Important Features_: area, area_name, question, percent
- _Specific question_: 'Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good?'
- _Format_: JSON
- _Num data points after processing_: 54

Dataset 2: 
- _Name_: Bureau of Justice Statistics: Crime Known to Law Enforcement 2024
- _Datatype_: Web CSV
- _URL_: https://gist.githubusercontent.com/lrli1/d560e4d04b6b6e8315900bbe3224fc0c/raw/9dce7b56a93cc5e03e763b87e2dd5e56053525e0/Crime_Data.csv
- _Description_: Estimates and RMSE for rate of violent victimization by state 2024
- _Important Features_: state, rate per 100,000 estimate
- _Format_: CSV
-_ Num data points after processing_: 45

Dataset 3: 
- _Name_: United States Census Bureau: ACS 5-year Estimates (2020-2025) Selected Economic Characteristics All States in the United States
- _Datatype_: Web CSV
- _URL_: https://gist.githubusercontent.com/lrli1/820584669eb70989d4d8d20b47d65e52/raw/809ccd245292102bcbae9a8c2c51f537462376f8/gistfile1.txt
- _Description_: Economic demographic data for states in the US
- _Important Features_: NAME, Percent!!PERCENTAGE OF FAMILIES AND PEOPLE WHOSE INCOME IN THE PAST 12 MONTHS IS BELOW THE POVERTY LEVEL!!All people, Percent!!HEALTH INSURANCE COVERAGE!!Civilian noninstitutionalized population!!No health insurance coverage, Percent!!EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force!!Unemployed
- _Format_: CSV
- _Num data points after professing_: 52

# Results 
Variable Analysis: 
- West Virginia has the highest rate of poor mental health (%) from a 30-day period  
- New Mexico has the highest rate of violent crime.
- Louisiana has the highest poverty rate.
- Texas has the highest rate of no health insurance (%). 
- Nevada has the highest unemployment rate.

Scatter Plot Analysis:
- Mental health and violent crime are slightly positively correlated, but not very strongly
- outliers and separate clusters exist

Heat Map Analysis:
- Violent crime and poor mental health have a correlation coefficient of 0.4
- Poverty rate has the highest correlation with poor mental health
- Poverty rate also has the highest correlation with violent crime

Clustering Analysis (no socioeconomic variables):
Cluster 0: Alabama, California, Colorado, Delaware, Florida, Georgia, Indiana, Kansas, Maryland, Michigan, Missouri, Montana, North Carolina, Nevada, New York, Ohio, Oregon, South Carolina, Texas, Washington, Wisconsin

Cluster 1: Arkansas, Louisiana, New Mexico, Oklahoma, Tennessee, West Virginia

Cluster 2:
['Connecticut', 'Iowa', 'Idaho', 'Illinois', 'Kentucky', 'Massachusetts', 'Maine', 'Minnesota', 'North Dakota', 'Nebraska', 'New Hampshire', 'New Jersey', 'Rhode Island', 'South Dakota', 'Utah', 'Virginia', 'Vermont', 'Wyoming']

Clustering Analysis (with socioeconomic variables):

# Installation
The API endpoint is public and stored in the config.py file.
CSV files are public via a web CSV URL, which is stored in the config.py file as well.
No further installation is needed to run the project.
Libraries used include numpy, pandas (for data cleaning), matplotlib (for visualization), sklearn.preprocessing (for cluster scaling), and sklearn.cluster (for cluster analysis).

# Running analysis 
From the 'src/' directory, run 'python3 main.py'. Results will output in the terminal and in the `results/` directory. Optionally, run 'python3 results.ipynb'. 
