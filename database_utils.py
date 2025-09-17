"""
Database utilities for AI Knowledge Hub
Optimized Supabase operations with proper error handling and caching
"""

import streamlit as st
from supabase import create_client, Client
from typing import List, Dict, Optional, Any
import json
from datetime import datetime, timedelta
import hashlib

class DatabaseManager:
    def __init__(self, supabase_client: Client):
        self.supabase = supabase_client
        self.cache_duration = timedelta(minutes=15)  # Cache for 15 minutes
    
    def _get_cache_key(self, table: str, filters: Dict = None) -> str:
        """Generate cache key for query results"""
        key_data = f"{table}_{json.dumps(filters, sort_keys=True) if filters else 'all'}"
        return hashlib.md5(key_data.encode()).hexdigest()
    
    def _is_cache_valid(self, cache_key: str) -> bool:
        """Check if cached data is still valid"""
        if f"cache_{cache_key}" not in st.session_state:
            return False
        
        cache_time = st.session_state.get(f"cache_time_{cache_key}")
        if not cache_time:
            return False
        
        return datetime.now() - cache_time < self.cache_duration
    
    def _set_cache(self, cache_key: str, data: Any):
        """Store data in cache with timestamp"""
        st.session_state[f"cache_{cache_key}"] = data
        st.session_state[f"cache_time_{cache_key}"] = datetime.now()
    
    def _get_cache(self, cache_key: str) -> Any:
        """Retrieve data from cache"""
        return st.session_state.get(f"cache_{cache_key}")
    
    # Knowledge Articles Operations
    def get_knowledge_articles(self, category: str = None, featured: bool = None) -> List[Dict]:
        """Get knowledge articles with optional filtering"""
        filters = {}
        if category:
            filters['category'] = category
        if featured is not None:
            filters['featured'] = featured
        
        cache_key = self._get_cache_key('knowledge_articles', filters)
        
        if self._is_cache_valid(cache_key):
            return self._get_cache(cache_key)
        
        try:
            query = self.supabase.table('knowledge_articles').select('*')
            
            if category:
                query = query.eq('category', category)
            if featured is not None:
                query = query.eq('featured', featured)
            
            result = query.order('created_at', desc=True).execute()
            
            self._set_cache(cache_key, result.data)
            return result.data
        except Exception as e:
            st.error(f"Error fetching knowledge articles: {str(e)}")
            return []
    
    def get_article_by_slug(self, slug: str) -> Optional[Dict]:
        """Get a specific article by slug"""
        cache_key = self._get_cache_key('knowledge_articles', {'slug': slug})
        
        if self._is_cache_valid(cache_key):
            return self._get_cache(cache_key)
        
        try:
            result = self.supabase.table('knowledge_articles').select('*').eq('slug', slug).execute()
            
            if result.data:
                article = result.data[0]
                self._set_cache(cache_key, article)
                return article
            return None
        except Exception as e:
            st.error(f"Error fetching article: {str(e)}")
            return None
    
    # Ollama Course Operations
    def get_ollama_modules(self, difficulty: str = None) -> List[Dict]:
        """Get Ollama course modules"""
        filters = {'difficulty': difficulty} if difficulty else {}
        cache_key = self._get_cache_key('ollama_modules', filters)
        
        if self._is_cache_valid(cache_key):
            return self._get_cache(cache_key)
        
        try:
            query = self.supabase.table('ollama_modules').select('*')
            
            if difficulty:
                query = query.eq('difficulty', difficulty)
            
            result = query.order('module_order').execute()
            
            self._set_cache(cache_key, result.data)
            return result.data
        except Exception as e:
            st.error(f"Error fetching Ollama modules: {str(e)}")
            return []
    
    def get_module_lessons(self, module_id: int) -> List[Dict]:
        """Get lessons for a specific module"""
        cache_key = self._get_cache_key('ollama_lessons', {'module_id': module_id})
        
        if self._is_cache_valid(cache_key):
            return self._get_cache(cache_key)
        
        try:
            result = self.supabase.table('ollama_lessons').select('*').eq('module_id', module_id).order('lesson_order').execute()
            
            self._set_cache(cache_key, result.data)
            return result.data
        except Exception as e:
            st.error(f"Error fetching lessons: {str(e)}")
            return []
    
    # GitHub Resources Operations
    def get_github_resources(self, category: str = None, language: str = None) -> List[Dict]:
        """Get GitHub resources with optional filtering"""
        filters = {}
        if category:
            filters['category'] = category
        if language:
            filters['primary_language'] = language
        
        cache_key = self._get_cache_key('github_resources', filters)
        
        if self._is_cache_valid(cache_key):
            return self._get_cache(cache_key)
        
        try:
            query = self.supabase.table('github_resources').select('*')
            
            if category:
                query = query.eq('category', category)
            if language:
                query = query.eq('primary_language', language)
            
            result = query.order('stars', desc=True).execute()
            
            self._set_cache(cache_key, result.data)
            return result.data
        except Exception as e:
            st.error(f"Error fetching GitHub resources: {str(e)}")
            return []
    
    def increment_download_count(self, resource_id: int):
        """Increment download count for a GitHub resource"""
        try:
            # First get current count
            result = self.supabase.table('github_resources').select('download_count').eq('id', resource_id).execute()
            
            if result.data:
                current_count = result.data[0].get('download_count', 0)
                new_count = current_count + 1
                
                # Update the count
                self.supabase.table('github_resources').update({'download_count': new_count}).eq('id', resource_id).execute()
                
                # Clear cache to force refresh
                self._clear_github_cache()
        except Exception as e:
            st.error(f"Error updating download count: {str(e)}")
    
    def _clear_github_cache(self):
        """Clear GitHub resources cache"""
        keys_to_remove = [key for key in st.session_state.keys() if key.startswith('cache_') and 'github_resources' in key]
        for key in keys_to_remove:
            del st.session_state[key]
    
    # User Activity Tracking
    def log_user_activity(self, user_id: str, activity_type: str, resource_id: int = None, details: Dict = None):
        """Log user activity for analytics"""
        try:
            activity_data = {
                'user_id': user_id,
                'activity_type': activity_type,
                'timestamp': datetime.now().isoformat(),
                'resource_id': resource_id,
                'details': json.dumps(details) if details else None
            }
            
            self.supabase.table('user_activities').insert(activity_data).execute()
        except Exception as e:
            # Don't show error to user for activity logging failures
            print(f"Activity logging error: {str(e)}")
    
    def get_user_progress(self, user_id: str) -> Dict:
        """Get user's learning progress"""
        cache_key = self._get_cache_key('user_progress', {'user_id': user_id})
        
        if self._is_cache_valid(cache_key):
            return self._get_cache(cache_key)
        
        try:
            # Get completed lessons
            completed_lessons = self.supabase.table('user_activities').select('resource_id').eq('user_id', user_id).eq('activity_type', 'lesson_completed').execute()
            
            # Get downloaded resources
            downloaded_resources = self.supabase.table('user_activities').select('resource_id').eq('user_id', user_id).eq('activity_type', 'resource_downloaded').execute()
            
            progress = {
                'completed_lessons': [item['resource_id'] for item in completed_lessons.data],
                'downloaded_resources': [item['resource_id'] for item in downloaded_resources.data],
                'total_activities': len(completed_lessons.data) + len(downloaded_resources.data)
            }
            
            self._set_cache(cache_key, progress)
            return progress
        except Exception as e:
            st.error(f"Error fetching user progress: {str(e)}")
            return {'completed_lessons': [], 'downloaded_resources': [], 'total_activities': 0}
    
    # Search Operations
    def search_content(self, query: str, content_types: List[str] = None) -> Dict:
        """Search across all content types"""
        if not content_types:
            content_types = ['knowledge_articles', 'ollama_modules', 'github_resources']
        
        results = {}
        
        for content_type in content_types:
            try:
                if content_type == 'knowledge_articles':
                    result = self.supabase.table('knowledge_articles').select('*').or_(f'title.ilike.%{query}%,content.ilike.%{query}%,tags.cs.{{{query}}}').execute()
                elif content_type == 'ollama_modules':
                    result = self.supabase.table('ollama_modules').select('*').or_(f'title.ilike.%{query}%,description.ilike.%{query}%').execute()
                elif content_type == 'github_resources':
                    result = self.supabase.table('github_resources').select('*').or_(f'name.ilike.%{query}%,description.ilike.%{query}%,tags.cs.{{{query}}}').execute()
                
                results[content_type] = result.data
            except Exception as e:
                st.error(f"Error searching {content_type}: {str(e)}")
                results[content_type] = []
        
        return results

# Initialize database manager
@st.cache_resource
def get_database_manager():
    """Get cached database manager instance"""
    url = st.secrets.get("SUPABASE_URL", "https://ejvzdfnspcwcazltweig.supabase.co")
    key = st.secrets.get("SUPABASE_ANON_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVqdnpkZm5zcGN3Y2F6bHR3ZWlnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTc0NjM5NjQsImV4cCI6MjA3MzAzOTk2NH0.Qga-V6HVc5kpnTlTraxxO6fxvQEfTYGDFeDWhKNbobU")
    supabase = create_client(url, key)
    return DatabaseManager(supabase)

