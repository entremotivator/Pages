import streamlit as st
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
        <div style="display: flex; justify-content: center; align-items: center; margin: 2rem 0;">
            <img src="data:image/png;base64,{get_base64_of_bin_file(logo_path)}" alt="AI Agent Toolkit Logo" style="max-width: 300px; height: auto; filter: drop-shadow(0 8px 32px rgba(245, 158, 11, 0.3));">
        </div>
        """, unsafe_allow_html=True)

# Apply hiding and styling
hide_streamlit_style()

# Page configuration
st.set_page_config(
    page_title="AI Tools - AI Agent Toolkit",
    page_icon="🛠️",
    layout="wide"
)

# Display logo
display_logo()

# Page content
st.title("🛠️ AI Tools Directory")

st.markdown("""
Explore our curated collection of the best AI tools available today. This comprehensive directory is part of the AI Agent Toolkit by D Hudson and features tools across various categories to enhance your AI development and deployment workflows.

## Featured Tool Categories

### 🎨 Content Creation & Writing
- **Jasper**: AI-powered content platform for blogs and marketing
- **Copy.ai**: Advanced copywriting assistant
- **Writesonic**: SEO-friendly content generation
- **Grammarly**: AI-powered writing enhancement

### 🖼️ Image & Visual AI
- **Midjourney**: Text-to-image generation
- **DALL-E 2**: OpenAI's image creation tool
- **Stable Diffusion**: Open-source image generation
- **Canva AI**: Design automation platform

### 🎥 Video & Audio
- **Synthesia**: AI video generation with avatars
- **Runway**: Next-generation video editing
- **Descript**: Audio and video editing suite
- **Murf**: AI voice generation

### 💼 Business & Productivity
- **Notion AI**: Intelligent workspace assistant
- **Zapier**: Workflow automation
- **Monday.com**: Project management with AI
- **Salesforce Einstein**: CRM intelligence

### 🔍 Data & Analytics
- **Tableau**: Data visualization with AI insights
- **DataRobot**: Automated machine learning
- **H2O.ai**: Open-source ML platform
- **Alteryx**: Data science automation

## How to Choose the Right AI Tool

When selecting AI tools for your projects, consider:

1. **Purpose Alignment**: Does the tool match your specific needs?
2. **Integration Capabilities**: Can it work with your existing systems?
3. **Scalability**: Will it grow with your requirements?
4. **Cost Effectiveness**: Does the pricing model fit your budget?
5. **Learning Curve**: How quickly can your team adopt it?

## Download Our Complete AI Tools Guide

Get access to our comprehensive **250 Best AI Tools** PDF guide with detailed descriptions, pricing, and use cases.
""")

# Download section
if os.path.exists("/home/ubuntu/ai-agent-toolkit/250_Best_AI_Tools.pdf"):
    with open("/home/ubuntu/ai-agent-toolkit/250_Best_AI_Tools.pdf", "rb") as file:
        st.download_button(
            label="📥 Download 250 Best AI Tools PDF",
            data=file.read(),
            file_name="250_Best_AI_Tools.pdf",
            mime="application/pdf",
            use_container_width=True
        )

st.markdown("""
## Stay Updated with the Latest AI Tools

The AI landscape evolves rapidly. For the most current tools, reviews, and recommendations, visit:
""")

st.markdown("""
<div style="text-align: center; margin: 2rem 0;">
    <a href="https://entremotivator.com" target="_blank" style="display: inline-block; background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); color: #000000 !important; padding: 0.75rem 1.5rem; border-radius: 12px; text-decoration: none; font-weight: 600; font-family: 'Inter', sans-serif; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(245, 158, 11, 0.3); margin: 0.5rem;">
        🚀 Discover More AI Tools at Entremotivator.com
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("*This page is part of the AI Agent Toolkit by D Hudson. Explore other sections for comprehensive AI development resources.*")
