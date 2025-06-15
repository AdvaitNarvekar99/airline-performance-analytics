from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()  # Load .env values into environment

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)

with open(os.path.join("sql", "create_schema.sql"), "r") as f:
    schema_sql = f.read()

conn.autocommit = True
cur = conn.cursor()
cur.execute(schema_sql)
cur.close()
conn.close()

print("✅ Schema created securely.")