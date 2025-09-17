-- Fixed Supabase Database Schema for AI Knowledge Hub
-- Run these commands in your Supabase SQL editor to fix RLS recursion issues

-- First, drop existing policies to avoid conflicts
DROP POLICY IF EXISTS "Users can view their own profile" ON public.user_profiles;
DROP POLICY IF EXISTS "Users can update their own profile" ON public.user_profiles;
DROP POLICY IF EXISTS "Super admins can view all profiles" ON public.user_profiles;
DROP POLICY IF EXISTS "Users can view their own activity" ON public.user_activity_logs;
DROP POLICY IF EXISTS "Super admins can view all activity" ON public.user_activity_logs;
DROP POLICY IF EXISTS "Only super admins can manage settings" ON public.system_settings;
DROP POLICY IF EXISTS "Users can view their own sessions" ON public.user_sessions;
DROP POLICY IF EXISTS "Super admins can view all sessions" ON public.user_sessions;
DROP POLICY IF EXISTS "Users can view their own downloads" ON public.download_logs;
DROP POLICY IF EXISTS "Super admins can view all downloads" ON public.download_logs;

-- Create custom user profiles table (extends auth.users)
CREATE TABLE IF NOT EXISTS public.user_profiles (
    id UUID REFERENCES auth.users(id) ON DELETE CASCADE PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    full_name TEXT,
    role TEXT DEFAULT 'user' CHECK (role IN ('super_admin', 'admin', 'moderator', 'user', 'viewer')),
    status TEXT DEFAULT 'pending' CHECK (status IN ('active', 'pending', 'suspended', 'inactive')),
    phone TEXT,
    location TEXT,
    profile_complete BOOLEAN DEFAULT FALSE,
    email_verified BOOLEAN DEFAULT FALSE,
    login_count INTEGER DEFAULT 0,
    last_login TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    approved_by UUID REFERENCES auth.users(id),
    approved_at TIMESTAMP WITH TIME ZONE,
    notes TEXT
);

