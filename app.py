import streamlit as st

# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="MediCare AI - Smart Pharmacy",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# API Access
# -------------------------------

st.sidebar.title("💊 MediCare AI")

st.sidebar.subheader(
    "🔑 API Access"
)

if "gemini_key" not in st.session_state:
    st.session_state["gemini_key"] = ""

if "openai_key" not in st.session_state:
    st.session_state["openai_key"] = ""

gemini_key = st.sidebar.text_input(
    "Gemini API Key",
    type="password",
    placeholder="Paste Gemini API Key"
)

openai_key = st.sidebar.text_input(
    "OpenAI API Key (optional)",
    type="password",
    placeholder="Paste OpenAI Key"
)

if st.sidebar.button(
    "Activate Access",
    key="activate_button"
):

    st.session_state[
        "gemini_key"
    ] = gemini_key

    st.session_state[
        "openai_key"
    ] = openai_key

    st.sidebar.success(
        "✅ Access Activated"
    )


st.sidebar.divider()

st.sidebar.info("""

24/7 AI Medical Support

Medicine Search

AI Chatbot

Order Tracking

Medicine Upload

""")


# lock site until key entered

if not st.session_state[
    "gemini_key"
]:

    st.warning("""

🔒 Please enter your
Gemini API key from
the sidebar.

Then click:

Activate Access

""")

    st.stop()

# -------------------------------
# CSS
# -------------------------------

st.markdown("""
<style>

[data-testid="stMetricValue"]{
font-size:28px;
}

.hero{
background:
linear-gradient(
135deg,
#667eea 0%,
#764ba2 100%
);

padding:40px;

border-radius:15px;

text-align:center;

color:white;

margin-bottom:30px;
}

.review{
background:#f0f2f6;

padding:15px;

border-radius:10px;

border-left:5px solid blue;

margin:10px;
}

.tip{

background:#fff3cd;

padding:15px;

border-radius:10px;

margin:10px;

}

</style>

""",unsafe_allow_html=True)


# -------------------------------
# Hero
# -------------------------------

st.markdown("""

<div class="hero">

<h1>

🏥 MediCare AI

</h1>

<h3>

Smart Pharmacy &
Healthcare Platform

</h3>

<p>

AI powered healthcare
assistant platform

</p>

</div>

""",unsafe_allow_html=True)


# -------------------------------
# Categories
# -------------------------------

st.subheader(
"📚 Featured Categories"
)

c1,c2,c3,c4=st.columns(4)

with c1:
    st.metric(
    "💊 Pain Relief",
    "2500+"
    )

with c2:
    st.metric(
    "🤧 Cold & Flu",
    "1800+"
    )

with c3:
    st.metric(
    "❤️ Heart Care",
    "950+"
    )

with c4:
    st.metric(
    "🧠 Mental Health",
    "1200+"
    )

st.divider()

# -------------------------------
# Quick Links
# -------------------------------

st.subheader(
"🚀 Get Started"
)

q1,q2,q3,q4=st.columns(4)

with q1:

    if st.button(
        "🔍 Search",
        width="stretch",
        key="search_page"
    ):

        st.switch_page(
        "pages/3_Medicine_Search.py"
        )


with q2:

    if st.button(
        "💬 Chatbot",
        width="stretch",
        key="chat_page"
    ):

        st.switch_page(
        "pages/4_AI_Chatbot.py"
        )


with q3:

    if st.button(
        "📸 Upload",
        width="stretch",
        key="upload_page"
    ):

        st.switch_page(
        "pages/8_Upload_Medicine.py"
        )


with q4:

    if st.button(
        "❓ FAQ",
        width="stretch",
        key="faq_page"
    ):

        st.switch_page(
        "pages/7_FAQ.py"
        )

st.divider()

st.caption("""

© 2026 MediCare AI

Educational use only

Consult doctors before
medical decisions.

""")