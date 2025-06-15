from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
import os
import sys

# Load environment variables from .env file
load_dotenv()

# Build the database connection string
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

if not all([db_user, db_pass, db_host, db_port, db_name]):
    sys.exit("❌ Missing database credentials in .env file.")

db_url = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"

# Connect to PostgreSQL
try:
    engine = create_engine(db_url)
except Exception as e:
    sys.exit(f"❌ Database connection failed: {e}")

# Load data and push to SQL
try:
    df = pd.read_csv("outputs/Cleaned_Airline_Delay.csv")
    df.to_sql("delays", engine, if_exists="replace", index=False)  # Change to "append" later if needed
    print("✅ Data loaded into 'delays' table successfully.")
except FileNotFoundError:
    sys.exit("❌ CSV file not found. Check path: outputs/Cleaned_Airline_Delay.csv")
except Exception as e:
    sys.exit(f"❌ Failed to load data into SQL: {e}")