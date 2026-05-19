import streamlit as st
from chatbot import get_response

st.set_page_config(
    page_title="AI Chatbot - MediCare AI",
    page_icon="💬",
    layout="wide"
)

st.markdown("---")
st.title("💬 AI Medical Chatbot")
st.markdown("---")

st.write("Chat with our AI assistant for instant health guidance, medicine information, and support.")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
chat_container = st.container()
with chat_container:
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

st.divider()

# Chat input section
col1, col2 = st.columns([5, 1])

with col1:
    user_input = st.chat_input(
        "Ask me about medicines, symptoms, healthcare...",
        key="user_input"
    )

with col2:
    if st.button("🗑️ Clear", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

# Process user message
if user_input:
    # Add user message to history
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_input
    })
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_response(user_input)
            st.markdown(response)
    
    # Add assistant message to history
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": response
    })

st.divider()

# Quick questions section
if len(st.session_state.chat_history) == 0:
    st.subheader("💡 Quick Questions")
    st.write("Try asking one of these questions:")
    
    quick_questions = [
        "What are the common side effects of Paracetamol?",
        "How long does it take for Ibuprofen to work?",
        "Can I take antibiotics with milk?",
        "What are natural ways to reduce fever?",
        "Is it safe to mix medicines?",
    ]
    
    for question in quick_questions:
        if st.button(question, use_container_width=True):
            st.session_state.chat_history.append({
                "role": "user",
                "content": question
            })
            
            with st.chat_message("user"):
                st.markdown(question)
            
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = get_response(question)
                    st.markdown(response)
            
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": response
            })
            
            st.rerun()

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.info("""
    ℹ️ **About Our AI Assistant**
    
    - Powered by Gemini AI with OpenAI fallback
    - Available 24/7
    - Handles multiple topics
    - Provides instant responses
    """)

with col2:
    st.warning("""
    ⚠️ **Important Disclaimer**
    
    - For medical emergencies, call 911
    - Not a substitute for professional medical advice
    - Always consult healthcare professionals
    - Information is for educational purposes only
    """)
