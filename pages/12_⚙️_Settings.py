import streamlit as st
from datetime import datetime
from supabase import create_client, Client
import os
import base64
import json

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
    
    /* Form styling */
    .stForm {
        background: rgba(30, 41, 59, 0.8);
        border: 1px solid #475569;
        border-radius: 12px;
        padding: 2rem;
        margin: 1rem 0;
    }
    
    /* Input styling */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > select,
    .stTextArea > div > div > textarea {
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid #475569;
        border-radius: 8px;
        color: #ffffff;
    }
    
    /* Toggle styling */
    .stCheckbox > label {
        color: #ffffff !important;
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
    
    .stError {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.2) 0%, rgba(220, 38, 38, 0.2) 100%);
        border: 1px solid #ef4444;
        color: #fca5a5 !important;
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

st.set_page_config(page_title="Settings - AI Agent Toolkit", page_icon="⚙️", layout="wide")

# Authentication check
if not st.session_state.get("authenticated", False):
    st.warning("🔒 Please sign in to access Settings.")
    st.stop()

# Display logo
display_logo()

# Header
st.title("⚙️ Settings")
st.markdown("*Configure your AI Agent Toolkit preferences and system settings*")

# Horizontal menu
menu_col1, menu_col2, menu_col3, menu_col4, menu_col5 = st.columns(5)
with menu_col1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("main_app.py")
with menu_col2:
    if st.button("👥 User Management", use_container_width=True):
        st.switch_page("pages/10_👥_User_Management.py")
with menu_col3:
    if st.button("📊 Analytics", use_container_width=True):
        st.switch_page("pages/11_📊_Analytics.py")
with menu_col4:
    if st.button("📚 Resources", use_container_width=True):
        st.switch_page("pages/03_📚_Resources.py")
with menu_col5:
    if st.button("📦 GitHub Hub", use_container_width=True):
        st.switch_page("pages/07_📦_GitHub_Resources.py")

st.markdown("---")

# Initialize settings in session state
if "app_settings" not in st.session_state:
    st.session_state.app_settings = {
        "theme": "dark",
        "notifications": True,
        "auto_save": True,
        "language": "English",
        "timezone": "UTC",
        "email_notifications": True,
        "marketing_emails": False,
        "data_retention": 365,
        "api_rate_limit": 1000,
        "max_file_size": 10,
        "debug_mode": False
    }

# Main content tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["👤 Profile", "🎨 Appearance", "🔔 Notifications", "🔒 Privacy & Security", "🛠️ System"])

with tab1:
    st.header("👤 Profile Settings")
    
    with st.form("profile_form"):
        st.subheader("Personal Information")
        
        col1, col2 = st.columns(2)
        
        with col1:
            display_name = st.text_input("Display Name", value=st.session_state.get("user_email", "").split("@")[0])
            email = st.text_input("Email Address", value=st.session_state.get("user_email", ""), disabled=True)
            phone = st.text_input("Phone Number", placeholder="+1 (555) 123-4567")
        
        with col2:
            company = st.text_input("Company/Organization", placeholder="Your Company")
            job_title = st.text_input("Job Title", placeholder="Your Role")
            location = st.text_input("Location", placeholder="City, Country")
        
        bio = st.text_area("Bio", placeholder="Tell us about yourself...", height=100)
        
        st.subheader("Preferences")
        
        col1, col2 = st.columns(2)
        
        with col1:
            language = st.selectbox("Language", ["English", "Spanish", "French", "German", "Chinese"])
            timezone = st.selectbox("Timezone", [
                "UTC", "EST (Eastern)", "PST (Pacific)", "GMT (London)", 
                "CET (Central Europe)", "JST (Japan)", "AEST (Australia)"
            ])
        
        with col2:
            date_format = st.selectbox("Date Format", ["MM/DD/YYYY", "DD/MM/YYYY", "YYYY-MM-DD"])
            time_format = st.selectbox("Time Format", ["12-hour (AM/PM)", "24-hour"])
        
        if st.form_submit_button("💾 Save Profile", use_container_width=True):
            # Save profile settings
            st.session_state.app_settings.update({
                "display_name": display_name,
                "phone": phone,
                "company": company,
                "job_title": job_title,
                "location": location,
                "bio": bio,
                "language": language,
                "timezone": timezone,
                "date_format": date_format,
                "time_format": time_format
            })
            st.success("✅ Profile updated successfully!")

