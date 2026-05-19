import streamlit as st

st.set_page_config(
    page_title="Order Tracking - MediCare AI",
    page_icon="📦",
    layout="wide"
)

st.markdown("---")
st.title("📦 Order Tracking")
st.markdown("---")

st.write("Track your medicine orders in real-time and stay updated on delivery status.")

st.divider()

# Order search
col1, col2, col3 = st.columns([2, 2, 1])

with col1:
    order_id = st.text_input(
        "Enter your Order ID:",
        placeholder="e.g., MCA-123456",
        label_visibility="collapsed"
    )

with col2:
    email = st.text_input(
        "Email Address:",
        placeholder="your@email.com",
        label_visibility="collapsed"
    )

with col3:
    track_btn = st.button("Track Order", use_container_width=True)

st.divider()

if track_btn and order_id:
    # Display order details
    st.subheader(f"Order #{order_id}")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Status", "In Transit")
    with col2:
        st.metric("Ordered On", "May 20, 2024")
    with col3:
        st.metric("Est. Delivery", "Today")
    with col4:
        st.metric("Total Amount", "$45.99")
    
    st.divider()
    
    # Order timeline
    st.subheader("📍 Delivery Timeline")
    
    timeline_events = [
        {
            "status": "✅ Order Confirmed",
            "time": "10:00 AM",
            "date": "May 20, 2024",
            "completed": True,
            "description": "Your order has been confirmed and payment received"
        },
        {
            "status": "✅ Pharmacy Processing",
            "time": "10:30 AM",
            "date": "May 20, 2024",
            "completed": True,
            "description": "Medicines are being prepared at our pharmacy"
        },
        {
            "status": "✅ Out for Delivery",
            "time": "02:00 PM",
            "date": "May 20, 2024",
            "completed": True,
            "description": "Your order is out for delivery with our partner"
        },
        {
            "status": "🔄 Arriving Soon",
            "time": "Estimated 04:00 PM",
            "date": "May 20, 2024",
            "completed": False,
            "description": "Expected delivery within the next 2 hours"
        }
    ]
    
    for event in timeline_events:
        col1, col2 = st.columns([1, 5])
        
        with col1:
            if event["completed"]:
                st.success(event["status"])
            else:
                st.info(event["status"])
        
        with col2:
            st.write(f"**{event['time']}** - {event['date']}")
            st.caption(event["description"])
    
    st.divider()
    
    # Order details
    st.subheader("📋 Order Details")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("""
        **Medicines Ordered:**
        - Aspirin 500mg x10
        - Vitamin C 1000mg x5
        - Antacid tablets x1
        """)
    
    with col2:
        st.write("""
        **Delivery Address:**
        123 Health Street
        Medical City, MC 12345
        Contact: +1-XXX-XXX-XXXX
        """)
    
    st.divider()
    
    # Order actions
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("📞 Contact Support", use_container_width=True):
            st.info("Connecting you to support team...")
    
    with col2:
        if st.button("🗺️ View Map", use_container_width=True):
            st.info("Opening delivery tracking map...")
    
    with col3:
        if st.button("🔄 Reschedule", use_container_width=True):
            st.info("Opening reschedule options...")
    
elif track_btn:
    st.warning("⚠️ Please enter a valid Order ID to track your order.")

else:
    st.info("💡 Enter your Order ID above to track your medicine order in real-time.")

st.divider()

# Recent orders section (if no order ID entered)
if not track_btn:
    st.subheader("📨 Recent Orders")
    
    recent_orders = [
        {"id": "MCA-123456", "date": "May 20, 2024", "status": "In Transit", "total": "$45.99"},
        {"id": "MCA-123455", "date": "May 18, 2024", "status": "Delivered", "total": "$32.50"},
        {"id": "MCA-123454", "date": "May 15, 2024", "status": "Delivered", "total": "$28.75"},
    ]
    
    for order in recent_orders:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.write(f"**{order['id']}**")
        with col2:
            st.caption(order['date'])
        with col3:
            if order['status'] == "Delivered":
                st.success(order['status'])
            else:
                st.info(order['status'])
        with col4:
            st.write(order['total'])
        
        if st.button(f"Track {order['id']}", key=f"track_{order['id']}", use_container_width=True):
            order_id = order['id']
            st.rerun()

st.divider()

st.subheader("❓ Frequently Asked Questions")

with st.expander("How can I cancel my order?"):
    st.write("""
    You can cancel your order within 15 minutes of placing it. 
    Go to your order details and click the cancel button.
    """)

with st.expander("Can I change my delivery address?"):
    st.write("""
    Yes, you can change the delivery address before the order is out for delivery.
    Contact our support team for assistance.
    """)

with st.expander("What if my order is delayed?"):
    st.write("""
    If your order is delayed beyond the estimated delivery time, 
    contact our support team for a refund or reshipping.
    """)
