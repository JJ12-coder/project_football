from csv import DictReader
from pathlib import Path
import sqlite3


BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "superbowl.db"
CSV_PATH = BASE_DIR / "teams.csv"


def convert_value(column: str, value: str):
    if value == "":
        return None

    if column in {"teamID", "name", "category", "record", "totalRecord"}:
        return value
    if column in {"season", "wins", "losses", "pointDifferential", "playoffWins", "playoffLosses", "turnoverMargin"}:
        return int(value)
    if column in {"winPct", "pointsFor", "pointsAgainst"}:
        return float(value)

    return value


schema = """
CREATE TABLE teams (
    teamID TEXT PRIMARY KEY,
    name TEXT,
    season INTEGER,
    category TEXT,
    record TEXT,
    wins INTEGER,
    losses INTEGER,
    winPct REAL,
    pointsFor REAL,
    pointsAgainst REAL,
    pointDifferential INTEGER,
    playoffWins INTEGER,
    playoffLosses INTEGER,
    totalRecord TEXT,
    turnoverMargin INTEGER
)
"""


if DB_PATH.exists():
    DB_PATH.unlink()

with sqlite3.connect(DB_PATH) as conn:
    conn.execute(schema)

    with CSV_PATH.open(newline="", encoding="utf-8") as csv_file:
        reader = DictReader(csv_file)
        rows = []
        for row in reader:
            rows.append(
                {
                    column: convert_value(column, value)
                    for column, value in row.items()
                }
            )

    conn.executemany(
        """
        INSERT INTO teams (
            teamID, name, season, category, record, wins, losses, winPct,
            pointsFor, pointsAgainst, pointDifferential, playoffWins,
            playoffLosses, totalRecord, turnoverMargin
        ) VALUES (
            :teamID, :name, :season, :category, :record, :wins, :losses, :winPct,
            :pointsFor, :pointsAgainst, :pointDifferential, :playoffWins,
            :playoffLosses, :totalRecord, :turnoverMargin
        )
        """,
        rows,
    )

print("superbowl.db created successfully.")