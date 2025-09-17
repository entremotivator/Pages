import streamlit as st
from supabase import create_client, Client
from PIL import Image
import os
from auth_utils import AuthManager, render_auth_sidebar, init_session_state
from styles import apply_custom_css, hide_streamlit_elements, add_custom_header

# Page configuration with new branding
st.set_page_config(
    page_title="AI Knowledge Hub", 
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom styling and hide Streamlit elements
apply_custom_css()
hide_streamlit_elements()

# Initialize authentication
auth_manager = AuthManager()
init_session_state()

# Custom header
add_custom_header()

# Display logo and title
col1, col2 = st.columns([1, 4])
with col1:
    if os.path.exists("assets/logo.png"):
        logo = Image.open("assets/logo.png")
        st.image(logo, width=100)
with col2:
    st.title("AI Knowledge Hub")
    st.markdown("*Your comprehensive resource for AI learning and development*")

# Render authentication sidebar
render_auth_sidebar(auth_manager)

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


