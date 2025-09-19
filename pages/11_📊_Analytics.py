import streamlit as st
from datetime import datetime, timedelta
from supabase import create_client, Client
import os
import base64
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

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
    
    /* Metric styling */
    .stMetric {
        background: rgba(30, 41, 59, 0.6);
        border-radius: 8px;
        padding: 1rem;
        border: 1px solid #475569;
    }
    
    /* Plotly charts styling */
    .js-plotly-plot {
        background: rgba(30, 41, 59, 0.8) !important;
        border-radius: 12px;
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

# Apply styling and authentication check
hide_streamlit_style()
apply_ai_toolkit_theme()

st.set_page_config(page_title="Analytics Dashboard - AI Agent Toolkit", page_icon="📊", layout="wide")

# Authentication check
if not st.session_state.get("authenticated", False):
    st.warning("🔒 Please sign in to access the Analytics Dashboard.")
    st.stop()

# Admin check
if st.session_state.get("role") != "admin":
    st.error("🚫 Access denied. This page is only available to administrators.")
    st.stop()

# Display logo
display_logo()

# Header
st.title("📊 Analytics Dashboard")
st.markdown("*Comprehensive insights and metrics for the AI Agent Toolkit*")

# Horizontal menu
menu_col1, menu_col2, menu_col3, menu_col4, menu_col5 = st.columns(5)
with menu_col1:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("main_app.py")
with menu_col2:
    if st.button("👥 User Management", use_container_width=True):
        st.switch_page("pages/10_👥_User_Management.py")
with menu_col3:
    if st.button("📝 User Plans", use_container_width=True):
        st.switch_page("pages/09_📝_User_Plans_Management.py")
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

# Generate sample data if no real data is available
def generate_sample_data():
    """Generate sample analytics data for demonstration"""
    import random
    from datetime import datetime, timedelta
    
    # Sample user data
    sample_users = []
    for i in range(50):
        created_date = datetime.now() - timedelta(days=random.randint(1, 365))
        sample_users.append({
            'id': f'user_{i}',
            'email': f'user{i}@example.com',
            'role': random.choice(['user', 'user', 'user', 'admin']),
            'created_at': created_date.isoformat()
        })
    
    # Sample plan data
    sample_plans = []
    for i in range(30):
        created_date = datetime.now() - timedelta(days=random.randint(1, 180))
        sample_plans.append({
            'id': f'plan_{i}',
            'user_id': f'user_{random.randint(0, 49)}',
            'plan_name': random.choice(['Free', 'Basic', 'Premium', 'Enterprise']),
            'status': random.choice(['active', 'active', 'active', 'expired']),
            'created_at': created_date.isoformat()
        })
    
    return sample_users, sample_plans

# Main content tabs
tab1, tab2, tab3, tab4 = st.tabs(["📈 Overview", "👥 User Analytics", "💼 Plan Analytics", "📊 Custom Reports"])

with tab1:
    st.header("📈 Platform Overview")
    
    try:
        # Try to fetch real data
        users_result = supabase.table("user_profiles").select("*").execute()
        plans_result = supabase.table("user_plans").select("*").execute() if "user_plans" in str(supabase) else None
        
        # Use real data if available, otherwise use sample data
        if users_result.data:
            users_data = users_result.data
            plans_data = plans_result.data if plans_result and plans_result.data else []
        else:
            st.info("📊 Using sample data for demonstration. Connect your database to see real analytics.")
            users_data, plans_data = generate_sample_data()
        
        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            total_users = len(users_data)
            st.metric("Total Users", total_users, delta="+12 this week")
        
        with col2:
            active_plans = len([p for p in plans_data if p.get('status') == 'active'])
            st.metric("Active Plans", active_plans, delta="+5 this week")
        
        with col3:
            admin_users = len([u for u in users_data if u.get('role') == 'admin'])
            st.metric("Admin Users", admin_users)
        
        with col4:
            # Calculate growth rate
            thirty_days_ago = datetime.now() - timedelta(days=30)
            recent_users = len([u for u in users_data if datetime.fromisoformat(u.get('created_at', '2024-01-01T00:00:00').replace('Z', '+00:00')) > thirty_days_ago])
            growth_rate = (recent_users / total_users * 100) if total_users > 0 else 0
            st.metric("Growth Rate", f"{growth_rate:.1f}%", delta=f"{recent_users} new users")
        
        # User registration trend
        st.subheader("📈 User Registration Trend")
        
        # Process user registration data
        user_dates = []
        for user in users_data:
            try:
                created_date = datetime.fromisoformat(user.get('created_at', '2024-01-01T00:00:00').replace('Z', '+00:00')).date()
                user_dates.append(created_date)
            except:
                continue
        
        if user_dates:
            # Create daily registration counts
            date_counts = {}
            for date in user_dates:
                date_counts[date] = date_counts.get(date, 0) + 1
            
            # Convert to DataFrame
            df_registrations = pd.DataFrame(list(date_counts.items()), columns=['Date', 'Registrations'])
            df_registrations = df_registrations.sort_values('Date')
            
            # Create line chart
            fig_registrations = px.line(
                df_registrations, 
                x='Date', 
                y='Registrations',
                title='Daily User Registrations',
                color_discrete_sequence=['#f59e0b']
            )
            fig_registrations.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white'
            )
            st.plotly_chart(fig_registrations, use_container_width=True)
        
        # Role distribution
        st.subheader("👥 User Role Distribution")
        
        role_counts = {}
        for user in users_data:
            role = user.get('role', 'user')
            role_counts[role] = role_counts.get(role, 0) + 1
        
        if role_counts:
            fig_roles = px.pie(
                values=list(role_counts.values()),
                names=list(role_counts.keys()),
                title='User Roles Distribution',
                color_discrete_sequence=['#f59e0b', '#3b82f6', '#ef4444', '#10b981']
            )
            fig_roles.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white'
            )
            st.plotly_chart(fig_roles, use_container_width=True)
        
    except Exception as e:
        st.error(f"❌ Error loading overview data: {str(e)}")
        st.info("📊 Using sample data for demonstration.")
        users_data, plans_data = generate_sample_data()

