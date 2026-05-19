import streamlit as st
from chatbot import get_response
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Upload Medicine - MediCare AI",
    page_icon="📸",
    layout="wide"
)

st.title("📸 Upload & Scan Medicine")
st.markdown("---")

st.write(
    "Upload a medicine image and MediCare AI will provide medicine information."
)

st.divider()

# -------------------------------
# Upload Section
# -------------------------------

uploaded_file = st.file_uploader(
    "Choose Medicine Image",
    type=["jpg","jpeg","png","gif","bmp"]
)

if uploaded_file:

    col1,col2 = st.columns([2,1])

    with col1:

        st.image(
            uploaded_file,
            caption="Uploaded Image",
            width="stretch"
        )

    with col2:

        st.subheader("Image Details")

        st.write(
            f"Type: {uploaded_file.type}"
        )

        st.write(
            f"Size: {uploaded_file.size/1024:.2f} KB"
        )

    st.divider()

    medicine_name = st.text_input(
        "Enter Medicine Name",
        placeholder="Aspirin / Paracetamol..."
    )

    if st.button(
        "🔍 Analyze Medicine",
        width="stretch",
        key="analyze_btn"
    ):

        if medicine_name:

            with st.spinner(
                "Analyzing..."
            ):

                response=get_response(
                f"""
                Provide medicine information:

                {medicine_name}

                Include:

                1. Uses
                2. Dosage
                3. Side Effects
                4. Precautions
                5. Storage
                """
                )

                st.success(
                    f"Information for {medicine_name}"
                )

                st.markdown(
                    response
                )

                st.divider()

                c1,c2,c3=st.columns(3)

                with c1:

                    if st.button(
                        "💬 Chat",
                        width="stretch",
                        key="chat1"
                    ):

                        st.session_state[
                        "selected_medicine"
                        ]=medicine_name

                        st.switch_page(
                        "pages/4_AI_Chatbot.py"
                        )

                with c2:

                    if st.button(
                        "🛒 Add Cart",
                        width="stretch",
                        key="cart1"
                    ):

                        st.success(
                        "Added"
                        )

                with c3:

                    if st.button(
                        "💾 Save",
                        width="stretch",
                        key="save1"
                    ):

                        st.success(
                        "Saved"
                        )

        else:

            st.warning(
                "Enter medicine name"
            )

else:

    st.info("""

### Steps

1 Upload image

2 Enter medicine name

3 AI gives:

- Uses
- Side Effects
- Dosage
- Storage
""")

st.divider()

# -------------------------------
# Manual Search
# -------------------------------

st.subheader(
"🔍 Manual Search"
)

manual_medicine=st.text_input(
"Medicine Name",
placeholder="Paracetamol",
key="manual_search"
)

if st.button(
"Search",
width="stretch",
key="search_btn"
):

    if manual_medicine:

        with st.spinner(
        "Searching..."
        ):

            response=get_response(
            f"""
            Give complete details
            about {manual_medicine}
            """
            )

            st.markdown(
            response
            )

    else:

        st.warning(
        "Enter medicine"
        )


st.divider()

# -------------------------------
# Popular Medicines
# -------------------------------

st.subheader(
"🏥 Popular Medicines"
)

popular_categories={

"💊 Pain & Fever":[
"Aspirin",
"Paracetamol",
"Ibuprofen"
],

"🤧 Cold & Cough":[
"Cough Syrup",
"Antihistamine",
"Decongestant"
],

"💊 Digestive":[
"Antacid",
"Omeprazole",
"Loperamide"
],

"❤️ Heart":[
"Aspirin",
"Amlodipine",
"Metoprolol"
]
}


for category,medicines in popular_categories.items():

    with st.expander(category):

        cols=st.columns(3)

        for i,med in enumerate(
        medicines
        ):

            with cols[i%3]:

                unique_key=(
                f"{category}_{med}_{i}"
                )

                if st.button(
                    med,
                    width="stretch",
                    key=unique_key
                ):

                    st.session_state[
                    "selected_medicine"
                    ]=med

                    st.success(
                    f"Selected {med}"
                    )

st.divider()

st.warning("""

⚠ Disclaimer

This application is for
educational purposes only.

Consult doctors before
taking medicine.

""")

st.info("""

💡 Tips

• Read dosage instructions

• Check side effects

• Verify allergies

• Store properly

""")