import streamlit as st

st.set_page_config(page_title="Dashboard", page_icon="📊")

if not st.session_state.get("authenticated", False):
    st.warning("Please log in to access this page.")
    st.stop()

st.title("Dashboard")
st.write("Welcome to your AI Toolkit Dashboard! Here you can see an overview of your tools and usage.")

st.subheader("Quick Stats")
st.info("Total tools used: 5")
st.success("Active projects: 2")
st.warning("Pending tasks: 1")