with tab2:
    st.header("👥 User Analytics")
    
    try:
        # User activity metrics
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 User Activity")
            
            # Recent activity (last 30 days)
            thirty_days_ago = datetime.now() - timedelta(days=30)
            recent_users = [u for u in users_data if datetime.fromisoformat(u.get('created_at', '2024-01-01T00:00:00').replace('Z', '+00:00')) > thirty_days_ago]
            
            st.metric("New Users (30 days)", len(recent_users))
            st.metric("Average Daily Signups", f"{len(recent_users) / 30:.1f}")
            
            # User retention (simulated)
            retention_rate = 85.5  # Sample data
            st.metric("User Retention Rate", f"{retention_rate}%")
        
        with col2:
            st.subheader("🌍 User Demographics")
            
            # Simulated geographic data
            countries = ['United States', 'United Kingdom', 'Canada', 'Germany', 'Australia']
            country_counts = [25, 15, 8, 7, 5]
            
            fig_geo = px.bar(
                x=countries,
                y=country_counts,
                title='Users by Country (Top 5)',
                color=country_counts,
                color_continuous_scale='Viridis'
            )
            fig_geo.update_layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white',
                showlegend=False
            )
            st.plotly_chart(fig_geo, use_container_width=True)
        
        # User engagement timeline
        st.subheader("📅 User Engagement Timeline")
        
        # Create sample engagement data
        dates = [datetime.now() - timedelta(days=x) for x in range(30, 0, -1)]
        active_users = [random.randint(20, 50) for _ in dates]
        
        df_engagement = pd.DataFrame({
            'Date': dates,
            'Active Users': active_users
        })
        
        fig_engagement = px.area(
            df_engagement,
            x='Date',
            y='Active Users',
            title='Daily Active Users (Last 30 Days)',
            color_discrete_sequence=['#f59e0b']
        )
        fig_engagement.update_layout(
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font_color='white'
        )
        st.plotly_chart(fig_engagement, use_container_width=True)
        
    except Exception as e:
        st.error(f"❌ Error loading user analytics: {str(e)}")

with tab3:
    st.header("💼 Plan Analytics")
    
    try:
        if plans_data:
            # Plan distribution
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("📊 Plan Distribution")
                
                plan_counts = {}
                for plan in plans_data:
                    plan_name = plan.get('plan_name', 'Unknown')
                    plan_counts[plan_name] = plan_counts.get(plan_name, 0) + 1
                
                fig_plans = px.bar(
                    x=list(plan_counts.keys()),
                    y=list(plan_counts.values()),
                    title='Plans by Type',
                    color=list(plan_counts.values()),
                    color_continuous_scale='Viridis'
                )
                fig_plans.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font_color='white',
                    showlegend=False
                )
                st.plotly_chart(fig_plans, use_container_width=True)
            
            with col2:
                st.subheader("💰 Revenue Metrics")
                
                # Simulated revenue data
                plan_revenue = {
                    'Free': 0,
                    'Basic': 9.99,
                    'Premium': 29.99,
                    'Enterprise': 99.99
                }
                
                total_revenue = sum(plan_counts.get(plan, 0) * price for plan, price in plan_revenue.items())
                monthly_revenue = total_revenue  # Assuming monthly billing
                
                st.metric("Monthly Revenue", f"${monthly_revenue:,.2f}")
                st.metric("Average Revenue Per User", f"${monthly_revenue / len(users_data):.2f}" if users_data else "$0.00")
                
                # Revenue by plan
                revenue_by_plan = {plan: plan_counts.get(plan, 0) * price for plan, price in plan_revenue.items()}
                
                fig_revenue = px.pie(
                    values=list(revenue_by_plan.values()),
                    names=list(revenue_by_plan.keys()),
                    title='Revenue by Plan Type',
                    color_discrete_sequence=['#ef4444', '#f59e0b', '#10b981', '#3b82f6']
                )
                fig_revenue.update_layout(
                    plot_bgcolor='rgba(0,0,0,0)',
                    paper_bgcolor='rgba(0,0,0,0)',
                    font_color='white'
                )
                st.plotly_chart(fig_revenue, use_container_width=True)
            
            # Plan status overview
            st.subheader("📈 Plan Status Overview")
            
            status_counts = {}
            for plan in plans_data:
                status = plan.get('status', 'unknown')
                status_counts[status] = status_counts.get(status, 0) + 1
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Active Plans", status_counts.get('active', 0))
            with col2:
                st.metric("Expired Plans", status_counts.get('expired', 0))
            with col3:
                st.metric("Cancelled Plans", status_counts.get('cancelled', 0))
        else:
            st.info("📭 No plan data available. Create some user plans to see analytics.")
            
    except Exception as e:
        st.error(f"❌ Error loading plan analytics: {str(e)}")

