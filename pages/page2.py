import streamlit as st

st.set_page_config(page_title="AI Tools", page_icon="🛠️")

if not st.session_state.get("authenticated", False):
    st.warning("Please log in to access this page.")
    st.stop()

st.title("AI Tools")
st.write("Explore various AI tools available in your toolkit.")

st.subheader("Text Generation")
st.write("Generate creative text formats, like poems, code, scripts, musical pieces, email, letters, etc.")

st.subheader("Image Analysis")
st.write("Upload an image to get insights and descriptions.")

st.subheader("Data Prediction")
st.write("Use machine learning models to make predictions on your data.")


