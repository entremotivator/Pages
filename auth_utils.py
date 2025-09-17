import streamlit as st
from supabase import create_client, Client
from typing import Optional, Dict, Any, List
import hashlib
import secrets
from datetime import datetime, timedelta
import uuid

# Super admin email
SUPER_ADMIN_EMAIL = "entremotivator@gmail.com"

class AuthManager:
    """Enhanced authentication manager with real Supabase database integration"""
    
    def __init__(self):
        self.supabase = self._init_supabase()
    
    def _init_supabase(self) -> Client:
        """Initialize Supabase client"""
        url = st.secrets.get("SUPABASE_URL", "https://ejvzdfnspcwcazltweig.supabase.co")
        key = st.secrets.get("SUPABASE_ANON_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVqdnpkZm5zcGN3Y2F6bHR3ZWlnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTc0NjM5NjQsImV4cCI6MjA3MzAzOTk2NH0.Qga-V6HVc5kpnTlTraxxO6fxvQEfTYGDFeDWhKNbobU")
        return create_client(url, key)
    
    def is_super_admin(self, email: str) -> bool:
        """Check if user is super admin"""
        return email.lower() == SUPER_ADMIN_EMAIL.lower()
    
    def sign_up_user(self, email: str, password: str, full_name: str = None) -> Dict[str, Any]:
        """Register a new user with real database integration"""
        try:
            # Create user in Supabase Auth
            response = self.supabase.auth.sign_up({
                "email": email,
                "password": password,
                "options": {
                    "data": {
                        "full_name": full_name or email.split('@')[0],
                        "role": "super_admin" if self.is_super_admin(email) else "user",
                        "is_super_admin": self.is_super_admin(email)
                    }
                }
            })
            
            if response.user:
                # Log the registration activity
                self.log_user_activity(
                    response.user.id,
                    "registration",
                    f"User registered with email: {email}"
                )
                
                return {
                    "success": True,
                    "user": response.user,
                    "message": "Registration successful! Please check your email for verification." if not self.is_super_admin(email) else "Super admin account created successfully!"
                }
            else:
                return {
                    "success": False,
                    "message": "Registration failed. Please try again."
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "message": f"Registration failed: {str(e)}"
            }
    
    def sign_in_user(self, email: str, password: str) -> Dict[str, Any]:
        """Sign in a user with real database integration"""
        try:
            response = self.supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
            
            if response.user:
                # Get user profile from database
                profile_response = self.supabase.table("user_profiles").select("*").eq("id", response.user.id).execute()
                
                if profile_response.data:
                    profile = profile_response.data[0]
                    
                    # Check if user is approved (except super admin)
                    if not self.is_super_admin(email) and profile.get("status") != "active":
                        # Sign out unapproved user
                        self.supabase.auth.sign_out()
                        return {
                            "success": False,
                            "message": f"Your account status is: {profile.get('status', 'pending')}. Please contact the administrator."
                        }
                    
                    # Update login statistics
                    self.update_user_login_stats(response.user.id)
                    
                    return {
                        "success": True,
                        "user": response.user,
                        "profile": profile,
                        "is_super_admin": self.is_super_admin(email),
                        "message": "Login successful!"
                    }
                else:
                    return {
                        "success": False,
                        "message": "User profile not found. Please contact administrator."
                    }
            else:
                return {
                    "success": False,
                    "message": "Invalid login credentials."
                }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "message": f"Login failed: {str(e)}"
            }
    
    def sign_out_user(self) -> bool:
        """Sign out current user"""
        try:
            self.supabase.auth.sign_out()
            return True
        except:
            return False
    
    def get_current_user(self) -> Optional[Dict[str, Any]]:
        """Get current authenticated user with profile"""
        try:
            user = self.supabase.auth.get_user()
            if user and user.user:
                # Get user profile
                profile_response = self.supabase.table("user_profiles").select("*").eq("id", user.user.id).execute()
                
                profile = profile_response.data[0] if profile_response.data else {}
                
                return {
                    "id": user.user.id,
                    "email": user.user.email,
                    "is_super_admin": self.is_super_admin(user.user.email),
                    "profile": profile,
                    "metadata": user.user.user_metadata or {}
                }
            return None
        except:
            return None
    
    def get_all_users(self) -> List[Dict[str, Any]]:
        """Get all users from database (super admin only)"""
        try:
            response = self.supabase.table("user_profiles").select("*").order("created_at", desc=True).execute()
            return response.data if response.data else []
        except Exception as e:
            st.error(f"Error fetching users: {str(e)}")
            return []
    
    def get_user_statistics(self) -> Dict[str, int]:
        """Get user statistics from database"""
        try:
            # Use the database function for statistics
            response = self.supabase.rpc("get_user_statistics").execute()
            
            if response.data and len(response.data) > 0:
                stats = response.data[0]
                return {
                    "total_users": stats.get("total_users", 0),
                    "active_users": stats.get("active_users", 0),
                    "pending_users": stats.get("pending_users", 0),
                    "suspended_users": stats.get("suspended_users", 0),
                    "inactive_users": stats.get("inactive_users", 0),
                    "total_logins": stats.get("total_logins", 0),
                    "users_today": stats.get("users_today", 0)
                }
            else:
                # Fallback to manual count
                users = self.get_all_users()
                return {
                    "total_users": len(users),
                    "active_users": len([u for u in users if u.get("status") == "active"]),
                    "pending_users": len([u for u in users if u.get("status") == "pending"]),
                    "suspended_users": len([u for u in users if u.get("status") == "suspended"]),
                    "inactive_users": len([u for u in users if u.get("status") == "inactive"]),
                    "total_logins": sum(u.get("login_count", 0) for u in users),
                    "users_today": len([u for u in users if u.get("created_at", "").startswith(datetime.now().strftime("%Y-%m-%d"))])
                }
        except Exception as e:
            st.error(f"Error fetching statistics: {str(e)}")
            return {
                "total_users": 0,
                "active_users": 0,
                "pending_users": 0,
                "suspended_users": 0,
                "inactive_users": 0,
                "total_logins": 0,
                "users_today": 0
            }
    
    def approve_user(self, user_id: str, approver_id: str) -> bool:
        """Approve a user (super admin only)"""
        try:
            # Use the database function for approval
            response = self.supabase.rpc("approve_user", {
                "target_user_id": user_id,
                "approver_id": approver_id
            }).execute()
            
            return response.data if response.data else False
        except Exception as e:
            st.error(f"Error approving user: {str(e)}")
            return False
    
    def suspend_user(self, user_id: str, admin_id: str, reason: str = None) -> bool:
        """Suspend a user (super admin only)"""
        try:
            # Use the database function for suspension
            response = self.supabase.rpc("suspend_user", {
                "target_user_id": user_id,
                "admin_id": admin_id,
                "reason": reason
            }).execute()
            
            return response.data if response.data else False
        except Exception as e:
            st.error(f"Error suspending user: {str(e)}")
            return False
    
    def update_user_role(self, user_id: str, new_role: str, admin_id: str) -> bool:
        """Update user role (super admin only)"""
        try:
            response = self.supabase.table("user_profiles").update({
                "role": new_role,
                "updated_at": datetime.now().isoformat()
            }).eq("id", user_id).execute()
            
            if response.data:
                # Log the role change
                self.log_user_activity(
                    user_id,
                    "role_changed",
                    f"Role changed to {new_role} by admin"
                )
                return True
            return False
        except Exception as e:
            st.error(f"Error updating user role: {str(e)}")
            return False
    
    def reactivate_user(self, user_id: str, admin_id: str) -> bool:
        """Reactivate a suspended user"""
        try:
            response = self.supabase.table("user_profiles").update({
                "status": "active",
                "updated_at": datetime.now().isoformat()
            }).eq("id", user_id).execute()
            
            if response.data:
                # Log the reactivation
                self.log_user_activity(
                    user_id,
                    "reactivated",
                    "User account reactivated by admin"
                )
                return True
            return False
        except Exception as e:
            st.error(f"Error reactivating user: {str(e)}")
            return False
    
    def delete_user(self, user_id: str, admin_id: str) -> bool:
        """Delete a user (super admin only)"""
        try:
            # First delete from user_profiles (cascading will handle other tables)
            response = self.supabase.table("user_profiles").delete().eq("id", user_id).execute()
            
            if response.data:
                # Log the deletion
                self.log_user_activity(
                    admin_id,
                    "user_deleted",
                    f"Deleted user account: {user_id}"
                )
                return True
            return False
        except Exception as e:
            st.error(f"Error deleting user: {str(e)}")
            return False
    
    def add_user_manually(self, email: str, full_name: str, role: str, admin_id: str) -> Dict[str, Any]:
        """Manually add a user (super admin only)"""
        try:
            # Generate a temporary password
            temp_password = secrets.token_urlsafe(12)
            
            # Create user in Supabase Auth
            response = self.supabase.auth.admin.create_user({
                "email": email,
                "password": temp_password,
                "email_confirm": True,
                "user_metadata": {
                    "full_name": full_name,
                    "role": role,
                    "manually_created": True,
                    "created_by": admin_id
                }
            })
            
            if response.user:
                # Update the profile with correct role and status
                self.supabase.table("user_profiles").update({
                    "full_name": full_name,
                    "role": role,
                    "status": "active",
                    "email_verified": True,
                    "profile_complete": True,
                    "approved_by": admin_id,
                    "approved_at": datetime.now().isoformat()
                }).eq("id", response.user.id).execute()
                
                # Log the manual creation
                self.log_user_activity(
                    response.user.id,
                    "manually_created",
                    f"User manually created by admin with role: {role}"
                )
                
                return {
                    "success": True,
                    "user": response.user,
                    "temp_password": temp_password,
                    "message": f"User {email} created successfully!"
                }
            else:
                return {
                    "success": False,
                    "message": "Failed to create user account."
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "message": f"Error creating user: {str(e)}"
            }
    
    def update_user_login_stats(self, user_id: str):
        """Update user login statistics"""
        try:
            # Use the database function for updating login stats
            self.supabase.rpc("update_user_login_stats", {"user_id": user_id}).execute()
        except Exception as e:
            st.error(f"Error updating login stats: {str(e)}")
    
    def log_user_activity(self, user_id: str, activity_type: str, description: str = None):
        """Log user activity"""
        try:
            # Use the database function for logging activity
            self.supabase.rpc("log_user_activity", {
                "user_id": user_id,
                "activity_type": activity_type,
                "description": description
            }).execute()
        except Exception as e:
            st.error(f"Error logging activity: {str(e)}")
    
    def get_user_activity_logs(self, user_id: str = None, limit: int = 100) -> List[Dict[str, Any]]:
        """Get user activity logs"""
        try:
            query = self.supabase.table("user_activity_logs").select("*")
            
            if user_id:
                query = query.eq("user_id", user_id)
            
            response = query.order("created_at", desc=True).limit(limit).execute()
            return response.data if response.data else []
        except Exception as e:
            st.error(f"Error fetching activity logs: {str(e)}")
            return []
    
    def get_system_settings(self) -> Dict[str, Any]:
        """Get system settings"""
        try:
            response = self.supabase.table("system_settings").select("*").execute()
            
            settings = {}
            if response.data:
                for setting in response.data:
                    settings[setting["setting_key"]] = setting["setting_value"]
            
            return settings
        except Exception as e:
            st.error(f"Error fetching system settings: {str(e)}")
            return {}
    
    def update_system_setting(self, key: str, value: Any, admin_id: str) -> bool:
        """Update system setting"""
        try:
            response = self.supabase.table("system_settings").upsert({
                "setting_key": key,
                "setting_value": value,
                "updated_by": admin_id,
                "updated_at": datetime.now().isoformat()
            }).execute()
            
            return bool(response.data)
        except Exception as e:
            st.error(f"Error updating system setting: {str(e)}")
            return False

