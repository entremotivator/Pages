import streamlit as st
from supabase import create_client, Client
from typing import Optional, Dict, Any
import hashlib
import secrets

# Super admin email
SUPER_ADMIN_EMAIL = "entremotivator@gmail.com"

class AuthManager:
    """Enhanced authentication manager with super admin functionality"""
    
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
    
    def sign_up_user(self, email: str, password: str) -> Dict[str, Any]:
        """Register a new user"""
        try:
            # Check if super admin is trying to register
            if self.is_super_admin(email):
                # Allow super admin registration
                response = self.supabase.auth.sign_up({
                    "email": email,
                    "password": password,
                    "options": {
                        "data": {
                            "role": "super_admin",
                            "is_super_admin": True
                        }
                    }
                })
            else:
                # Regular user registration - require approval
                response = self.supabase.auth.sign_up({
                    "email": email,
                    "password": password,
                    "options": {
                        "data": {
                            "role": "user",
                            "is_super_admin": False,
                            "approved": False
                        }
                    }
                })
            
            return {
                "success": True,
                "user": response.user,
                "message": "Registration successful! Please check your email for verification." if not self.is_super_admin(email) else "Super admin account created successfully!"
            }
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "message": f"Registration failed: {str(e)}"
            }
    
    def sign_in_user(self, email: str, password: str) -> Dict[str, Any]:
        """Sign in a user"""
        try:
            response = self.supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
            
            if response.user:
                # Check if user is approved (except super admin)
                user_metadata = response.user.user_metadata or {}
                
                if not self.is_super_admin(email):
                    if not user_metadata.get("approved", False):
                        # Sign out unapproved user
                        self.supabase.auth.sign_out()
                        return {
                            "success": False,
                            "message": "Your account is pending approval. Please contact the administrator."
                        }
                
                return {
                    "success": True,
                    "user": response.user,
                    "is_super_admin": self.is_super_admin(email),
                    "message": "Login successful!"
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
        """Get current authenticated user"""
        try:
            user = self.supabase.auth.get_user()
            if user and user.user:
                return {
                    "id": user.user.id,
                    "email": user.user.email,
                    "is_super_admin": self.is_super_admin(user.user.email),
                    "metadata": user.user.user_metadata or {}
                }
            return None
        except:
            return None
    
    def list_all_users(self) -> list:
        """List all users (super admin only)"""
        try:
            # This would require admin privileges in Supabase
            # For now, return empty list as this requires server-side implementation
            return []
        except Exception as e:
            st.error(f"Error fetching users: {str(e)}")
            return []
    
    def approve_user(self, user_id: str) -> bool:
        """Approve a user (super admin only)"""
        try:
            # This would require admin privileges in Supabase
            # For now, return False as this requires server-side implementation
            return False
        except Exception as e:
            st.error(f"Error approving user: {str(e)}")
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

def render_auth_sidebar(auth_manager: AuthManager):
    """Render authentication sidebar"""
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
                            st.success(result["message"])
                            st.rerun()
                        else:
                            st.error(result["message"])
            
            with tab2:
                with st.form("register_form"):
                    st.markdown("### Create Account")
                    reg_email = st.text_input("Email", placeholder="Enter your email address", key="reg_email")
                    reg_password = st.text_input("Password", type="password", placeholder="Create a password", key="reg_password")
                    reg_password_confirm = st.text_input("Confirm Password", type="password", placeholder="Confirm your password", key="reg_password_confirm")
                    register_button = st.form_submit_button("Create Account", use_container_width=True)
                    
                    if register_button:
                        if not reg_email or not reg_password:
                            st.error("Please fill in all fields.")
                        elif reg_password != reg_password_confirm:
                            st.error("Passwords do not match.")
                        elif len(reg_password) < 6:
                            st.error("Password must be at least 6 characters long.")
                        else:
                            result = auth_manager.sign_up_user(reg_email, reg_password)
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

