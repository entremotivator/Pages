import streamlit as st

st.set_page_config(page_title="Settings", page_icon="⚙️")

if not st.session_state.get("authenticated", False):
    st.warning("Please log in to access this page.")
    st.stop()

st.title("Settings")
st.write("Manage your AI Toolkit settings.")

st.subheader("Profile Settings")
st.text_input("Username", value=st.session_state.get("username", ""))
st.text_input("Email", value=st.session_state.get("user_email", ""))

st.subheader("API Keys")
st.text_input("OpenAI API Key", type="password")
st.text_input("Another API Key", type="password")

st.button("Save Settings")


