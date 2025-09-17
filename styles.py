import streamlit as st

def apply_custom_css():
    """Apply custom CSS for gold theme and hidden Streamlit settings"""
    
    custom_css = """
    <style>
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Hide the "Deploy" button and other toolbar items */
    .stDeployButton {display: none;}
    .stToolbar {display: none;}
    
    /* Hide the hamburger menu */
    button[title="View fullscreen"] {display: none;}
    
    /* Gold theme for sidebar */
    .css-1d391kg, .css-1lcbmhc, .css-17eq0hr {
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 50%, #FF8C00 100%);
        background-attachment: fixed;
    }
    
    /* Sidebar text styling */
    .css-1d391kg .css-1v0mbdj, 
    .css-1lcbmhc .css-1v0mbdj,
    .css-17eq0hr .css-1v0mbdj {
        color: #1a1a1a !important;
        font-weight: 600;
    }
    
    /* Sidebar headers */
    .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3,
    .css-1lcbmhc h1, .css-1lcbmhc h2, .css-1lcbmhc h3,
    .css-17eq0hr h1, .css-17eq0hr h2, .css-17eq0hr h3 {
        color: #1a1a1a !important;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.3);
    }
    
    /* Sidebar buttons */
    .css-1d391kg .stButton > button,
    .css-1lcbmhc .stButton > button,
    .css-17eq0hr .stButton > button {
        background: linear-gradient(45deg, #1a1a1a, #333333);
        color: #FFD700 !important;
        border: 2px solid #FFD700;
        border-radius: 8px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    
    .css-1d391kg .stButton > button:hover,
    .css-1lcbmhc .stButton > button:hover,
    .css-17eq0hr .stButton > button:hover {
        background: linear-gradient(45deg, #FFD700, #FFA500);
        color: #1a1a1a !important;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }
    
    /* Sidebar input fields */
    .css-1d391kg .stTextInput > div > div > input,
    .css-1lcbmhc .stTextInput > div > div > input,
    .css-17eq0hr .stTextInput > div > div > input {
        background-color: rgba(255,255,255,0.9);
        color: #1a1a1a;
        border: 2px solid #FFD700;
        border-radius: 6px;
    }
    
    /* Sidebar selectbox */
    .css-1d391kg .stSelectbox > div > div > div,
    .css-1lcbmhc .stSelectbox > div > div > div,
    .css-17eq0hr .stSelectbox > div > div > div {
        background-color: rgba(255,255,255,0.9);
        color: #1a1a1a;
        border: 2px solid #FFD700;
    }
    
    /* Main content area enhancement */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 1rem;
    }
    
    /* Enhanced title styling */
    .main h1 {
        color: #1a1a1a;
        text-align: center;
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(45deg, #FFD700, #FFA500);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    
    /* Enhanced subtitle styling */
    .main h1 + p {
        text-align: center;
        font-style: italic;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: linear-gradient(90deg, #FFD700, #FFA500);
        border-radius: 10px;
        padding: 4px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background: rgba(255,255,255,0.2);
        color: #1a1a1a;
        font-weight: 600;
        border-radius: 6px;
        padding: 8px 16px;
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(255,255,255,0.4);
        transform: translateY(-1px);
    }
    
    .stTabs [aria-selected="true"] {
        background: #1a1a1a !important;
        color: #FFD700 !important;
    }
    
    /* Metric styling */
    .css-1xarl3l {
        background: linear-gradient(135deg, #FFD700, #FFA500);
        border-radius: 10px;
        padding: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .css-1xarl3l .css-1wivap2 {
        color: #1a1a1a !important;
        font-weight: bold;
    }
    
    /* Success/Info/Warning/Error message styling */
    .stSuccess {
        background: linear-gradient(135deg, #28a745, #20c997);
        border: none;
        border-radius: 8px;
        color: white;
    }
    
    .stInfo {
        background: linear-gradient(135deg, #17a2b8, #6f42c1);
        border: none;
        border-radius: 8px;
        color: white;
    }
    
    .stWarning {
        background: linear-gradient(135deg, #ffc107, #fd7e14);
        border: none;
        border-radius: 8px;
        color: #1a1a1a;
    }
    
    .stError {
        background: linear-gradient(135deg, #dc3545, #e83e8c);
        border: none;
        border-radius: 8px;
        color: white;
    }
    
    /* Download button styling */
    .stDownloadButton > button {
        background: linear-gradient(45deg, #FFD700, #FFA500);
        color: #1a1a1a;
        border: none;
        border-radius: 8px;
        font-weight: bold;
        padding: 0.5rem 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    
    .stDownloadButton > button:hover {
        background: linear-gradient(45deg, #FFA500, #FF8C00);
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }
    
    /* Form styling */
    .stForm {
        background: rgba(255,215,0,0.1);
        border: 2px solid #FFD700;
        border-radius: 10px;
        padding: 1rem;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: linear-gradient(90deg, #FFD700, #FFA500);
        color: #1a1a1a;
        font-weight: bold;
        border-radius: 8px;
    }
    
    /* Container borders */
    .element-container {
        border-radius: 8px;
    }
    
    /* Custom scrollbar for sidebar */
    .css-1d391kg::-webkit-scrollbar,
    .css-1lcbmhc::-webkit-scrollbar,
    .css-17eq0hr::-webkit-scrollbar {
        width: 8px;
    }
    
    .css-1d391kg::-webkit-scrollbar-track,
    .css-1lcbmhc::-webkit-scrollbar-track,
    .css-17eq0hr::-webkit-scrollbar-track {
        background: rgba(255,255,255,0.2);
        border-radius: 4px;
    }
    
    .css-1d391kg::-webkit-scrollbar-thumb,
    .css-1lcbmhc::-webkit-scrollbar-thumb,
    .css-17eq0hr::-webkit-scrollbar-thumb {
        background: #1a1a1a;
        border-radius: 4px;
    }
    
    .css-1d391kg::-webkit-scrollbar-thumb:hover,
    .css-1lcbmhc::-webkit-scrollbar-thumb:hover,
    .css-17eq0hr::-webkit-scrollbar-thumb:hover {
        background: #333333;
    }
    
    /* Animation for page load */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .main .block-container {
        animation: fadeInUp 0.6s ease-out;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main h1 {
            font-size: 2rem;
        }
        
        .main .block-container {
            margin: 0.5rem;
            padding: 1rem;
        }
    }
    </style>
    """
    
    st.markdown(custom_css, unsafe_allow_html=True)

