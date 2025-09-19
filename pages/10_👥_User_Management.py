import streamlit as st
from datetime import datetime
from supabase import create_client, Client
import os
import base64
import pandas as pd

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
    
    /* DataFrames styling */
    .stDataFrame {
        background: rgba(30, 41, 59, 0.8);
        border-radius: 12px;
        border: 1px solid #475569;
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

st.set_page_config(page_title="User Management - AI Agent Toolkit", page_icon="👥", layout="wide")

# Authentication check
if not st.session_state.get("authenticated", False):
    st.warning("🔒 Please sign in to access User Management.")
    st.stop()

# Admin check
if st.session_state.get("role") != "admin":
    st.error("🚫 Access denied. This page is only available to administrators.")
    st.stop()

# Display logo
display_logo()

# Header
st.title("👥 User Management")
st.markdown("*Manage users, roles, and access permissions*")

# Horizontal menu
menu_col1, menu_col2, menu_col3, menu_col4, menu_col5 = st.columns(5)
with menu_col1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("main_app.py")
with menu_col2:
    if st.button("📝 User Plans", use_container_width=True):
        st.switch_page("pages/09_📝_User_Plans_Management.py")
with menu_col3:
    if st.button("📊 Analytics", use_container_width=True):
        st.switch_page("pages/11_📊_Analytics.py")
with menu_col4:
    if st.button("📚 Resources", use_container_width=True):
        st.switch_page("pages/03_📚_Resources.py")
with menu_col5:
    if st.button("⚙️ Settings", use_container_width=True):
        st.switch_page("pages/12_⚙️_Settings.py")

st.markdown("---")

# Load Supabase credentials safely
def get_supabase_credentials():
    # Try nested secrets first
    if "supabase" in st.secrets:
        url = st.secrets["supabase"].get("url")
        key = st.secrets["supabase"].get("key")
        service_key = st.secrets["supabase"].get("service_role_key")
    else:  # fallback to flat structure
        url = st.secrets.get("SUPABASE_URL")
        key = st.secrets.get("SUPABASE_ANON_KEY")
        service_key = st.secrets.get("SUPABASE_SERVICE_KEY")

    if not url or not key:
        st.error("❌ Supabase credentials are missing. Check your secrets.toml.")
        st.stop()
    return url, key, service_key

try:
    SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_SERVICE_KEY = get_supabase_credentials()
    
    @st.cache_resource
    def init_supabase_client():
        return create_client(SUPABASE_URL, SUPABASE_ANON_KEY)

    supabase: Client = init_supabase_client()
    
except Exception as e:
    st.error(f"Failed to initialize Supabase client: {str(e)}")
    st.stop()

# Main content tabs
tab1, tab2, tab3, tab4 = st.tabs(["👥 All Users", "🔍 Search Users", "📊 User Analytics", "⚙️ Bulk Actions"])

with tab1:
    st.header("👥 All Users")
    
    try:
        # Fetch all user profiles
        users_result = supabase.table("user_profiles").select("*").execute()
        
        if users_result.data:
            st.subheader(f"📊 Total Users: {len(users_result.data)}")
            
            # Display users in a more organized way
            for i, user in enumerate(users_result.data):
                with st.expander(f"👤 {user.get('email', 'No email')} - {user.get('role', 'user').title()}"):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown(f"**User ID:** `{user.get('id', 'N/A')}`")
                        st.markdown(f"**Email:** {user.get('email', 'N/A')}")
                        st.markdown(f"**Role:** {user.get('role', 'user').title()}")
                        st.markdown(f"**Created:** {user.get('created_at', 'N/A')}")
                    
                    with col2:
                        # User actions
                        st.markdown("**Actions:**")
                        
                        action_col1, action_col2, action_col3 = st.columns(3)
                        
                        with action_col1:
                            if st.button("👑 Make Admin", key=f"admin_{i}"):
                                try:
                                    supabase.table("user_profiles").update({"role": "admin"}).eq("id", user.get('id')).execute()
                                    st.success("User promoted to admin!")
                                    st.rerun()
                                except Exception as e:
                                    st.error(f"Error: {str(e)}")
                        
                        with action_col2:
                            if st.button("👤 Make User", key=f"user_{i}"):
                                try:
                                    supabase.table("user_profiles").update({"role": "user"}).eq("id", user.get('id')).execute()
                                    st.success("User role updated!")
                                    st.rerun()
                                except Exception as e:
                                    st.error(f"Error: {str(e)}")
                        
                        with action_col3:
                            if st.button("🚫 Suspend", key=f"suspend_{i}"):
                                try:
                                    supabase.table("user_profiles").update({"role": "suspended"}).eq("id", user.get('id')).execute()
                                    st.success("User suspended!")
                                    st.rerun()
                                except Exception as e:
                                    st.error(f"Error: {str(e)}")
        else:
            st.info("📭 No users found.")
            
    except Exception as e:
        st.error(f"❌ Error fetching users: {str(e)}")

with tab2:
    st.header("🔍 Search Users")
    
    # Search filters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        search_email = st.text_input("🔍 Search by Email")
    with col2:
        filter_role = st.selectbox("Filter by Role", ["All", "user", "admin", "suspended"])
    with col3:
        date_filter = st.date_input("Created after", value=None)
    
    if st.button("🔍 Search Users", use_container_width=True):
        try:
            # Build query
            query = supabase.table("user_profiles").select("*")
            
            if search_email:
                query = query.ilike("email", f"%{search_email}%")
            
            if filter_role != "All":
                query = query.eq("role", filter_role)
            
            if date_filter:
                query = query.gte("created_at", date_filter.isoformat())
            
            search_result = query.execute()
            
            if search_result.data:
                st.success(f"Found {len(search_result.data)} users matching your criteria")
                
                # Convert to DataFrame for better display
                df = pd.DataFrame(search_result.data)
                if not df.empty:
                    # Select relevant columns
                    display_columns = ['email', 'role', 'created_at']
                    available_columns = [col for col in display_columns if col in df.columns]
                    
                    if available_columns:
                        st.dataframe(df[available_columns], use_container_width=True)
                    else:
                        st.dataframe(df, use_container_width=True)
            else:
                st.info("No users found matching your search criteria.")
                
        except Exception as e:
            st.error(f"❌ Search error: {str(e)}")

with tab3:
    st.header("📊 User Analytics")
    
    try:
        # Fetch user data for analytics
        users_result = supabase.table("user_profiles").select("*").execute()
        
        if users_result.data:
            users_data = users_result.data
            
            # Summary metrics
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                total_users = len(users_data)
                st.metric("Total Users", total_users)
            
            with col2:
                admin_users = len([u for u in users_data if u.get('role') == 'admin'])
                st.metric("Admin Users", admin_users)
            
            with col3:
                regular_users = len([u for u in users_data if u.get('role') == 'user'])
                st.metric("Regular Users", regular_users)
            
            with col4:
                suspended_users = len([u for u in users_data if u.get('role') == 'suspended'])
                st.metric("Suspended Users", suspended_users)
            
            # Role distribution
            st.subheader("📈 User Role Distribution")
            
            role_counts = {}
            for user in users_data:
                role = user.get('role', 'unknown')
                role_counts[role] = role_counts.get(role, 0) + 1
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Role Breakdown:**")
                for role, count in role_counts.items():
                    percentage = (count / total_users) * 100 if total_users > 0 else 0
                    st.markdown(f"- {role.title()}: {count} ({percentage:.1f}%)")
            
            with col2:
                # Recent registrations
                st.markdown("**Recent Activity:**")
                try:
                    recent_users = sorted(users_data, key=lambda x: x.get('created_at', ''), reverse=True)[:5]
                    for user in recent_users:
                        created_date = user.get('created_at', 'Unknown')
                        if created_date != 'Unknown':
                            try:
                                created_date = datetime.fromisoformat(created_date.replace('Z', '+00:00')).strftime('%Y-%m-%d')
                            except:
                                pass
                        st.markdown(f"- {user.get('email', 'No email')} ({created_date})")
                except:
                    st.markdown("- Unable to load recent activity")
        else:
            st.info("📭 No user data available for analytics.")
            
    except Exception as e:
        st.error(f"❌ Error generating analytics: {str(e)}")

with tab4:
    st.header("⚙️ Bulk Actions")
    
    st.warning("⚠️ **Warning:** Bulk actions affect multiple users at once. Use with caution!")
    
    # Bulk role assignment
    st.subheader("👥 Bulk Role Assignment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        bulk_role = st.selectbox("Select Role to Assign", ["user", "admin", "suspended"])
        user_emails = st.text_area("User Emails (one per line)", placeholder="user1@example.com\nuser2@example.com")
    
    with col2:
        st.markdown("**Preview:**")
        if user_emails:
            email_list = [email.strip() for email in user_emails.split('\n') if email.strip()]
            st.markdown(f"- **Action:** Set role to '{bulk_role}'")
            st.markdown(f"- **Affected users:** {len(email_list)}")
            for email in email_list[:5]:  # Show first 5
                st.markdown(f"  - {email}")
            if len(email_list) > 5:
                st.markdown(f"  - ... and {len(email_list) - 5} more")
    
    if st.button("🚀 Execute Bulk Action", use_container_width=True):
        if user_emails and bulk_role:
            email_list = [email.strip() for email in user_emails.split('\n') if email.strip()]
            
            success_count = 0
            error_count = 0
            
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i, email in enumerate(email_list):
                try:
                    result = supabase.table("user_profiles").update({"role": bulk_role}).eq("email", email).execute()
                    if result.data:
                        success_count += 1
                    else:
                        error_count += 1
                except Exception as e:
                    error_count += 1
                
                # Update progress
                progress = (i + 1) / len(email_list)
                progress_bar.progress(progress)
                status_text.text(f"Processing {i + 1}/{len(email_list)}: {email}")
            
            progress_bar.empty()
            status_text.empty()
            
            if success_count > 0:
                st.success(f"✅ Successfully updated {success_count} users")
            if error_count > 0:
                st.error(f"❌ Failed to update {error_count} users")
        else:
            st.warning("Please provide user emails and select a role.")

# Footer with navigation
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📝 User Plans", use_container_width=True):
        st.switch_page("pages/09_📝_User_Plans_Management.py")

with col2:
    if st.button("📊 Analytics Dashboard", use_container_width=True):
        st.switch_page("pages/11_📊_Analytics.py")

with col3:
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("main_app.py")

# Sidebar with quick stats
with st.sidebar:
    st.markdown("### 📊 Quick Stats")
    
    try:
        users_result = supabase.table("user_profiles").select("*").execute()
        if users_result.data:
            total_users = len(users_result.data)
            admin_users = len([u for u in users_result.data if u.get('role') == 'admin'])
            regular_users = len([u for u in users_result.data if u.get('role') == 'user'])
            
            st.metric("Total Users", total_users)
            st.metric("Admins", admin_users)
            st.metric("Regular Users", regular_users)
    except:
        st.metric("Total Users", "N/A")
        st.metric("Admins", "N/A")
        st.metric("Regular Users", "N/A")
    
    st.markdown("### 🔗 External Resources")
    st.markdown("""
    <div style="margin: 1rem 0;">
        <a href="https://entremotivator.com" target="_blank" class="resource-link">
            🚀 Visit Entremotivator.com
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    - [User Management Best Practices](https://docs.example.com)
    - [Supabase Auth Docs](https://supabase.com/docs/guides/auth)
    - [GDPR Compliance Guide](https://gdpr.eu/)
    """)

st.markdown("---")
st.markdown("*This page is part of the AI Agent Toolkit by D Hudson. Manage your user base effectively and securely.*")
