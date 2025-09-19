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
    page_title="Resources - AI Agent Toolkit",
    page_icon="📚",
    layout="wide"
)

# Display logo
display_logo()

# Page content
st.title("📚 AI Agent Toolkit Resources")

st.markdown("""
Welcome to the comprehensive resource center of the AI Agent Toolkit by D Hudson. Here you'll find everything you need to master AI agent development, from beginner guides to advanced implementation strategies.

## 📥 Download Our Premium Guides

Get instant access to our professionally crafted PDF guides that will accelerate your AI journey.
""")

# Resource downloads
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📋 The Ultimate AI & Bot Checklist")
    st.markdown("""
    A comprehensive, step-by-step checklist that covers every aspect of AI agent development:
    
    - **Planning & Design**: Define goals and map user flows
    - **Development**: Implementation best practices
    - **Testing & Deployment**: Quality assurance strategies  
    - **Monitoring & Maintenance**: Long-term success metrics
    
    This checklist ensures you never miss a critical step in your AI project.
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
    st.markdown("### 🛠️ 250 Best AI Tools")
    st.markdown("""
    Our curated directory of the most powerful AI tools available:
    
    - **Content Creation**: Writing, design, and media tools
    - **Development**: Coding assistants and frameworks
    - **Business Intelligence**: Analytics and automation
    - **Specialized Applications**: Industry-specific solutions
    
    Each tool includes detailed descriptions, pricing, and use cases.
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

st.markdown("---")

st.markdown("""
## 🎓 Learning Pathways

### Beginner Track
1. **Understanding AI Fundamentals**
2. **Introduction to AI Agents**
3. **Building Your First Bot**
4. **Basic Deployment Strategies**

### Intermediate Track
1. **Advanced Agent Architectures**
2. **Integration with APIs and Databases**
3. **Natural Language Processing**
4. **Performance Optimization**

### Advanced Track
1. **Multi-Agent Systems**
2. **Machine Learning Integration**
3. **Enterprise Deployment**
4. **Custom Framework Development**

## 🔗 External Resources

### Official Documentation
- **OpenAI API**: Complete guide to GPT integration
- **LangChain**: Framework for LLM applications
- **Streamlit**: Web app framework for Python
- **Supabase**: Backend-as-a-Service platform

### Community Resources
- **GitHub Repositories**: Open-source AI agent projects
- **Discord Communities**: Real-time help and collaboration
- **YouTube Channels**: Video tutorials and walkthroughs
- **Medium Articles**: In-depth technical guides

## 🌐 Stay Connected and Learn More

For the latest updates, tutorials, and advanced resources, visit our main resource hub:
""")

st.markdown("""
<div style="text-align: center; margin: 3rem 0;">
    <a href="https://entremotivator.com" target="_blank" style="display: inline-block; background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); color: #000000 !important; padding: 1rem 2rem; border-radius: 12px; text-decoration: none; font-weight: 600; font-family: 'Inter', sans-serif; transition: all 0.3s ease; box-shadow: 0 4px 12px rgba(245, 158, 11, 0.3); margin: 0.5rem; font-size: 1.1rem;">
        🚀 Explore More Resources at Entremotivator.com
    </a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
## 📧 Get Support

Need help with your AI agent project? Our community and expert network are here to assist:

- **Technical Questions**: Get help with implementation challenges
- **Best Practices**: Learn from experienced developers
- **Project Reviews**: Receive feedback on your AI agents
- **Career Guidance**: Navigate the AI job market

## 🎯 What's Next?

After downloading our resources and exploring the toolkit:

1. **Start Small**: Begin with a simple AI agent project
2. **Join Communities**: Connect with other AI developers
3. **Keep Learning**: Stay updated with the latest AI trends
4. **Share Your Work**: Contribute back to the community

---

*The AI Agent Toolkit by D Hudson is your complete resource for building intelligent, autonomous systems. Whether you're just starting or looking to advance your skills, we have the tools and knowledge you need to succeed.*
""")

st.markdown("---")
st.markdown("*This page is part of the AI Agent Toolkit by D Hudson. Explore other sections for comprehensive AI development resources.*")
