import streamlit as st
from datetime import date, datetime
from supabase import create_client, Client
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
    .stDateInput > div > div > input {
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid #475569;
        border-radius: 8px;
        color: #ffffff;
    }
    
    /* Table styling */
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

st.set_page_config(page_title="User Plans Management - AI Agent Toolkit", page_icon="📝", layout="wide")

# Authentication check
if not st.session_state.get("authenticated", False):
    st.warning("🔒 Please sign in to access User Plans Management.")
    st.stop()

# Admin check
if st.session_state.get("role") != "admin":
    st.error("🚫 Access denied. This page is only available to administrators.")
    st.stop()

# Display logo
display_logo()

# Header
st.title("📝 User Plans Management")
st.markdown("*Manage user subscription plans and access levels*")

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
tab1, tab2, tab3 = st.tabs(["➕ Add Plan", "📋 Manage Plans", "📊 Plan Statistics"])

with tab1:
    st.header("➕ Add New User Plan")
    
    with st.form("add_user_plan_form"):
        st.subheader("Plan Details")
        
        col1, col2 = st.columns(2)
        
        with col1:
            user_id = st.text_input("User ID (UUID)", help="UUID from Supabase auth.users table")
            plan_name = st.selectbox("Plan Name", ["Free", "Basic", "Premium", "Enterprise"])
            
        with col2:
            start_date = st.date_input("Start Date", value=date.today())
            end_date = st.date_input("End Date", value=date.today().replace(year=date.today().year + 1))
        
        # Additional plan features
        st.subheader("Plan Features")
        
        feature_col1, feature_col2 = st.columns(2)
        
        with feature_col1:
            max_projects = st.number_input("Max Projects", min_value=1, max_value=1000, value=10)
            max_storage_gb = st.number_input("Max Storage (GB)", min_value=1, max_value=1000, value=10)
        
        with feature_col2:
            api_calls_limit = st.number_input("API Calls Limit", min_value=100, max_value=100000, value=1000)
            priority_support = st.checkbox("Priority Support")
        
        notes = st.text_area("Notes (Optional)", placeholder="Any additional notes about this plan...")
        
        submitted = st.form_submit_button("Add Plan", use_container_width=True)

        if submitted:
            if user_id and plan_name and start_date and end_date:
                try:
                    # Insert new plan
                    plan_data = {
                        "user_id": user_id,
                        "plan_name": plan_name,
                        "start_date": start_date.isoformat(),
                        "end_date": end_date.isoformat(),
                        "max_projects": max_projects,
                        "max_storage_gb": max_storage_gb,
                        "api_calls_limit": api_calls_limit,
                        "priority_support": priority_support,
                        "notes": notes,
                        "created_at": datetime.now().isoformat(),
                        "status": "active"
                    }
                    
                    result = supabase.table("user_plans").insert(plan_data).execute()
                    
                    if result.data:
                        st.success(f"✅ Successfully added {plan_name} plan for user {user_id}")
                        st.rerun()
                    else:
                        st.error("❌ Failed to add plan. Please check the user ID and try again.")
                        
                except Exception as e:
                    st.error(f"❌ Error adding plan: {str(e)}")
            else:
                st.warning("⚠️ Please fill in all required fields.")

with tab2:
    st.header("📋 Manage Existing Plans")
    
    try:
        # Fetch all user plans
        plans_result = supabase.table("user_plans").select("*").execute()
        
        if plans_result.data:
            st.subheader(f"📊 Total Plans: {len(plans_result.data)}")
            
            # Search and filter options
            col1, col2, col3 = st.columns(3)
            
            with col1:
                search_user = st.text_input("🔍 Search by User ID")
            with col2:
                filter_plan = st.selectbox("Filter by Plan", ["All", "Free", "Basic", "Premium", "Enterprise"])
            with col3:
                filter_status = st.selectbox("Filter by Status", ["All", "active", "expired", "cancelled"])
            
            # Filter plans based on search criteria
            filtered_plans = plans_result.data
            
            if search_user:
                filtered_plans = [p for p in filtered_plans if search_user.lower() in p.get('user_id', '').lower()]
            
            if filter_plan != "All":
                filtered_plans = [p for p in filtered_plans if p.get('plan_name') == filter_plan]
            
            if filter_status != "All":
                filtered_plans = [p for p in filtered_plans if p.get('status') == filter_status]
            
            # Display plans
            for plan in filtered_plans:
                with st.expander(f"📋 {plan.get('plan_name', 'Unknown')} - {plan.get('user_id', 'Unknown')[:8]}..."):
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown(f"**User ID:** `{plan.get('user_id', 'N/A')}`")
                        st.markdown(f"**Plan:** {plan.get('plan_name', 'N/A')}")
                        st.markdown(f"**Status:** {plan.get('status', 'N/A')}")
                        st.markdown(f"**Start Date:** {plan.get('start_date', 'N/A')}")
                        st.markdown(f"**End Date:** {plan.get('end_date', 'N/A')}")
                    
                    with col2:
                        st.markdown(f"**Max Projects:** {plan.get('max_projects', 'N/A')}")
                        st.markdown(f"**Max Storage:** {plan.get('max_storage_gb', 'N/A')} GB")
                        st.markdown(f"**API Calls Limit:** {plan.get('api_calls_limit', 'N/A')}")
                        st.markdown(f"**Priority Support:** {'Yes' if plan.get('priority_support') else 'No'}")
                    
                    if plan.get('notes'):
                        st.markdown(f"**Notes:** {plan.get('notes')}")
                    
                    # Action buttons
                    action_col1, action_col2, action_col3 = st.columns(3)
                    
                    with action_col1:
                        if st.button(f"✏️ Edit", key=f"edit_{plan.get('id')}"):
                            st.session_state[f"editing_{plan.get('id')}"] = True
                    
                    with action_col2:
                        if st.button(f"🚫 Suspend", key=f"suspend_{plan.get('id')}"):
                            try:
                                supabase.table("user_plans").update({"status": "suspended"}).eq("id", plan.get('id')).execute()
                                st.success("Plan suspended successfully!")
                                st.rerun()
                            except Exception as e:
                                st.error(f"Error suspending plan: {str(e)}")
                    
                    with action_col3:
                        if st.button(f"🗑️ Delete", key=f"delete_{plan.get('id')}"):
                            try:
                                supabase.table("user_plans").delete().eq("id", plan.get('id')).execute()
                                st.success("Plan deleted successfully!")
                                st.rerun()
                            except Exception as e:
                                st.error(f"Error deleting plan: {str(e)}")
        else:
            st.info("📭 No user plans found. Add some plans to get started!")
            
    except Exception as e:
        st.error(f"❌ Error fetching plans: {str(e)}")

