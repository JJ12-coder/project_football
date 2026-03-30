from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from sqlmodel import Session, select
from models import engine, Teams

app = FastAPI()


@app.get("/teams")
async def get_teams():
    with Session(engine) as session:
        teams = session.exec(
            select(Teams).order_by(Teams.category)
        ).all()

    return [
        {
            "teamID": team.teamID,
            "name": team.name,
            "season": team.season,
            "category": team.category,
            "record": team.record,
            "wins": team.wins,
            "losses": team.losses,
            "winPct": team.winPct,
            "pointsFor": team.pointsFor,
            "pointsAgainst": team.pointsAgainst,
            "pointDifferential": team.pointDifferential,
            "playoffWins": team.playoffWins,
            "playoffLosses": team.playoffLosses,
            "totalRecord": team.totalRecord,
            "turnoverMargin": team.turnoverMargin,
        }
        for team in teams
    ]


@app.get("/best")
async def get_best_team():
    with Session(engine) as session:
        team = session.exec(
            select(Teams).where(Teams.category == "Best")
        ).first()

    if not team:
        return {"error": "Team not found"}

    return {
        "teamID": team.teamID,
        "name": team.name,
        "season": team.season,
        "category": team.category,
        "record": team.record,
        "wins": team.wins,
        "losses": team.losses,
        "winPct": team.winPct,
        "pointsFor": team.pointsFor,
        "pointsAgainst": team.pointsAgainst,
        "pointDifferential": team.pointDifferential,
        "playoffWins": team.playoffWins,
        "playoffLosses": team.playoffLosses,
        "totalRecord": team.totalRecord,
        "turnoverMargin": team.turnoverMargin,
    }


@app.get("/worst")
async def get_worst_team():
    with Session(engine) as session:
        team = session.exec(
            select(Teams).where(Teams.category == "Worst")
        ).first()

    if not team:
        return {"error": "Team not found"}

    return {
        "teamID": team.teamID,
        "name": team.name,
        "season": team.season,
        "category": team.category,
        "record": team.record,
        "wins": team.wins,
        "losses": team.losses,
        "winPct": team.winPct,
        "pointsFor": team.pointsFor,
        "pointsAgainst": team.pointsAgainst,
        "pointDifferential": team.pointDifferential,
        "playoffWins": team.playoffWins,
        "playoffLosses": team.playoffLosses,
        "totalRecord": team.totalRecord,
        "turnoverMargin": team.turnoverMargin,
    }


app.mount("/", StaticFiles(directory="static", html=True), name="static")