def add_custom_header():
    """Add a custom header with branding"""
    header_html = """
    <div style="
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 50%, #FF8C00 100%);
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    ">
        <h2 style="
            color: #1a1a1a;
            margin: 0;
            font-weight: 700;
            text-shadow: 1px 1px 2px rgba(255,255,255,0.3);
        ">🏆 AI Knowledge Hub - Premium Experience</h2>
        <p style="
            color: #333;
            margin: 0.5rem 0 0 0;
            font-style: italic;
        ">Enhanced with golden theme and advanced features</p>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)

def add_footer():
    """Add a custom footer"""
    footer_html = """
    <div style="
        margin-top: 3rem;
        padding: 2rem;
        background: linear-gradient(135deg, #1a1a1a, #333333);
        border-radius: 10px;
        text-align: center;
        color: #FFD700;
    ">
        <h4 style="margin: 0 0 1rem 0;">✨ AI Knowledge Hub</h4>
        <p style="margin: 0; opacity: 0.8;">
            Powered by advanced AI technology • Enhanced user experience • Premium gold theme
        </p>
        <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; opacity: 0.6;">
            © 2024 AI Knowledge Hub. All rights reserved.
        </p>
    </div>
    """
    st.markdown(footer_html, unsafe_allow_html=True)

def hide_streamlit_elements():
    """Hide specific Streamlit UI elements"""
    hide_elements = """
    <style>
    /* Hide the link button for headers */
    .css-15zrgzn {display: none}
    .css-eczf16 {display: none}
    .css-jn99sy {display: none}
    
    /* Hide "Made with Streamlit" */
    .css-cio0dv.egzxvld1 {display: none}
    
    /* Hide fullscreen button for plots */
    button[title="View fullscreen"] {display: none !important}
    
    /* Hide the settings menu */
    .css-14xtw13.e8zbici0 {display: none}
    
    /* Hide deploy button */
    .css-1rs6os.edgvbvh3 {display: none}
    
    /* Hide GitHub icon */
    .css-1544g2n.e1fqkh3o4 {display: none}
    
    /* Additional hiding for various Streamlit elements */
    .reportview-container .main .block-container {{
        padding-top: 1rem;
    }}
    
    /* Hide the hamburger menu completely */
    .css-1rs6os.edgvbvh3,
    .css-10trblm.e16nr0p30,
    .css-1kyxreq.etr89bj2 {{
        display: none !important;
    }}
    </style>
    """
    st.markdown(hide_elements, unsafe_allow_html=True)

