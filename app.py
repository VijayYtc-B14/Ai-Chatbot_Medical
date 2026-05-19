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
# Custom CSS
# -------------------------------

st.markdown("""
<style>

[data-testid="stMetricValue"]{
font-size:28px;
}

.hero{
background:linear-gradient(
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
# Sidebar
# -------------------------------

st.sidebar.title(
"💊 MediCare AI"
)

st.sidebar.write(
"Smart Healthcare Platform"
)

st.sidebar.divider()

st.sidebar.info("""
24/7 AI Medical Support

Medicine Search

AI Chatbot

Order Tracking
""")

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

AI powered medical
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
# Stats
# -------------------------------

st.subheader(
"📊 Platform Statistics"
)

a,b,c,d=st.columns(4)

with a:
    st.metric(
    "Users",
    "150K+",
    "+15K"
    )

with b:
    st.metric(
    "Medicines",
    "10K+",
    "+500"
    )

with c:
    st.metric(
    "Orders",
    "500K+",
    "+50K"
    )

with d:
    st.metric(
    "Satisfaction",
    "98%",
    "+2%"
    )

st.divider()

# -------------------------------
# Reviews
# -------------------------------

st.subheader(
"⭐ Customer Reviews"
)

r1,r2,r3=st.columns(3)

with r1:

    st.markdown("""

<div class="review">

Rajesh ⭐⭐⭐⭐⭐

Excellent service.

Fast delivery.

Helpful chatbot.

</div>

""",unsafe_allow_html=True)

with r2:

    st.markdown("""

<div class="review">

Priya ⭐⭐⭐⭐⭐

Medicine search
works very well

</div>

""",unsafe_allow_html=True)

with r3:

    st.markdown("""

<div class="review">

Amit ⭐⭐⭐⭐

Great experience

</div>

""",unsafe_allow_html=True)

st.divider()

# -------------------------------
# Health Tips
# -------------------------------

st.subheader(
"💡 Daily Health Tips"
)

t1,t2=st.columns(2)

with t1:

    st.markdown(
    """
<div class="tip">

💧 Drink water daily

</div>
""",
unsafe_allow_html=True
)

    st.markdown(
    """
<div class="tip">

🏃 Exercise 30 mins

</div>
""",
unsafe_allow_html=True
)

with t2:

    st.markdown(
"""
<div class="tip">

😴 Sleep 7-9 hours

</div>
""",
unsafe_allow_html=True
)

    st.markdown(
"""
<div class="tip">

🥗 Eat healthy food

</div>
""",
unsafe_allow_html=True
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

# -------------------------------
# Footer
# -------------------------------

st.caption(
"""
© 2026 MediCare AI

Educational purposes only.

Consult healthcare
professionals.

"""
)