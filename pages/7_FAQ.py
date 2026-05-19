import streamlit as st

st.set_page_config(
    page_title="FAQ - MediCare AI",
    page_icon="❓",
    layout="wide"
)

st.markdown("---")
st.title("❓ Frequently Asked Questions")
st.markdown("---")

st.write("Find answers to common questions about MediCare AI, medicines, orders, and more.")

st.divider()

# General Questions
with st.expander("**📱 General Questions**", expanded=True):
    with st.expander("What is MediCare AI?"):
        st.write("""
        MediCare AI is an AI-powered pharmacy platform that provides:
        - Medicine information and search
        - 24/7 AI chatbot support
        - Fast medicine delivery
        - Online consultations
        - Order tracking
        - Prescription management
        """)
    
    with st.expander("Is the platform free to use?"):
        st.write("""
        Basic services are completely free:
        - Medicine search
        - AI chatbot
        - Order tracking
        
        Premium services have a small fee:
        - Online consultations
        - Priority delivery
        - Medicine subscriptions
        """)
    
    with st.expander("How do I create an account?"):
        st.write("""
        1. Download the MediCare AI app or visit our website
        2. Click "Sign Up"
        3. Enter your email and phone number
        4. Verify your email with the code
        5. Complete your profile
        6. Start ordering!
        """)
    
    with st.expander("Is my data safe?"):
        st.write("""
        Yes! We use:
        - 256-bit SSL encryption
        - HIPAA-compliant servers
        - Regular security audits
        - Encrypted databases
        - Two-factor authentication
        - Zero-knowledge storage
        """)

st.divider()

# Medicine & Health Questions
with st.expander("**💊 Medicine & Health Questions**", expanded=False):
    with st.expander("Can the AI provide medical diagnosis?"):
        st.write("""
        No, our AI provides general information only:
        - It's not a substitute for professional medical advice
        - Always consult a doctor for diagnosis
        - For emergencies, call 911
        - Serious symptoms need professional evaluation
        """)
    
    with st.expander("How accurate is the medicine information?"):
        st.write("""
        Our medicine data is:
        - Verified by licensed healthcare professionals
        - Updated regularly from official sources
        - Cross-checked with medical databases
        - Includes FDA/regulatory information
        
        However, always verify with your doctor or pharmacist.
        """)
    
    with st.expander("Can I check for drug interactions?"):
        st.write("""
        Yes! Our AI can:
        - Check interactions between medicines
        - Identify contraindications
        - Provide severity warnings
        - Suggest safer alternatives
        
        Always consult a pharmacist for professional advice.
        """)
    
    with st.expander("What if I'm allergic to a medicine?"):
        st.write("""
        1. Tell our AI about your allergies
        2. We'll note it in your profile
        3. Get alternative suggestions
        4. Consult your doctor for confirmation
        5. Inform the pharmacist before pickup
        """)

st.divider()

# Ordering & Delivery
with st.expander("**🛒 Ordering & Delivery Questions**", expanded=False):
    with st.expander("What's the minimum order value?"):
        st.write("""
        - No minimum order value
        - But we offer free shipping on orders above $20
        - Smaller orders have a $2 shipping fee
        - Sign up discounts available
        """)
    
    with st.expander("How long is delivery?"):
        st.write("""
        **Delivery Options:**
        - Express: 2 hours (select areas)
        - Same-day: By 9 PM (orders before 12 PM)
        - Next-day: By 12 PM
        - Standard: 2-3 business days (nationwide)
        
        Real-time tracking available for all orders.
        """)
    
    with st.expander("What payment methods do you accept?"):
        st.write("""
        We accept:
        - Credit/Debit cards (Visa, Mastercard)
        - Digital wallets (Apple Pay, Google Pay)
        - UPI/Bank transfers
        - Buy Now Pay Later
        - Cash on Delivery (in select areas)
        """)
    
    with st.expander("Can I cancel or modify my order?"):
        st.write("""
        **You can cancel if:**
        - Order is within 15 minutes of placement
        - Order hasn't been confirmed by pharmacy
        
        **To modify:**
        - Contact support within 15 minutes
        - Changes may not be possible after pharmacy processes
        """)
    
    with st.expander("Do you deliver prescription medicines?"):
        st.write("""
        Yes! For prescription medicines:
        1. Upload valid prescription
        2. Our pharmacist verifies it
        3. Medicine is dispensed
        4. Delivered to your address
        
        We accept prescriptions from any doctor/clinic.
        """)

