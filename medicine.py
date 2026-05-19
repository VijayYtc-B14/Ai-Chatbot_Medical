import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

gemini_client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MEDICINE_PROMPT = """
You are a pharmacy medicine database AI. Provide accurate medical information about medicines.

When given a medicine name, provide:
1. Generic Name
2. Brand Names
3. Uses
4. Dosage
5. Side Effects
6. Contraindications
7. Drug Interactions
8. Storage Instructions
9. Price Range (approximate)

DISCLAIMER: This is for informational purposes only. Always consult a healthcare professional.
"""

def search_medicine(medicine_name):
    """Search for medicine information."""
    try:
        response = gemini_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"{MEDICINE_PROMPT}\n\nMedicine Name: {medicine_name}"
        )
        return response.text
    except Exception as e:
        return f"Error searching medicine: {str(e)}"

def get_medicine_alternatives(medicine_name):
    """Get alternative medicines for a given medicine."""
    try:
        response = gemini_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""You are a pharmacist. Suggest safe alternatives/generic equivalents for: {medicine_name}
            
List alternatives with:
- Generic Name
- Brand Names
- Why it's a good alternative
- Price comparison

DISCLAIMER: Consult a doctor before switching medicines."""
        )
        return response.text
    except Exception as e:
        return f"Error finding alternatives: {str(e)}"

def check_price(medicine_name):
    """Get approximate pricing for a medicine."""
    try:
        response = gemini_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"""Provide approximate pricing information for: {medicine_name}
            
Include:
- Price range (typical market prices)
- Dosage variants and their prices
- Where to buy (pharmacy types)
- Any available discounts or offers

Note: Prices vary by region and pharmacy."""
        )
        return response.text
    except Exception as e:
        return f"Error checking price: {str(e)}"
