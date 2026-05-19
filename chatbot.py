import os
from dotenv import load_dotenv
from google import genai
from openai import OpenAI

# -----------------------------------
# Load environment variables
# -----------------------------------

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# -----------------------------------
# Initialize clients
# -----------------------------------

gemini_client = None
openai_client = None

if GEMINI_API_KEY:

    gemini_client = genai.Client(
        api_key=GEMINI_API_KEY
    )


if OPENAI_API_KEY:

    openai_client = OpenAI(
        api_key=OPENAI_API_KEY
    )


# -----------------------------------
# System Prompt
# -----------------------------------

SYSTEM_PROMPT = """
You are MediCare AI Assistant,
a professional healthcare chatbot.

Responsibilities:

• Medicine information
• Side effects
• Dosage guidance
• Precautions
• Drug interactions
• Delivery support
• Healthcare support

Rules:

1. Provide informational guidance only

2. Never diagnose diseases

3. Recommend consulting doctors
for serious concerns

4. Keep answers concise

5. Use bullet points where useful

6. Never claim certainty


Always include:

Disclaimer:
This information is educational
and not a substitute for
professional medical advice.
"""


# -----------------------------------
# Main Chat Function
# -----------------------------------

def get_response(user_message: str):

    try:

        if gemini_client:

            print(
                "Using Gemini..."
            )

            response = gemini_client.models.generate_content(

                model="gemini-2.5-flash",

                contents=f"""

{SYSTEM_PROMPT}

User Question:

{user_message}

"""
            )

            if response:

                if hasattr(
                    response,
                    "text"
                ):

                    return response.text

    except Exception as e:

        print(
            "Gemini Error:",
            e
        )



    try:

        if openai_client:

            print(
                "Switching to OpenAI..."
            )

            response = openai_client.chat.completions.create(

                model="gpt-4o-mini",

                messages=[

                    {
                        "role":"system",

                        "content":
                        SYSTEM_PROMPT
                    },

                    {
                        "role":"user",

                        "content":
                        user_message
                    }

                ]
            )

            return response.choices[
                0
            ].message.content

    except Exception as e:

        print(
            "OpenAI Error:",
            e
        )



    return """

⚠ AI service unavailable.

Please try again later.

"""


# -----------------------------------
# Medicine Information
# -----------------------------------

def get_medicine_info(
    medicine_name
):

    prompt = f"""

Provide complete information
about:

{medicine_name}


Include:

1. Generic Name

2. Uses

3. Dosage

4. Side Effects

5. Precautions

6. Storage

7. Drug Interactions

8. Disclaimer

"""

    return get_response(
        prompt
    )


# -----------------------------------
# Drug Interaction Checker
# -----------------------------------

def check_interactions(
    medicines
):

    medicines_text = ", ".join(
        medicines
    )

    prompt = f"""

Check interaction among:

{medicines_text}


Provide:

1. Interactions

2. Severity

3. Recommendations

4. Disclaimer

"""

    return get_response(
        prompt
    )


# -----------------------------------
# Health Tips
# -----------------------------------

def health_tips():

    prompt = """

Give 5 short health tips.

"""

    return get_response(
        prompt
    )


# -----------------------------------
# Delivery Support
# -----------------------------------

def order_support(
    order_id
):

    return f"""

Order ID:
{order_id}

Status:
Out for delivery

Expected:
Tomorrow

"""