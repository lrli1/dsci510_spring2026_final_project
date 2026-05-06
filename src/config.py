from pathlib import Path
from dotenv import load_dotenv

# project configuration from .env (secret part)
env_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=env_path)  # loads into os.environ

# project configuration
DATA_DIR = "../data"
RESULTS_DIR = "../results"

# data sources configuration
CDC_URL = 'https://data.cdc.gov/resource/5eh7-pjx8.json?$limit=50000'
CENSUS_URL = 'https://gist.githubusercontent.com/lrli1/820584669eb70989d4d8d20b47d65e52/raw/809ccd245292102bcbae9a8c2c51f537462376f8/gistfile1.txt'
FBI_URL = 'https://gist.githubusercontent.com/lrli1/d560e4d04b6b6e8315900bbe3224fc0c/raw/9dce7b56a93cc5e03e763b87e2dd5e56053525e0/Crime_Data.csv'

