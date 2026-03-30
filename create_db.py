import pandas as pd
import sqlite3

DB_PATH = "superbowl.db"

teams = pd.read_csv("teams.csv")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

def sqlite_type(dtype):
    if pd.api.types.is_integer_dtype(dtype):
        return "INTEGER"
    elif pd.api.types.is_float_dtype(dtype):
        return "REAL"
    else:
        return "TEXT"

cols = ", ".join(
    f'"{c}" {sqlite_type(teams[c])}' for c in teams.columns
)

cur.execute(f'CREATE TABLE teams ({cols}, PRIMARY KEY ("teamID"))')

teams.to_sql("teams", conn, if_exists="append", index=False)

conn.commit()
conn.close()
print("superbowl.db created successfully.")