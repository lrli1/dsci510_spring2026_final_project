# Understanding the Relationship Between Mental Health and Crime Rates Using Socioeconomic Factors
This project aims to explore the relationship between mental health status and crime rates at the state level using bar charts, correlation calculations, and clustering analyses. Poor untreated mental health can often lead to violence, confusion, and impulsive behavior. Therefore, it is important to address potential patterns and correlations. That way, we can implement policy programs, health insurance, mental health shelters, etc., to help solve crime from the ground up rather than top-down. There are many confounders to crime rates, so CDC economic data, including health insurance rates, unemployment rates, and poverty rates, are analyzed as well. Mental health is measured as a percentage of survey responses on happiness/emotion, and violent crime is measured based on the number of homicides, aggravated assaults, robberies, and rape cases per 100,000 people. 

# Data sources
Dataset 1: 
- _Name_: CDC (Center for Disease Control and Prevention)'s Behavioral Risk Factor Surveillance System (BRFSS) Mental Health Indicators
- _Datatype_: API
- _API URL_: https://data.cdc.gov/resource/5eh7-pjx8.json?$limit=50000
- Source URL_: https://data.cdc.gov/Mental-Health/Behavioral-Risk-Factor-Surveillance-System-BRFSS-M/5eh7-pjx8/about_data
- _Description_: Mental Health Data by state
- _Important Features_: area, area_name, question, percent
- _Specific question_: 'Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good?'
- _Format_: JSON
- _Num data points after processing_: 54

Dataset 2: 
- _Name_: Bureau of Justice Statistics: Crime Known to Law Enforcement 2024
- _Datatype_: Web CSV
- _Source URL_: https://bjs.ojp.gov/library/publications/crime-known-law-enforcement-2024 
- _URL_: https://gist.githubusercontent.com/lrli1/d560e4d04b6b6e8315900bbe3224fc0c/raw/9dce7b56a93cc5e03e763b87e2dd5e56053525e0/Crime_Data.csv
- _Description_: Estimates and RMSE for rate of violent victimization by state 2024
- _Important Features_: state, rate per 100,000 estimate
- _Format_: CSV
-_ Num data points after processing_: 45

Dataset 3: 
- _Name_: United States Census Bureau: ACS 5-year Estimates (2020-2025) Selected Economic Characteristics All States in the United States
- _Datatype_: Web CSV
- _Source URL_: https://data.census.gov/table/ACSDP5YSPT2021.DP03?g=010XX00US$3100000&d=ACS+5-Year+Estimates+Selected+Population+Data+Profiles
- _URL_: https://gist.githubusercontent.com/lrli1/820584669eb70989d4d8d20b47d65e52/raw/809ccd245292102bcbae9a8c2c51f537462376f8/gistfile1.txt
- _Description_: Economic demographic data for states in the US
- _Important Features_: NAME, Percent!!PERCENTAGE OF FAMILIES AND PEOPLE WHOSE INCOME IN THE PAST 12 MONTHS IS BELOW THE POVERTY LEVEL!!All people, Percent!!HEALTH INSURANCE COVERAGE!!Civilian noninstitutionalized population!!No health insurance coverage, Percent!!EMPLOYMENT STATUS!!Population 16 years and over!!In labor force!!Civilian labor force!!Unemployed
- _Format_: CSV
- _Num data points after professing_: 52

# Results 
**Variable Analysis:**
- West Virginia has the highest rate of poor mental health (%) from a 30-day period  
- New Mexico has the highest rate of violent crime.
- Louisiana has the highest poverty rate.
- Texas has the highest rate of no health insurance (%). 
- Nevada has the highest unemployment rate.

**Scatter Plot Analysis:**
- Mental health and violent crime are slightly positively correlated, but not very strongly
- outliers and separate clusters exist

**Heat Map Analysis:**
- Violent crime and poor mental health have a correlation coefficient of 0.4
- Poverty rate has the highest correlation with poor mental health
- Poverty rate also has the highest correlation with violent crime

**Clustering Analysis (no socioeconomic variables):**
- _Cluster 0_: Alabama, California, Colorado, Delaware, Florida, Georgia, Indiana, Kansas, Maryland, Michigan, Missouri, Montana, North Carolina, Nevada, New York, Ohio, Oregon, South Carolina, Texas, Washington, Wisconsin

- _Cluster 1:_ Arkansas, Louisiana, New Mexico, Oklahoma, Tennessee, West Virginia

- _Cluster 2:_ Connecticut, Iowa, Idaho, Illinois, Kentucky, Massachusetts, Maine, Minnesota, North Dakota, Nebraska, New Hampshire,  New Jersey, Rhode Island, South Dakota, Utah, Virginia, Vermont, Wyoming
  
Cluster 0 represents the moderate states in the middle range, moderate crime and moderate poor mental health. Cluster 1 represents states with high crime and high rates of poor mental health. Cluster 2 represents states with low crime and low rates of poor mental health. This clustering tells us that without socioeconomic variables, there is a slight positive associative pattern. This tells us that crime rates and mental health are related in some way. 

**Clustering Analysis (with socioeconomic variables):**
- _Cluster 0_: California, Colorado, Connecticut, Delaware, Illinois, Massachusetts, Maryland, Michigan, New Jersey, New York, Ohio, Oregon, Rhode Island, Washington

- _Cluster 1_: Iowa, Idaho, Indiana, Kansas, Maine, Minnesota, Montana, North Dakota, Nebraska, New Hampshire, South Dakota, Utah, Virginia, Vermont, Wisconsin, Wyoming 

- _Cluster 2_: Alabama, Arkansas, Florida, Georgia, Kentucky, Louisiana, Missouri, North Carolina, New Mexico, Nevada, Oklahoma, South Carolina, Tennessee, Texas, West Virginia

After adding in socioeconomic variables, the clusters become more intertwined, and the relationship between mental health and crime is less distinct. There isn't a clear separation boundary between clusters that we can see in the 2D plane. The cluster assignments changed significantly. Therefore, we can conclude that socioeconomic factors also drive mental health and crime. The relationship between mental health and crime is partly driven by underlying socioeconomic factors. 

Additionally, states in cluster 0 seem to be from the coast. States in cluster 1 seem more in the Midwest. States in cluster 2 seem to be from the South. Other factors that could potentially drive patterns include urban/rural, political party, population, and more. 

# Installation
The API endpoint is public and stored in the config.py file.
CSV files are public via a web CSV URL, which is stored in the config.py file as well.
No further installation is needed to run the project.
Libraries used include numpy, pandas (for data cleaning), matplotlib (for visualization), sklearn.preprocessing (for cluster scaling), and sklearn.cluster (for cluster analysis).

# Running analysis 
From the 'src/' directory, run 'python3 main.py'. Results will output in the terminal and in the `results/` directory. Optionally, run 'python3 results.ipynb'. 

# AI usage 
For my clustering analysis, AI in the form of Google Gemini engine searches was used to see which packages and tools to use. Prior knowledge of coding and ML pipelines helped shape the rest of the code. 