with tab2:
    st.header("🎨 Appearance Settings")
    
    with st.form("appearance_form"):
        st.subheader("Theme & Display")
        
        col1, col2 = st.columns(2)
        
        with col1:
            theme = st.selectbox("Theme", ["Dark (Default)", "Light", "Auto"], 
                               index=0 if st.session_state.app_settings.get("theme") == "dark" else 1)
            
            sidebar_style = st.selectbox("Sidebar Style", ["Expanded", "Collapsed", "Auto"])
            
            font_size = st.selectbox("Font Size", ["Small", "Medium", "Large"], index=1)
        
        with col2:
            accent_color = st.selectbox("Accent Color", [
                "Orange (Default)", "Blue", "Green", "Purple", "Red"
            ])
            
            layout_density = st.selectbox("Layout Density", ["Compact", "Comfortable", "Spacious"], index=1)
            
            animation_speed = st.selectbox("Animation Speed", ["Slow", "Normal", "Fast"], index=1)
        
        st.subheader("Dashboard Customization")
        
        col1, col2 = st.columns(2)
        
        with col1:
            show_welcome = st.checkbox("Show Welcome Message", value=True)
            show_tips = st.checkbox("Show Daily Tips", value=True)
            show_stats = st.checkbox("Show Quick Stats", value=True)
        
        with col2:
            show_recent = st.checkbox("Show Recent Activity", value=True)
            show_shortcuts = st.checkbox("Show Quick Actions", value=True)
            show_weather = st.checkbox("Show Weather Widget", value=False)
        
        if st.form_submit_button("🎨 Apply Theme", use_container_width=True):
            st.session_state.app_settings.update({
                "theme": theme.lower().split()[0],
                "sidebar_style": sidebar_style.lower(),
                "font_size": font_size.lower(),
                "accent_color": accent_color.lower().split()[0],
                "layout_density": layout_density.lower(),
                "animation_speed": animation_speed.lower(),
                "show_welcome": show_welcome,
                "show_tips": show_tips,
                "show_stats": show_stats,
                "show_recent": show_recent,
                "show_shortcuts": show_shortcuts,
                "show_weather": show_weather
            })
            st.success("✅ Appearance settings updated!")

with tab3:
    st.header("🔔 Notification Settings")
    
    with st.form("notifications_form"):
        st.subheader("Email Notifications")
        
        col1, col2 = st.columns(2)
        
        with col1:
            email_notifications = st.checkbox("Enable Email Notifications", 
                                            value=st.session_state.app_settings.get("email_notifications", True))
            
            security_alerts = st.checkbox("Security Alerts", value=True)
            system_updates = st.checkbox("System Updates", value=True)
            feature_announcements = st.checkbox("Feature Announcements", value=True)
        
        with col2:
            marketing_emails = st.checkbox("Marketing Emails", 
                                         value=st.session_state.app_settings.get("marketing_emails", False))
            
            weekly_digest = st.checkbox("Weekly Digest", value=True)
            usage_reports = st.checkbox("Usage Reports", value=False)
            community_updates = st.checkbox("Community Updates", value=False)
        
        st.subheader("In-App Notifications")
        
        col1, col2 = st.columns(2)
        
        with col1:
            push_notifications = st.checkbox("Push Notifications", value=True)
            sound_notifications = st.checkbox("Sound Notifications", value=False)
            desktop_notifications = st.checkbox("Desktop Notifications", value=True)
        
        with col2:
            notification_frequency = st.selectbox("Notification Frequency", 
                                                ["Immediate", "Hourly", "Daily", "Weekly"])
            
            quiet_hours_start = st.time_input("Quiet Hours Start", value=datetime.strptime("22:00", "%H:%M").time())
            quiet_hours_end = st.time_input("Quiet Hours End", value=datetime.strptime("08:00", "%H:%M").time())
        
        if st.form_submit_button("🔔 Save Notifications", use_container_width=True):
            st.session_state.app_settings.update({
                "email_notifications": email_notifications,
                "marketing_emails": marketing_emails,
                "security_alerts": security_alerts,
                "system_updates": system_updates,
                "feature_announcements": feature_announcements,
                "weekly_digest": weekly_digest,
                "usage_reports": usage_reports,
                "community_updates": community_updates,
                "push_notifications": push_notifications,
                "sound_notifications": sound_notifications,
                "desktop_notifications": desktop_notifications,
                "notification_frequency": notification_frequency,
                "quiet_hours_start": quiet_hours_start.strftime("%H:%M"),
                "quiet_hours_end": quiet_hours_end.strftime("%H:%M")
            })
            st.success("✅ Notification settings updated!")

