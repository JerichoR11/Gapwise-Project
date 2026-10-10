from fastapi import FastAPI, HTTPException  

app = FastAPI(
    title="Gapwise API",
    description="Maps NIST SP 800-53 and CSA CCM controls to policies, "
                "scores audit readiness, and lists gaps.",
    version="0.1.0",
)

# Frameworks that will be used for validation
VALID_FRAMEWORKS = {"NIST", "CCM"}


def check_framework(framework: str) -> str:
    """Normalize and validate the framework name from the URL."""
    framework = framework.upper()
    if framework not in VALID_FRAMEWORKS:
        raise HTTPException(status_code=404, detail=f"Unknown framework: {framework}")
    return framework
# run command  .venv\Scripts\Activate.ps1 
# py -m uvicorn app.main:app --reload
# http://localaddress:PORTNUMBER/docs
#

# ----------------------------------------------------------------------------
# Health Check to check if the Application is working
# ----------------------------------------------------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}
