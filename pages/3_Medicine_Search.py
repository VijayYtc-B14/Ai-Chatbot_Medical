import streamlit as st
from chatbot import get_medicine_info

st.set_page_config(
    page_title="Medicine Search - MediCare AI",
    page_icon="🔍",
    layout="wide"
)

st.markdown("---")
st.title("🔍 Medicine Search & Database")
st.markdown("---")

st.write("Search for medicines and get detailed information about their uses, side effects, and dosages.")

# Search section
col1, col2 = st.columns([4, 1])

with col1:
    medicine_name = st.text_input(
        "Enter medicine name:",
        placeholder="e.g., Aspirin, Paracetamol, Amoxicillin...",
        label_visibility="collapsed"
    )

with col2:
    search_button = st.button("🔍 Search", use_container_width=True)

st.divider()

if search_button and medicine_name:
    with st.spinner(f"Searching for {medicine_name}..."):
        result = get_medicine_info(medicine_name)
        st.markdown(result)
        
        st.divider()
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("💬 Chat about this medicine"):
                st.session_state.page = "AI_Chatbot"
                st.rerun()
        
        with col2:
            if st.button("📋 Add to cart"):
                st.success(f"✅ {medicine_name} added to cart!")

elif search_button:
    st.warning("⚠️ Please enter a medicine name to search.")

st.divider()

# Popular medicines section
st.subheader("🏥 Popular Medicines")

popular_meds = [
    "Paracetamol",
    "Aspirin",
    "Ibuprofen",
    "Amoxicillin",
    "Omeprazole",
    "Vitamin C",
    "Loperamide",
    "Antihistamine"
]

cols = st.columns(4)
for i, med in enumerate(popular_meds):
    with cols[i % 4]:
        if st.button(med, use_container_width=True):
            medicine_name = med
            search_button = True

st.divider()

# Medicine categories
st.subheader("📚 Browse by Category")

categories = {
    "💊 Pain Relief": ["Paracetamol", "Ibuprofen", "Aspirin"],
    "🤧 Cold & Cough": ["Cough syrup", "Antihistamine", "Decongestant"],
    "❤️ Heart Care": ["Aspirin", "Amlodipine", "Metoprolol"],
    "🩺 Diabetes": ["Metformin", "Glipizide", "Insulin"],
    "🧠 Mental Health": ["Sertraline", "Fluoxetine", "Alprazolam"],
    "🏥 Antibiotics": ["Amoxicillin", "Azithromycin", "Ciprofloxacin"],
}

tabs = st.tabs([category for category in categories.keys()])

for tab, (category, medicines) in zip(tabs, categories.items()):
    with tab:
        cols = st.columns(3)
        for i, medicine in enumerate(medicines):
            with cols[i % 3]:
                st.write(f"**{medicine}**")
                if st.button(f"View {medicine}", key=f"view_{medicine}"):
                    st.session_state.selected_medicine = medicine
                    st.rerun()

st.divider()

st.info("""
💡 **Tips for Medicine Search:**
- Search by generic name or brand name
- Use partial names if you're not sure
- Check interactions before taking new medicines
- Always follow dosage instructions
- Consult a doctor before taking new medicines
""")

st.warning("""
⚠️ **Disclaimer:** This information is for educational purposes only. 
Always consult a healthcare professional before starting any medication.
""")
