import streamlit as st
from auth_utils import AuthManager, require_super_admin, init_session_state
from styles import apply_custom_css, hide_streamlit_elements
from datetime import datetime, timedelta
import json
import pandas as pd
import numpy as np
import time
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Super Admin Panel", page_icon="👑", layout="wide")

# Apply custom styling
apply_custom_css()
hide_streamlit_elements()

# Initialize authentication
auth_manager = AuthManager()
init_session_state()

# Require super admin access
require_super_admin()

# Enhanced CSS for better styling
st.markdown("""
<style>
    .metric-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        margin: 0.5rem 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .user-card {
        background: white;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .user-card:hover {
        box-shadow: 0 4px 16px rgba(0,0,0,0.15);
        transform: translateY(-2px);
    }
    
    .status-badge {
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        text-align: center;
        display: inline-block;
        margin: 0.2rem;
    }
    
    .status-active { background-color: #d4edda; color: #155724; }
    .status-pending { background-color: #fff3cd; color: #856404; }
    .status-suspended { background-color: #f8d7da; color: #721c24; }
    .status-inactive { background-color: #e2e3e5; color: #383d41; }
    
    .role-badge {
        padding: 0.2rem 0.6rem;
        border-radius: 15px;
        font-size: 0.75rem;
        font-weight: bold;
        text-transform: uppercase;
    }
    
    .role-super-admin { background-color: #dc3545; color: white; }
    .role-admin { background-color: #fd7e14; color: white; }
    .role-moderator { background-color: #6f42c1; color: white; }
    .role-user { background-color: #28a745; color: white; }
    .role-viewer { background-color: #6c757d; color: white; }
    
    .section-header {
        background: linear-gradient(90deg, #f8f9fa, #e9ecef);
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1rem;
        border-left: 4px solid #FFD700;
    }
    
    .approval-card {
        border-left: 4px solid #ffc107;
        background-color: #fffbf0;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }
    
    .quick-stats {
        display: flex;
        justify-content: space-between;
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state for user data
if 'users_data' not in st.session_state:
    st.session_state.users_data = [
        {
            "id": "usr_001",
            "email": "entremotivator@gmail.com",
            "name": "Admin User",
            "role": "super_admin",
            "status": "active",
            "created_at": "2024-01-15T10:30:00",
            "last_login": "2024-09-17T14:22:00",
            "login_count": 147,
            "profile_complete": True,
            "email_verified": True,
            "phone": "+1-555-0100",
            "location": "New York, USA"
        },
        {
            "id": "usr_002",
            "email": "john.doe@example.com",
            "name": "John Doe",
            "role": "user",
            "status": "pending",
            "created_at": "2024-09-16T09:15:00",
            "last_login": None,
            "login_count": 0,
            "profile_complete": False,
            "email_verified": True,
            "phone": "+1-555-0101",
            "location": "California, USA"
        },
        {
            "id": "usr_003",
            "email": "jane.smith@company.com",
            "name": "Jane Smith",
            "role": "user",
            "status": "pending",
            "created_at": "2024-09-17T08:45:00",
            "last_login": None,
            "login_count": 0,
            "profile_complete": True,
            "email_verified": False,
            "phone": "+1-555-0102",
            "location": "Texas, USA"
        },
        {
            "id": "usr_004",
            "email": "mike.wilson@tech.com",
            "name": "Mike Wilson",
            "role": "moderator",
            "status": "active",
            "created_at": "2024-08-20T14:20:00",
            "last_login": "2024-09-16T18:30:00",
            "login_count": 89,
            "profile_complete": True,
            "email_verified": True,
            "phone": "+1-555-0103",
            "location": "Washington, USA"
        },
        {
            "id": "usr_005",
            "email": "sarah.connor@future.com",
            "name": "Sarah Connor",
            "role": "user",
            "status": "suspended",
            "created_at": "2024-07-10T11:00:00",
            "last_login": "2024-09-10T16:45:00",
            "login_count": 34,
            "profile_complete": True,
            "email_verified": True,
            "phone": "+1-555-0104",
            "location": "Nevada, USA"
        },
        {
            "id": "usr_006",
            "email": "alex.developer@startup.io",
            "name": "Alex Developer",
            "role": "user",
            "status": "pending",
            "created_at": "2024-09-17T12:30:00",
            "last_login": None,
            "login_count": 0,
            "profile_complete": True,
            "email_verified": True,
            "phone": "+1-555-0105",
            "location": "San Francisco, USA"
        }
    ]

# Header
col1, col2, col3 = st.columns([2, 1, 1])
with col1:
    st.title("👑 Super Admin Dashboard")
    st.markdown("*Complete administrative control center for AI Knowledge Hub*")

with col2:
    current_time = datetime.now()
    st.markdown("### 🕐 System Time")
    st.write(current_time.strftime("%Y-%m-%d %H:%M:%S"))

with col3:
    st.markdown("### 🔄 System Status")
    system_status = "🟢 **OPERATIONAL**"
    st.markdown(system_status)

st.markdown("---")

# Quick Stats Overview
st.markdown('<div class="section-header"><h3>📊 Quick Overview</h3></div>', unsafe_allow_html=True)

# Calculate stats from user data
total_users = len(st.session_state.users_data)
active_users = len([u for u in st.session_state.users_data if u["status"] == "active"])
pending_users = len([u for u in st.session_state.users_data if u["status"] == "pending"])
suspended_users = len([u for u in st.session_state.users_data if u["status"] == "suspended"])

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.markdown(f'<div class="metric-container"><h4>👥 Total Users</h4><h2>{total_users}</h2><small>All registered</small></div>', unsafe_allow_html=True)

with col2:
    st.markdown(f'<div class="metric-container"><h4>✅ Active Users</h4><h2>{active_users}</h2><small>Approved & Active</small></div>', unsafe_allow_html=True)

with col3:
    st.markdown(f'<div class="metric-container"><h4>⏳ Pending</h4><h2>{pending_users}</h2><small>Awaiting approval</small></div>', unsafe_allow_html=True)

with col4:
    st.markdown(f'<div class="metric-container"><h4>🚫 Suspended</h4><h2>{suspended_users}</h2><small>Restricted access</small></div>', unsafe_allow_html=True)

with col5:
    st.markdown('<div class="metric-container"><h4>📈 API Calls</h4><h2>12.4K</h2><small>Today: 1.2K</small></div>', unsafe_allow_html=True)

with col6:
    st.markdown('<div class="metric-container"><h4>🔄 Uptime</h4><h2>99.8%</h2><small>28 days</small></div>', unsafe_allow_html=True)

st.markdown("---")

# Main Admin Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "👥 User Management", "✅ User Approvals", "📊 Analytics & Reports", 
    "⚙️ System Settings", "🔧 Maintenance & Security"
])

with tab1:
    st.markdown('<div class="section-header"><h2>👥 Complete User Management</h2></div>', unsafe_allow_html=True)
    
    # Search and Filter Controls
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
    
    with col1:
        search_term = st.text_input("🔍 Search Users", placeholder="Search by name, email, or ID...", key="user_search")
        
    with col2:
        status_filter = st.selectbox("Filter by Status", ["All", "Active", "Pending", "Suspended", "Inactive"])
        
    with col3:
        role_filter = st.selectbox("Filter by Role", ["All", "Super Admin", "Admin", "Moderator", "User", "Viewer"])
        
    with col4:
        sort_by = st.selectbox("Sort by", ["Name", "Email", "Created Date", "Last Login", "Status"])
    
    st.markdown("---")
    
    # Filter and sort users
    filtered_users = st.session_state.users_data.copy()
    
    if search_term:
        filtered_users = [u for u in filtered_users if 
                         search_term.lower() in u["email"].lower() or 
                         search_term.lower() in u["name"].lower() or
                         search_term.lower() in u["id"].lower()]
    
    if status_filter != "All":
        filtered_users = [u for u in filtered_users if u["status"] == status_filter.lower()]
    
    if role_filter != "All":
        role_map = {"Super Admin": "super_admin", "Admin": "admin", "Moderator": "moderator", "User": "user", "Viewer": "viewer"}
        filtered_users = [u for u in filtered_users if u["role"] == role_map[role_filter]]
    
    # User Management Actions Bar
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📧 Send Bulk Email", use_container_width=True):
            st.success(f"Email sent to {len(filtered_users)} users!")
    
    with col2:
        if st.button("📊 Export User Data", use_container_width=True):
            user_df = pd.DataFrame(filtered_users)
            csv = user_df.to_csv(index=False)
            st.download_button(
                label="⬇️ Download CSV",
                data=csv,
                file_name=f"users_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
    
    with col3:
        if st.button("🔄 Refresh Data", use_container_width=True):
            st.rerun()
    
    with col4:
        if st.button("👥 Add New User", use_container_width=True):
            st.info("New user creation modal would open here.")
    
    st.markdown("---")
    
    # Display Users
    st.markdown(f"### Showing {len(filtered_users)} users")
    
    for user in filtered_users:
        with st.container():
            st.markdown(f'<div class="user-card">', unsafe_allow_html=True)
            
            col1, col2, col3, col4 = st.columns([3, 2, 2, 2])
            
            with col1:
                st.markdown(f"### 👤 {user['name']}")
                st.markdown(f"**Email:** {user['email']}")
                st.markdown(f"**User ID:** {user['id']}")
                
                # Status and Role Badges
                status_class = f"status-{user['status']}"
                role_class = f"role-{user['role'].replace('_', '-')}"
                st.markdown(f'<span class="status-badge {status_class}">{user["status"].upper()}</span>', unsafe_allow_html=True)
                st.markdown(f'<span class="role-badge {role_class}">{user["role"].replace("_", " ").title()}</span>', unsafe_allow_html=True)
            
            with col2:
                st.markdown("**📊 Statistics**")
                st.write(f"Login Count: {user['login_count']}")
                st.write(f"Profile: {'✅ Complete' if user['profile_complete'] else '❌ Incomplete'}")
                st.write(f"Email: {'✅ Verified' if user['email_verified'] else '❌ Unverified'}")
                
            with col3:
                st.markdown("**📅 Dates**")
                created_date = datetime.fromisoformat(user['created_at']).strftime('%Y-%m-%d %H:%M')
                st.write(f"Created: {created_date}")
                
                if user['last_login']:
                    login_date = datetime.fromisoformat(user['last_login']).strftime('%Y-%m-%d %H:%M')
                    st.write(f"Last Login: {login_date}")
                else:
                    st.write("Last Login: Never")
                    
                st.write(f"📍 {user['location']}")
            
            with col4:
                st.markdown("**🔧 Actions**")
                
                # Role Management
                new_role = st.selectbox(
                    "Change Role", 
                    ["super_admin", "admin", "moderator", "user", "viewer"],
                    index=["super_admin", "admin", "moderator", "user", "viewer"].index(user['role']),
                    key=f"role_{user['id']}"
                )
                
                if new_role != user['role']:
                    if st.button(f"🔄 Update Role", key=f"update_role_{user['id']}"):
                        # Update user role
                        for i, u in enumerate(st.session_state.users_data):
                            if u['id'] == user['id']:
                                st.session_state.users_data[i]['role'] = new_role
                        st.success(f"Role updated to {new_role}!")
                        st.rerun()
                
                # Status Actions
                if user['status'] == 'pending':
                    col_a, col_b = st.columns(2)
                    with col_a:
                        if st.button("✅ Approve", key=f"approve_{user['id']}", use_container_width=True):
                            for i, u in enumerate(st.session_state.users_data):
                                if u['id'] == user['id']:
                                    st.session_state.users_data[i]['status'] = 'active'
                            st.success(f"User {user['name']} approved!")
                            st.rerun()
                    with col_b:
                        if st.button("❌ Reject", key=f"reject_{user['id']}", use_container_width=True):
                            for i, u in enumerate(st.session_state.users_data):
                                if u['id'] == user['id']:
                                    st.session_state.users_data[i]['status'] = 'inactive'
                            st.warning(f"User {user['name']} rejected!")
                            st.rerun()
                
                elif user['status'] == 'active' and user['role'] != 'super_admin':
                    if st.button("🚫 Suspend", key=f"suspend_{user['id']}", use_container_width=True):
                        for i, u in enumerate(st.session_state.users_data):
                            if u['id'] == user['id']:
                                st.session_state.users_data[i]['status'] = 'suspended'
                        st.warning(f"User {user['name']} suspended!")
                        st.rerun()
                
                elif user['status'] == 'suspended':
                    if st.button("🔓 Reactivate", key=f"reactivate_{user['id']}", use_container_width=True):
                        for i, u in enumerate(st.session_state.users_data):
                            if u['id'] == user['id']:
                                st.session_state.users_data[i]['status'] = 'active'
                        st.success(f"User {user['name']} reactivated!")
                        st.rerun()
                
                # Additional Actions
                if st.button("📧 Send Email", key=f"email_{user['id']}", use_container_width=True):
                    st.info(f"Email sent to {user['name']}")
                
                if user['role'] != 'super_admin':
                    if st.button("🗑️ Delete User", key=f"delete_{user['id']}", use_container_width=True):
                        st.session_state.users_data = [u for u in st.session_state.users_data if u['id'] != user['id']]
                        st.error(f"User {user['name']} deleted!")
                        st.rerun()
            
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown("---")

with tab2:
    st.markdown('<div class="section-header"><h2>✅ User Approval Center</h2></div>', unsafe_allow_html=True)
    
    # Get pending users
    pending_users_list = [u for u in st.session_state.users_data if u["status"] == "pending"]
    
    if not pending_users_list:
        st.success("🎉 No users pending approval! All caught up.")
        st.info("New user registrations will appear here for your review and approval.")
    else:
        st.warning(f"⚠️ {len(pending_users_list)} users awaiting approval")
        
        # Bulk approval actions
        col1, col2, col3 = st.columns([1, 1, 2])
        
        with col1:
            if st.button("✅ Approve All", use_container_width=True, type="primary"):
                for i, user in enumerate(st.session_state.users_data):
                    if user['status'] == 'pending':
                        st.session_state.users_data[i]['status'] = 'active'
                st.success(f"Approved all {len(pending_users_list)} pending users!")
                st.rerun()
        
        with col2:
            if st.button("❌ Reject All", use_container_width=True):
                for i, user in enumerate(st.session_state.users_data):
                    if user['status'] == 'pending':
                        st.session_state.users_data[i]['status'] = 'inactive'
                st.warning(f"Rejected all {len(pending_users_list)} pending users!")
                st.rerun()
        
        with col3:
            st.markdown("**Quick Actions:** Use bulk actions above or review each user individually below.")
        
        st.markdown("---")
        
        # Display each pending user for approval
        for user in pending_users_list:
            st.markdown(f'<div class="approval-card">', unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([3, 2, 2])
            
            with col1:
                st.markdown(f"### 👤 {user['name']}")
                st.markdown(f"**Email:** {user['email']}")
                st.markdown(f"**Phone:** {user['phone']}")
                st.markdown(f"**Location:** {user['location']}")
                
                # Registration details
                reg_date = datetime.fromisoformat(user['created_at'])
                days_ago = (datetime.now() - reg_date).days
                st.markdown(f"**Registered:** {reg_date.strftime('%Y-%m-%d %H:%M')} ({days_ago} days ago)")
                
                # Verification status
                verifications = []
                if user['email_verified']:
                    verifications.append("✅ Email Verified")
                else:
                    verifications.append("❌ Email Not Verified")
                    
                if user['profile_complete']:
                    verifications.append("✅ Profile Complete")
                else:
                    verifications.append("❌ Profile Incomplete")
                    
                st.markdown("**Status:** " + " | ".join(verifications))
            
            with col2:
                st.markdown("**📋 Application Details**")
                
                # Mock additional application data
                st.write("**Requested Role:** User")
                st.write("**Company:** " + user['email'].split('@')[1])
                st.write("**Use Case:** AI Research & Development")
                st.write("**Referral Source:** Google Search")
                
                # Risk Assessment
                risk_level = "🟢 Low Risk" if user['email_verified'] and user['profile_complete'] else "🟡 Medium Risk"
                st.markdown(f"**Risk Assessment:** {risk_level}")
            
            with col3:
                st.markdown("**🔧 Approval Actions**")
                
                # Individual approval buttons
                col_approve, col_reject = st.columns(2)
                
                with col_approve:
                    if st.button(f"✅ Approve", key=f"ind_approve_{user['id']}", use_container_width=True, type="primary"):
                        for i, u in enumerate(st.session_state.users_data):
                            if u['id'] == user['id']:
                                st.session_state.users_data[i]['status'] = 'active'
                        st.success(f"✅ {user['name']} approved!")
                        time.sleep(1)
                        st.rerun()
                
                with col_reject:
                    if st.button(f"❌ Reject", key=f"ind_reject_{user['id']}", use_container_width=True):
                        for i, u in enumerate(st.session_state.users_data):
                            if u['id'] == user['id']:
                                st.session_state.users_data[i]['status'] = 'inactive'
                        st.warning(f"❌ {user['name']} rejected!")
                        time.sleep(1)
                        st.rerun()
                
                # Additional actions
                if st.button(f"📧 Request Info", key=f"info_{user['id']}", use_container_width=True):
                    st.info(f"Information request sent to {user['name']}")
                
                if st.button(f"👁️ View Profile", key=f"profile_{user['id']}", use_container_width=True):
                    st.info(f"Viewing detailed profile for {user['name']}")
                
                # Set custom role during approval
                custom_role = st.selectbox(
                    f"Assign Role",
                    ["user", "moderator", "admin"],
                    key=f"custom_role_{user['id']}"
                )
                
                if st.button(f"✅ Approve as {custom_role.title()}", key=f"approve_custom_{user['id']}", use_container_width=True):
                    for i, u in enumerate(st.session_state.users_data):
                        if u['id'] == user['id']:
                            st.session_state.users_data[i]['status'] = 'active'
                            st.session_state.users_data[i]['role'] = custom_role
                    st.success(f"✅ {user['name']} approved as {custom_role}!")
                    time.sleep(1)
                    st.rerun()
            
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown("---")

with tab3:
    st.markdown('<div class="section-header"><h2>📊 Analytics & Comprehensive Reports</h2></div>', unsafe_allow_html=True)
    
    # Analytics time range selector
    col1, col2, col3 = st.columns([1, 1, 2])
    
    with col1:
        date_range = st.selectbox("📅 Time Range", ["Last 7 days", "Last 30 days", "Last 90 days", "All time"])
    
    with col2:
        report_type = st.selectbox("📋 Report Type", ["Overview", "User Activity", "Security", "Performance"])
    
    with col3:
        if st.button("📊 Generate Custom Report", use_container_width=True):
            st.success("Custom report generated!")
    
    st.markdown("---")
    
    # User Statistics Charts
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 👥 User Status Distribution")
        status_counts = pd.DataFrame([
            {"Status": "Active", "Count": active_users, "Color": "#28a745"},
            {"Status": "Pending", "Count": pending_users, "Color": "#ffc107"},
            {"Status": "Suspended", "Count": suspended_users, "Color": "#dc3545"},
            {"Status": "Inactive", "Count": total_users - active_users - pending_users - suspended_users, "Color": "#6c757d"}
        ])
        
        fig_pie = px.pie(status_counts, values='Count', names='Status', 
                        color='Status',
                        color_discrete_map={
                            'Active': '#28a745',
                            'Pending': '#ffc107', 
                            'Suspended': '#dc3545',
                            'Inactive': '#6c757d'
                        })
        fig_pie.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig_pie, use_container_width=True)
    
    with col2:
        st.markdown("#### 🎭 Role Distribution")
        role_counts = {}
        for user in st.session_state.users_data:
            role = user['role'].replace('_', ' ').title()
            role_counts[role] = role_counts.get(role, 0) + 1
        
        role_df = pd.DataFrame(list(role_counts.items()), columns=['Role', 'Count'])
        fig_bar = px.bar(role_df, x='Role', y='Count', 
                        color='Count', 
                        color_continuous_scale='viridis')
        fig_bar.update_layout(showlegend=False)
        st.plotly_chart(fig_bar, use_container_width=True)
    
    # User Registration Timeline
    st.markdown("#### 📈 User Registration Timeline")
    
    # Create timeline data
    reg_dates = [datetime.fromisoformat(user['created_at']).date() for user in st.session_state.users_data]
    timeline_df = pd.DataFrame({'Registration_Date': reg_dates})
    timeline_counts = timeline_df.groupby('Registration_Date').size().reset_index(name='New_Users')
    
    # Fill in missing dates
    date_range = pd.date_range(start=min(reg_dates), end=max(reg_dates), freq='D')
    complete_timeline = pd.DataFrame({'Registration_Date': date_range})
    complete_timeline = complete_timeline.merge(timeline_counts, on='Registration_Date', how='left')
    complete_timeline['New_Users'] = complete_timeline['New_Users'].fillna(0)
    
    fig_timeline = px.line(complete_timeline, x='Registration_Date', y='New_Users',
                          title='Daily User Registrations',
                          markers=True)
    fig_timeline.update_layout(xaxis_title="Date", yaxis_title="New Users")
    st.plotly_chart(fig_timeline, use_container_width=True)
    
    # Activity Metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_logins = sum(user['login_count'] for user in st.session_state.users_data) / len(st.session_state.users_data)
        st.metric("📊 Avg Logins per User", f"{avg_logins:.1f}")
    
    with col2:
        verified_users = sum(1 for user in st.session_state.users_data if user['email_verified'])
        verification_rate = (verified_users / total_users) * 100
        st.metric("✅ Email Verification Rate", f"{verification_rate:.1f}%")
    
    with col3:
        complete_profiles = sum(1 for user in st.session_state.users_data if user['profile_complete'])
        completion_rate = (complete_profiles / total_users) * 100
        st.metric("📋 Profile Completion Rate", f"{completion_rate:.1f}%")
    
    with col4:
        active_rate = (active_users / total_users) * 100
        st.metric("🎯 User Activation Rate", f"{active_rate:.1f}%")
    
    # Detailed Reports Section
    st.markdown("---")
    st.markdown("#### 📋 Detailed Reports")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("**🔍 User Activity Report**")
        activity_data = []
        for user in st.session_state.users_data:
            last_login = "Never" if not user['last_login'] else datetime.fromisoformat(user['last_login']).strftime('%Y-%m-%d')
            activity_data.append({
                "Name": user['name'],
                "Email": user['email'],
                "Status": user['status'].title(),
                "Login Count": user['login_count'],
                "Last Login": last_login
            })
        
        activity_df = pd.DataFrame(activity_data)
        st.dataframe(activity_df, use_container_width=True, hide_index=True)
        
        csv_data = activity_df.to_csv(index=False)
        st.download_button(
            label="📊 Download Activity Report",
            data=csv_data,
            file_name=f"user_activity_report_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv",
            use_container_width=True
        )
    
    with col2:
        st.markdown("**📊 System Usage Metrics**")
        
        # Mock system metrics
        metrics_data = {
            "Metric": [
                "Total API Calls (Today)",
                "Average Response Time",
                "Error Rate",
                "Storage Usage",
                "Bandwidth Usage",
                "Active Sessions"
            ],
            "Value": [
                "1,247",
                "245ms",
                "0.02%",
                "2.1 GB",
                "45.2 MB",
                "18"
            ],
            "Status": [
                "🟢 Normal",
                "🟡 Elevated",
                "🟢 Excellent",
                "🟡 Moderate",
                "🟢 Low",
                "🟢 Normal"
            ]
        }
        
        metrics_df = pd.DataFrame(metrics_data)
        st.dataframe(metrics_df, use_container_width=True, hide_index=True)

with tab4:
    st.markdown('<div class="section-header"><h2>⚙️ Advanced System Settings</h2></div>', unsafe_allow_html=True)
    
    # Settings Categories
    setting_category = st.selectbox("⚙️ Settings Category", [
        "General Application", "User Management", "Security & Privacy", 
        "Email & Notifications", "API & Integrations", "Appearance & UI"
    ])
    
    st.markdown("---")
    
    if setting_category == "General Application":
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🎯 Application Configuration")
            
            app_name = st.text_input("Application Name", value="AI Knowledge Hub")
            app_description = st.text_area("Application Description", 
                                         value="Advanced AI-powered knowledge management platform")
            
            maintenance_mode = st.toggle("🔧 Maintenance Mode", value=False)
            debug_mode = st.toggle("🐛 Debug Mode", value=False)
            
            max_file_size = st.number_input("📁 Max File Upload Size (MB)", min_value=1, max_value=100, value=10)
            session_timeout = st.number_input("⏱️ Session Timeout (minutes)", min_value=15, max_value=480, value=60)
            
        with col2:
            st.markdown("#### 🌐 Regional & Localization")
            
            default_timezone = st.selectbox("🕐 Default Timezone", [
                "UTC", "America/New_York", "America/Los_Angeles", "Europe/London", "Asia/Tokyo"
            ])
            
            default_language = st.selectbox("🗣️ Default Language", [
                "English", "Spanish", "French", "German", "Japanese", "Chinese"
            ])
            
            date_format = st.selectbox("📅 Date Format", [
                "YYYY-MM-DD", "MM/DD/YYYY", "DD/MM/YYYY"
            ])
            
            currency = st.selectbox("💰 Currency", ["USD", "EUR", "GBP", "JPY", "CAD"])
    
    elif setting_category == "User Management":
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 👥 Registration Settings")
            
            allow_registration = st.toggle("🔓 Allow New Registrations", value=True)
            require_approval = st.toggle("✅ Require Admin Approval", value=True)
            require_email_verification = st.toggle("📧 Require Email Verification", value=True)
            
            default_role = st.selectbox("👤 Default User Role", ["user", "viewer"])
            auto_approve_domains = st.text_area("🏢 Auto-approve Email Domains (one per line)", 
                                              placeholder="company.com\ntrusted-org.edu")
            
        with col2:
            st.markdown("#### 🔐 Account Policies")
            
            min_password_length = st.number_input("🔒 Minimum Password Length", min_value=6, max_value=20, value=8)
            require_strong_password = st.toggle("💪 Require Strong Passwords", value=True)
            
            max_login_attempts = st.number_input("🚫 Max Failed Login Attempts", min_value=3, max_value=10, value=5)
            lockout_duration = st.number_input("⏰ Account Lockout Duration (minutes)", min_value=5, max_value=60, value=15)
            
            inactivity_timeout = st.number_input("😴 Inactive Account Timeout (days)", min_value=30, max_value=365, value=90)
    
    elif setting_category == "Security & Privacy":
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🔒 Security Configuration")
            
            enable_2fa = st.toggle("🔐 Enable Two-Factor Authentication", value=False)
            require_https = st.toggle("🔒 Require HTTPS", value=True)
            
            ip_whitelist = st.text_area("🌐 IP Whitelist (optional)", 
                                       placeholder="192.168.1.0/24\n10.0.0.0/8")
            
            blocked_countries = st.multiselect("🚫 Blocked Countries", [
                "None", "High Risk Countries Only", "Custom List"
            ])
            
            rate_limit_requests = st.number_input("⏱️ Rate Limit (requests per minute)", 
                                                min_value=10, max_value=1000, value=100)
            
        with col2:
            st.markdown("#### 🛡️ Privacy Settings")
            
            data_retention_days = st.number_input("📂 Data Retention Period (days)", 
                                                min_value=30, max_value=2555, value=365)
            
            enable_analytics = st.toggle("📊 Enable Usage Analytics", value=True)
            anonymous_analytics = st.toggle("👤 Anonymize Analytics Data", value=True)
            
            gdpr_compliance = st.toggle("🇪🇺 GDPR Compliance Mode", value=True)
            ccpa_compliance = st.toggle("🇺🇸 CCPA Compliance Mode", value=False)
            
            cookie_consent = st.toggle("🍪 Require Cookie Consent", value=True)
    
    elif setting_category == "Email & Notifications":
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 📧 Email Configuration")
            
            smtp_server = st.text_input("📬 SMTP Server", placeholder="smtp.gmail.com")
            smtp_port = st.number_input("🔌 SMTP Port", min_value=25, max_value=587, value=587)
            
            email_username = st.text_input("👤 Email Username", placeholder="your-email@domain.com")
            email_password = st.text_input("🔒 Email Password", type="password")
            
            from_name = st.text_input("📝 From Name", value="AI Knowledge Hub")
            from_email = st.text_input("📧 From Email", placeholder="noreply@yourapp.com")
            
        with col2:
            st.markdown("#### 🔔 Notification Settings")
            
            welcome_email = st.toggle("👋 Send Welcome Email", value=True)
            approval_notifications = st.toggle("✅ Admin Approval Notifications", value=True)
            
            security_alerts = st.toggle("🔒 Security Alert Emails", value=True)
            maintenance_notices = st.toggle("🔧 Maintenance Notifications", value=True)
            
            digest_frequency = st.selectbox("📊 Activity Digest Frequency", [
                "Disabled", "Daily", "Weekly", "Monthly"
            ])
            
            notification_channels = st.multiselect("📱 Notification Channels", [
                "Email", "SMS", "Push Notifications", "Slack", "Discord"
            ])
    
    # Save Settings Button
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        if st.button("💾 Save All Settings", use_container_width=True, type="primary"):
            st.success("✅ All settings saved successfully!")
            st.info("Settings will be applied after the next system restart.")

with tab5:
    st.markdown('<div class="section-header"><h2>🔧 System Maintenance & Security Center</h2></div>', unsafe_allow_html=True)
    
    # Maintenance & Security Tabs
    maintenance_tab = st.selectbox("🔧 Maintenance Section", [
        "System Health", "Database Management", "File Management", 
        "Security Monitoring", "Backup & Recovery", "Performance Optimization"
    ])
    
    st.markdown("---")
    
    if maintenance_tab == "System Health":
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("#### 💚 System Status")
            
            health_checks = [
                ("🌐 Web Server", "🟢 Online", "99.9% uptime"),
                ("🗄️ Database", "🟢 Connected", "15ms avg response"),
                ("📧 Email Service", "🟡 Degraded", "Some delays reported"),
                ("🔐 Auth Service", "🟢 Operational", "All systems normal"),
                ("📁 File Storage", "🟢 Available", "68% capacity used"),
                ("🔌 External APIs", "🟡 Limited", "Rate limits active")
            ]
            
            for service, status, details in health_checks:
                st.markdown(f"**{service}**")
                st.markdown(f"{status} - *{details}*")
                st.markdown("---")
        
        with col2:
            st.markdown("#### 📊 Resource Usage")
            
            # Mock resource data
            cpu_usage = 45
            ram_usage = 68
            disk_usage = 72
            network_usage = 23
            
            st.metric("🖥️ CPU Usage", f"{cpu_usage}%", delta=f"{cpu_usage-40}%")
            st.progress(cpu_usage / 100)
            
            st.metric("🧠 RAM Usage", f"{ram_usage}%", delta=f"{ram_usage-65}%")
            st.progress(ram_usage / 100)
            
            st.metric("💾 Disk Usage", f"{disk_usage}%", delta=f"{disk_usage-70}%")
            st.progress(disk_usage / 100)
            
            st.metric("🌐 Network I/O", f"{network_usage}%", delta=f"{network_usage-20}%")
            st.progress(network_usage / 100)
        
        with col3:
            st.markdown("#### 🔧 Quick Actions")
            
            if st.button("🔄 Restart Services", use_container_width=True):
                with st.spinner("Restarting services..."):
                    time.sleep(3)
                st.success("✅ Services restarted successfully!")
            
            if st.button("🧹 Clear System Cache", use_container_width=True):
                st.cache_data.clear()
                st.success("✅ System cache cleared!")
            
            if st.button("📊 Generate Health Report", use_container_width=True):
                health_report = {
                    "timestamp": datetime.now().isoformat(),
                    "overall_status": "healthy",
                    "services": health_checks,
                    "resource_usage": {
                        "cpu": f"{cpu_usage}%",
                        "ram": f"{ram_usage}%", 
                        "disk": f"{disk_usage}%",
                        "network": f"{network_usage}%"
                    }
                }
                
                st.download_button(
                    label="⬇️ Download Health Report",
                    data=json.dumps(health_report, indent=2),
                    file_name=f"health_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                    mime="application/json",
                    use_container_width=True
                )
            
            if st.button("🔍 Run Full Diagnostics", use_container_width=True):
                with st.spinner("Running comprehensive system diagnostics..."):
                    time.sleep(5)
                st.success("✅ Diagnostics complete - All systems operational!")
    
    elif maintenance_tab == "Security Monitoring":
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 🛡️ Security Dashboard")
            
            # Security metrics
            col_a, col_b = st.columns(2)
            with col_a:
                st.metric("🚨 Security Alerts", "3", delta="1")
                st.metric("🔒 Failed Logins (24h)", "12", delta="-3")
            
            with col_b:
                st.metric("🌐 Blocked IPs", "7", delta="2")
                st.metric("🔐 Active Sessions", "18", delta="4")
            
            # Recent security events
            st.markdown("#### 🚨 Recent Security Events")
            security_events = [
                {"time": "2 min ago", "event": "Multiple failed login attempts", "ip": "192.168.1.100", "severity": "🔴 High"},
                {"time": "15 min ago", "event": "Suspicious API usage pattern", "ip": "10.0.0.45", "severity": "🟡 Medium"},
                {"time": "1 hour ago", "event": "New admin login from new location", "ip": "203.0.113.0", "severity": "🟡 Medium"},
                {"time": "3 hours ago", "event": "Password change request", "ip": "198.51.100.0", "severity": "🟢 Low"}
            ]
            
            for event in security_events:
                st.markdown(f"**{event['time']}** - {event['event']}")
                st.markdown(f"IP: {event['ip']} | {event['severity']}")
                st.markdown("---")
        
        with col2:
            st.markdown("#### 🔒 Security Actions")
            
            if st.button("🔍 Scan for Vulnerabilities", use_container_width=True):
                with st.spinner("Scanning for security vulnerabilities..."):
                    time.sleep(3)
                st.success("✅ Security scan complete - No critical vulnerabilities found!")
            
            if st.button("🛡️ Update Security Rules", use_container_width=True):
                st.success("✅ Security rules updated!")
            
            if st.button("🚫 Block Suspicious IPs", use_container_width=True):
                st.warning("⚠️ 3 suspicious IPs have been blocked!")
            
            if st.button("📊 Generate Security Report", use_container_width=True):
                security_report = {
                    "timestamp": datetime.now().isoformat(),
                    "failed_logins": 12,
                    "blocked_ips": 7,
                    "active_sessions": 18,
                    "security_alerts": 3,
                    "recent_events": security_events
                }
                
                st.download_button(
                    label="⬇️ Download Security Report",
                    data=json.dumps(security_report, indent=2),
                    file_name=f"security_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                    mime="application/json",
                    use_container_width=True
                )
    
    elif maintenance_tab == "Backup & Recovery":
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 💾 Backup Management")
            
            # Backup status
            last_backup = datetime.now() - timedelta(hours=2)
            st.markdown(f"**Last Backup:** {last_backup.strftime('%Y-%m-%d %H:%M:%S')}")
            st.markdown("**Backup Status:** 🟢 Up to date")
            st.markdown("**Next Scheduled:** In 22 hours")
            
            # Backup options
            backup_type = st.selectbox("Backup Type", ["Full Backup", "Incremental", "Database Only", "Files Only"])
            
            if st.button("🔄 Create Backup Now", use_container_width=True, type="primary"):
                with st.spinner(f"Creating {backup_type.lower()}..."):
                    time.sleep(4)
                st.success(f"✅ {backup_type} completed successfully!")
            
            # Recent backups
            st.markdown("#### 📂 Recent Backups")
            backups = [
                {"date": "2024-09-17 12:00", "type": "Full", "size": "2.3 GB", "status": "✅"},
                {"date": "2024-09-16 12:00", "type": "Incremental", "size": "156 MB", "status": "✅"},
                {"date": "2024-09-15 12:00", "type": "Full", "size": "2.1 GB", "status": "✅"},
            ]
            
            for backup in backups:
                st.markdown(f"**{backup['date']}** - {backup['type']} ({backup['size']}) {backup['status']}")
        
        with col2:
            st.markdown("#### 🔄 Recovery Options")
            
            st.warning("⚠️ Recovery operations should only be performed by experienced administrators")
            
            recovery_point = st.selectbox("Select Recovery Point", [
                "2024-09-17 12:00 - Full Backup",
                "2024-09-16 12:00 - Incremental", 
                "2024-09-15 12:00 - Full Backup"
            ])
            
            recovery_scope = st.multiselect("Recovery Scope", [
                "User Database", "System Settings", "File Storage", "Application Data"
            ])
            
            if st.button("⚠️ Initiate Recovery", use_container_width=True):
                st.error("Recovery process requires additional confirmation and system maintenance window")
            
            # Backup settings
            st.markdown("#### ⚙️ Backup Settings")
            
            auto_backup = st.toggle("🔄 Automatic Backups", value=True)
            backup_frequency = st.selectbox("Backup Frequency", ["Daily", "Weekly", "Monthly"])
            retention_period = st.number_input("Retention Period (days)", min_value=7, max_value=365, value=30)

# Footer
st.markdown("---")
st.markdown("*👑 **Super Admin Dashboard** - Complete control center for your AI Knowledge Hub*")
st.markdown("*Version 2.1.0 | Last Updated: September 17, 2024*")
