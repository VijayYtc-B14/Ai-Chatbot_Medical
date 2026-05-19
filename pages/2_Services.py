import streamlit as st

st.set_page_config(
    page_title="Services - MediCare AI",
    page_icon="⚙️",
    layout="wide"
)

st.markdown("---")
st.title("⚙️ Our Services")
st.markdown("---")

st.subheader("🏥 Comprehensive Healthcare Solutions")
st.write("MediCare AI offers a wide range of services to meet all your healthcare needs.")

st.divider()

# Services tabs
tab1, tab2, tab3, tab4 = st.tabs(["💊 Medicine Services", "🤖 AI Services", "🚚 Delivery", "👨‍⚕️ Support"])

with tab1:
    st.header("💊 Medicine Services")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Medicine Search")
        st.write("""
        - Search by medicine name, brand, or generic
        - View detailed medicine information
        - Check side effects and precautions
        - Compare alternative medicines
        - Check drug interactions
        - View availability and pricing
        """)
        st.info("💡 Tip: Use wildcards for partial searches")
    
    with col2:
        st.subheader("Price Comparison")
        st.write("""
        - Compare prices across pharmacies
        - Find best deals and discounts
        - Track price history
        - Get notifications on price drops
        - Bulk order discounts available
        - Loyalty rewards program
        """)
        st.success("🎉 Get up to 30% off on bulk orders")

with tab2:
    st.header("🤖 AI Services")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("24/7 AI Chatbot")
        st.write("""
        - Instant health guidance
        - Medicine recommendations
        - Symptom checker
        - Health tips and advice
        - Drug interaction checker
        - Delivery status updates
        """)
        st.info("💬 Chat with our AI anytime, anywhere")
    
    with col2:
        st.subheader("Prescription Upload & Analysis")
        st.write("""
        - Upload prescription images (.jpg, .png)
        - AI extracts medicine names
        - Automatic medicine lookup
        - Dosage schedule management
        - Refill reminders
        - Save prescription history
        """)
        st.success("📸 Supports multiple prescription formats")

with tab3:
    st.header("🚚 Delivery Services")
    
    st.write("""
    ### Fast & Reliable Delivery Options
    """)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("⚡ **Express Delivery**")
        st.caption("2-hour delivery in metro areas")
    
    with col2:
        st.write("🌙 **24-Hour Delivery**")
        st.caption("Same-day delivery available")
    
    with col3:
        st.write("🏆 **Standard Delivery**")
        st.caption("24-48 hours nationwide")
    
    st.divider()
    
    st.write("""
    ### Additional Features
    - Free shipping on orders above ₹500
    - Temperature-controlled delivery for sensitive medicines
    - Live tracking with GPS
    - Discreet packaging for privacy
    - Cash on delivery available
    - Multiple payment options
    - Doorstep delivery
    """)

with tab4:
    st.header("👨‍⚕️ Customer Support & Consultation")
    
    st.write("""
    ### Premium Support Services
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Online Doctor Consultation**")
        st.write("""
        - Video consultations with licensed doctors
        - Text chat support
        - Prescription through telemedicine
        - Health report discussions
        - Follow-up consultations
        """)
    
    with col2:
        st.write("**Pharmacist Support**")
        st.write("""
        - Medicine counseling
        - Dosage guidance
        - Side effect information
        - Alternative medicine suggestions
        - Interaction checking
        """)
    
    st.divider()
    
    st.write("""
    ### Contact Support
    - **Email**: support@medcare-ai.com
    - **Phone**: +1-800-MEDCARE
    - **Live Chat**: Available 24/7
    - **WhatsApp**: Support via WhatsApp
    - **Response Time**: Usually within 5 minutes
    """)

st.divider()

st.success("🎯 All services are secure, reliable, and designed with your health in mind.")
