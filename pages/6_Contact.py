import streamlit as st

st.set_page_config(
    page_title="Contact Us - MediCare AI",
    page_icon="📞",
    layout="wide"
)

st.markdown("---")
st.title("📞 Contact Us")
st.markdown("---")

st.write("We'd love to hear from you! Get in touch with us for any questions or feedback.")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📧 Send us a Message")
    
    with st.form("contact_form"):
        name = st.text_input(
            "Full Name *",
            placeholder="Your Name"
        )
        
        email = st.text_input(
            "Email Address *",
            placeholder="your@email.com"
        )
        
        phone = st.text_input(
            "Phone Number",
            placeholder="+1-XXX-XXX-XXXX"
        )
        
        subject = st.selectbox(
            "Subject *",
            [
                "General Inquiry",
                "Technical Support",
                "Billing Question",
                "Medical Question",
                "Feedback",
                "Partnership Opportunity",
                "Other"
            ]
        )
        
        message = st.text_area(
            "Your Message *",
            placeholder="Tell us how we can help...",
            height=150
        )
        
        submitted = st.form_submit_button("Send Message", use_container_width=True)
        
        if submitted:
            if name and email and message:
                st.success("✅ Thank you! Your message has been sent successfully.")
                st.write("We'll get back to you within 24 hours.")
            else:
                st.error("⚠️ Please fill in all required fields (marked with *).")

with col2:
    st.subheader("📍 Contact Information")
    
    st.markdown("""
    ### 📧 Email
    - **Support**: support@medcare-ai.com
    - **Sales**: sales@medcare-ai.com
    - **Partnerships**: partner@medcare-ai.com
    
    ### 📱 Phone
    - **Toll Free**: +1-800-MEDCARE (633-2273)
    - **International**: +1-202-555-0147
    - **WhatsApp**: +1-202-555-0147
    
    ### 🏢 Address
    MediCare AI Building
    100 Health Avenue
    Medical District
    Healthcare City, HC 12345
    USA
    
    ### 🕐 Business Hours
    - **Monday-Friday**: 9:00 AM - 9:00 PM
    - **Saturday**: 10:00 AM - 6:00 PM
    - **Sunday**: 11:00 AM - 5:00 PM
    - **24/7 Emergency Support**: Available
    """)

st.divider()

st.subheader("🔗 Follow Us on Social Media")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.write("📘 [Facebook](https://facebook.com/medcareal)")
with col2:
    st.write("𝕏 [Twitter](https://twitter.com/medcareal)")
with col3:
    st.write("📷 [Instagram](https://instagram.com/medcareal)")
with col4:
    st.write("💼 [LinkedIn](https://linkedin.com/company/medcare-ai)")

st.divider()

st.subheader("🗺️ Office Locations")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("**🇺🇸 USA Headquarters**")
    st.caption("""
    MediCare AI Building
    100 Health Avenue
    Healthcare City, HC 12345
    """)

with col2:
    st.write("**🇮🇳 Asia Operations**")
    st.caption("""
    MediCare AI India
    Tech Park Building
    Bangalore, KA 560001
    """)

with col3:
    st.write("**🇬🇧 Europe Office**")
    st.caption("""
    MediCare AI Europe
    Health Square
    London, UK
    """)

st.divider()

st.subheader("💬 Live Chat Support")

st.info("""
💬 Our live chat team is available 24/7 to help you with:
- Product questions
- Technical support
- Order issues
- General inquiries

Click the chat icon at the bottom right to start a conversation!
""")

st.divider()

st.subheader("❓ Quick Answers")

with st.expander("What's your response time?"):
    st.write("""
    - Email: Within 24 hours
    - Phone: Immediate (during business hours)
    - Live Chat: Within 5 minutes
    """)

with st.expander("Do you offer support in multiple languages?"):
    st.write("""
    Yes! We support:
    - English
    - Spanish
    - French
    - Hindi
    - And more...
    """)

with st.expander("How do I report a problem?"):
    st.write("""
    You can report issues through:
    1. This contact form
    2. Email to support@medcare-ai.com
    3. Call our toll-free number
    4. Live chat support
    """)

st.markdown("""
---
<div style="text-align: center; color: #666; font-size: 12px;">
    <p>© 2024 MediCare AI. All rights reserved.</p>
    <p>We're here to help. Don't hesitate to reach out!</p>
</div>
""", unsafe_allow_html=True)
