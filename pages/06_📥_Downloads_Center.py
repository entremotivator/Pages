import streamlit as st
import json
import os
import base64
from pathlib import Path
from datetime import datetime

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
    
    /* Download button styling */
    .stDownloadButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: #ffffff;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-family: 'Inter', sans-serif;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
    }
    
    .stDownloadButton > button:hover {
        background: linear-gradient(135deg, #059669 0%, #047857 100%);
        box-shadow: 0 6px 20px rgba(16, 185, 129, 0.5);
        transform: translateY(-2px);
    }
    
    /* File card styling */
    .file-card {
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid #475569;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    .file-card:hover {
        border-color: #f59e0b;
        box-shadow: 0 4px 20px rgba(245, 158, 11, 0.2);
        transform: translateY(-2px);
    }
    
    /* Metric styling */
    .stMetric {
        background: rgba(30, 41, 59, 0.6);
        border-radius: 8px;
        padding: 1rem;
        border: 1px solid #475569;
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
    
    .stWarning {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.2) 0%, rgba(217, 119, 6, 0.2) 100%);
        border: 1px solid #f59e0b;
        color: #fbbf24 !important;
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

def get_local_json_files():
    """Get all JSON files from the project directory"""
    project_root = Path("/home/ubuntu/ai-agent-toolkit")
    json_files = []
    
    # Look for JSON files in common directories
    search_paths = [
        project_root,
        project_root / "workflows",
        project_root / "data",
        project_root / "exports"
    ]
    
    for search_path in search_paths:
        if search_path.exists():
            for json_file in search_path.glob("**/*.json"):
                if json_file.is_file():
                    try:
                        # Get file stats
                        stat = json_file.stat()
                        size = stat.st_size
                        modified = datetime.fromtimestamp(stat.st_mtime)
                        
                        # Try to read and validate JSON
                        with open(json_file, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                        
                        json_files.append({
                            'name': json_file.name,
                            'path': str(json_file),
                            'relative_path': str(json_file.relative_to(project_root)),
                            'size': size,
                            'modified': modified,
                            'data': data,
                            'valid': True
                        })
                    except Exception as e:
                        json_files.append({
                            'name': json_file.name,
                            'path': str(json_file),
                            'relative_path': str(json_file.relative_to(project_root)),
                            'size': json_file.stat().st_size if json_file.exists() else 0,
                            'modified': datetime.fromtimestamp(json_file.stat().st_mtime) if json_file.exists() else None,
                            'data': None,
                            'valid': False,
                            'error': str(e)
                        })
    
    return sorted(json_files, key=lambda x: x['name'])

def format_file_size(size_bytes):
    """Format file size in human readable format"""
    if size_bytes == 0:
        return "0 B"
    size_names = ["B", "KB", "MB", "GB"]
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024.0
        i += 1
    return f"{size_bytes:.1f} {size_names[i]}"

def analyze_workflow(data):
    """Analyze workflow JSON data"""
    if not data or not isinstance(data, dict):
        return None
    
    nodes = data.get('nodes', [])
    connections = data.get('connections', {})
    
    analysis = {
        'node_count': len(nodes),
        'connection_count': len(connections),
        'node_types': list(set(node.get('type', 'Unknown') for node in nodes)),
        'active': data.get('active', False),
        'name': data.get('name', 'Unnamed Workflow'),
        'has_webhook': any(node.get('type') == 'n8n-nodes-base.webhook' for node in nodes),
        'has_trigger': any('trigger' in node.get('type', '').lower() for node in nodes)
    }
    
    return analysis

# Apply styling and authentication check
hide_streamlit_style()
apply_ai_toolkit_theme()

st.set_page_config(page_title="Downloads Center - AI Agent Toolkit", page_icon="📥", layout="wide")

# Authentication check
if not st.session_state.get("authenticated", False):
    st.warning("🔒 Please sign in to access the Downloads Center.")
    st.stop()

# Display logo
display_logo()

# Header
st.title("📥 Downloads Center")
st.markdown("*Access and download available JSON workflow files and resources*")

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
    if st.button("🦙 Ollama Course", use_container_width=True):
        st.switch_page("pages/05_🦙_Ollama_Course.py")

st.markdown("---")

# Main content tabs
tab1, tab2, tab3 = st.tabs(["📁 JSON Files", "📄 PDF Resources", "🔧 Workflow Tools"])

with tab1:
    st.header("📁 Available JSON Files")
    
    # Get local JSON files
    json_files = get_local_json_files()
    
    if not json_files:
        st.info("📂 No JSON files found in the project directory.")
        st.markdown("""
        **To add JSON files:**
        1. Place your JSON files in the project root directory
        2. Or create a `workflows` folder and add them there
        3. Refresh this page to see them appear
        """)
    else:
        # Summary statistics
        col1, col2, col3, col4 = st.columns(4)
        
        valid_files = [f for f in json_files if f['valid']]
        total_size = sum(f['size'] for f in json_files)
        
        with col1:
            st.metric("Total Files", len(json_files))
        with col2:
            st.metric("Valid JSON", len(valid_files))
        with col3:
            st.metric("Total Size", format_file_size(total_size))
        with col4:
            st.metric("Invalid Files", len(json_files) - len(valid_files))
        
        st.markdown("---")
        
        # File listing
        for file_info in json_files:
            st.markdown(f'<div class="file-card">', unsafe_allow_html=True)
            
            col1, col2 = st.columns([3, 1])
            
            with col1:
                # File header
                status_icon = "✅" if file_info['valid'] else "❌"
                st.markdown(f"### {status_icon} {file_info['name']}")
                st.markdown(f"**Path:** `{file_info['relative_path']}`")
                st.markdown(f"**Size:** {format_file_size(file_info['size'])}")
                st.markdown(f"**Modified:** {file_info['modified'].strftime('%Y-%m-%d %H:%M:%S') if file_info['modified'] else 'Unknown'}")
                
                # Analysis for valid JSON files
                if file_info['valid'] and file_info['data']:
                    analysis = analyze_workflow(file_info['data'])
                    if analysis:
                        st.markdown(f"**Workflow Name:** {analysis['name']}")
                        
                        # Metrics row
                        metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)
                        with metric_col1:
                            st.metric("Nodes", analysis['node_count'])
                        with metric_col2:
                            st.metric("Connections", analysis['connection_count'])
                        with metric_col3:
                            st.metric("Active", "Yes" if analysis['active'] else "No")
                        with metric_col4:
                            st.metric("Has Trigger", "Yes" if analysis['has_trigger'] else "No")
                        
                        # Node types
                        if analysis['node_types']:
                            st.markdown(f"**Node Types:** {', '.join(analysis['node_types'][:5])}{'...' if len(analysis['node_types']) > 5 else ''}")
                
                # Error information for invalid files
                elif not file_info['valid']:
                    st.error(f"**Error:** {file_info.get('error', 'Unknown error')}")
            
            with col2:
                st.markdown("### Actions")
                
                # Download button for valid files
                if file_info['valid']:
                    try:
                        with open(file_info['path'], 'rb') as f:
                            file_data = f.read()
                        
                        st.download_button(
                            label="📥 Download",
                            data=file_data,
                            file_name=file_info['name'],
                            mime="application/json",
                            use_container_width=True,
                            key=f"download_{file_info['name']}"
                        )
                    except Exception as e:
                        st.error(f"Error reading file: {str(e)}")
                
                # View button for JSON preview
                if file_info['valid'] and st.button("👁️ Preview", key=f"preview_{file_info['name']}", use_container_width=True):
                    with st.expander(f"JSON Preview - {file_info['name']}", expanded=True):
                        st.json(file_info['data'])
            
            st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.header("📄 PDF Resources")
    
    # PDF downloads section
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 The Ultimate AI & Bot Checklist")
        st.markdown("""
        A comprehensive, step-by-step checklist that covers every aspect of AI agent development:
        
        - **Planning & Design**: Define goals and map user flows
        - **Development**: Implementation best practices
        - **Testing & Deployment**: Quality assurance strategies  
        - **Monitoring & Maintenance**: Long-term success metrics
        """)
        
        if os.path.exists("/home/ubuntu/ai-agent-toolkit/AI_and_Bot_Checklist.pdf"):
            with open("/home/ubuntu/ai-agent-toolkit/AI_and_Bot_Checklist.pdf", "rb") as file:
                st.download_button(
                    label="📥 Download AI & Bot Checklist PDF",
                    data=file.read(),
                    file_name="AI_and_Bot_Checklist.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
    
    with col2:
        st.subheader("🛠️ 250 Best AI Tools")
        st.markdown("""
        Our curated directory of the most powerful AI tools available:
        
        - **Content Creation**: Writing, design, and media tools
        - **Development**: Coding assistants and frameworks
        - **Business Intelligence**: Analytics and automation
        - **Specialized Applications**: Industry-specific solutions
        """)
        
        if os.path.exists("/home/ubuntu/ai-agent-toolkit/250_Best_AI_Tools.pdf"):
            with open("/home/ubuntu/ai-agent-toolkit/250_Best_AI_Tools.pdf", "rb") as file:
                st.download_button(
                    label="📥 Download 250 AI Tools PDF",
                    data=file.read(),
                    file_name="250_Best_AI_Tools.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )

with tab3:
    st.header("🔧 Workflow Tools")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 JSON Validator")
        
        uploaded_file = st.file_uploader("Upload JSON file to validate", type=['json'])
        
        if uploaded_file is not None:
            try:
                json_data = json.load(uploaded_file)
                st.success("✅ Valid JSON file!")
                
                # Basic analysis
                if isinstance(json_data, dict):
                    st.markdown("**File Analysis:**")
                    st.markdown(f"- Keys: {len(json_data.keys())}")
                    st.markdown(f"- Type: {type(json_data).__name__}")
                    
                    # Workflow analysis if applicable
                    analysis = analyze_workflow(json_data)
                    if analysis:
                        st.markdown(f"- Workflow Name: {analysis['name']}")
                        st.markdown(f"- Nodes: {analysis['node_count']}")
                        st.markdown(f"- Connections: {analysis['connection_count']}")
                
                with st.expander("View JSON Content"):
                    st.json(json_data)
                    
            except json.JSONDecodeError as e:
                st.error(f"❌ Invalid JSON: {str(e)}")
            except Exception as e:
                st.error(f"❌ Error processing file: {str(e)}")
    
    with col2:
        st.subheader("🔄 Format Converter")
        
        st.markdown("""
        **Available Conversions:**
        - JSON to YAML
        - JSON to CSV (for tabular data)
        - JSON prettify/minify
        - Workflow export formats
        """)
        
        st.info("💡 **Coming Soon**: Advanced conversion tools for different workflow formats.")

# Footer with navigation
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📦 GitHub Resources", use_container_width=True):
        st.switch_page("pages/07_📦_GitHub_Resources.py")

with col2:
    if st.button("🧠 AI Knowledge Base", use_container_width=True):
        st.switch_page("pages/04_🧠_AI_Knowledge_Base.py")

with col3:
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("main_app.py")

# Sidebar with quick stats
with st.sidebar:
    st.markdown("### 📊 Download Statistics")
    
    json_files = get_local_json_files()
    valid_files = [f for f in json_files if f['valid']]
    
    st.metric("JSON Files", len(json_files))
    st.metric("Valid Files", len(valid_files))
    st.metric("PDF Resources", 2)
    
    st.markdown("### 🔗 External Resources")
    st.markdown("""
    <div style="margin: 1rem 0;">
        <a href="https://entremotivator.com" target="_blank" class="resource-link">
            🚀 Visit Entremotivator.com
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    - [JSON Validator Online](https://jsonlint.com/)
    - [n8n Community](https://community.n8n.io/)
    - [Workflow Templates](https://n8n.io/workflows/)
    """)

st.markdown("---")
st.markdown("*This page is part of the AI Agent Toolkit by D Hudson. Download and manage your workflow resources.*")
