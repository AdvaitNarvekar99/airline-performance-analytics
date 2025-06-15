import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Construct database URL
db_url = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@" \
         f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

engine = create_engine(db_url)

# Choose the SQL file to execute
sql_files = [
    "sql/create_view_carrier_delay_summary.sql",
    "sql/create_view_top_delay_causes.sql",
    "sql/create_view_airport_level_metrics.sql",
    "sql/create_view_monthly_trend.sql"
]

# Execute each SQL file
with engine.connect() as conn:
    for sql_path in sql_files:
        with open(sql_path, "r") as file:
            print(f"▶ Executing {sql_path}...")
            conn.execute(text(file.read()))
            print(f"✅ {sql_path} executed successfully.")