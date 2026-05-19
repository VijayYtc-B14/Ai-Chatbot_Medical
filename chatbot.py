import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
from openai import OpenAI

# -----------------------------------
# Load .env as backup
# -----------------------------------

load_dotenv()

# -----------------------------------
# Get keys from Home page input
# fallback -> .env
# -----------------------------------

GEMINI_API_KEY = st.session_state.get(
    "gemini_key",
    os.getenv("GEMINI_API_KEY")
)

OPENAI_API_KEY = st.session_state.get(
    "openai_key",
    os.getenv("OPENAI_API_KEY")
)

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
You are MediCare AI Assistant.

Responsibilities:

• Medicine information
• Side effects
• Dosage guidance
• Precautions
• Drug interactions
• Delivery support
• Healthcare support

Rules:

1. Informational use only
2. Never diagnose disease
3. Recommend doctors
4. Keep answers concise
5. Use bullet points

Always include disclaimer:
Educational only. Not medical advice.
"""

# -----------------------------------
# Main response
# -----------------------------------

def get_response(user_message):

    try:

        if gemini_client:

            response = gemini_client.models.generate_content(

                model="gemini-2.5-flash",

                contents=f"""

{SYSTEM_PROMPT}

User:

{user_message}

"""
            )

            if response and response.text:

                return response.text

    except Exception as e:

        print(
        "Gemini Error:",
        e
        )


    try:

        if openai_client:

            response = openai_client.chat.completions.create(

                model="gpt-4o-mini",

                messages=[

                    {
                    "role":"system",
                    "content":SYSTEM_PROMPT
                    },

                    {
                    "role":"user",
                    "content":user_message
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
⚠ Service unavailable
"""

# -----------------------------------
# Medicine info
# -----------------------------------

def get_medicine_info(
medicine_name
):

    prompt=f"""

Provide:

1 Uses

2 Dosage

3 Side Effects

4 Precautions

for:

{medicine_name}

"""

    return get_response(
    prompt
    )

# -----------------------------------
# Interactions
# -----------------------------------

def check_interactions(
medicines
):

    medicine_text=", ".join(
    medicines
    )

    prompt=f"""

Check interaction:

{medicine_text}

"""

    return get_response(
    prompt
    )