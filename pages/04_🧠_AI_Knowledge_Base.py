import streamlit as st
import requests
from datetime import datetime
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
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] > div {
        background: linear-gradient(180deg, #1e293b 0%, #334155 100%);
        border-right: 2px solid #f59e0b;
    }
    
    section[data-testid="stSidebar"] .stMarkdown,
    section[data-testid="stSidebar"] .stText,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] div {
        color: white !important;
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

st.set_page_config(page_title="AI Knowledge Base - AI Agent Toolkit", page_icon="🧠", layout="wide")

# Authentication check
if not st.session_state.get("authenticated", False):
    st.warning("🔒 Please sign in to access the AI Knowledge Base.")
    st.stop()

# Display logo
display_logo()

# Header
st.title("🧠 AI Knowledge Base")
st.markdown("*Comprehensive guides and resources for artificial intelligence*")

# Horizontal menu
menu_col1, menu_col2, menu_col3, menu_col4, menu_col5 = st.columns(5)
with menu_col1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("main_app.py")
with menu_col2:
    if st.button("🤖 AI Agents", use_container_width=True):
        st.switch_page("pages/01_🤖_AI_Agents.py")
with menu_col3:
    if st.button("🛠️ AI Tools", use_container_width=True):
        st.switch_page("pages/02_🛠️_AI_Tools.py")
with menu_col4:
    if st.button("📚 Resources", use_container_width=True):
        st.switch_page("pages/03_📚_Resources.py")
with menu_col5:
    if st.button("🦙 Ollama Course", use_container_width=True):
        st.switch_page("pages/05_🦙_Ollama_Course.py")

st.markdown("---")

# Navigation tabs
tab1, tab2, tab3, tab4 = st.tabs(["📚 Fundamentals", "🤖 Machine Learning", "🔬 Advanced Topics", "📈 Trends & Research"])

with tab1:
    st.header("AI Fundamentals")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 What is Artificial Intelligence?")
        st.markdown("""
        Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn like humans. 
        
        **Key Concepts:**
        - **Machine Learning**: Algorithms that improve through experience
        - **Deep Learning**: Neural networks with multiple layers
        - **Natural Language Processing**: Understanding and generating human language
        - **Computer Vision**: Interpreting and analyzing visual information
        """)
        
        with st.expander("📖 Learn More About AI History"):
            st.markdown("""
            **Timeline of AI Development:**
            - **1950s**: Alan Turing proposes the Turing Test
            - **1956**: The term "Artificial Intelligence" is coined
            - **1980s**: Expert systems gain popularity
            - **1990s**: Machine learning algorithms advance
            - **2010s**: Deep learning revolution begins
            - **2020s**: Large language models emerge
            """)
    
    with col2:
        st.subheader("🛠️ AI Applications")
        st.markdown("""
        **Current Applications:**
        - Healthcare diagnostics and drug discovery
        - Autonomous vehicles and transportation
        - Financial fraud detection and trading
        - Content creation and recommendation systems
        - Virtual assistants and chatbots
        - Image and speech recognition
        """)
        
        st.info("💡 **Did you know?** AI is projected to contribute $15.7 trillion to the global economy by 2030.")

with tab2:
    st.header("Machine Learning Deep Dive")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Types of Machine Learning")
        
        st.markdown("**1. Supervised Learning**")
        st.markdown("- Uses labeled training data")
        st.markdown("- Examples: Classification, Regression")
        st.markdown("- Algorithms: Linear Regression, Random Forest, SVM")
        
        st.markdown("**2. Unsupervised Learning**")
        st.markdown("- Finds patterns in unlabeled data")
        st.markdown("- Examples: Clustering, Dimensionality Reduction")
        st.markdown("- Algorithms: K-Means, PCA, DBSCAN")
        
        st.markdown("**3. Reinforcement Learning**")
        st.markdown("- Learns through interaction and rewards")
        st.markdown("- Examples: Game playing, Robotics")
        st.markdown("- Algorithms: Q-Learning, Policy Gradient")
    
    with col2:
        st.subheader("🧮 Popular ML Frameworks")
        
        frameworks = {
            "TensorFlow": "Google's open-source ML platform",
            "PyTorch": "Facebook's dynamic neural network library",
            "Scikit-learn": "Simple and efficient ML tools for Python",
            "Keras": "High-level neural networks API",
            "XGBoost": "Optimized gradient boosting framework"
        }
        
        for framework, description in frameworks.items():
            with st.expander(f"🔧 {framework}"):
                st.markdown(f"**{description}**")
                st.markdown("Perfect for beginners and experts alike!")

with tab3:
    st.header("Advanced AI Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔮 Large Language Models (LLMs)")
        st.markdown("""
        **Understanding LLMs:**
        - Transformer architecture revolutionized NLP
        - Pre-trained on massive text datasets
        - Fine-tuned for specific tasks
        
        **Popular Models:**
        - GPT series (OpenAI)
        - BERT and variants (Google)
        - LLaMA (Meta)
        - Claude (Anthropic)
        """)
        
        st.subheader("🎨 Generative AI")
        st.markdown("""
        **Applications:**
        - Text generation and completion
        - Image synthesis and editing
        - Code generation and debugging
        - Music and art creation
        """)
    
    with col2:
        st.subheader("🤖 AI Agents & Automation")
        st.markdown("""
        **Agent Architectures:**
        - ReAct (Reasoning + Acting)
        - Multi-agent systems
        - Tool-using agents
        - Memory-augmented agents
        
        **Popular Frameworks:**
        - LangChain
        - CrewAI
        - AutoGen
        - Semantic Kernel
        """)
        
        st.success("🚀 **Next Step**: Explore our Ollama Course to learn about local AI deployment!")

with tab4:
    st.header("Latest Trends & Research")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Current Trends (2024-2025)")
        trends = [
            "🏠 Local AI deployment with Ollama",
            "🔗 Multi-modal AI systems",
            "🧠 Retrieval-Augmented Generation (RAG)",
            "🤝 AI agent collaboration",
            "⚡ Edge AI and optimization",
            "🛡️ AI safety and alignment"
        ]
        
        for trend in trends:
            st.markdown(f"- {trend}")
    
    with col2:
        st.subheader("🔬 Research Areas")
        st.markdown("""
        **Hot Research Topics:**
        - Constitutional AI and RLHF
        - Few-shot and zero-shot learning
        - Federated learning
        - Explainable AI (XAI)
        - Quantum machine learning
        - Neuromorphic computing
        """)

# Footer with quick actions
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🦙 Explore Ollama Course", use_container_width=True):
        st.switch_page("pages/05_🦙_Ollama_Course.py")

with col2:
    if st.button("📦 Browse GitHub Resources", use_container_width=True):
        st.switch_page("pages/07_📦_GitHub_Resources.py")

with col3:
    if st.button("🛠️ AI Tools Directory", use_container_width=True):
        st.switch_page("pages/02_🛠️_AI_Tools.py")

# Sidebar with quick reference
with st.sidebar:
    st.markdown("### 📚 Quick Reference")
    st.markdown("""
    **AI Glossary:**
    - **AGI**: Artificial General Intelligence
    - **API**: Application Programming Interface
    - **CNN**: Convolutional Neural Network
    - **GPU**: Graphics Processing Unit
    - **NLP**: Natural Language Processing
    - **RNN**: Recurrent Neural Network
    """)
    
    st.markdown("### 🔗 Useful Links")
    st.markdown("""
    <div style="margin: 1rem 0;">
        <a href="https://entremotivator.com" target="_blank" class="resource-link">
            🚀 Visit Entremotivator.com
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    - [Papers With Code](https://paperswithcode.com/)
    - [Hugging Face](https://huggingface.co/)
    - [OpenAI Documentation](https://platform.openai.com/docs)
    - [Google AI](https://ai.google/)
    """)

st.markdown("---")
st.markdown("*This page is part of the AI Agent Toolkit by D Hudson. Explore other sections for comprehensive AI development resources.*")
