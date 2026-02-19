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
    Generate a formal Suspicious Activity Report (SAR) based on the following alert data.
    Include sections for:
    1. Subject Information
    2. Suspicious Activity Description
    3. Transaction Analysis
    4. Conclusion/Recommendation

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
