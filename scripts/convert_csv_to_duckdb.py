import os
import duckdb

current_dir = os.path.dirname(__file__)
csv_path = os.path.join(current_dir, '..', 'weather.csv')
db_path = os.path.join(current_dir, '..', 'weather.duckdb')  # DuckDB file path

conn = duckdb.connect(db_path)

conn.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        event_start TIMESTAMP,
        belief_horizon_in_sec INTEGER,
        event_value DOUBLE,
        sensor TEXT,
        unit TEXT
    )
""")

conn.execute(f"COPY weather FROM '{csv_path}' (AUTO_DETECT TRUE)")

# Optional: Query the table to verify the data was imported
query = "SELECT * FROM weather LIMIT 5"
result = conn.execute(query).fetchdf()
print(result)

conn.close()
