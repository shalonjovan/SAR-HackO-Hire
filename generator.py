import os
import google.generativeai as genai
from dotenv import load_dotenv
from datetime import datetime
from services import CASE_STORE

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def generateSAR(alert_id: str):
    """
    Generates a Suspicious Activity Report (SAR)
    using Gemini based on in-memory case data.
    """

    # 🔥 FIX: No more localhost call
    alert_data = CASE_STORE.get(alert_id)

    if not alert_data:
        return "Case not found."

    today_date = datetime.now().strftime("%Y-%m-%d")

    import os
import google.generativeai as genai
from dotenv import load_dotenv
from datetime import datetime
from services import CASE_STORE

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def generateSAR(alert_id: str):
    """
    Generates a Suspicious Activity Report (SAR)
    using Gemini based on in-memory case data.
    """

    # 🔥 FIX: No more localhost call
    alert_data = CASE_STORE.get(alert_id)

    if not alert_data:
        return "Case not found."

    today_date = datetime.now().strftime("%Y-%m-%d")

    prompt = f"""
You are a financial crime compliance officer at a bank generating an internal Suspicious Activity Report (SAR).

Generate a SAR using ONLY the data provided in the JSON below. Follow these strict rules:
- Do NOT infer criminal intent or speculate beyond the data.
- Use neutral, factual, regulatory-compliant language.
- Clearly separate observed facts from indicators requiring review.
- Do NOT use markdown.
- Use ALL CAPS for section headers.
- Use dashes (-) for bullet points.
- Separate sections with a blank line.

Output EXACTLY this structure:

SUSPICIOUS ACTIVITY REPORT (SAR)
Report ID: {alert_id}
Date Generated: {today_date}

---

SECTION 1 — SUBJECT INFORMATION

SECTION 2 — ACCOUNT SUMMARY

SECTION 3 — ALERT REASON

SECTION 4 — TRANSACTION SUMMARY

SECTION 5 — SUSPICIOUS ACTIVITY INDICATORS

SECTION 6 — NARRATIVE

SECTION 7 — RECOMMENDED ACTION

---
CONFIDENTIAL — FOR INTERNAL COMPLIANCE USE ONLY

Alert Data:
{alert_data}
"""

    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating SAR: {e}"


    try:
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating SAR: {e}"