with tab3:
    st.header("📊 Plan Statistics")
    
    try:
        # Fetch plan statistics
        plans_result = supabase.table("user_plans").select("*").execute()
        
        if plans_result.data:
            plans_data = plans_result.data
            
            # Summary metrics
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                total_plans = len(plans_data)
                st.metric("Total Plans", total_plans)
            
            with col2:
                active_plans = len([p for p in plans_data if p.get('status') == 'active'])
                st.metric("Active Plans", active_plans)
            
            with col3:
                premium_plans = len([p for p in plans_data if p.get('plan_name') in ['Premium', 'Enterprise']])
                st.metric("Premium Plans", premium_plans)
            
            with col4:
                avg_storage = sum(p.get('max_storage_gb', 0) for p in plans_data) / len(plans_data) if plans_data else 0
                st.metric("Avg Storage (GB)", f"{avg_storage:.1f}")
            
            # Plan distribution
            st.subheader("📈 Plan Distribution")
            
            plan_counts = {}
            for plan in plans_data:
                plan_name = plan.get('plan_name', 'Unknown')
                plan_counts[plan_name] = plan_counts.get(plan_name, 0) + 1
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("**Plans by Type:**")
                for plan_name, count in plan_counts.items():
                    percentage = (count / total_plans) * 100 if total_plans > 0 else 0
                    st.markdown(f"- {plan_name}: {count} ({percentage:.1f}%)")
            
            with col2:
                st.markdown("**Status Distribution:**")
                status_counts = {}
                for plan in plans_data:
                    status = plan.get('status', 'unknown')
                    status_counts[status] = status_counts.get(status, 0) + 1
                
                for status, count in status_counts.items():
                    percentage = (count / total_plans) * 100 if total_plans > 0 else 0
                    st.markdown(f"- {status.title()}: {count} ({percentage:.1f}%)")
        else:
            st.info("📭 No plan data available for statistics.")
            
    except Exception as e:
        st.error(f"❌ Error generating statistics: {str(e)}")

# Footer with navigation
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("👥 User Management", use_container_width=True):
        st.switch_page("pages/10_👥_User_Management.py")

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
        plans_result = supabase.table("user_plans").select("*").execute()
        if plans_result.data:
            total_plans = len(plans_result.data)
            active_plans = len([p for p in plans_result.data if p.get('status') == 'active'])
            
            st.metric("Total Plans", total_plans)
            st.metric("Active Plans", active_plans)
            st.metric("Success Rate", f"{(active_plans/total_plans*100):.1f}%" if total_plans > 0 else "0%")
    except:
        st.metric("Total Plans", "N/A")
        st.metric("Active Plans", "N/A")
        st.metric("Success Rate", "N/A")
    
    st.markdown("### 🔗 External Resources")
    st.markdown("""
    <div style="margin: 1rem 0;">
        <a href="https://entremotivator.com" target="_blank" class="resource-link">
            🚀 Visit Entremotivator.com
        </a>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    - [Supabase Docs](https://supabase.com/docs)
    - [User Management Guide](https://docs.example.com)
    - [Billing Integration](https://stripe.com/docs)
    """)

st.markdown("---")
st.markdown("*This page is part of the AI Agent Toolkit by D Hudson. Manage user subscriptions and access levels efficiently.*")