-- Create user activity logs table
CREATE TABLE IF NOT EXISTS public.user_activity_logs (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    activity_type TEXT NOT NULL,
    description TEXT,
    ip_address INET,
    user_agent TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create system settings table
CREATE TABLE IF NOT EXISTS public.system_settings (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    setting_key TEXT UNIQUE NOT NULL,
    setting_value JSONB,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_by UUID REFERENCES auth.users(id)
);

-- Create user sessions table for tracking
CREATE TABLE IF NOT EXISTS public.user_sessions (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    session_token TEXT UNIQUE,
    ip_address INET,
    user_agent TEXT,
    expires_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    last_activity TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create download logs table
CREATE TABLE IF NOT EXISTS public.download_logs (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    user_id UUID REFERENCES auth.users(id) ON DELETE CASCADE,
    file_name TEXT NOT NULL,
    file_path TEXT,
    file_size INTEGER,
    download_count INTEGER DEFAULT 1,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Enable Row Level Security on all tables
ALTER TABLE public.user_profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.user_activity_logs ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.system_settings ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.user_sessions ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.download_logs ENABLE ROW LEVEL SECURITY;

-- Create a helper function to check if user is super admin
CREATE OR REPLACE FUNCTION public.is_super_admin(user_id UUID)
RETURNS BOOLEAN AS $$
BEGIN
    RETURN EXISTS (
        SELECT 1 FROM auth.users 
        WHERE id = user_id 
        AND email = 'entremotivator@gmail.com'
    );
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Fixed RLS policies for user_profiles (avoiding recursion)
CREATE POLICY "Enable read access for users to own profile" ON public.user_profiles
    FOR SELECT USING (auth.uid() = id);

CREATE POLICY "Enable update access for users to own profile" ON public.user_profiles
    FOR UPDATE USING (auth.uid() = id);

CREATE POLICY "Enable insert access for authenticated users" ON public.user_profiles
    FOR INSERT WITH CHECK (auth.uid() = id);

CREATE POLICY "Enable super admin full access" ON public.user_profiles
    FOR ALL USING (public.is_super_admin(auth.uid()));

-- RLS policies for user_activity_logs
CREATE POLICY "Users can view own activity logs" ON public.user_activity_logs
    FOR SELECT USING (auth.uid() = user_id OR public.is_super_admin(auth.uid()));

CREATE POLICY "Enable insert for authenticated users" ON public.user_activity_logs
    FOR INSERT WITH CHECK (auth.uid() = user_id OR public.is_super_admin(auth.uid()));

CREATE POLICY "Super admin can manage all activity logs" ON public.user_activity_logs
    FOR ALL USING (public.is_super_admin(auth.uid()));

-- RLS policies for system_settings
CREATE POLICY "Super admin can manage system settings" ON public.system_settings
    FOR ALL USING (public.is_super_admin(auth.uid()));

-- RLS policies for user_sessions
CREATE POLICY "Users can view own sessions" ON public.user_sessions
    FOR SELECT USING (auth.uid() = user_id OR public.is_super_admin(auth.uid()));

CREATE POLICY "Users can insert own sessions" ON public.user_sessions
    FOR INSERT WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Super admin can manage all sessions" ON public.user_sessions
    FOR ALL USING (public.is_super_admin(auth.uid()));

-- RLS policies for download_logs
CREATE POLICY "Users can view own downloads" ON public.download_logs
    FOR SELECT USING (auth.uid() = user_id OR public.is_super_admin(auth.uid()));

CREATE POLICY "Users can insert own downloads" ON public.download_logs
    FOR INSERT WITH CHECK (auth.uid() = user_id);

CREATE POLICY "Super admin can manage all downloads" ON public.download_logs
    FOR ALL USING (public.is_super_admin(auth.uid()));

-- Create function to automatically create user profile on signup
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO public.user_profiles (id, email, full_name, email_verified, role, status)
    VALUES (
        NEW.id,
        NEW.email,
        COALESCE(NEW.raw_user_meta_data->>'full_name', NEW.email),
        COALESCE(NEW.email_confirmed_at IS NOT NULL, FALSE),
        CASE 
            WHEN NEW.email = 'entremotivator@gmail.com' THEN 'super_admin'
            ELSE 'user'
        END,
        CASE 
            WHEN NEW.email = 'entremotivator@gmail.com' THEN 'active'
            ELSE 'pending'
        END
    );
    RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Create trigger for new user signup
DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users;
CREATE TRIGGER on_auth_user_created
    AFTER INSERT ON auth.users
    FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();

-- Create function to update user login stats
CREATE OR REPLACE FUNCTION public.update_user_login_stats(user_id UUID)
RETURNS VOID AS $$
BEGIN
    UPDATE public.user_profiles 
    SET 
        login_count = login_count + 1,
        last_login = NOW(),
        updated_at = NOW()
    WHERE id = user_id;
    
    -- Log the login activity
    INSERT INTO public.user_activity_logs (user_id, activity_type, description)
    VALUES (user_id, 'login', 'User logged in successfully');
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Create function to log user activity
CREATE OR REPLACE FUNCTION public.log_user_activity(
    user_id UUID,
    activity_type TEXT,
    description TEXT DEFAULT NULL,
    ip_address INET DEFAULT NULL,
    user_agent TEXT DEFAULT NULL
)
RETURNS VOID AS $$
BEGIN
    INSERT INTO public.user_activity_logs (user_id, activity_type, description, ip_address, user_agent)
    VALUES (user_id, activity_type, description, ip_address, user_agent);
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Create function to get user statistics
CREATE OR REPLACE FUNCTION public.get_user_statistics()
RETURNS TABLE (
    total_users BIGINT,
    active_users BIGINT,
    pending_users BIGINT,
    suspended_users BIGINT,
    inactive_users BIGINT,
    total_logins BIGINT,
    users_today BIGINT
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        COUNT(*) as total_users,
        COUNT(*) FILTER (WHERE status = 'active') as active_users,
        COUNT(*) FILTER (WHERE status = 'pending') as pending_users,
        COUNT(*) FILTER (WHERE status = 'suspended') as suspended_users,
        COUNT(*) FILTER (WHERE status = 'inactive') as inactive_users,
        COALESCE(SUM(login_count), 0) as total_logins,
        COUNT(*) FILTER (WHERE created_at >= CURRENT_DATE) as users_today
    FROM public.user_profiles;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Create function to approve user (simplified to avoid recursion)
CREATE OR REPLACE FUNCTION public.approve_user(
    target_user_id UUID,
    approver_id UUID
)
RETURNS BOOLEAN AS $$
BEGIN
    -- Check if approver is super admin using direct email check
    IF NOT EXISTS (
        SELECT 1 FROM auth.users 
        WHERE id = approver_id AND email = 'entremotivator@gmail.com'
    ) THEN
        RETURN FALSE;
    END IF;
    
    -- Approve the user
    UPDATE public.user_profiles 
    SET 
        status = 'active',
        approved_by = approver_id,
        approved_at = NOW(),
        updated_at = NOW()
    WHERE id = target_user_id;
    
    -- Log the approval
    INSERT INTO public.user_activity_logs (user_id, activity_type, description)
    VALUES (target_user_id, 'approved', 'User account approved by admin');
    
    RETURN TRUE;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Create function to suspend user (simplified to avoid recursion)
CREATE OR REPLACE FUNCTION public.suspend_user(
    target_user_id UUID,
    admin_id UUID,
    reason TEXT DEFAULT NULL
)
RETURNS BOOLEAN AS $$
DECLARE
    target_email TEXT;
BEGIN
    -- Get target user email
    SELECT email INTO target_email 
    FROM auth.users 
    WHERE id = target_user_id;
    
    -- Can't suspend super admin
    IF target_email = 'entremotivator@gmail.com' THEN
        RETURN FALSE;
    END IF;
    
    -- Check if admin is super admin
    IF NOT EXISTS (
        SELECT 1 FROM auth.users 
        WHERE id = admin_id AND email = 'entremotivator@gmail.com'
    ) THEN
        RETURN FALSE;
    END IF;
    
    -- Suspend the user
    UPDATE public.user_profiles 
    SET 
        status = 'suspended',
        updated_at = NOW(),
        notes = COALESCE(notes || E'\n', '') || 'Suspended: ' || COALESCE(reason, 'No reason provided')
    WHERE id = target_user_id;
    
    -- Log the suspension
    INSERT INTO public.user_activity_logs (user_id, activity_type, description)
    VALUES (target_user_id, 'suspended', 'User account suspended: ' || COALESCE(reason, 'No reason provided'));
    
    RETURN TRUE;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Insert default system settings
INSERT INTO public.system_settings (setting_key, setting_value, description) VALUES
('app_name', '"AI Knowledge Hub"', 'Application name'),
('app_version', '"2.0.0"', 'Application version'),
('maintenance_mode', 'false', 'Enable/disable maintenance mode'),
('user_registration_enabled', 'true', 'Allow new user registrations'),
('auto_approve_users', 'false', 'Automatically approve new users'),
('session_timeout_minutes', '60', 'Session timeout in minutes'),
('max_login_attempts', '5', 'Maximum login attempts before lockout'),
('email_verification_required', 'true', 'Require email verification for new users')
ON CONFLICT (setting_key) DO NOTHING;

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_user_profiles_email ON public.user_profiles(email);
CREATE INDEX IF NOT EXISTS idx_user_profiles_status ON public.user_profiles(status);
CREATE INDEX IF NOT EXISTS idx_user_profiles_role ON public.user_profiles(role);
CREATE INDEX IF NOT EXISTS idx_user_profiles_created_at ON public.user_profiles(created_at);
CREATE INDEX IF NOT EXISTS idx_user_activity_logs_user_id ON public.user_activity_logs(user_id);
CREATE INDEX IF NOT EXISTS idx_user_activity_logs_created_at ON public.user_activity_logs(created_at);
CREATE INDEX IF NOT EXISTS idx_user_sessions_user_id ON public.user_sessions(user_id);
CREATE INDEX IF NOT EXISTS idx_download_logs_user_id ON public.download_logs(user_id);

-- Grant necessary permissions
GRANT USAGE ON SCHEMA public TO anon, authenticated;
GRANT ALL ON ALL TABLES IN SCHEMA public TO authenticated;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO authenticated;
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO authenticated;

-- Additional security: Create a service role function for admin operations
CREATE OR REPLACE FUNCTION public.admin_get_all_users()
RETURNS TABLE (
    id UUID,
    email TEXT,
    full_name TEXT,
    role TEXT,
    status TEXT,
    phone TEXT,
    location TEXT,
    profile_complete BOOLEAN,
    email_verified BOOLEAN,
    login_count INTEGER,
    last_login TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE,
    updated_at TIMESTAMP WITH TIME ZONE,
    approved_by UUID,
    approved_at TIMESTAMP WITH TIME ZONE,
    notes TEXT
) AS $$
BEGIN
    -- Only allow super admin to call this function
    IF NOT public.is_super_admin(auth.uid()) THEN
        RAISE EXCEPTION 'Access denied: Super admin privileges required';
    END IF;
    
    RETURN QUERY
    SELECT 
        up.id,
        up.email,
        up.full_name,
        up.role,
        up.status,
        up.phone,
        up.location,
        up.profile_complete,
        up.email_verified,
        up.login_count,
        up.last_login,
        up.created_at,
        up.updated_at,
        up.approved_by,
        up.approved_at,
        up.notes
    FROM public.user_profiles up
    ORDER BY up.created_at DESC;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

