import os
import requests
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generateSAR(alert_id: str):
    """
    Generates a Suspicious Activity Report (SAR) using the Gemini API based on alert data.
    Fetches data from the local /data/{alert_id} endpoint.
    """
    # Fetch data from the local API
    try:
        response = requests.get(f"http://127.0.0.1:8000/data/{alert_id}")
        response.raise_for_status()
        alert_data = response.json()
    except requests.exceptions.RequestException as e:
        return f"Error fetching alert data: {e}"

    # Construct the prompt for Gemini
    prompt = f"""
You are a financial crime compliance officer at a bank generating an internal Suspicious Activity Report (SAR).

Generate a SAR using ONLY the data provided in the JSON below. Follow these strict rules:
- Do NOT infer criminal intent or speculate beyond the data.
- Use neutral, factual, regulatory-compliant language throughout.
- Clearly separate observed facts from indicators requiring review.
- Do NOT use markdown syntax (no **, no __, no #). Use plain text only.
- Use ALL CAPS for section headers exactly as shown below.
- Use dashes (-) for bullet points under each section.
- Separate each section with a blank line.

Output the report in EXACTLY this structure:

SUSPICIOUS ACTIVITY REPORT (SAR)
Report ID: [alert_id from data]
Date Generated: [today's date]

---

SECTION 1 — SUBJECT INFORMATION
- Full Name: [value]
- Customer ID: [value]
- Date of Birth: [value]
- Country of Residence: [value]
- Occupation: [value]

SECTION 2 — ACCOUNT SUMMARY
- Account Open Date: [value]
- KYC Status: [value]
- Risk Rating: [value]
- PEP Flag: [value]
- Sanctions Screening Flag: [value]
- Adverse Media Flag: [value]
- Annual Income (USD): [value]
- Expected Monthly Transaction Volume (USD): [value]
- Last KYC Review Date: [value]

SECTION 3 — ALERT REASON
[Write 1-2 sentences describing the alert trigger based on the reason field in the data.]

SECTION 4 — TRANSACTION SUMMARY
[For each transaction, list it as a numbered entry:]
1. Transaction ID: [value]
   Date/Time: [value]
   Type: [value]
   Channel: [value]
   Amount: [currency] [amount]
   Receiver ID: [value]
   Receiver KYC Status: [value]
   Category: [value]

SECTION 5 — SUSPICIOUS ACTIVITY INDICATORS
[List each indicator as a bullet point starting with -. Be factual and specific.]

SECTION 6 — NARRATIVE
[Write 3-5 full sentences summarizing the customer profile, the observed activity, what makes it notable relative to the customer's profile, and that the activity warrants further review. Do not allege wrongdoing.]

SECTION 7 — RECOMMENDED ACTION
[List 2-4 concrete recommended actions as bullet points starting with -.]

---
CONFIDENTIAL — FOR INTERNAL COMPLIANCE USE ONLY

Alert Data:
{alert_data}
"""

    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating SAR with Gemini: {e}"

if __name__ == "__main__":
    # Example usage
    import sys
    if len(sys.argv) > 1:
        print(generateSAR(sys.argv[1]))
    else:
        print("Please provide an alert_id as an argument.")