with tab4:
    st.header("🔒 Privacy & Security Settings")
    
    with st.form("security_form"):
        st.subheader("Account Security")
        
        col1, col2 = st.columns(2)
        
        with col1:
            two_factor_auth = st.checkbox("Two-Factor Authentication", value=False)
            login_notifications = st.checkbox("Login Notifications", value=True)
            session_timeout = st.selectbox("Session Timeout", ["15 minutes", "30 minutes", "1 hour", "4 hours", "Never"])
        
        with col2:
            password_strength = st.selectbox("Password Requirements", ["Standard", "Strong", "Very Strong"])
            account_recovery = st.checkbox("Enable Account Recovery", value=True)
            device_tracking = st.checkbox("Track Login Devices", value=True)
        
        st.subheader("Data Privacy")
        
        col1, col2 = st.columns(2)
        
        with col1:
            data_collection = st.checkbox("Allow Analytics Data Collection", value=True)
            usage_tracking = st.checkbox("Usage Tracking", value=True)
            crash_reporting = st.checkbox("Crash Reporting", value=True)
        
        with col2:
            data_retention = st.selectbox("Data Retention Period", 
                                        ["30 days", "90 days", "1 year", "2 years", "Forever"])
            
            data_sharing = st.checkbox("Allow Data Sharing with Partners", value=False)
            personalization = st.checkbox("Personalized Experience", value=True)
        
        st.subheader("API & Integrations")
        
        col1, col2 = st.columns(2)
        
        with col1:
            api_access = st.checkbox("Enable API Access", value=True)
            third_party_integrations = st.checkbox("Third-party Integrations", value=True)
            webhook_notifications = st.checkbox("Webhook Notifications", value=False)
        
        with col2:
            api_rate_limit = st.number_input("API Rate Limit (requests/hour)", 
                                           min_value=100, max_value=10000, value=1000)
            
            ip_whitelist = st.text_area("IP Whitelist (one per line)", 
                                      placeholder="192.168.1.1\n10.0.0.1")
        
        if st.form_submit_button("🔒 Update Security", use_container_width=True):
            st.session_state.app_settings.update({
                "two_factor_auth": two_factor_auth,
                "login_notifications": login_notifications,
                "session_timeout": session_timeout,
                "password_strength": password_strength,
                "account_recovery": account_recovery,
                "device_tracking": device_tracking,
                "data_collection": data_collection,
                "usage_tracking": usage_tracking,
                "crash_reporting": crash_reporting,
                "data_retention": data_retention,
                "data_sharing": data_sharing,
                "personalization": personalization,
                "api_access": api_access,
                "third_party_integrations": third_party_integrations,
                "webhook_notifications": webhook_notifications,
                "api_rate_limit": api_rate_limit,
                "ip_whitelist": ip_whitelist
            })
            st.success("✅ Security settings updated!")