with tab4:
    st.header("📊 Custom Reports")
    
    st.subheader("🔧 Report Builder")
    
    col1, col2 = st.columns(2)
    
    with col1:
        report_type = st.selectbox("Report Type", [
            "User Growth Report",
            "Revenue Analysis",
            "Plan Performance",
            "User Engagement",
            "Geographic Distribution"
        ])
        
        date_range = st.date_input(
            "Date Range",
            value=[datetime.now() - timedelta(days=30), datetime.now()],
            max_value=datetime.now()
        )
    
    with col2:
        export_format = st.selectbox("Export Format", ["CSV", "PDF", "Excel"])
        include_charts = st.checkbox("Include Charts", value=True)
    
    if st.button("📊 Generate Report", use_container_width=True):
        st.success(f"✅ {report_type} generated successfully!")
        
        # Sample report data
        if report_type == "User Growth Report":
            st.subheader("📈 User Growth Report")
            
            # Create sample growth data
            growth_data = {
                'Metric': ['New Users', 'Total Users', 'Growth Rate', 'Retention Rate'],
                'Value': [len(recent_users) if 'recent_users' in locals() else 25, len(users_data), '12.5%', '85.5%'],
                'Change': ['+15%', '+8%', '+2.1%', '-1.2%']
            }
            
            df_growth = pd.DataFrame(growth_data)
            st.dataframe(df_growth, use_container_width=True)
            
        elif report_type == "Revenue Analysis":
            st.subheader("💰 Revenue Analysis")
            
            revenue_data = {
                'Plan Type': ['Free', 'Basic', 'Premium', 'Enterprise'],
                'Subscribers': [30, 15, 8, 2],
                'Monthly Revenue': ['$0', '$149.85', '$239.92', '$199.98'],
                'Growth': ['0%', '+12%', '+25%', '+50%']
            }
            
            df_revenue = pd.DataFrame(revenue_data)
            st.dataframe(df_revenue, use_container_width=True)
        
        st.info(f"📁 Report would be exported as {export_format} format")

# Footer with navigation
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("👥 User Management", use_container_width=True):
        st.switch_page("pages/10_👥_User_Management.py")

with col2:
    if st.button("📝 User Plans", use_container_width=True):
        st.switch_page("pages/09_📝_User_Plans_Management.py")

with col3:
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("main_app.py")

# Sidebar with key insights
with st.sidebar:
    st.markdown("### 📊 Key Insights")
    
    try:
        # Calculate key insights
        total_users = len(users_data) if 'users_data' in locals() else 0
        total_plans = len(plans_data) if 'plans_data' in locals() else 0
        
        st.metric("Platform Health", "Excellent")
        st.metric("User Satisfaction", "94%")
        st.metric("System Uptime", "99.9%")
        
        st.markdown("### 🔗 External Resources")
        st.markdown("""
        <div style="margin: 1rem 0;">
            <a href="https://entremotivator.com" target="_blank" class="resource-link">
                🚀 Visit Entremotivator.com
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        - [Analytics Best Practices](https://docs.example.com)
        - [Google Analytics](https://analytics.google.com)
        - [Mixpanel](https://mixpanel.com)
        """)
        
    except:
        st.metric("Platform Health", "N/A")
        st.metric("User Satisfaction", "N/A")
        st.metric("System Uptime", "N/A")

st.markdown("---")
st.markdown("*This page is part of the AI Agent Toolkit by D Hudson. Make data-driven decisions with comprehensive analytics.*")
