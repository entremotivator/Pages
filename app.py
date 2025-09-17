import streamlit as st
from supabase import create_client, Client
from st_supabase_connection import SupabaseConnection

st.set_page_config(page_title="AI Toolkit", page_icon="🤖")
st.title("Welcome to the AI Toolkit")

# Initialize connection. Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    url = st.secrets.get("SUPABASE_URL", "https://ejvzdfnspcwcazltweig.supabase.co")
    key = st.secrets.get("SUPABASE_ANON_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVqdnpkZm5zcGN3Y2F6bHR3ZWlnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTc0NjM5NjQsImV4cCI6MjA3MzAzOTk2NH0.Qga-V6HVc5kpnTlTraxxO6fxvQEfTYGDFeDWhKNbobU")
    return create_client(url, key)

supabase: Client = init_connection()

# --- Authentication --- #
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
    st.session_state["username"] = None
    st.session_state["user_id"] = None

with st.sidebar:
    st.subheader("Authentication")
    if not st.session_state["authenticated"]:
        with st.form("login_form"):
            st.markdown("### Login / Sign Up")
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            login_button = st.form_submit_button("Login")
            signup_button = st.form_submit_button("Sign Up")

            if login_button:
                try:
                    user_data = supabase.auth.sign_in_with_password({"email": email, "password": password})
                    if user_data.user:
                        st.session_state["authenticated"] = True
                        st.session_state["username"] = user_data.user.email
                        st.session_state["user_id"] = user_data.user.id
                        st.sidebar.success(f"Welcome {st.session_state['username']}!")
                        st.rerun()
                    else:
                        st.sidebar.error("Invalid login credentials.")
                except Exception as e:
                    st.sidebar.error(f"Login failed: {e}")

            if signup_button:
                try:
                    user_data = supabase.auth.sign_up({"email": email, "password": password})
                    if user_data.user:
                        st.session_state["authenticated"] = True
                        st.session_state["username"] = user_data.user.email
                        st.session_state["user_id"] = user_data.user.id
                        st.sidebar.success(f"Account created and logged in as {st.session_state['username']}!")
                        st.rerun()
                    else:
                        st.sidebar.error("Failed to create account.")
                except Exception as e:
                    st.sidebar.error(f"Sign up failed: {e}")
    else:
        st.sidebar.success(f"Welcome {st.session_state['username']}!")
        if st.sidebar.button("Logout"):
            supabase.auth.sign_out()
            st.session_state["authenticated"] = False
            st.session_state["username"] = None
            st.session_state["user_id"] = None
            st.rerun()

if st.session_state["authenticated"]:
    st.write("You are logged in. Use the sidebar to navigate to other pages.")
else:
    st.write("Please log in or sign up using the sidebar to access the AI Toolkit pages.")