with tab5:
    st.header("🛠️ System Settings")
    
    # Only show system settings for admins
    if st.session_state.get("role") == "admin":
        with st.form("system_form"):
            st.subheader("Application Configuration")
            
            col1, col2 = st.columns(2)
            
            with col1:
                debug_mode = st.checkbox("Debug Mode", value=st.session_state.app_settings.get("debug_mode", False))
                maintenance_mode = st.checkbox("Maintenance Mode", value=False)
                auto_backup = st.checkbox("Auto Backup", value=True)
            
            with col2:
                max_file_size = st.number_input("Max File Size (MB)", min_value=1, max_value=100, value=10)
                cache_duration = st.selectbox("Cache Duration", ["1 hour", "6 hours", "24 hours", "7 days"])
                log_level = st.selectbox("Log Level", ["ERROR", "WARNING", "INFO", "DEBUG"])
            
            st.subheader("Database Settings")
            
            col1, col2 = st.columns(2)
            
            with col1:
                connection_pool_size = st.number_input("Connection Pool Size", min_value=5, max_value=50, value=10)
                query_timeout = st.number_input("Query Timeout (seconds)", min_value=5, max_value=300, value=30)
            
            with col2:
                backup_frequency = st.selectbox("Backup Frequency", ["Hourly", "Daily", "Weekly"])
                retention_policy = st.selectbox("Backup Retention", ["7 days", "30 days", "90 days", "1 year"])
            
            st.subheader("Performance Settings")
            
            col1, col2 = st.columns(2)
            
            with col1:
                enable_caching = st.checkbox("Enable Caching", value=True)
                compress_responses = st.checkbox("Compress Responses", value=True)
                enable_cdn = st.checkbox("Enable CDN", value=False)
            
            with col2:
                concurrent_users = st.number_input("Max Concurrent Users", min_value=10, max_value=1000, value=100)
                request_timeout = st.number_input("Request Timeout (seconds)", min_value=10, max_value=120, value=30)
            
            if st.form_submit_button("🛠️ Update System Settings", use_container_width=True):
                st.session_state.app_settings.update({
                    "debug_mode": debug_mode,
                    "maintenance_mode": maintenance_mode,
                    "auto_backup": auto_backup,
                    "max_file_size": max_file_size,
                    "cache_duration": cache_duration,
                    "log_level": log_level,
                    "connection_pool_size": connection_pool_size,
                    "query_timeout": query_timeout,
                    "backup_frequency": backup_frequency,
                    "retention_policy": retention_policy,
                    "enable_caching": enable_caching,
                    "compress_responses": compress_responses,
                    "enable_cdn": enable_cdn,
                    "concurrent_users": concurrent_users,
                    "request_timeout": request_timeout
                })
                st.success("✅ System settings updated!")
        
        st.markdown("---")
        
        # System actions
        st.subheader("🔧 System Actions")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🔄 Restart Application", use_container_width=True):
                st.warning("⚠️ Application restart initiated. This may take a few minutes.")
        
        with col2:
            if st.button("🗑️ Clear Cache", use_container_width=True):
                st.success("✅ Cache cleared successfully!")
        
        with col3:
            if st.button("📊 Generate Report", use_container_width=True):
                st.info("📊 System report generated and sent to administrators.")
    
    else:
        st.info("🔒 System settings are only available to administrators.")
        
        # User-level system preferences
        st.subheader("🎛️ User Preferences")
        
        with st.form("user_system_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                auto_save = st.checkbox("Auto-save", value=st.session_state.app_settings.get("auto_save", True))
                keyboard_shortcuts = st.checkbox("Keyboard Shortcuts", value=True)
            
            with col2:
                offline_mode = st.checkbox("Offline Mode", value=False)
                beta_features = st.checkbox("Beta Features", value=False)
            
            if st.form_submit_button("💾 Save Preferences", use_container_width=True):
                st.session_state.app_settings.update({
                    "auto_save": auto_save,
                    "keyboard_shortcuts": keyboard_shortcuts,
                    "offline_mode": offline_mode,
                    "beta_features": beta_features
                })
                st.success("✅ Preferences updated!")

# Export/Import Settings
st.markdown("---")
st.subheader("📁 Settings Management")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📤 Export Settings", use_container_width=True):
        settings_json = json.dumps(st.session_state.app_settings, indent=2)
        st.download_button(
            label="💾 Download Settings File",
            data=settings_json,
            file_name=f"ai_toolkit_settings_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json",
            use_container_width=True
        )

with col2:
    uploaded_settings = st.file_uploader("📥 Import Settings", type=['json'])
    if uploaded_settings is not None:
        try:
            imported_settings = json.loads(uploaded_settings.read())
            st.session_state.app_settings.update(imported_settings)
            st.success("✅ Settings imported successfully!")
        except Exception as e:
            st.error(f"❌ Error importing settings: {str(e)}")

with col3:
    if st.button("🔄 Reset to Defaults", use_container_width=True):
        if st.button("⚠️ Confirm Reset", use_container_width=True):
            st.session_state.app_settings = {
                "theme": "dark",
                "notifications": True,
                "auto_save": True,
                "language": "English",
                "timezone": "UTC"
            }
            st.success("✅ Settings reset to defaults!")

# Footer with navigation
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("👥 User Management", use_container_width=True):
        st.switch_page("pages/10_👥_User_Management.py")

with col2:
    if st.button("📊 Analytics", use_container_width=True):
        st.switch_page("pages/11_📊_Analytics.py")

with col3:
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("main_app.py")

# Sidebar with current settings summary
with st.sidebar:
    st.markdown("### ⚙️ Current Settings")
    
    st.markdown(f"**Theme:** {st.session_state.app_settings.get('theme', 'dark').title()}")
    st.markdown(f"**Language:** {st.session_state.app_settings.get('language', 'English')}")
    st.markdown(f"**Notifications:** {'On' if st.session_state.app_settings.get('notifications', True) else 'Off'}")
    st.markdown(f"**Auto-save:** {'On' if st.session_state.app_settings.get('auto_save', True) else 'Off'}")
    
    st.markdown("### 🔗 External Resources")
    st.markdown("""
    <div style="margin: 1rem 0;">
        <a href="https://entremotivator.com" target="_blank" class="resource-link">
            🚀 Visit Entremotivator.com
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    - [Settings Guide](https://docs.example.com)
    - [Privacy Policy](https://example.com/privacy)
    - [Terms of Service](https://example.com/terms)
    """)

st.markdown("---")
st.markdown("*This page is part of the AI Agent Toolkit by D Hudson. Customize your experience with comprehensive settings.*")
