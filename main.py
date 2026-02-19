from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models import AlertRequest
from services import build_case_data, CASE_STORE
from generator import generateSAR

app = FastAPI(title="SAR Prototype Service")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("test_data_access.html", {"request": request})


@app.post("/alert")
def receive_alert(alert: AlertRequest):
    if alert.alert_id in CASE_STORE:
        raise HTTPException(status_code=400, detail="Alert already processed")

    case_data = build_case_data(alert)
    CASE_STORE[alert.alert_id] = case_data

    return {
        "message": "Case built successfully",
        "alert_id": alert.alert_id
    }


@app.get("/data/{alert_id}")
def get_case(alert_id: str):
    if alert_id not in CASE_STORE:
        raise HTTPException(status_code=404, detail="Case not found")

    return CASE_STORE[alert_id]


@app.get("/case/{alert_id}")
def get_SAR(alert_id: str):
    if alert_id not in CASE_STORE:
        raise HTTPException(status_code=404, detail="SAR not found")

    return generateSAR(alert_id)


@app.get("/all")
def get_all_cases():
    return CASE_STORE
