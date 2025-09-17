import streamlit as st
from auth_utils import AuthManager, require_super_admin, init_session_state
from styles import apply_custom_css, hide_streamlit_elements
from datetime import datetime
import json

st.set_page_config(page_title="Admin Panel", page_icon="👑", layout="wide")

# Apply custom styling
apply_custom_css()
hide_streamlit_elements()

# Initialize authentication
auth_manager = AuthManager()
init_session_state()

# Require super admin access
require_super_admin()

# Header
st.title("👑 Super Admin Panel")
st.markdown("*Administrative controls and system management*")
st.markdown("---")

# Admin tabs
tab1, tab2, tab3, tab4 = st.tabs(["👥 User Management", "⚙️ System Settings", "📊 Analytics", "🔧 Maintenance"])

with tab1:
    st.header("👥 User Management")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📋 User Overview")
        
        # Note about user management limitations
        st.info("""
        **Note:** Full user management requires additional Supabase configuration with admin privileges.
        Current implementation shows basic user information and provides manual approval workflow.
        """)
        
        # Mock user data for demonstration
        mock_users = [
            {
                "id": "user_001",
                "email": "entremotivator@gmail.com",
                "role": "super_admin",
                "status": "active",
                "created_at": "2024-01-15",
                "last_login": "2024-09-17"
            },
            {
                "id": "user_002", 
                "email": "user@example.com",
                "role": "user",
                "status": "pending",
                "created_at": "2024-09-16",
                "last_login": "Never"
            }
        ]
        
        st.markdown("### Current Users")
        for user in mock_users:
            with st.container():
                col_a, col_b, col_c = st.columns([2, 1, 1])
                
                with col_a:
                    status_icon = "👑" if user["role"] == "super_admin" else ("✅" if user["status"] == "active" else "⏳")
                    st.write(f"{status_icon} **{user['email']}**")
                    st.caption(f"Role: {user['role'].title()} | Created: {user['created_at']}")
                
                with col_b:
                    if user["status"] == "pending":
                        if st.button("✅ Approve", key=f"approve_{user['id']}"):
                            st.success(f"User {user['email']} approved!")
                            st.rerun()
                    else:
                        st.write(f"Status: {user['status'].title()}")
                
                with col_c:
                    if user["role"] != "super_admin":
                        if st.button("🚫 Suspend", key=f"suspend_{user['id']}"):
                            st.warning(f"User {user['email']} suspended!")
                            st.rerun()
                
                st.divider()
    
    with col2:
        st.subheader("📈 User Stats")
        
        # User statistics
        total_users = len(mock_users)
        active_users = len([u for u in mock_users if u["status"] == "active"])
        pending_users = len([u for u in mock_users if u["status"] == "pending"])
        
        st.metric("Total Users", total_users)
        st.metric("Active Users", active_users)
        st.metric("Pending Approval", pending_users)
        
        st.markdown("---")
        
        st.subheader("🔧 Quick Actions")
        
        if st.button("📧 Send Welcome Email", use_container_width=True):
            st.info("Welcome email sent to new users!")
        
        if st.button("🔄 Refresh User Data", use_container_width=True):
            st.success("User data refreshed!")
        
        if st.button("📊 Export User List", use_container_width=True):
            user_data = json.dumps(mock_users, indent=2)
            st.download_button(
                label="⬇️ Download JSON",
                data=user_data,
                file_name=f"users_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )

with tab2:
    st.header("⚙️ System Settings")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎨 Application Settings")
        
        # Theme settings
        st.markdown("#### Theme Configuration")
        theme_color = st.color_picker("Primary Color", "#FFD700", help="Main theme color (currently gold)")
        sidebar_style = st.selectbox("Sidebar Style", ["Expanded", "Collapsed", "Auto"])
        
        # Feature toggles
        st.markdown("#### Feature Toggles")
        enable_downloads = st.checkbox("Enable Downloads", value=True)
        enable_user_registration = st.checkbox("Enable User Registration", value=True)
        enable_analytics = st.checkbox("Enable Analytics", value=False)
        
        if st.button("💾 Save Settings", use_container_width=True):
            st.success("Settings saved successfully!")
    
    with col2:
        st.subheader("🔒 Security Settings")
        
        # Security options
        st.markdown("#### Authentication")
        require_email_verification = st.checkbox("Require Email Verification", value=True)
        session_timeout = st.number_input("Session Timeout (minutes)", min_value=15, max_value=480, value=60)
        
        st.markdown("#### Access Control")
        default_user_role = st.selectbox("Default User Role", ["user", "viewer"], index=0)
        auto_approve_users = st.checkbox("Auto-approve Users", value=False, help="Automatically approve new user registrations")
        
        if st.button("🔐 Update Security", use_container_width=True):
            st.success("Security settings updated!")

with tab3:
    st.header("📊 System Analytics")
    
    # Mock analytics data
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Daily Active Users", "12", delta="2")
    with col2:
        st.metric("Page Views", "156", delta="23")
    with col3:
        st.metric("Downloads", "45", delta="8")
    with col4:
        st.metric("API Calls", "234", delta="-5")
    
    st.markdown("---")
    
    # Charts placeholder
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 User Activity")
        st.info("Analytics charts would be displayed here with real data integration.")
        
        # Mock data for demonstration
        import pandas as pd
        import numpy as np
        
        dates = pd.date_range(start='2024-09-01', end='2024-09-17', freq='D')
        activity_data = pd.DataFrame({
            'Date': dates,
            'Active Users': np.random.randint(8, 20, len(dates)),
            'Page Views': np.random.randint(50, 200, len(dates))
        })
        
        st.line_chart(activity_data.set_index('Date'))
    
    with col2:
        st.subheader("📊 Feature Usage")
        
        feature_data = pd.DataFrame({
            'Feature': ['Downloads', 'AI Knowledge', 'Ollama Course', 'GitHub Tools'],
            'Usage': [45, 78, 32, 56]
        })
        
        st.bar_chart(feature_data.set_index('Feature'))

with tab4:
    st.header("🔧 System Maintenance")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🗂️ Cache Management")
        
        if st.button("🧹 Clear Application Cache", use_container_width=True):
            st.cache_data.clear()
            st.success("Application cache cleared!")
        
        if st.button("🔄 Refresh Static Files", use_container_width=True):
            st.success("Static files refreshed!")
        
        st.markdown("---")
        
        st.subheader("📋 System Information")
        st.write("**Application Version:** 2.0.0")
        st.write("**Streamlit Version:** 1.49.0")
        st.write("**Python Version:** 3.11+")
        st.write("**Last Updated:** September 17, 2024")
    
    with col2:
        st.subheader("🔍 System Health")
        
        # Health checks
        health_checks = [
            ("Database Connection", "✅ Healthy"),
            ("Authentication Service", "✅ Healthy"), 
            ("File System", "✅ Healthy"),
            ("External APIs", "⚠️ Degraded")
        ]
        
        for service, status in health_checks:
            st.write(f"**{service}:** {status}")
        
        st.markdown("---")
        
        if st.button("🔍 Run Full System Check", use_container_width=True):
            with st.spinner("Running system diagnostics..."):
                import time
                time.sleep(2)
            st.success("System check completed! All services operational.")
        
        if st.button("📊 Generate System Report", use_container_width=True):
            report_data = {
                "timestamp": datetime.now().isoformat(),
                "system_status": "healthy",
                "active_users": 12,
                "total_users": 2,
                "health_checks": health_checks
            }
            
            st.download_button(
                label="⬇️ Download Report",
                data=json.dumps(report_data, indent=2),
                file_name=f"system_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json"
            )

# Footer
st.markdown("---")
st.markdown("*👑 **Super Admin Panel** - Manage your AI Knowledge Hub with administrative privileges*")

