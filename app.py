import streamlit as st
from supabase import create_client, Client
from PIL import Image
import os

# Page configuration with new branding
st.set_page_config(
    page_title="AI Knowledge Hub", 
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Display logo and title
col1, col2 = st.columns([1, 4])
with col1:
    if os.path.exists("assets/logo.png"):
        logo = Image.open("assets/logo.png")
        st.image(logo, width=100)
with col2:
    st.title("AI Knowledge Hub")
    st.markdown("*Your comprehensive resource for AI learning and development*")

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
    st.subheader("🔐 Access Control")
    if not st.session_state["authenticated"]:
        with st.form("login_form"):
            st.markdown("### Sign In")
            st.info("Sign in to access the AI Knowledge Hub resources")
            email = st.text_input("Email", placeholder="Enter your email address")
            password = st.text_input("Password", type="password", placeholder="Enter your password")
            login_button = st.form_submit_button("Sign In", use_container_width=True)

            if login_button:
                if email and password:
                    try:
                        user_data = supabase.auth.sign_in_with_password({"email": email, "password": password})
                        if user_data.user:
                            st.session_state["authenticated"] = True
                            st.session_state["username"] = user_data.user.email
                            st.session_state["user_id"] = user_data.user.id
                            st.sidebar.success(f"Welcome back, {st.session_state['username'].split('@')[0]}!")
                            st.rerun()
                        else:
                            st.sidebar.error("Invalid login credentials.")
                    except Exception as e:
                        st.sidebar.error(f"Login failed: {str(e)}")
                else:
                    st.sidebar.warning("Please enter both email and password.")
        
        st.sidebar.markdown("---")
        st.sidebar.markdown("**Need access?** Contact your administrator.")
    else:
        st.sidebar.success(f"👋 Welcome, {st.session_state['username'].split('@')[0]}!")
        st.sidebar.markdown("---")
        if st.sidebar.button("🚪 Sign Out", use_container_width=True):
            try:
                supabase.auth.sign_out()
            except:
                pass  # Continue with logout even if API call fails
            st.session_state["authenticated"] = False
            st.session_state["username"] = None
            st.session_state["user_id"] = None
            st.rerun()

if st.session_state["authenticated"]:
    st.markdown("---")
    
    # Welcome section
    st.markdown("## 🎯 Welcome to Your AI Learning Journey")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        ### 📖 AI Knowledge Base
        Comprehensive guides, tutorials, and documentation about artificial intelligence, machine learning, and related technologies.
        """)
    
    with col2:
        st.markdown("""
        ### 🦙 Ollama Course
        Step-by-step learning materials and resources for mastering Ollama and local AI model deployment.
        """)
    
    with col3:
        st.markdown("""
        ### 📦 GitHub Resources
        Curated collection of downloadable AI projects, tools, and agent implementations from GitHub repositories.
        """)
    
    st.markdown("---")
    st.info("💡 **Tip:** Use the sidebar navigation to explore different sections of the knowledge hub.")
    
else:
    st.markdown("---")
    
    # Public landing page
    st.markdown("## 🚀 Your Gateway to AI Knowledge")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        Welcome to the **AI Knowledge Hub** - your comprehensive resource for learning about artificial intelligence, 
        machine learning, and AI development tools.
        
        ### What you'll find here:
        
        🧠 **Comprehensive AI Knowledge Base**
        - In-depth guides on AI concepts and technologies
        - Best practices for AI development
        - Latest trends and research insights
        
        🦙 **Ollama Learning Course**
        - Complete tutorials for local AI model deployment
        - Step-by-step guides and practical examples
        - Advanced configuration and optimization tips
        
        📚 **Curated GitHub Resources**
        - Hand-picked AI projects and tools
        - Downloadable agent implementations
        - Open-source AI libraries and frameworks
        
        ### Ready to start learning?
        Sign in using the sidebar to access all resources and begin your AI journey.
        """)
    
    with col2:
        st.markdown("""
        ### 📊 Platform Stats
        
        **Knowledge Articles:** 50+  
        **Ollama Tutorials:** 25+  
        **GitHub Resources:** 100+  
        **Active Learners:** 500+
        
        ---
        
        ### 🎯 Learning Paths
        - **Beginner:** Start with AI basics
        - **Intermediate:** Dive into Ollama
        - **Advanced:** Explore agent development
        """)


