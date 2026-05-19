import streamlit as st

st.set_page_config(
    page_title="About Us - MediCare AI",
    page_icon="ℹ️",
    layout="wide"
)

st.markdown("---")
st.title("ℹ️ About MediCare AI")
st.markdown("---")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🎯 Our Mission")
    st.write("""
We aim to revolutionize healthcare access by leveraging artificial intelligence to provide 
accurate, timely, and reliable medical information to everyone, everywhere. Our mission is to 
democratize healthcare and empower individuals to make informed decisions about their health 
and medications.
    """)

with col2:
    st.subheader("🌟 Our Vision")
    st.write("""
A world where technology and healthcare combine seamlessly to provide:
- Accessible healthcare information 24/7
- Personalized health guidance
- Reliable medicine information
- Fast and affordable pharmacy services
- Improved patient outcomes
    """)

st.divider()

st.subheader("👥 Our Team")
st.write("""
Our dedicated team consists of experienced professionals from healthcare, technology, and customer service sectors.
""")

team_members = [
    {"name": "Dr. Vikram Singh", "role": "Chief Medical Officer", "bio": "MBBS, MD with 15+ years of healthcare experience"},
    {"name": "Priya Desai", "role": "AI/ML Lead", "bio": "PhD in Computer Science, specializes in healthcare AI"},
    {"name": "Rahul Menon", "role": "CTO", "bio": "Full-stack developer with expertise in healthcare applications"},
    {"name": "Sarah Johnson", "role": "Customer Success", "bio": "Dedicated to ensuring excellent customer experience"},
]

col1, col2 = st.columns(2)

for i, member in enumerate(team_members):
    if i < 2:
        with col1:
            st.write(f"**{member['name']}** - *{member['role']}*")
            st.caption(member['bio'])
    else:
        with col2:
            st.write(f"**{member['name']}** - *{member['role']}*")
            st.caption(member['bio'])

st.divider()

st.subheader("🏆 Why Choose MediCare AI?")

benefits = [
    ("✅ Accuracy", "Medical data verified by healthcare professionals"),
    ("✅ Accessibility", "Available 24/7 for your convenience"),
    ("✅ Technology", "Powered by cutting-edge AI and machine learning"),
    ("✅ Security", "Your data is encrypted and HIPAA compliant"),
    ("✅ Support", "Expert help whenever you need it"),
    ("✅ Affordability", "Competitive prices and regular discounts"),
]

col1, col2, col3 = st.columns(3)

for i, (title, description) in enumerate(benefits):
    if i < 2:
        with col1:
            st.write(f"**{title}**")
            st.caption(description)
    elif i < 4:
        with col2:
            st.write(f"**{title}**")
            st.caption(description)
    else:
        with col3:
            st.write(f"**{title}**")
            st.caption(description)

st.divider()

st.subheader("📞 Get In Touch")
st.write("""
We'd love to hear from you! Reach out to us with any questions or feedback.
""")

contact_info = """
- **Email**: info@medcare-ai.com
- **Phone**: +1-800-MEDCARE
- **Address**: MediCare AI Building, Healthcare District, Tech City
- **Hours**: 24/7 Support Available
"""

st.markdown(contact_info)

st.divider()

st.markdown("""
<div style="text-align: center; color: #666; font-size: 12px;">
    <p>© 2024 MediCare AI. All rights reserved.</p>
    <p>⚕️ We prioritize your health and privacy above all else.</p>
</div>
""", unsafe_allow_html=True)
