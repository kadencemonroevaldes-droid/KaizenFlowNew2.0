from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String, Float, Date
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import date
import pandas as pd, random

app = FastAPI(title="Kaizen Flow Platform")
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# ---- Database ----
engine = create_engine("sqlite:///app/db/kaizen.db", connect_args={"check_same_thread": False})
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

class Idea(Base):
    __tablename__ = "ideas"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    goal = Column(String)
    sdg = Column(String)
    progress = Column(Float)
    date_logged = Column(Date)

Base.metadata.create_all(bind=engine)

def get_summary():
    ideas = session.query(Idea).all()
    df = pd.DataFrame([{"progress": i.progress, "sdg": i.sdg} for i in ideas]) if ideas else pd.DataFrame(columns=["progress","sdg"])
    avg = round(df["progress"].mean(),1) if not df.empty else 0
    sdg_count = df["sdg"].value_counts().to_dict()
    return ideas, avg, sdg_count

# --- Dashboard ---
@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    ideas, avg, sdg_count = get_summary()
    return templates.TemplateResponse("dashboard.html", {"request":request, "ideas":ideas, "avg":avg, "sdg_count":sdg_count})

# --- Tracker ---
@app.get("/tracker", response_class=HTMLResponse)
def tracker(request: Request):
    ideas, avg, sdg_count = get_summary()
    return templates.TemplateResponse("tracker.html", {"request":request, "ideas":ideas, "avg":avg})

@app.post("/add", response_class=RedirectResponse)
def add(title: str = Form(...), goal: str = Form(...), sdg: str = Form(...)):
    new = Idea(title=title, goal=goal, sdg=sdg,
               progress=random.randint(30,100), date_logged=date.today())
    session.add(new)
    session.commit()
    return RedirectResponse("/tracker", status_code=303)

# --- Culture Lens ---
@app.get("/culture", response_class=HTMLResponse)
def culture(request: Request):
    c = random.choice([
        ("Collectivist","Team harmony and shared accountability."),
        ("Individualist","Personal ownership and initiative."),
        ("High-Context","Meaning via tone and relationships."),
        ("Low-Context","Direct, explicit communication.")
    ])
    return templates.TemplateResponse("culture.html", {"request":request, "culture":c})
