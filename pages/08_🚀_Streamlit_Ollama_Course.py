import streamlit as st
import time
from datetime import datetime
import json
import os
import base64

# -------------------------
# Hide Streamlit Elements for Cloud Deployment
# -------------------------
def hide_streamlit_style():
    """Hide Streamlit default elements for cloud deployment"""
    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stDeployButton {display:none;}
            .stDecoration {display:none;}
            .css-14xtw13.e8zbici0 {display: none;}
            .css-1rs6os.edgvbvh3 {display: none;}
            .css-vk3wp9.e1akgbir0 {display: none;}
            .css-1j8o68f.edgvbvh9 {display: none;}
            .css-1dp5vir.e8zbici0 {display: none;}
            div[data-testid="stToolbar"] {visibility: hidden;}
            div[data-testid="stDecoration"] {visibility: hidden;}
            div[data-testid="stStatusWidget"] {visibility: hidden;}
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)

def apply_ai_toolkit_theme():
    """Apply AI Agent Toolkit theme with course-specific styling"""
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Main app styling */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #334155 100%);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }
    
    /* Text colors */
    .stMarkdown, .stText, p, span, div, .stSelectbox label, .stTextInput label {
        color: #ffffff !important;
        font-family: 'Inter', sans-serif;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #f59e0b !important;
        font-weight: 600;
        font-family: 'Inter', sans-serif;
    }
    
    /* Course-specific styling */
    .lesson-card {
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid #475569;
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        border-left: 5px solid #f59e0b;
        transition: all 0.3s ease;
    }
    
    .lesson-card:hover {
        border-color: #f59e0b;
        box-shadow: 0 8px 25px rgba(245, 158, 11, 0.3);
        transform: translateY(-2px);
    }
    
    .code-block {
        background: #1e293b;
        color: #e2e8f0;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        font-family: 'Courier New', monospace;
        border-left: 5px solid #f59e0b;
        border: 1px solid #475569;
    }
    
    .highlight-box {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.2) 0%, rgba(217, 119, 6, 0.2) 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #f59e0b;
        border: 1px solid #f59e0b;
    }
    
    .warning-box {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.2) 0%, rgba(220, 38, 38, 0.2) 100%);
        border: 1px solid #ef4444;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #ef4444;
        color: #fca5a5 !important;
    }
    
    .success-box {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.2) 0%, rgba(16, 185, 129, 0.2) 100%);
        border: 1px solid #22c55e;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #22c55e;
        color: #86efac !important;
    }
    
    .project-card {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: #000000;
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        box-shadow: 0 8px 25px rgba(245, 158, 11, 0.3);
        font-weight: 600;
    }
    
    .step-counter {
        background: #f59e0b;
        color: #000000;
        width: 30px;
        height: 30px;
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        margin-right: 10px;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: #000000;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-family: 'Inter', sans-serif;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(245, 158, 11, 0.3);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #d97706 0%, #b45309 100%);
        box-shadow: 0 6px 20px rgba(245, 158, 11, 0.5);
        transform: translateY(-2px);
    }
    
    /* Progress bar styling */
    .stProgress > div > div > div > div {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background-color: transparent;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: rgba(30, 41, 59, 0.8);
        border: 2px solid #475569;
        border-radius: 12px 12px 0 0;
        color: #cbd5e1;
        padding: 1rem 2rem;
        font-weight: 500;
        font-family: 'Inter', sans-serif;
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: #000000 !important;
        border-color: #f59e0b;
        font-weight: 600;
    }
    
    /* Logo styling */
    .logo-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 2rem 0;
    }
    
    .logo-container img {
        max-width: 200px;
        height: auto;
        filter: drop-shadow(0 8px 32px rgba(245, 158, 11, 0.3));
    }
    
    /* Resource links styling */
    .resource-link {
        display: inline-block;
        background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
        color: #000000 !important;
        padding: 0.75rem 1.5rem;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 600;
        font-family: 'Inter', sans-serif;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(245, 158, 11, 0.3);
        margin: 0.5rem;
    }
    
    .resource-link:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(245, 158, 11, 0.5);
        text-decoration: none;
        color: #000000 !important;
    }
    </style>
    """, unsafe_allow_html=True)

def get_base64_of_bin_file(bin_file):
    """Get base64 encoding of binary file"""
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def display_logo():
    """Display the AI Agent Toolkit logo"""
    logo_path = "/home/ubuntu/ai-agent-toolkit/logo.png"
    if os.path.exists(logo_path):
        st.markdown(f"""
        <div class="logo-container">
            <img src="data:image/png;base64,{get_base64_of_bin_file(logo_path)}" alt="AI Agent Toolkit Logo">
        </div>
        """, unsafe_allow_html=True)

# Apply styling and authentication check
hide_streamlit_style()
apply_ai_toolkit_theme()

st.set_page_config(
    page_title="Streamlit + Ollama Course - AI Agent Toolkit",
    page_icon="🚀",
    layout="wide"
)

# Authentication check
if not st.session_state.get("authenticated", False):
    st.warning("🔒 Please sign in to access the Streamlit + Ollama Course.")
    st.stop()

# Display logo
display_logo()

# Initialize session state
if "current_lesson" not in st.session_state:
    st.session_state.current_lesson = 0
if "lesson_progress" not in st.session_state:
    st.session_state.lesson_progress = {}
if "course_completed" not in st.session_state:
    st.session_state.course_completed = False

# Header
st.title("🚀 Streamlit + Ollama Mastery Course")
st.markdown("*Build powerful AI applications with Streamlit and local Ollama models*")

# Horizontal menu
menu_col1, menu_col2, menu_col3, menu_col4, menu_col5 = st.columns(5)
with menu_col1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("main_app.py")
with menu_col2:
    if st.button("🧠 Knowledge Base", use_container_width=True):
        st.switch_page("pages/04_🧠_AI_Knowledge_Base.py")
with menu_col3:
    if st.button("🦙 Ollama Course", use_container_width=True):
        st.switch_page("pages/05_🦙_Ollama_Course.py")
with menu_col4:
    if st.button("📚 Resources", use_container_width=True):
        st.switch_page("pages/03_📚_Resources.py")
with menu_col5:
    if st.button("📦 GitHub Hub", use_container_width=True):
        st.switch_page("pages/07_📦_GitHub_Resources.py")

st.markdown("---")

# Course progress
total_lessons = 8
completed_lessons = len(st.session_state.lesson_progress)
progress = completed_lessons / total_lessons if total_lessons > 0 else 0

st.progress(progress, text=f"Course Progress: {completed_lessons}/{total_lessons} lessons completed")

# Course content tabs
tab1, tab2, tab3, tab4 = st.tabs(["🎯 Course Overview", "💻 Setup & Installation", "🔧 Building Apps", "🚀 Advanced Projects"])

with tab1:
    st.markdown('<div class="lesson-card">', unsafe_allow_html=True)
    st.header("Welcome to Streamlit + Ollama Mastery!")
    
    st.markdown("""
    ## 🎯 What You'll Learn
    
    This comprehensive course will teach you how to build powerful AI applications by combining **Streamlit's** 
    intuitive web framework with **Ollama's** local AI models.
    
    ### Course Modules:
    
    **Module 1: Foundations**
    - Understanding Streamlit architecture
    - Setting up Ollama locally
    - Basic integration patterns
    
    **Module 2: Building Applications**
    - Creating chat interfaces
    - Document analysis tools
    - Real-time AI assistants
    
    **Module 3: Advanced Features**
    - Multi-model applications
    - Custom UI components
    - Performance optimization
    
    **Module 4: Production Deployment**
    - Containerization with Docker
    - Cloud deployment strategies
    - Monitoring and scaling
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Course benefits
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="highlight-box">', unsafe_allow_html=True)
        st.markdown("""
        ### 🌟 Why This Course?
        
        - **Privacy-First**: Keep your data local with Ollama
        - **Cost-Effective**: No API fees or usage limits
        - **Practical**: Build real applications, not just tutorials
        - **Modern**: Latest Streamlit and Ollama features
        - **Comprehensive**: From basics to production deployment
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="success-box">', unsafe_allow_html=True)
        st.markdown("""
        ### ✅ Prerequisites
        
        - Basic Python knowledge
        - Familiarity with web concepts
        - Computer with 8GB+ RAM
        - Willingness to learn and experiment
        
        **Optional but helpful:**
        - Experience with Streamlit
        - Understanding of AI/ML concepts
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("🚀 Start Course", key="start_course"):
        st.session_state.current_lesson = 1
        st.success("Course started! Let's begin with the setup.")
        st.rerun()

with tab2:
    st.markdown('<div class="lesson-card">', unsafe_allow_html=True)
    st.header("💻 Setup & Installation")
    
    # Lesson 1: Environment Setup
    st.subheader("📋 Lesson 1: Environment Setup")
    
    st.markdown("""
    ### Step 1: Install Python Dependencies
    
    First, let's set up our Python environment with the required packages:
    """)
    
    st.markdown('<div class="code-block">', unsafe_allow_html=True)
    st.code("""
# Create a virtual environment
python -m venv streamlit-ollama-env

# Activate the environment
# Windows:
streamlit-ollama-env\\Scripts\\activate
# macOS/Linux:
source streamlit-ollama-env/bin/activate

# Install required packages
pip install streamlit
pip install requests
pip install python-dotenv
pip install pandas
pip install plotly
    """, language="bash")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Step 2: Install Ollama
    
    Download and install Ollama for your operating system:
    """)
    
    os_col1, os_col2, os_col3 = st.columns(3)
    
    with os_col1:
        st.markdown("**🪟 Windows**")
        st.markdown('<div class="code-block">', unsafe_allow_html=True)
        st.code("""
# Download from ollama.com
# Or use winget:
winget install Ollama.Ollama
        """, language="bash")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with os_col2:
        st.markdown("**🐧 Linux**")
        st.markdown('<div class="code-block">', unsafe_allow_html=True)
        st.code("""
# Install via curl:
curl -fsSL https://ollama.com/install.sh | sh

# Or download manually from ollama.com
        """, language="bash")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with os_col3:
        st.markdown("**🍎 macOS**")
        st.markdown('<div class="code-block">', unsafe_allow_html=True)
        st.code("""
# Install via Homebrew:
brew install ollama

# Or download from ollama.com
        """, language="bash")
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Step 3: Download Your First Model
    
    Let's download a lightweight model to get started:
    """)
    
    st.markdown('<div class="code-block">', unsafe_allow_html=True)
    st.code("""
# Start Ollama service
ollama serve

# In a new terminal, download a model
ollama pull llama2:7b

# Test the model
ollama run llama2:7b "Hello, how are you?"
    """, language="bash")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("✅ Mark Setup Complete", key="lesson1_complete"):
        st.session_state.lesson_progress["lesson1"] = True
        st.success("Setup lesson completed! 🎉")
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="lesson-card">', unsafe_allow_html=True)
    st.header("🔧 Building Your First App")
    
    # Lesson 2: Basic Chat App
    st.subheader("💬 Lesson 2: Basic Chat Interface")
    
    st.markdown("""
    Let's build a simple chat application that connects Streamlit with Ollama:
    """)
    
    st.markdown('<div class="code-block">', unsafe_allow_html=True)
    st.code("""
import streamlit as st
import requests
import json

# App configuration
st.set_page_config(
    page_title="Ollama Chat",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Ollama Chat Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to call Ollama API
def call_ollama(prompt, model="llama2:7b"):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return response.json()["response"]
        else:
            return "Error: Could not connect to Ollama"
    except Exception as e:
        return f"Error: {str(e)}"

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = call_ollama(prompt)
            st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    """, language="python")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown("""
    ### Key Features Explained:
    
    1. **Session State**: Maintains chat history across interactions
    2. **Ollama API**: Communicates with local Ollama instance
    3. **Chat Interface**: Uses Streamlit's built-in chat components
    4. **Error Handling**: Gracefully handles connection issues
    """)
    
    if st.button("✅ Mark Lesson 2 Complete", key="lesson2_complete"):
        st.session_state.lesson_progress["lesson2"] = True
        st.success("Basic chat app lesson completed! 🎉")
        st.rerun()
    
    # Lesson 3: Enhanced Features
    st.subheader("⚡ Lesson 3: Enhanced Features")
    
    st.markdown("""
    Let's add more advanced features to our chat app:
    """)
    
    st.markdown('<div class="code-block">', unsafe_allow_html=True)
    st.code("""
# Add to your existing app

# Sidebar for settings
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Model selection
    available_models = ["llama2:7b", "codellama", "mistral"]
    selected_model = st.selectbox("Choose Model", available_models)
    
    # Temperature control
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7)
    
    # Max tokens
    max_tokens = st.slider("Max Tokens", 50, 2000, 500)
    
    # Clear chat button
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# Enhanced Ollama function
def call_ollama_enhanced(prompt, model="llama2:7b", temperature=0.7, max_tokens=500):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": temperature,
            "num_predict": max_tokens
        }
    }
    
    try:
        response = requests.post(url, json=data, timeout=30)
        if response.status_code == 200:
            return response.json()["response"]
        else:
            return f"Error: {response.status_code} - {response.text}"
    except requests.exceptions.Timeout:
        return "Error: Request timed out"
    except Exception as e:
        return f"Error: {str(e)}"

# Add file upload capability
uploaded_file = st.file_uploader("📁 Upload a text file", type=['txt', 'md'])
if uploaded_file is not None:
    content = uploaded_file.read().decode('utf-8')
    st.text_area("File Content", content, height=200)
    
    if st.button("📖 Analyze Document"):
        analysis_prompt = f"Please analyze this document and provide a summary:\\n\\n{content}"
        with st.spinner("Analyzing document..."):
            response = call_ollama_enhanced(analysis_prompt, selected_model, temperature, max_tokens)
            st.markdown("### 📊 Analysis Results")
            st.markdown(response)
    """, language="python")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("✅ Mark Lesson 3 Complete", key="lesson3_complete"):
        st.session_state.lesson_progress["lesson3"] = True
        st.success("Enhanced features lesson completed! 🎉")
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="lesson-card">', unsafe_allow_html=True)
    st.header("🚀 Advanced Projects")
    
    # Project 1: Multi-Model Comparison
    st.subheader("🔄 Project 1: Multi-Model Comparison Tool")
    
    st.markdown("""
    Build a tool that compares responses from different Ollama models:
    """)
    
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown("""
    ### 🎯 Project Features:
    - Side-by-side model comparison
    - Response time measurement
    - Quality scoring system
    - Export comparison results
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="code-block">', unsafe_allow_html=True)
    st.code("""
import streamlit as st
import requests
import time
import pandas as pd

st.title("🔄 Model Comparison Tool")

# Model selection
col1, col2 = st.columns(2)
with col1:
    model1 = st.selectbox("Model 1", ["llama2:7b", "codellama", "mistral"])
with col2:
    model2 = st.selectbox("Model 2", ["llama2:7b", "codellama", "mistral"])

# Prompt input
prompt = st.text_area("Enter your prompt:", height=100)

if st.button("🚀 Compare Models") and prompt:
    col1, col2 = st.columns(2)
    
    # Model 1 response
    with col1:
        st.subheader(f"📊 {model1}")
        start_time = time.time()
        
        with st.spinner(f"Getting response from {model1}..."):
            response1 = call_ollama(prompt, model1)
            response_time1 = time.time() - start_time
        
        st.markdown(response1)
        st.caption(f"Response time: {response_time1:.2f} seconds")
    
    # Model 2 response
    with col2:
        st.subheader(f"📊 {model2}")
        start_time = time.time()
        
        with st.spinner(f"Getting response from {model2}..."):
            response2 = call_ollama(prompt, model2)
            response_time2 = time.time() - start_time
        
        st.markdown(response2)
        st.caption(f"Response time: {response_time2:.2f} seconds")
    
    # Comparison summary
    st.subheader("📈 Comparison Summary")
    comparison_data = {
        "Model": [model1, model2],
        "Response Time (s)": [f"{response_time1:.2f}", f"{response_time2:.2f}"],
        "Response Length": [len(response1), len(response2)]
    }
    
    df = pd.DataFrame(comparison_data)
    st.dataframe(df, use_container_width=True)
    """, language="python")
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("✅ Complete Project 1", key="project1_complete"):
        st.session_state.lesson_progress["project1"] = True
        st.success("Multi-model comparison project completed! 🎉")
        st.rerun()
    
    # Project 2: Document Q&A System
    st.subheader("📚 Project 2: Document Q&A System")
    
    st.markdown("""
    Create an intelligent document analysis system:
    """)
    
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    st.markdown("""
    ### 🎯 Project Features:
    - Multiple document format support
    - Context-aware Q&A
    - Document summarization
    - Key insights extraction
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if st.button("✅ Complete Project 2", key="project2_complete"):
        st.session_state.lesson_progress["project2"] = True
        st.success("Document Q&A system project completed! 🎉")
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Course completion check
if len(st.session_state.lesson_progress) >= 6:  # Adjust based on total lessons
    if not st.session_state.course_completed:
        st.balloons()
        st.success("🎉 Congratulations! You've completed the Streamlit + Ollama Mastery Course!")
        st.session_state.course_completed = True

# Footer with navigation
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🦙 Basic Ollama Course", use_container_width=True):
        st.switch_page("pages/05_🦙_Ollama_Course.py")

with col2:
    if st.button("📦 GitHub Resources", use_container_width=True):
        st.switch_page("pages/07_📦_GitHub_Resources.py")

with col3:
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("main_app.py")

# Sidebar with progress tracking
with st.sidebar:
    st.markdown("### 🎯 Course Progress")
    
    lessons = {
        "lesson1": "💻 Environment Setup",
        "lesson2": "💬 Basic Chat App",
        "lesson3": "⚡ Enhanced Features",
        "project1": "🔄 Multi-Model Tool",
        "project2": "📚 Document Q&A",
    }
    
    for lesson_key, lesson_name in lessons.items():
        if lesson_key in st.session_state.lesson_progress:
            st.success(f"✅ {lesson_name}")
        else:
            st.markdown(f"⏳ {lesson_name}")
    
    st.progress(len(st.session_state.lesson_progress) / len(lessons))
    
    st.markdown("### 🔗 Quick Links")
    st.markdown("""
    <div style="margin: 1rem 0;">
        <a href="https://entremotivator.com" target="_blank" class="resource-link">
            🚀 Visit Entremotivator.com
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    - [Streamlit Docs](https://docs.streamlit.io/)
    - [Ollama Documentation](https://ollama.com/)
    - [Course GitHub Repo](https://github.com/example/streamlit-ollama)
    """)

st.markdown("---")
st.markdown("*This page is part of the AI Agent Toolkit by D Hudson. Master the art of building AI applications with Streamlit and Ollama!*")