def init_session_state():
    """Initialize authentication session state"""
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    if "username" not in st.session_state:
        st.session_state["username"] = None
    if "user_id" not in st.session_state:
        st.session_state["user_id"] = None
    if "is_super_admin" not in st.session_state:
        st.session_state["is_super_admin"] = False
    if "user_profile" not in st.session_state:
        st.session_state["user_profile"] = {}

def render_auth_sidebar(auth_manager: AuthManager):
    """Render authentication sidebar with real database integration"""
    init_session_state()
    
    with st.sidebar:
        st.subheader("🔐 Access Control")
        
        if not st.session_state["authenticated"]:
            # Login/Register tabs
            tab1, tab2 = st.tabs(["Sign In", "Register"])
            
            with tab1:
                with st.form("login_form"):
                    st.markdown("### Sign In")
                    email = st.text_input("Email", placeholder="Enter your email address")
                    password = st.text_input("Password", type="password", placeholder="Enter your password")
                    login_button = st.form_submit_button("Sign In", use_container_width=True)
                    
                    if login_button and email and password:
                        result = auth_manager.sign_in_user(email, password)
                        if result["success"]:
                            st.session_state["authenticated"] = True
                            st.session_state["username"] = email
                            st.session_state["user_id"] = result["user"].id
                            st.session_state["is_super_admin"] = result["is_super_admin"]
                            st.session_state["user_profile"] = result.get("profile", {})
                            st.success(result["message"])
                            st.rerun()
                        else:
                            st.error(result["message"])
            
            with tab2:
                with st.form("register_form"):
                    st.markdown("### Create Account")
                    reg_email = st.text_input("Email", placeholder="Enter your email address", key="reg_email")
                    reg_name = st.text_input("Full Name", placeholder="Enter your full name", key="reg_name")
                    reg_password = st.text_input("Password", type="password", placeholder="Create a password", key="reg_password")
                    reg_password_confirm = st.text_input("Confirm Password", type="password", placeholder="Confirm your password", key="reg_password_confirm")
                    register_button = st.form_submit_button("Create Account", use_container_width=True)
                    
                    if register_button:
                        if not reg_email or not reg_password or not reg_name:
                            st.error("Please fill in all fields.")
                        elif reg_password != reg_password_confirm:
                            st.error("Passwords do not match.")
                        elif len(reg_password) < 6:
                            st.error("Password must be at least 6 characters long.")
                        else:
                            result = auth_manager.sign_up_user(reg_email, reg_password, reg_name)
                            if result["success"]:
                                st.success(result["message"])
                                if auth_manager.is_super_admin(reg_email):
                                    st.info("🔑 Super admin account created! You can now sign in.")
                            else:
                                st.error(result["message"])
            
            st.markdown("---")
            st.markdown("**Need help?** Contact your administrator.")
        
        else:
            # User is logged in
            username_display = st.session_state['username'].split('@')[0]
            if st.session_state["is_super_admin"]:
                st.success(f"👑 Super Admin: {username_display}")
            else:
                st.success(f"👋 Welcome, {username_display}!")
            
            # Show user profile info
            profile = st.session_state.get("user_profile", {})
            if profile:
                st.caption(f"Role: {profile.get('role', 'user').title()}")
                st.caption(f"Status: {profile.get('status', 'unknown').title()}")
                if profile.get('login_count'):
                    st.caption(f"Logins: {profile.get('login_count', 0)}")
            
            st.markdown("---")
            
            # Super admin controls
            if st.session_state["is_super_admin"]:
                st.markdown("### 🛠️ Admin Controls")
                if st.button("👥 Manage Users", use_container_width=True):
                    st.session_state["show_user_management"] = True
                if st.button("⚙️ System Settings", use_container_width=True):
                    st.session_state["show_system_settings"] = True
                st.markdown("---")
            
            # Sign out button
            if st.button("🚪 Sign Out", use_container_width=True):
                auth_manager.sign_out_user()
                st.session_state["authenticated"] = False
                st.session_state["username"] = None
                st.session_state["user_id"] = None
                st.session_state["is_super_admin"] = False
                st.session_state["user_profile"] = {}
                st.rerun()

def require_auth():
    """Decorator/function to require authentication"""
    if not st.session_state.get("authenticated", False):
        st.warning("🔒 Please sign in to access this page.")
        st.stop()

def require_super_admin():
    """Decorator/function to require super admin privileges"""
    require_auth()
    if not st.session_state.get("is_super_admin", False):
        st.error("🚫 Super admin privileges required to access this feature.")
        st.stop()

