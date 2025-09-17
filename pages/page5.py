import streamlit as st

st.set_page_config(page_title="New Page 5", page_icon="✨")

if not st.session_state.get("authenticated", False):
    st.warning("Please log in to access this page.")
    st.stop()

st.title("New Page 5")
st.write("This is an additional page for the AI Toolkit.")


