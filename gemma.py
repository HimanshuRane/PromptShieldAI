import os
import json
from google import genai
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT

# Load environment variables
load_dotenv()

# Create Gemma client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_prompt(user_prompt):
    """
    Sends the user's prompt to Gemma and returns structured JSON.
    """

    try:
        response = client.models.generate_content(
            model="models/gemma-4-31b-it",
            contents=f"""
{SYSTEM_PROMPT}

User Prompt:
{user_prompt}
"""
        )

        text = response.text.strip()

        # Remove markdown if Gemma accidentally returns it
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        return json.loads(text)

    except json.JSONDecodeError:

        return {
            "risk_level": "Unknown",
            "privacy_score": 0,
            "safe_to_share": "Unknown",
            "detected_items": [],
            "privacy_risks": [
                "Gemma returned an unexpected response."
            ],
            "recommendations": [
                "Please try again."
            ],
            "sanitized_prompt": user_prompt
        }

    except Exception as e:

        return {
            "risk_level": "Error",
            "privacy_score": 0,
            "safe_to_share": "Unknown",
            "detected_items": [],
            "privacy_risks": [
                str(e)
            ],
            "recommendations": [
                "Check API key or internet connection."
            ],
            "sanitized_prompt": user_prompt
        }