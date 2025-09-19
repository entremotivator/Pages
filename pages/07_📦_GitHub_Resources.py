import streamlit as st
import requests
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
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid #475569;
        border-radius: 12px;
        color: #ffffff !important;
        font-family: 'Inter', sans-serif;
    }
    
    /* Project card styling */
    .project-card {
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid #475569;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        border-color: #f59e0b;
        box-shadow: 0 4px 20px rgba(245, 158, 11, 0.2);
        transform: translateY(-2px);
    }
    
    /* Badge styling */
    .topic-badge {
        background-color: #1e40af;
        color: #dbeafe;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 12px;
        margin-right: 8px;
        margin-bottom: 4px;
        display: inline-block;
        font-weight: 500;
    }
    
    .language-badge {
        background-color: #059669;
        color: #d1fae5;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 500;
    }
    
    .stars-badge {
        background-color: #f59e0b;
        color: #000000;
        padding: 4px 12px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 600;
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

def render_project_card(project):
    """Render a project card with styling"""
    st.markdown('<div class="project-card">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        st.markdown(f"### 🚀 {project['name']}")
        st.markdown(f"**Repository:** `{project['repo']}`")
        st.markdown(f"**Description:** {project['description']}")
        
        # Badges
        badges_html = f'<span class="stars-badge">⭐ {project["stars"]}</span> '
        badges_html += f'<span class="language-badge">{project["language"]}</span>'
        st.markdown(badges_html, unsafe_allow_html=True)
        
        # Topics
        if project.get('topics'):
            topics_html = " ".join([f'<span class="topic-badge">{topic}</span>' for topic in project['topics']])
            st.markdown(topics_html, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### Quick Actions")
        if st.button(f"📥 Download ZIP", key=f"download_{project['repo'].replace('/', '_')}", use_container_width=True):
            st.success(f"Download link: {project['download_url']}")
            st.markdown(f"[Click here to download]({project['download_url']})")
        
        if st.button(f"🔗 View on GitHub", key=f"github_{project['repo'].replace('/', '_')}", use_container_width=True):
            st.markdown(f"[Open Repository](https://github.com/{project['repo']})")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Apply styling and authentication check
hide_streamlit_style()
apply_ai_toolkit_theme()

st.set_page_config(page_title="GitHub Resources - AI Agent Toolkit", page_icon="📦", layout="wide")

# Authentication check
if not st.session_state.get("authenticated", False):
    st.warning("🔒 Please sign in to access GitHub Resources.")
    st.stop()

# Display logo
display_logo()

# Header
st.title("📦 GitHub Resources Hub")
st.markdown("*Curated collection of AI projects, tools, and agent implementations*")

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
    if st.button("📥 Downloads", use_container_width=True):
        st.switch_page("pages/06_📥_Downloads_Center.py")

st.markdown("---")

# Resource categories
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🤖 AI Agents", "🧠 LLM Projects", "🛠️ Tools & Frameworks", "📚 Learning Resources", "🔥 Trending"])

with tab1:
    st.header("🤖 AI Agent Repositories")
    
    # Featured agent projects
    agent_projects = [
        {
            "name": "Microsoft AI Agents for Beginners",
            "repo": "microsoft/ai-agents-for-beginners",
            "description": "12 comprehensive lessons covering AI agent fundamentals",
            "stars": "2.5k",
            "language": "Python",
            "topics": ["Education", "Beginners", "Tutorial"],
            "download_url": "https://github.com/microsoft/ai-agents-for-beginners/archive/refs/heads/main.zip"
        },
        {
            "name": "GenAI Agents Collection",
            "repo": "NirDiamant/GenAI_Agents",
            "description": "Tutorials and implementations for various Generative AI Agent techniques",
            "stars": "1.8k",
            "language": "Python",
            "topics": ["Generative AI", "Advanced", "Implementations"],
            "download_url": "https://github.com/NirDiamant/GenAI_Agents/archive/refs/heads/main.zip"
        },
        {
            "name": "AI Agents Masterclass",
            "repo": "coleam00/ai-agents-masterclass",
            "description": "Complete code repository for AI Agents Masterclass video series",
            "stars": "950",
            "language": "Python",
            "topics": ["Video Course", "Practical", "Hands-on"],
            "download_url": "https://github.com/coleam00/ai-agents-masterclass/archive/refs/heads/main.zip"
        },
        {
            "name": "500+ AI Agent Projects",
            "repo": "ashishpatel26/500-AI-Agents-Projects",
            "description": "Curated collection of AI agent use cases across industries",
            "stars": "1.2k",
            "language": "Multiple",
            "topics": ["Use Cases", "Industry", "Collection"],
            "download_url": "https://github.com/ashishpatel26/500-AI-Agents-Projects/archive/refs/heads/main.zip"
        }
    ]
    
    for project in agent_projects:
        render_project_card(project)

with tab2:
    st.header("🧠 Large Language Model Projects")
    
    llm_projects = [
        {
            "name": "Ollama",
            "repo": "ollama/ollama",
            "description": "Get up and running with large language models locally",
            "stars": "95k",
            "language": "Go",
            "topics": ["Local AI", "LLM", "Privacy"],
            "download_url": "https://github.com/ollama/ollama/archive/refs/heads/main.zip"
        },
        {
            "name": "LangChain",
            "repo": "langchain-ai/langchain",
            "description": "Framework for developing applications powered by language models",
            "stars": "94k",
            "language": "Python",
            "topics": ["Framework", "LLM", "Applications"],
            "download_url": "https://github.com/langchain-ai/langchain/archive/refs/heads/master.zip"
        },
        {
            "name": "Transformers",
            "repo": "huggingface/transformers",
            "description": "State-of-the-art Machine Learning for PyTorch, TensorFlow, and JAX",
            "stars": "133k",
            "language": "Python",
            "topics": ["ML", "Transformers", "Hugging Face"],
            "download_url": "https://github.com/huggingface/transformers/archive/refs/heads/main.zip"
        },
        {
            "name": "LocalAI",
            "repo": "mudler/LocalAI",
            "description": "Free, Open Source OpenAI alternative for local deployment",
            "stars": "24k",
            "language": "Go",
            "topics": ["Local AI", "OpenAI Alternative", "Self-hosted"],
            "download_url": "https://github.com/mudler/LocalAI/archive/refs/heads/master.zip"
        }
    ]
    
    for project in llm_projects:
        render_project_card(project)

with tab3:
    st.header("🛠️ Tools & Frameworks")
    
    tools_projects = [
        {
            "name": "n8n",
            "repo": "n8n-io/n8n",
            "description": "Free and source-available fair-code licensed workflow automation tool",
            "stars": "47k",
            "language": "TypeScript",
            "topics": ["Workflow", "Automation", "No-code"],
            "download_url": "https://github.com/n8n-io/n8n/archive/refs/heads/master.zip"
        },
        {
            "name": "CrewAI",
            "repo": "joaomdmoura/crewAI",
            "description": "Framework for orchestrating role-playing, autonomous AI agents",
            "stars": "19k",
            "language": "Python",
            "topics": ["Multi-agent", "Framework", "Orchestration"],
            "download_url": "https://github.com/joaomdmoura/crewAI/archive/refs/heads/main.zip"
        },
        {
            "name": "AutoGen",
            "repo": "microsoft/autogen",
            "description": "Multi-agent conversation framework for building AI applications",
            "stars": "31k",
            "language": "Python",
            "topics": ["Multi-agent", "Microsoft", "Conversation"],
            "download_url": "https://github.com/microsoft/autogen/archive/refs/heads/main.zip"
        },
        {
            "name": "Streamlit",
            "repo": "streamlit/streamlit",
            "description": "Streamlit — A faster way to build and share data apps",
            "stars": "35k",
            "language": "Python",
            "topics": ["Web Apps", "Data Science", "Dashboard"],
            "download_url": "https://github.com/streamlit/streamlit/archive/refs/heads/develop.zip"
        }
    ]
    
    for project in tools_projects:
        render_project_card(project)

with tab4:
    st.header("📚 Learning Resources")
    
    learning_projects = [
        {
            "name": "Machine Learning Yearning",
            "repo": "ajaymache/machine-learning-yearning",
            "description": "Andrew Ng's Machine Learning Yearning book in markdown format",
            "stars": "7.6k",
            "language": "Markdown",
            "topics": ["Education", "Andrew Ng", "ML Theory"],
            "download_url": "https://github.com/ajaymache/machine-learning-yearning/archive/refs/heads/master.zip"
        },
        {
            "name": "AI Expert Roadmap",
            "repo": "AMAI-GmbH/AI-Expert-Roadmap",
            "description": "Roadmap to becoming an Artificial Intelligence Expert",
            "stars": "29k",
            "language": "Markdown",
            "topics": ["Roadmap", "Career", "AI Expert"],
            "download_url": "https://github.com/AMAI-GmbH/AI-Expert-Roadmap/archive/refs/heads/main.zip"
        },
        {
            "name": "Deep Learning Papers",
            "repo": "floodsung/Deep-Learning-Papers-Reading-Roadmap",
            "description": "Deep Learning papers reading roadmap for anyone interested",
            "stars": "37k",
            "language": "Markdown",
            "topics": ["Research", "Papers", "Deep Learning"],
            "download_url": "https://github.com/floodsung/Deep-Learning-Papers-Reading-Roadmap/archive/refs/heads/master.zip"
        },
        {
            "name": "Awesome AI",
            "repo": "owainlewis/awesome-artificial-intelligence",
            "description": "A curated list of Artificial Intelligence resources",
            "stars": "25k",
            "language": "Markdown",
            "topics": ["Awesome List", "Resources", "Curated"],
            "download_url": "https://github.com/owainlewis/awesome-artificial-intelligence/archive/refs/heads/master.zip"
        }
    ]
    
    for project in learning_projects:
        render_project_card(project)

with tab5:
    st.header("🔥 Trending AI Projects")
    
    trending_projects = [
        {
            "name": "ChatGPT Next Web",
            "repo": "ChatGPTNextWeb/ChatGPT-Next-Web",
            "description": "A cross-platform ChatGPT/Gemini UI (Web / PWA / Linux / Win / MacOS)",
            "stars": "75k",
            "language": "TypeScript",
            "topics": ["ChatGPT", "UI", "Cross-platform"],
            "download_url": "https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web/archive/refs/heads/main.zip"
        },
        {
            "name": "Open WebUI",
            "repo": "open-webui/open-webui",
            "description": "User-friendly WebUI for LLMs (Formerly Ollama WebUI)",
            "stars": "42k",
            "language": "Svelte",
            "topics": ["WebUI", "Ollama", "LLM Interface"],
            "download_url": "https://github.com/open-webui/open-webui/archive/refs/heads/main.zip"
        },
        {
            "name": "Dify",
            "repo": "langgenius/dify",
            "description": "Dify is an open-source LLM app development platform",
            "stars": "47k",
            "language": "TypeScript",
            "topics": ["LLM Apps", "Platform", "Development"],
            "download_url": "https://github.com/langgenius/dify/archive/refs/heads/main.zip"
        },
        {
            "name": "Cursor Rules",
            "repo": "PatrickJS/awesome-cursorrules",
            "description": "A curated list of awesome .cursorrules files",
            "stars": "2.1k",
            "language": "Markdown",
            "topics": ["Cursor", "AI Coding", "Rules"],
            "download_url": "https://github.com/PatrickJS/awesome-cursorrules/archive/refs/heads/main.zip"
        }
    ]
    
    for project in trending_projects:
        render_project_card(project)

# Footer with navigation
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📥 Downloads Center", use_container_width=True):
        st.switch_page("pages/06_📥_Downloads_Center.py")

with col2:
    if st.button("🧠 AI Knowledge Base", use_container_width=True):
        st.switch_page("pages/04_🧠_AI_Knowledge_Base.py")

with col3:
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("main_app.py")

# Sidebar with GitHub stats
with st.sidebar:
    st.markdown("### 📊 GitHub Statistics")
    
    st.metric("Featured Repositories", 16)
    st.metric("Total Stars", "500k+")
    st.metric("Categories", 5)
    
    st.markdown("### 🔗 External Resources")
    st.markdown("""
    <div style="margin: 1rem 0;">
        <a href="https://entremotivator.com" target="_blank" class="resource-link">
            🚀 Visit Entremotivator.com
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    - [GitHub Trending](https://github.com/trending)
    - [Papers With Code](https://paperswithcode.com/)
    - [Awesome Lists](https://github.com/sindresorhus/awesome)
    - [AI Collection](https://github.com/ai-collection/ai-collection)
    """)
    
    st.markdown("### 💡 Pro Tips")
    st.info("""
    **GitHub Best Practices:**
    - ⭐ Star repositories you find useful
    - 🍴 Fork projects to experiment
    - 📋 Read README files thoroughly
    - 🐛 Check issues for known problems
    """)

st.markdown("---")
st.markdown("*This page is part of the AI Agent Toolkit by D Hudson. Discover and download the best AI projects from GitHub.*")
