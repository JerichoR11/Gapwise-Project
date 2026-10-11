from fastapi import FastAPI, HTTPException  
from pathlib import Path
# from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
#---------------------------------------------------------
# from sqlalchemy.orm import Session
# from app.database import get_db
# from app import modles, get_schemas # for the database
# from app.service.scoring import calculate_readiness, find_gaps # services to add
# from app.services.coverage import update_coverage #audit logs
app = FastAPI(
    title="Gapwise API",
    description="Maps NIST SP 800-53 and CSA CCM controls to policies, "
                "scores audit readiness, and lists gaps.",
    version="0.1.0",
)

# Frameworks that will be used for validation
VALID_FRAMEWORKS = {"NIST", "CCM"}
BASE_DIR = Path(__file__).parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")

def check_framework(framework: str) -> str:
    """Normalize and validate the framework name from the URL."""
    framework = framework.upper()
    if framework not in VALID_FRAMEWORKS:
        raise HTTPException(status_code=404, detail=f"Unknown framework: {framework}")
    return framework
# run command  .venv\Scripts\Activate.ps1 
# py -m uvicorn app.main:app --reload
# http://localaddress:PORTNUMBER/docs
#October 11: new command  uv run fastapi dev main.py

# ----------------------------------------------------------------------------
# Health Check to check if the Application is working
# ----------------------------------------------------------------------------


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {"title": "Gapwise"})
@app.get("/dashboard",response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse(request, "dashboard.html", {"title": "dashboard"})