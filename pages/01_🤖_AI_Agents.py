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
    page_title="AI Agents - AI Agent Toolkit",
    page_icon="🤖",
    layout="wide"
)

# Display logo
display_logo()

# Page content
st.title("🤖 AI Agents")

st.markdown("""
Welcome to the **AI Agents** section of the AI Agent Toolkit by D Hudson. This comprehensive guide will help you understand, build, and deploy powerful AI agents for various applications.

## What are AI Agents?

AI agents are autonomous software entities that can perceive their environment, make decisions, and take actions to achieve specific goals. They combine artificial intelligence with automation to create intelligent systems that can work independently or alongside humans.

## Types of AI Agents

### 1. Reactive Agents
- Respond to immediate stimuli
- No memory of past actions
- Simple rule-based behavior

### 2. Deliberative Agents
- Plan actions based on goals
- Maintain internal state
- Use reasoning and decision-making

### 3. Hybrid Agents
- Combine reactive and deliberative approaches
- Balance quick responses with strategic planning
- Most common in real-world applications

## Building Your First AI Agent

### Step 1: Define the Purpose
Clearly articulate what your AI agent should accomplish:
- Customer service automation
- Data analysis and reporting
- Content generation
- Process automation

### Step 2: Choose the Right Framework
Popular AI agent frameworks include:
- **LangChain**: For language model applications
- **AutoGPT**: For autonomous task execution
- **CrewAI**: For multi-agent collaboration
- **Microsoft Bot Framework**: For conversational agents

### Step 3: Design the Architecture
Consider these components:
- **Perception**: How the agent receives input
- **Decision Making**: The AI model and logic
- **Action**: How the agent responds or acts
- **Memory**: Storing context and learning

## Best Practices

1. **Start Simple**: Begin with basic functionality and iterate
2. **Test Thoroughly**: Ensure reliable performance across scenarios
3. **Monitor Performance**: Track metrics and user satisfaction
4. **Plan for Scale**: Design with growth in mind
5. **Ensure Security**: Protect data and prevent misuse

## Resources for Learning More

For additional resources, tutorials, and advanced techniques, visit:
""")

st.markdown("""
<div style="text-align: center; margin: 2rem 0;">
    <a href="https://entremotivator.com" target="_blank" style="display: inline-block; background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); color: #000000 !important; padding: 0.75rem 1.5rem; border-radius: 12px; text-decoration: none; font-weight: 600; font-family: 'Inter', sans-serif; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(245, 158, 11, 0.3); margin: 0.5rem;">
        🚀 Visit Entremotivator.com for More AI Resources
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.markdown("*This page is part of the AI Agent Toolkit by D Hudson. Explore other sections for comprehensive AI development resources.*")
