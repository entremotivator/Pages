import streamlit as st
import os
from datetime import datetime
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
    """Apply AI Agent Toolkit theme"""
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
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid #475569;
        border-radius: 12px;
        color: #ffffff !important;
        font-family: 'Inter', sans-serif;
    }
    
    /* Info/Success/Warning boxes */
    .stInfo {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.2) 0%, rgba(99, 102, 241, 0.2) 100%);
        border: 1px solid #3b82f6;
        color: #93c5fd !important;
    }
    
    .stSuccess {
        background: linear-gradient(135deg, rgba(34, 197, 94, 0.2) 0%, rgba(16, 185, 129, 0.2) 100%);
        border: 1px solid #22c55e;
        color: #86efac !important;
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

st.set_page_config(page_title="Ollama Course - AI Agent Toolkit", page_icon="🦙", layout="wide")

# Authentication check
if not st.session_state.get("authenticated", False):
    st.warning("🔒 Please sign in to access the Ollama Course.")
    st.stop()

# Display logo
display_logo()

# Header
st.title("🦙 Ollama Mastery Course")
st.markdown("*Complete guide to running AI models locally*")

# Horizontal menu
menu_col1, menu_col2, menu_col3, menu_col4, menu_col5 = st.columns(5)
with menu_col1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("main_app.py")
with menu_col2:
    if st.button("🧠 Knowledge Base", use_container_width=True):
        st.switch_page("pages/04_🧠_AI_Knowledge_Base.py")
with menu_col3:
    if st.button("🛠️ AI Tools", use_container_width=True):
        st.switch_page("pages/02_🛠️_AI_Tools.py")
with menu_col4:
    if st.button("📚 Resources", use_container_width=True):
        st.switch_page("pages/03_📚_Resources.py")
with menu_col5:
    if st.button("📦 GitHub Hub", use_container_width=True):
        st.switch_page("pages/07_📦_GitHub_Resources.py")

st.markdown("---")

# Course progress tracking
if "ollama_progress" not in st.session_state:
    st.session_state.ollama_progress = {
        "completed_lessons": [],
        "current_lesson": 1,
        "total_lessons": 12
    }

# Progress bar
progress = len(st.session_state.ollama_progress["completed_lessons"]) / st.session_state.ollama_progress["total_lessons"]
st.progress(progress, text=f"Course Progress: {len(st.session_state.ollama_progress['completed_lessons'])}/{st.session_state.ollama_progress['total_lessons']} lessons completed")

# Course navigation
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🚀 Getting Started", "⚙️ Installation", "🎯 Basic Usage", "🔧 Advanced Topics", "📚 Resources"])

with tab1:
    st.header("Welcome to Ollama!")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ## What is Ollama?
        
        Ollama is a powerful tool that allows you to run large language models locally on your machine. 
        It's designed to make AI accessible, private, and fast - without relying on cloud services.
        
        ### 🎯 Why Choose Ollama?
        
        **Privacy First**
        - Your data never leaves your machine
        - No internet connection required for inference
        - Complete control over your AI interactions
        
        **Cost Effective**
        - No API fees or usage limits
        - Run unlimited queries locally
        - One-time setup, lifetime usage
        
        **Performance**
        - Optimized for local hardware
        - GPU acceleration support
        - Fast inference times
        
        **Flexibility**
        - Support for multiple model formats
        - Easy model switching
        - Custom model fine-tuning
        """)
        
        if st.button("✅ Mark Lesson 1 Complete", key="lesson1"):
            if 1 not in st.session_state.ollama_progress["completed_lessons"]:
                st.session_state.ollama_progress["completed_lessons"].append(1)
                st.success("Lesson 1 completed! 🎉")
                st.rerun()
    
    with col2:
        st.markdown("### 📋 Course Overview")
        
        lessons = [
            "🚀 Introduction to Ollama",
            "💻 System Requirements",
            "⬇️ Installation Guide",
            "🔧 First Setup",
            "🤖 Running Your First Model",
            "💬 Chat Interface",
            "🛠️ Model Management",
            "⚡ Performance Optimization",
            "🔌 API Integration",
            "🎨 Custom Models",
            "🔒 Security & Privacy",
            "🚀 Advanced Use Cases"
        ]
        
        for i, lesson in enumerate(lessons, 1):
            if i in st.session_state.ollama_progress["completed_lessons"]:
                st.success(f"{lesson} ✅")
            else:
                st.markdown(f"{lesson}")

with tab2:
    st.header("Installation & Setup")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💻 System Requirements")
        st.markdown("""
        **Minimum Requirements:**
        - 8GB RAM (16GB recommended)
        - 10GB free disk space
        - Modern CPU (Intel/AMD 64-bit)
        
        **Recommended:**
        - 32GB RAM for larger models
        - NVIDIA GPU with 8GB+ VRAM
        - SSD storage for faster loading
        """)
        
        st.subheader("⬇️ Installation Steps")
        
        # Operating system tabs
        os_tab1, os_tab2, os_tab3 = st.tabs(["🪟 Windows", "🐧 Linux", "🍎 macOS"])
        
        with os_tab1:
            st.code("""
# Download and run installer
curl -fsSL https://ollama.com/install.sh | sh

# Or download from website
# Visit: https://ollama.com/download
            """, language="bash")
        
        with os_tab2:
            st.code("""
# Install via curl
curl -fsSL https://ollama.com/install.sh | sh

# Or via package manager
sudo apt install ollama  # Ubuntu/Debian
sudo yum install ollama   # RHEL/CentOS
            """, language="bash")
        
        with os_tab3:
            st.code("""
# Install via Homebrew
brew install ollama

# Or download from website
# Visit: https://ollama.com/download
            """, language="bash")
    
    with col2:
        st.subheader("🔧 First Setup")
        st.markdown("""
        **1. Verify Installation**
        ```bash
        ollama --version
        ```
        
        **2. Start Ollama Service**
        ```bash
        ollama serve
        ```
        
        **3. Download Your First Model**
        ```bash
        ollama pull llama2
        ```
        
        **4. Test the Installation**
        ```bash
        ollama run llama2
        ```
        """)
        
        if st.button("✅ Mark Installation Complete", key="lesson2"):
            if 2 not in st.session_state.ollama_progress["completed_lessons"]:
                st.session_state.ollama_progress["completed_lessons"].append(2)
                st.success("Installation lesson completed! 🎉")
                st.rerun()

with tab3:
    st.header("Basic Usage")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🤖 Running Models")
        st.markdown("""
        **Basic Commands:**
        
        ```bash
        # List available models
        ollama list
        
        # Run a model interactively
        ollama run llama2
        
        # Run with specific prompt
        ollama run llama2 "Explain quantum computing"
        
        # Pull a new model
        ollama pull codellama
        
        # Remove a model
        ollama rm llama2
        ```
        """)
        
        st.subheader("💬 Chat Interface")
        st.markdown("""
        **Interactive Chat:**
        - Type your questions naturally
        - Use `/bye` to exit
        - Use `/clear` to clear context
        - Use `/help` for more commands
        """)
    
    with col2:
        st.subheader("🎯 Popular Models")
        
        models = {
            "Llama 2": "Meta's flagship model - great for general tasks",
            "Code Llama": "Specialized for code generation and debugging",
            "Mistral": "Fast and efficient for most applications",
            "Vicuna": "Fine-tuned for conversation and instruction following",
            "Orca Mini": "Compact model good for resource-constrained systems"
        }
        
        for model, description in models.items():
            with st.expander(f"🤖 {model}"):
                st.markdown(f"**{description}**")
                st.code(f"ollama pull {model.lower().replace(' ', '')}")
        
        if st.button("✅ Mark Basic Usage Complete", key="lesson3"):
            if 3 not in st.session_state.ollama_progress["completed_lessons"]:
                st.session_state.ollama_progress["completed_lessons"].append(3)
                st.success("Basic usage lesson completed! 🎉")
                st.rerun()

with tab4:
    st.header("Advanced Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔌 API Integration")
        st.markdown("""
        **REST API Usage:**
        
        ```python
        import requests
        
        response = requests.post('http://localhost:11434/api/generate',
            json={
                'model': 'llama2',
                'prompt': 'Why is the sky blue?',
                'stream': False
            })
        
        print(response.json()['response'])
        ```
        
        **Python Library:**
        ```python
        import ollama
        
        response = ollama.chat(model='llama2', messages=[
          {
            'role': 'user',
            'content': 'Why is the sky blue?',
          },
        ])
        print(response['message']['content'])
        ```
        """)
    
    with col2:
        st.subheader("⚡ Performance Optimization")
        st.markdown("""
        **GPU Acceleration:**
        - Ensure CUDA is installed
        - Ollama automatically detects GPU
        - Monitor GPU usage with `nvidia-smi`
        
        **Memory Management:**
        - Use `OLLAMA_NUM_PARALLEL` for concurrent requests
        - Set `OLLAMA_MAX_LOADED_MODELS` to limit memory
        - Use smaller models for better performance
        
        **Custom Modelfiles:**
        ```dockerfile
        FROM llama2
        
        PARAMETER temperature 0.8
        PARAMETER top_p 0.9
        
        SYSTEM You are a helpful assistant.
        ```
        """)
        
        if st.button("✅ Mark Advanced Topics Complete", key="lesson4"):
            if 4 not in st.session_state.ollama_progress["completed_lessons"]:
                st.session_state.ollama_progress["completed_lessons"].append(4)
                st.success("Advanced topics lesson completed! 🎉")
                st.rerun()

with tab5:
    st.header("Resources & Community")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📚 Official Resources")
        st.markdown("""
        **Documentation:**
        - [Ollama GitHub](https://github.com/ollama/ollama)
        - [Model Library](https://ollama.com/library)
        - [API Documentation](https://github.com/ollama/ollama/blob/main/docs/api.md)
        
        **Community:**
        - [Discord Server](https://discord.gg/ollama)
        - [Reddit Community](https://reddit.com/r/ollama)
        - [GitHub Discussions](https://github.com/ollama/ollama/discussions)
        """)
    
    with col2:
        st.subheader("🛠️ Integration Examples")
        st.markdown("""
        **Popular Integrations:**
        - LangChain with Ollama
        - Streamlit + Ollama chatbots
        - VS Code extensions
        - Jupyter notebook examples
        
        **Use Cases:**
        - Local code assistant
        - Private document analysis
        - Creative writing helper
        - Educational Q&A system
        """)

# Footer with navigation
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🧠 AI Knowledge Base", use_container_width=True):
        st.switch_page("pages/04_🧠_AI_Knowledge_Base.py")

with col2:
    if st.button("📦 GitHub Resources", use_container_width=True):
        st.switch_page("pages/07_📦_GitHub_Resources.py")

with col3:
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("main_app.py")

# Sidebar with course progress
with st.sidebar:
    st.markdown("### 🎯 Course Progress")
    
    completed = len(st.session_state.ollama_progress["completed_lessons"])
    total = st.session_state.ollama_progress["total_lessons"]
    
    st.metric("Lessons Completed", f"{completed}/{total}")
    st.progress(completed / total)
    
    st.markdown("### 🔗 Quick Links")
    st.markdown("""
    <div style="margin: 1rem 0;">
        <a href="https://entremotivator.com" target="_blank" class="resource-link">
            🚀 Visit Entremotivator.com
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    - [Ollama Official Site](https://ollama.com/)
    - [Model Library](https://ollama.com/library)
    - [GitHub Repository](https://github.com/ollama/ollama)
    - [API Docs](https://github.com/ollama/ollama/blob/main/docs/api.md)
    """)

st.markdown("---")
st.markdown("*This page is part of the AI Agent Toolkit by D Hudson. Master local AI deployment with Ollama!*")
