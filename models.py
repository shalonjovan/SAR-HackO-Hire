from pydantic import BaseModel
from typing import List, Dict, Any


class AlertRequest(BaseModel):
    alert_id: str
    account_id: str
    customer_id: str


class CaseData(BaseModel):
    alert: Dict[str, Any]
    account: Dict[str, Any]
    transactions: List[Dict[str, Any]]
    kyc: Dict[str, Any]