st.divider()

# Account & Technical
with st.expander("**👤 Account & Technical Questions**", expanded=False):
    with st.expander("How do I reset my password?"):
        st.write("""
        1. Click "Forgot Password" on login page
        2. Enter your email
        3. Check your email for reset link
        4. Click the link (valid for 24 hours)
        5. Enter your new password
        6. You're all set!
        """)
    
    with st.expander("Can I have multiple addresses?"):
        st.write("""
        Yes! You can:
        - Add up to 5 addresses
        - Mark one as default
        - Select address while ordering
        - Update addresses anytime
        - Delete old addresses
        """)
    
    with st.expander("Why is the app not working?"):
        st.write("""
        Try these solutions:
        1. Clear app cache
        2. Update to latest version
        3. Restart your phone
        4. Check internet connection
        5. Contact support if issue persists
        """)
    
    with st.expander("How do I delete my account?"):
        st.write("""
        To delete your account:
        1. Go to Settings
        2. Select "Account"
        3. Click "Delete Account"
        4. Enter password for confirmation
        5. Provide reason (optional)
        6. Account deleted permanently
        
        Note: All data will be permanently deleted.
        """)

st.divider()

# Returns & Refunds
with st.expander("**💰 Returns & Refunds**", expanded=False):
    with st.expander("What's your return policy?"):
        st.write("""
        **30-Day Money-Back Guarantee:**
        - Non-prescription medicines: Full return
        - Prescription medicines: Non-returnable
        - Damaged/expired medicines: Full refund
        - Wrong item delivered: Free replacement
        
        Return within 30 days for refund.
        """)
    
    with st.expander("How long do refunds take?"):
        st.write("""
        Refund processing:
        - Initiated: 3-5 business days
        - To your account: 5-7 business days
        - Full refund: 10 business days
        
        We notify you at each step.
        """)
    
    with st.expander("What if I received wrong medicine?"):
        st.write("""
        Contact us immediately:
        1. Call: +1-800-MEDCARE
        2. Email: support@medcare-ai.com
        3. Live chat: Available 24/7
        
        We'll send correct medicine immediately!
        """)

st.divider()

# Subscription & Loyalty
with st.expander("**🎁 Subscription & Loyalty Questions**", expanded=False):
    with st.expander("What's the MediCare Plus membership?"):
        st.write("""
        **MediCare Plus Benefits:**
        - $5.99/month or $49.99/year
        - Free shipping on all orders
        - 15% discount on all medicines
        - Priority customer support
        - Exclusive deals and early access
        - Free health consultations
        """)
    
    with st.expander("How does the rewards program work?"):
        st.write("""
        **Earn Points:**
        - 1 point per $1 spent
        - 2 points per $1 on Plus members
        - Birthday bonus: 100 points
        - Referral: 50 points per friend
        
        **Redeem Points:**
        - 100 points = $1 off
        - Use on any purchase
        """)

st.divider()

st.subheader("💬 Still Need Help?")

col1, col2 = st.columns(2)

with col1:
    st.write("""
    **Contact Us:**
    - Email: support@medcare-ai.com
    - Phone: +1-800-MEDCARE
    - Live Chat: 24/7 Available
    - WhatsApp: +1-202-555-0147
    """)

with col2:
    st.write("""
    **Connect With Us:**
    - Facebook: @medcareal
    - Twitter: @medcareal
    - Instagram: @medcareal
    - LinkedIn: MediCare AI
    """)

st.divider()

st.info("💡 We're here to help! If you didn't find your answer, contact our support team.")
