from typing import Optional
from sqlmodel import SQLModel, Field, create_engine

DATABASE_URL = "sqlite:///superbowl.db"
engine = create_engine(DATABASE_URL)


class Teams(SQLModel, table=True):
    __tablename__ = "teams"

    teamID: str = Field(primary_key=True)
    name: Optional[str] = None
    season: Optional[int] = None
    category: Optional[str] = None
    record: Optional[str] = None
    wins: Optional[int] = None
    losses: Optional[int] = None
    winPct: Optional[float] = None
    pointsFor: Optional[float] = None
    pointsAgainst: Optional[float] = None
    pointDifferential: Optional[int] = None
    playoffWins: Optional[int] = None
    playoffLosses: Optional[int] = None
    totalRecord: Optional[str] = None
    turnoverMargin: Optional[int] = None