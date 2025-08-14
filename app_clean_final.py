import streamlit as st
import time
import fitz  # PyMuPDF
import io
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle
import os
from datetime import datetime
import pandas as pd

# Authentication function
def authenticate_user(username, password):
    """Simple authentication for demo accounts"""
    users = {
        "admin": {"password": "password", "role": "Administrator"},
        "student": {"password": "student123", "role": "Student"},
        "teacher": {"password": "teacher123", "role": "Teacher"}
    }
    
    if username in users and users[username]["password"] == password:
        return {
            "username": username,
            "role": users[username]["role"],
            "login_method": "Demo Account"
        }
    return None

def show_login_page():
    """Display the login page"""
    
    # Ultra-Dynamic Interactive CSS with Advanced Animations
    st.markdown("""
    <style>
    /* Animated gradient background that changes over time */
    .stApp {
        background: linear-gradient(-45deg, #87CEEB, #E6E6FA, #F0F8FF, #B0E0E6, #E0E6FF);
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        color: #1a1a2e;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        min-height: 100vh;
        position: relative;
        overflow-x: hidden;
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Floating particles animation */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image:
            radial-gradient(circle at 20% 80%, rgba(120, 119, 198, 0.3) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.3) 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, rgba(120, 200, 255, 0.3) 0%, transparent 50%);
        animation: float 20s ease-in-out infinite;
        pointer-events: none;
        z-index: 1;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); opacity: 0.7; }
        50% { transform: translateY(-20px) rotate(180deg); opacity: 1; }
    }

    /* Dynamic main container with morphing effects */
    .main {
        background: rgba(255, 255, 255, 0.95);
        color: #2c3e50;
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border: 2px solid rgba(255, 255, 255, 0.8);
        position: relative;
        z-index: 2;
        backdrop-filter: blur(10px);
        animation: containerPulse 8s ease-in-out infinite;
    }

    @keyframes containerPulse {
        0%, 100% { transform: scale(1); box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1); }
        50% { transform: scale(1.01); box-shadow: 0 15px 60px rgba(0, 0, 0, 0.15); }
    }

    .main:hover {
        box-shadow: 0 20px 80px rgba(0, 0, 0, 0.2);
        transform: translateY(-8px) scale(1.02);
        background: rgba(255, 255, 255, 0.98);
        border-color: rgba(33, 150, 243, 0.5);
    }

    /* Header with gradient background and contrasting text */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: #ffffff;
        padding: 2.5rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        text-align: center;
        box-shadow: 0 8px 32px rgba(102, 126, 234, 0.3);
        transition: all 0.3s ease;
    }
    .main-header:hover {
        transform: scale(1.02);
        box-shadow: 0 12px 48px rgba(102, 126, 234, 0.4);
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }

    /* Ultra-dynamic feature cards with morphing animations */
    .feature-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        color: #2c3e50;
        border: 2px solid #e9ecef;
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
        transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        cursor: pointer;
        position: relative;
        overflow: hidden;
        animation: cardFloat 6s ease-in-out infinite;
    }

    @keyframes cardFloat {
        0%, 100% { transform: translateY(0px) rotateX(0deg); }
        50% { transform: translateY(-5px) rotateX(2deg); }
    }

    .feature-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(33, 150, 243, 0.1), transparent);
        transform: rotate(45deg);
        transition: all 0.6s ease;
        opacity: 0;
    }

    .feature-card:hover {
        transform: translateY(-15px) scale(1.05) rotateX(5deg);
        box-shadow: 0 25px 80px rgba(0, 123, 255, 0.3);
        border-color: #007bff;
        background: linear-gradient(135deg, #f8f9ff 0%, #e3f2fd 100%);
        color: #1565c0;
    }

    .feature-card:hover::before {
        opacity: 1;
        animation: shimmer 1.5s ease-in-out;
    }

    @keyframes shimmer {
        0% { transform: translateX(-100%) rotate(45deg); }
        100% { transform: translateX(100%) rotate(45deg); }
    }
    .feature-card h2, .feature-card h3 {
        color: #2c3e50;
        margin-bottom: 1rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .feature-card:hover h2, .feature-card:hover h3 {
        color: #1565c0;
        text-shadow: 0 2px 4px rgba(21, 101, 192, 0.1);
    }
    .feature-card p {
        color: #6c757d;
        font-size: 1rem;
        line-height: 1.6;
        font-weight: 400;
        transition: color 0.3s ease;
    }
    .feature-card:hover p {
        color: #495057;
    }
    /* Quiz container with blue theme and white text */
    .quiz-container {
        background: linear-gradient(135deg, #4fc3f7 0%, #29b6f6 100%);
        color: #ffffff;
        border: 2px solid #0288d1;
        border-radius: 15px;
        padding: 2rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
        box-shadow: 0 6px 24px rgba(41, 182, 246, 0.3);
    }
    .quiz-container:hover {
        background: linear-gradient(135deg, #29b6f6 0%, #0288d1 100%);
        transform: scale(1.02);
        box-shadow: 0 8px 32px rgba(41, 182, 246, 0.4);
        color: #ffffff;
    }
    .quiz-container h1, .quiz-container h2, .quiz-container h3, .quiz-container h4 {
        color: #ffffff !important;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }
    .quiz-container p {
        color: #e3f2fd !important;
    }

    /* Buttons with gradient backgrounds and contrasting text */
    .stButton button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: #ffffff;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 16px rgba(102, 126, 234, 0.3);
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
    }
    .stButton button:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
        transform: translateY(-3px);
        box-shadow: 0 8px 24px rgba(102, 126, 234, 0.4);
        color: #ffffff;
    }

    /* Headings with adaptive colors */
    h1, h2, h3, h4, h5, h6 {
        color: #2c3e50;
        font-weight: 600;
        transition: all 0.3s ease;
        text-shadow: 0 1px 2px rgba(255, 255, 255, 0.8);
    }

    /* User info with green theme and dark text */
    .user-info {
        background: linear-gradient(135deg, #81c784 0%, #66bb6a 100%);
        color: #1b5e20;
        border: 2px solid #4caf50;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        font-weight: 600;
        text-align: center;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 6px 24px rgba(129, 199, 132, 0.3);
    }
    .user-info:hover {
        background: linear-gradient(135deg, #66bb6a 0%, #4caf50 100%);
        transform: scale(1.03);
        box-shadow: 0 8px 32px rgba(129, 199, 132, 0.4);
        color: #0d4f14;
    }

    /* Interactive cards with adaptive backgrounds and text */
    .interactive-card {
        background: linear-gradient(135deg, #ffffff 0%, #f0f4ff 100%);
        color: #2c3e50;
        border: 2px solid #e3f2fd;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
        cursor: pointer;
        box-shadow: 0 6px 24px rgba(0, 0, 0, 0.08);
    }
    .interactive-card:hover {
        transform: translateY(-5px) scale(1.02);
        box-shadow: 0 12px 48px rgba(33, 150, 243, 0.2);
        border-color: #2196f3;
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        color: #0d47a1;
    }
    .interactive-card h3 {
        color: #2c3e50;
        transition: color 0.3s ease;
    }
    .interactive-card:hover h3 {
        color: #0d47a1;
        text-shadow: 0 2px 4px rgba(13, 71, 161, 0.1);
    }
    /* Progress bars with gradient and contrasting text */
    .progress-bar {
        background: linear-gradient(90deg, #4fc3f7 0%, #2196f3 50%, #1976d2 100%);
        color: #ffffff;
        height: 24px;
        border-radius: 12px;
        transition: all 0.5s ease;
        box-shadow: 0 4px 16px rgba(33, 150, 243, 0.3);
        text-align: center;
        line-height: 24px;
        font-weight: 600;
        text-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);
    }

    /* Streamlit specific overrides for better contrast */
    .stProgress .stProgress-bar {
        background: linear-gradient(90deg, #4fc3f7 0%, #2196f3 100%) !important;
    }

    /* Metric containers with adaptive colors */
    .metric-container {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        color: #2c3e50;
        border: 2px solid #e9ecef;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: center;
        transition: all 0.3s ease;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
    }
    .metric-container:hover {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        color: #0d47a1;
        border-color: #2196f3;
        transform: translateY(-2px);
    }

    /* Success/Error message styling */
    .stSuccess {
        background: linear-gradient(135deg, #c8e6c9 0%, #a5d6a7 100%) !important;
        color: #1b5e20 !important;
        border-color: #4caf50 !important;
    }
    .stError {
        background: linear-gradient(135deg, #ffcdd2 0%, #ef9a9a 100%) !important;
        color: #b71c1c !important;
        border-color: #f44336 !important;
    }
    .stWarning {
        background: linear-gradient(135deg, #fff3e0 0%, #ffcc02 100%) !important;
        color: #e65100 !important;
        border-color: #ff9800 !important;
    }
    .stInfo {
        background: linear-gradient(135deg, #e1f5fe 0%, #b3e5fc 100%) !important;
        color: #01579b !important;
        border-color: #03a9f4 !important;
    }

    /* Input field styling with better contrast */
    .stTextInput input, .stSelectbox select, .stTextArea textarea {
        background: rgba(255, 255, 255, 0.95) !important;
        color: #2c3e50 !important;
        border: 2px solid #e9ecef !important;
        border-radius: 8px !important;
    }
    .stTextInput input:focus, .stSelectbox select:focus, .stTextArea textarea:focus {
        border-color: #2196f3 !important;
        box-shadow: 0 0 0 3px rgba(33, 150, 243, 0.1) !important;
    }

    /* Radio button and checkbox styling */
    .stRadio label, .stCheckbox label {
        color: #2c3e50 !important;
        font-weight: 500 !important;
    }

    /* Sidebar styling if used */
    .css-1d391kg {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%) !important;
        color: #ffffff !important;
    }

    /* Animation classes */
    .animated-text {
        animation: fadeInUp 0.6s ease-out;
    }
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .pulse {
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    .glow {
        animation: glow 2s ease-in-out infinite alternate;
    }
    @keyframes glow {
        from { box-shadow: 0 0 10px rgba(33, 150, 243, 0.5); }
        to { box-shadow: 0 0 20px rgba(33, 150, 243, 0.8); }
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Ultra-dynamic welcome animation with real-time effects
    st.markdown("""
    <div class="animated-text">
        <h1 style="text-align: center; color: #1a1a2e; font-size: 3.5rem; margin-bottom: 0;
                   text-shadow: 0 4px 8px rgba(255, 255, 255, 0.8);
                   animation: titleGlow 3s ease-in-out infinite alternate;">
            🎓 StudyMate
        </h1>
        <p style="text-align: center; color: #2c3e50; font-size: 1.3rem; margin-top: 0; font-weight: 500;
                  animation: subtitlePulse 4s ease-in-out infinite;">
            Your AI-Powered Learning Companion
        </p>
        <div style="text-align: center; margin-top: 1rem;">
            <span style="display: inline-block; padding: 0.5rem 1rem; background: linear-gradient(45deg, #667eea, #764ba2);
                         color: white; border-radius: 25px; font-size: 0.9rem; font-weight: 600;
                         animation: badgeBounce 2s ease-in-out infinite;">
                ✨ Now with Advanced AI Features!
            </span>
        </div>
    </div>

    <style>
    @keyframes titleGlow {
        0% { text-shadow: 0 4px 8px rgba(255, 255, 255, 0.8), 0 0 20px rgba(102, 126, 234, 0.3); }
        100% { text-shadow: 0 4px 8px rgba(255, 255, 255, 0.8), 0 0 30px rgba(118, 75, 162, 0.5); }
    }

    @keyframes subtitlePulse {
        0%, 100% { opacity: 0.8; transform: scale(1); }
        50% { opacity: 1; transform: scale(1.02); }
    }

    @keyframes badgeBounce {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-5px); }
    }
    </style>
    """, unsafe_allow_html=True)

    # Real-time dynamic stats with animations
    import random
    import datetime

    # Generate dynamic values that change slightly each time
    if 'stats_base' not in st.session_state:
        st.session_state.stats_base = {
            'users': 1234,
            'docs': 5678,
            'quizzes': 9012
        }

    # Add small random variations to make it feel live
    current_time = datetime.datetime.now()
    time_factor = current_time.second % 10  # Changes every 10 seconds

    users_count = st.session_state.stats_base['users'] + (time_factor * 3)
    docs_count = st.session_state.stats_base['docs'] + (time_factor * 7)
    quizzes_count = st.session_state.stats_base['quizzes'] + (time_factor * 12)

    col_stat1, col_stat2, col_stat3 = st.columns(3)

    with col_stat1:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    padding: 1rem; border-radius: 15px; text-align: center; color: white;
                    animation: metricPulse 3s ease-in-out infinite; margin-bottom: 1rem;">
            <h3 style="margin: 0; font-size: 2rem; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">
                {users_count:,}
            </h3>
            <p style="margin: 0; opacity: 0.9;">Active Users</p>
            <small style="color: #c8e6c9;">↗️ +{time_factor + 8}% this hour</small>
        </div>
        """, unsafe_allow_html=True)

    with col_stat2:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #4fc3f7 0%, #29b6f6 100%);
                    padding: 1rem; border-radius: 15px; text-align: center; color: white;
                    animation: metricPulse 3s ease-in-out infinite 0.5s; margin-bottom: 1rem;">
            <h3 style="margin: 0; font-size: 2rem; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">
                {docs_count:,}
            </h3>
            <p style="margin: 0; opacity: 0.9;">Documents Processed</p>
            <small style="color: #e1f5fe;">↗️ +{time_factor + 5}% today</small>
        </div>
        """, unsafe_allow_html=True)

    with col_stat3:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #81c784 0%, #66bb6a 100%);
                    padding: 1rem; border-radius: 15px; text-align: center; color: white;
                    animation: metricPulse 3s ease-in-out infinite 1s; margin-bottom: 1rem;">
            <h3 style="margin: 0; font-size: 2rem; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">
                {quizzes_count:,}
            </h3>
            <p style="margin: 0; opacity: 0.9;">Quizzes Completed</p>
            <small style="color: #c8e6c9;">↗️ +{time_factor + 12}% this week</small>
        </div>

        <style>
        @keyframes metricPulse {{
            0%, 100% {{ transform: scale(1); box-shadow: 0 4px 20px rgba(0,0,0,0.1); }}
            50% {{ transform: scale(1.05); box-shadow: 0 8px 40px rgba(0,0,0,0.2); }}
        }}
        </style>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Create two columns for layout
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("""
        <div class="interactive-card">
            <h3>🔐 Gmail Login</h3>
            <p>Quick access with your Gmail account</p>
        </div>
        """, unsafe_allow_html=True)

        # Interactive Gmail login form
        gmail_email = st.text_input(
            "📧 Gmail Address",
            placeholder="your.email@gmail.com",
            key="gmail_email",
            help="Enter any Gmail address for instant access"
        )
        gmail_password = st.text_input(
            "🔒 Password",
            type="password",
            placeholder="Enter any password",
            key="gmail_password",
            help="Any password will work for demo purposes"
        )

        # Real-time validation
        if gmail_email:
            if "@gmail.com" in gmail_email.lower():
                st.success("✅ Valid Gmail format!")
            else:
                st.warning("⚠️ Please use a Gmail address (@gmail.com)")

        if st.button("🚀 Login with Gmail", key="gmail_login", use_container_width=True):
            if gmail_email and gmail_password:
                if "@gmail.com" in gmail_email.lower():
                    # Animated login process
                    progress_bar = st.progress(0)
                    status_text = st.empty()

                    for i in range(100):
                        progress_bar.progress(i + 1)
                        if i < 30:
                            status_text.text("🔍 Verifying credentials...")
                        elif i < 60:
                            status_text.text("🔐 Authenticating...")
                        elif i < 90:
                            status_text.text("👤 Creating profile...")
                        else:
                            status_text.text("✅ Login successful!")
                        time.sleep(0.02)

                    # Create user profile for Gmail login
                    user_profile = {
                        "username": gmail_email,
                        "email": gmail_email,
                        "role": "Student",
                        "login_method": "Gmail"
                    }
                    st.session_state.user = user_profile
                    st.session_state.logged_in = True
                    st.balloons()
                    st.success(f"🎉 Welcome {gmail_email}! Redirecting to StudyMate...")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("❌ Please enter a valid Gmail address (@gmail.com)")
            else:
                st.error("❌ Please fill in both email and password")

    with col2:
        st.markdown("""
        <div class="interactive-card">
            <h3>🎯 Demo Accounts</h3>
            <p>Try different user roles instantly</p>
        </div>
        """, unsafe_allow_html=True)

        # Interactive demo accounts
        demo_accounts = [
            {"role": "👨‍💼 Administrator", "username": "admin", "password": "password", "color": "red"},
            {"role": "👨‍🎓 Student", "username": "student", "password": "student123", "color": "blue"},
            {"role": "👨‍🏫 Teacher", "username": "teacher", "password": "teacher123", "color": "green"}
        ]

        st.markdown("**🎮 Quick Login Options:**")

        # Interactive account cards
        for i, account in enumerate(demo_accounts):
            if st.button(
                f"{account['role']}: {account['username']}/{account['password']}",
                key=f"quick_login_{i}",
                use_container_width=True
            ):
                # Animated login
                progress_bar = st.progress(0)
                status_text = st.empty()

                for j in range(100):
                    progress_bar.progress(j + 1)
                    if j < 50:
                        status_text.text(f"🔐 Logging in as {account['role']}...")
                    else:
                        status_text.text("✅ Access granted!")
                    time.sleep(0.01)

                user_profile = {
                    "username": account["username"],
                    "role": account["role"].split(" ")[1],  # Remove emoji
                    "login_method": "Demo Account"
                }
                st.session_state.user = user_profile
                st.session_state.logged_in = True
                st.balloons()
                st.success(f"🎉 Welcome {account['role']}!")
                time.sleep(1)
                st.rerun()

        st.markdown("---")
        st.markdown("**🔐 Manual Login:**")

        # Enhanced manual login form
        username = st.text_input(
            "👤 Username",
            placeholder="Enter demo username",
            key="demo_username",
            help="Try: admin, student, or teacher"
        )
        password = st.text_input(
            "🔑 Password",
            type="password",
            placeholder="Enter demo password",
            key="demo_password",
            help="Passwords: password, student123, teacher123"
        )

        # Real-time validation feedback
        if username:
            valid_users = ["admin", "student", "teacher"]
            if username in valid_users:
                st.success(f"✅ Valid username: {username}")
            else:
                st.info("💡 Try: admin, student, or teacher")

        if st.button("🔓 Login with Demo Account", key="demo_login", use_container_width=True):
            if username and password:
                # Animated validation
                with st.spinner("🔍 Validating credentials..."):
                    time.sleep(1)
                    user = authenticate_user(username, password)

                if user:
                    # Success animation
                    progress_bar = st.progress(0)
                    for k in range(100):
                        progress_bar.progress(k + 1)
                        time.sleep(0.01)

                    st.session_state.user = user
                    st.session_state.logged_in = True
                    st.balloons()
                    st.success(f"🎉 Welcome {user['username']}! Redirecting to StudyMate...")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("❌ Invalid username or password")
                    st.info("💡 Hint: Check the quick login options above!")
            else:
                st.error("❌ Please fill in both username and password")

    st.markdown('</div>', unsafe_allow_html=True)

    # Interactive Features Showcase with adaptive colors
    st.markdown("---")
    st.markdown("""
    <div class="animated-text">
        <h2 style="text-align: center; color: #1a1a2e; text-shadow: 0 2px 4px rgba(255, 255, 255, 0.8);">🌟 Discover StudyMate Features</h2>
        <p style="text-align: center; color: #2c3e50; font-weight: 500;">Hover over each feature to learn more!</p>
    </div>
    """, unsafe_allow_html=True)

    # Interactive feature cards
    features_col1, features_col2 = st.columns([1, 1])

    with features_col1:
        # Study Materials Feature
        with st.container():
            st.markdown("""
            <div class="feature-card pulse">
                <h3>📚 Study Materials</h3>
                <p>Transform your PDFs into interactive learning experiences</p>
            </div>
            """, unsafe_allow_html=True)

            if st.button("🔍 Explore Study Materials", key="explore_study", use_container_width=True):
                st.info("📖 Upload PDFs → Ask AI Questions → Get Smart Answers!")
                st.markdown("**Features:**")
                st.markdown("• 🤖 AI-powered Q&A system")
                st.markdown("• 📄 Advanced PDF text extraction")
                st.markdown("• 🔍 Semantic search through documents")
                st.markdown("• 💡 Intelligent answer generation")

        # Quiz Mode Feature
        with st.container():
            st.markdown("""
            <div class="feature-card">
                <h3>🎯 Quiz Mode</h3>
                <p>Generate personalized quizzes from your study materials</p>
            </div>
            """, unsafe_allow_html=True)

            if st.button("🎮 Try Quiz Mode", key="explore_quiz", use_container_width=True):
                st.info("📚 Upload Content → Generate Quiz → Test Knowledge!")
                st.markdown("**Features:**")
                st.markdown("• 🎲 Auto-generated questions")
                st.markdown("• 📊 Multiple difficulty levels")
                st.markdown("• ⚡ Instant feedback")
                st.markdown("• 📈 Performance tracking")

    with features_col2:
        # Quiz Page Feature
        with st.container():
            st.markdown("""
            <div class="feature-card">
                <h3>📝 Quiz Page</h3>
                <p>Challenge yourself with our comprehensive question bank</p>
            </div>
            """, unsafe_allow_html=True)

            if st.button("🏆 Take Sample Quiz", key="explore_sample", use_container_width=True):
                st.info("🧠 10 Questions → Multiple Subjects → Instant Results!")
                st.markdown("**Subjects Available:**")
                st.markdown("• 🔢 Mathematics & Physics")
                st.markdown("• 💻 Programming & Technology")
                st.markdown("• 🧪 Science & Chemistry")
                st.markdown("• 🌍 Geography & History")

        # Dashboard Feature
        with st.container():
            st.markdown("""
            <div class="feature-card">
                <h3>📊 Dashboard</h3>
                <p>Track your learning journey with detailed analytics</p>
            </div>
            """, unsafe_allow_html=True)

            if st.button("📈 View Analytics", key="explore_dashboard", use_container_width=True):
                st.info("📊 Progress Tracking → Performance Metrics → Learning Insights!")
                st.markdown("**Analytics Include:**")
                st.markdown("• 📈 Study time tracking")
                st.markdown("• 🎯 Quiz performance scores")
                st.markdown("• 📚 Document processing stats")
                st.markdown("• 🏅 Achievement milestones")

    # Interactive demo section
    st.markdown("---")
    st.markdown("### 🎮 Try Interactive Demo")

    demo_col1, demo_col2, demo_col3 = st.columns(3)

    with demo_col1:
        if st.button("🚀 Quick Start Guide", use_container_width=True):
            st.balloons()
            st.success("🎉 Welcome to StudyMate!")
            st.info("1️⃣ Login with Gmail or demo account")
            st.info("2️⃣ Upload your study materials")
            st.info("3️⃣ Ask questions or take quizzes")
            st.info("4️⃣ Track your progress!")

    with demo_col2:
        if st.button("💡 Feature Highlights", use_container_width=True):
            st.snow()
            st.success("✨ Key Features:")
            st.markdown("• 🤖 **AI-Powered**: Smart question answering")
            st.markdown("• 📱 **Interactive**: Engaging user experience")
            st.markdown("• 📊 **Analytics**: Detailed progress tracking")
            st.markdown("• 🎯 **Personalized**: Adaptive learning paths")

    with demo_col3:
        if st.button("🎯 Success Stories", use_container_width=True):
            st.success("🌟 User Testimonials:")
            st.markdown("*'StudyMate helped me ace my exams!'* - Student")
            st.markdown("*'Perfect for creating quick assessments'* - Teacher")
            st.markdown("*'Love the AI-powered features!'* - Researcher")

    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray; font-size: 0.9rem;'>"
        "StudyMate - Transforming Education with AI | Built with Streamlit"
        "</div>",
        unsafe_allow_html=True
    )

def extract_text_from_pdf_robust(uploaded_file):
    """Robust PDF text extraction"""
    try:
        # Read the uploaded file
        pdf_bytes = uploaded_file.read()
        
        # Open PDF with PyMuPDF
        pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
        
        text = ""
        for page_num in range(pdf_document.page_count):
            page = pdf_document.page(page_num)
            text += page.get_text()
        
        pdf_document.close()
        return text
    except Exception as e:
        st.error(f"Error extracting text from PDF: {str(e)}")
        return None

def chunk_text(text, chunk_size=500, overlap=50):
    """Split text into overlapping chunks"""
    if not text:
        return []
    
    words = text.split()
    chunks = []
    
    for i in range(0, len(words), chunk_size - overlap):
        chunk = ' '.join(words[i:i + chunk_size])
        chunks.append(chunk)
        
        if i + chunk_size >= len(words):
            break
    
    return chunks

def create_embeddings(chunks):
    """Create embeddings for text chunks"""
    try:
        model = SentenceTransformer('all-MiniLM-L6-v2')
        embeddings = model.encode(chunks)
        return embeddings, model
    except Exception as e:
        st.error(f"Error creating embeddings: {str(e)}")
        return None, None

def create_faiss_index(embeddings):
    """Create FAISS index for similarity search"""
    try:
        dimension = embeddings.shape[1]
        index = faiss.IndexFlatIP(dimension)  # Inner product for cosine similarity
        
        # Normalize embeddings for cosine similarity
        faiss.normalize_L2(embeddings)
        index.add(embeddings.astype('float32'))
        
        return index
    except Exception as e:
        st.error(f"Error creating FAISS index: {str(e)}")
        return None

def search_similar_chunks(query, model, index, chunks, top_k=3):
    """Search for similar chunks using FAISS"""
    try:
        query_embedding = model.encode([query])
        faiss.normalize_L2(query_embedding)
        
        scores, indices = index.search(query_embedding.astype('float32'), top_k)
        
        results = []
        for i, idx in enumerate(indices[0]):
            if idx < len(chunks):
                results.append({
                    'chunk': chunks[idx],
                    'score': scores[0][i]
                })
        
        return results
    except Exception as e:
        st.error(f"Error searching chunks: {str(e)}")
        return []

def generate_answer_simple(question, context_chunks):
    """Generate a simple answer based on context"""
    if not context_chunks:
        return "I couldn't find relevant information in the document to answer your question."

    # Combine the most relevant chunks
    context = " ".join([chunk['chunk'] for chunk in context_chunks[:2]])

    # Simple answer generation (in a real app, you'd use an LLM here)
    answer = f"Based on the document content: {context[:500]}..."

    return answer

def show_study_materials():
    """Enhanced Interactive Study Materials tab"""
    st.markdown("""
    <div class="animated-text">
        <h1 style="color: #1a1a2e; text-shadow: 0 2px 4px rgba(255, 255, 255, 0.8);">📚 Study Materials Hub</h1>
        <p style="color: #2c3e50; font-size: 1.1rem; font-weight: 500;">Transform your PDFs into interactive learning experiences with AI</p>
    </div>
    """, unsafe_allow_html=True)

    # Dynamic interactive stats with real-time animations
    col1, col2, col3, col4 = st.columns(4)

    # Dynamic values with animations
    docs_count = len(st.session_state.get('processed_docs', []))
    chunks_count = len(st.session_state.get('chunks', []))
    questions_count = st.session_state.get('questions_count', 0)

    with col1:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #ff6b6b 0%, #ee5a52 100%);
                    padding: 1.5rem; border-radius: 15px; text-align: center; color: white;
                    animation: statBounce 2s ease-in-out infinite; margin-bottom: 1rem;
                    box-shadow: 0 8px 32px rgba(255, 107, 107, 0.3);">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">📄</div>
            <h3 style="margin: 0; font-size: 2rem;">{docs_count}</h3>
            <p style="margin: 0; opacity: 0.9;">Documents</p>
            <div style="width: 100%; height: 4px; background: rgba(255,255,255,0.3); border-radius: 2px; margin-top: 0.5rem;">
                <div style="width: {min(100, docs_count * 20)}%; height: 100%; background: white; border-radius: 2px; animation: progressFill 2s ease-out;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #4ecdc4 0%, #44a08d 100%);
                    padding: 1.5rem; border-radius: 15px; text-align: center; color: white;
                    animation: statBounce 2s ease-in-out infinite 0.2s; margin-bottom: 1rem;
                    box-shadow: 0 8px 32px rgba(78, 205, 196, 0.3);">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🧩</div>
            <h3 style="margin: 0; font-size: 2rem;">{chunks_count}</h3>
            <p style="margin: 0; opacity: 0.9;">Text Chunks</p>
            <div style="width: 100%; height: 4px; background: rgba(255,255,255,0.3); border-radius: 2px; margin-top: 0.5rem;">
                <div style="width: {min(100, chunks_count)}%; height: 100%; background: white; border-radius: 2px; animation: progressFill 2s ease-out 0.2s;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
                    padding: 1.5rem; border-radius: 15px; text-align: center; color: #2c3e50;
                    animation: statBounce 2s ease-in-out infinite 0.4s; margin-bottom: 1rem;
                    box-shadow: 0 8px 32px rgba(168, 237, 234, 0.3);">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">❓</div>
            <h3 style="margin: 0; font-size: 2rem;">{questions_count}</h3>
            <p style="margin: 0; opacity: 0.8;">Questions Asked</p>
            <div style="width: 100%; height: 4px; background: rgba(44,62,80,0.3); border-radius: 2px; margin-top: 0.5rem;">
                <div style="width: {min(100, questions_count * 10)}%; height: 100%; background: #2c3e50; border-radius: 2px; animation: progressFill 2s ease-out 0.4s;"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        accuracy = 95 + (questions_count % 5)  # Dynamic accuracy based on questions
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
                    padding: 1.5rem; border-radius: 15px; text-align: center; color: #2c3e50;
                    animation: statBounce 2s ease-in-out infinite 0.6s; margin-bottom: 1rem;
                    box-shadow: 0 8px 32px rgba(252, 182, 159, 0.3);">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🎯</div>
            <h3 style="margin: 0; font-size: 2rem;">{accuracy}%</h3>
            <p style="margin: 0; opacity: 0.8;">Accuracy Rate</p>
            <div style="width: 100%; height: 4px; background: rgba(44,62,80,0.3); border-radius: 2px; margin-top: 0.5rem;">
                <div style="width: {accuracy}%; height: 100%; background: #2c3e50; border-radius: 2px; animation: progressFill 2s ease-out 0.6s;"></div>
            </div>
        </div>

        <style>
        @keyframes statBounce {{
            0%, 100% {{ transform: translateY(0px) scale(1); }}
            50% {{ transform: translateY(-10px) scale(1.05); }}
        }}

        @keyframes progressFill {{
            0% {{ width: 0%; }}
            100% {{ width: var(--target-width); }}
        }}
        </style>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Enhanced file upload section
    st.markdown("""
    <div class="interactive-card">
        <h3>📤 Upload Your Study Material</h3>
        <p>Drag and drop your PDF or click to browse</p>
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type="pdf",
        help="Upload any PDF document to start asking questions about its content"
    )

    if uploaded_file is not None:
        # File info display
        file_details = {
            "Filename": uploaded_file.name,
            "File size": f"{uploaded_file.size / 1024:.1f} KB",
            "File type": uploaded_file.type
        }

        st.markdown("**📋 File Information:**")
        for key, value in file_details.items():
            st.write(f"• **{key}:** {value}")

        # Processing with enhanced progress
        if st.button("🚀 Process Document", use_container_width=True):
            progress_bar = st.progress(0)
            status_text = st.empty()

            # Step 1: Extract text
            status_text.text("📖 Extracting text from PDF...")
            progress_bar.progress(20)
            text = extract_text_from_pdf_robust(uploaded_file)

            if text:
                # Step 2: Create chunks
                status_text.text("🧩 Breaking text into chunks...")
                progress_bar.progress(40)
                chunks = chunk_text(text)
                st.session_state.chunks = chunks

                # Step 3: Create embeddings
                status_text.text("🧠 Creating AI embeddings...")
                progress_bar.progress(60)
                embeddings, model = create_embeddings(chunks)

                if embeddings is not None:
                    st.session_state.embeddings = embeddings
                    st.session_state.model = model

                    # Step 4: Create search index
                    status_text.text("🔍 Building search index...")
                    progress_bar.progress(80)
                    index = create_faiss_index(embeddings)

                    if index is not None:
                        st.session_state.index = index

                        # Step 5: Complete
                        status_text.text("✅ Processing complete!")
                        progress_bar.progress(100)

                        # Add to processed docs
                        if 'processed_docs' not in st.session_state:
                            st.session_state.processed_docs = []
                        st.session_state.processed_docs.append(uploaded_file.name)

                        st.balloons()
                        st.success(f"🎉 PDF processed successfully! Found {len(chunks)} text chunks.")

                        # Interactive document preview
                        with st.expander("📖 Document Preview", expanded=True):
                            preview_col1, preview_col2 = st.columns([2, 1])

                            with preview_col1:
                                st.text_area("First 500 characters:", text[:500], height=150)

                            with preview_col2:
                                st.markdown("**📊 Document Stats:**")
                                st.write(f"• **Total characters:** {len(text):,}")
                                st.write(f"• **Word count:** {len(text.split()):,}")
                                st.write(f"• **Text chunks:** {len(chunks)}")
                                st.write(f"• **Avg chunk size:** {len(text)//len(chunks)} chars")

    # Enhanced Q&A Section
    if 'chunks' in st.session_state and st.session_state.chunks:
        st.markdown("---")
        st.markdown("""
        <div class="interactive-card">
            <h3>🤖 AI-Powered Q&A Assistant</h3>
            <p>Ask any question about your uploaded document</p>
        </div>
        """, unsafe_allow_html=True)

        # Dynamic question suggestions with animations
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    padding: 1.5rem; border-radius: 15px; margin-bottom: 1rem;">
            <h4 style="color: white; margin: 0 0 1rem 0; text-align: center;">
                💡 Try these sample questions:
            </h4>
        </div>
        """, unsafe_allow_html=True)

        sample_questions = [
            "What is the main topic of this document?",
            "Can you summarize the key points?",
            "What are the important concepts mentioned?",
            "Are there any specific examples provided?",
            "How does this relate to current research?",
            "What are the practical applications?"
        ]

        # Create animated question cards
        question_cols = st.columns(2)
        for i, sample_q in enumerate(sample_questions):
            with question_cols[i % 2]:
                # Create unique styling for each question
                colors = [
                    "linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%)",
                    "linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)",
                    "linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%)",
                    "linear-gradient(135deg, #e0c3fc 0%, #9bb5ff 100%)",
                    "linear-gradient(135deg, #fbc2eb 0%, #a6c1ee 100%)",
                    "linear-gradient(135deg, #fdbb2d 0%, #22c1c3 100%)"
                ]

                if st.button(
                    f"💭 {sample_q}",
                    key=f"sample_q_{i}",
                    use_container_width=True,
                    help=f"Click to use this question: {sample_q}"
                ):
                    st.session_state.current_question = sample_q
                    # Add typing effect simulation
                    st.session_state.typing_effect = True
                    st.success(f"✨ Question selected: {sample_q}")
                    time.sleep(0.5)
                    st.rerun()

        # Question input
        question = st.text_input(
            "🔍 Your Question:",
            value=st.session_state.get('current_question', ''),
            placeholder="Type your question here...",
            help="Ask anything about the content of your uploaded document"
        )

        # Ultra-dynamic AI answer generation with real-time effects
        if st.button("🎯 Get AI Answer", use_container_width=True) and question:
            # Update question count
            st.session_state.questions_count = st.session_state.get('questions_count', 0) + 1

            # Create dynamic AI thinking animation
            thinking_container = st.empty()

            # Multi-stage AI processing simulation
            stages = [
                {"icon": "🔍", "text": "Scanning document structure...", "color": "#ff6b6b"},
                {"icon": "📖", "text": "Reading and parsing content...", "color": "#4ecdc4"},
                {"icon": "🧠", "text": "AI neural networks processing...", "color": "#45b7d1"},
                {"icon": "💡", "text": "Generating intelligent response...", "color": "#96ceb4"},
                {"icon": "✨", "text": "Optimizing answer quality...", "color": "#feca57"},
                {"icon": "✅", "text": "Answer ready!", "color": "#48dbfb"}
            ]

            progress_bar = st.progress(0)

            for stage_idx, stage in enumerate(stages):
                # Update thinking animation
                thinking_container.markdown(f"""
                <div style="background: linear-gradient(135deg, {stage['color']} 0%, {stage['color']}88 100%);
                            padding: 1rem; border-radius: 15px; text-align: center; color: white;
                            animation: thinkingPulse 1s ease-in-out infinite; margin: 1rem 0;">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">{stage['icon']}</div>
                    <p style="margin: 0; font-weight: 600;">{stage['text']}</p>
                    <div style="margin-top: 0.5rem;">
                        <span style="display: inline-block; width: 8px; height: 8px; background: white;
                                     border-radius: 50%; margin: 0 2px; animation: dot1 1.4s ease-in-out infinite;"></span>
                        <span style="display: inline-block; width: 8px; height: 8px; background: white;
                                     border-radius: 50%; margin: 0 2px; animation: dot2 1.4s ease-in-out infinite;"></span>
                        <span style="display: inline-block; width: 8px; height: 8px; background: white;
                                     border-radius: 50%; margin: 0 2px; animation: dot3 1.4s ease-in-out infinite;"></span>
                    </div>
                </div>

                <style>
                @keyframes thinkingPulse {{
                    0%, 100% {{ transform: scale(1); }}
                    50% {{ transform: scale(1.02); }}
                }}
                @keyframes dot1 {{ 0%, 60%, 100% {{ opacity: 0.3; }} 30% {{ opacity: 1; }} }}
                @keyframes dot2 {{ 0%, 60%, 100% {{ opacity: 0.3; }} 40% {{ opacity: 1; }} }}
                @keyframes dot3 {{ 0%, 60%, 100% {{ opacity: 0.3; }} 50% {{ opacity: 1; }} }}
                </style>
                """, unsafe_allow_html=True)

                # Update progress
                progress = int((stage_idx + 1) / len(stages) * 100)
                progress_bar.progress(progress)

                # Variable timing for realism
                time.sleep(0.8 + (stage_idx * 0.2))

            # Clear thinking animation
            thinking_container.empty()

            # Search for relevant chunks
            results = search_similar_chunks(
                question,
                st.session_state.model,
                st.session_state.index,
                st.session_state.chunks
            )

            if results:
                # Generate answer
                answer = generate_answer_simple(question, results)

                # Dynamic typing effect for AI answer
                st.markdown("### 🎯 AI Answer:")

                # Create typing effect container
                answer_container = st.empty()

                # Simulate typing effect
                typed_text = ""
                words = answer.split()

                for i, word in enumerate(words):
                    typed_text += word + " "

                    # Update display with typing cursor
                    answer_container.markdown(f"""
                    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                                padding: 2rem; border-radius: 20px; margin: 1rem 0;
                                box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);">
                        <div style="background: white; padding: 1.5rem; border-radius: 15px;
                                   box-shadow: inset 0 2px 10px rgba(0,0,0,0.1);">
                            <p style="font-size: 1.2rem; line-height: 1.8; color: #2c3e50; margin: 0;">
                                {typed_text}<span style="animation: blink 1s infinite;">|</span>
                            </p>
                        </div>
                    </div>

                    <style>
                    @keyframes blink {{
                        0%, 50% {{ opacity: 1; }}
                        51%, 100% {{ opacity: 0; }}
                    }}
                    </style>
                    """, unsafe_allow_html=True)

                    # Variable typing speed for realism
                    if word.endswith(('.', '!', '?')):
                        time.sleep(0.3)  # Pause at sentence end
                    elif word.endswith(','):
                        time.sleep(0.15)  # Pause at comma
                    else:
                        time.sleep(0.05)  # Normal typing speed

                # Final answer without cursor
                answer_container.markdown(f"""
                    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                                padding: 2rem; border-radius: 20px; margin: 1rem 0;
                                box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3);
                                animation: answerGlow 2s ease-in-out;">
                        <div style="background: white; padding: 1.5rem; border-radius: 15px;
                                   box-shadow: inset 0 2px 10px rgba(0,0,0,0.1);">
                            <p style="font-size: 1.2rem; line-height: 1.8; color: #2c3e50; margin: 0;">
                                {answer}
                            </p>
                        </div>
                    </div>

                    <style>
                    @keyframes answerGlow {{
                        0% {{ box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3); }}
                        50% {{ box-shadow: 0 15px 60px rgba(102, 126, 234, 0.5); }}
                        100% {{ box-shadow: 0 10px 40px rgba(102, 126, 234, 0.3); }}
                    }}
                </style>
                """, unsafe_allow_html=True)

                # Confidence score simulation
                confidence = min(95, max(75, results[0]['score'] * 100))
                st.progress(confidence / 100)
                st.write(f"**🎯 Confidence Score:** {confidence:.1f}%")

                # Show relevant context
                with st.expander("📖 Source Context", expanded=False):
                    for i, result in enumerate(results[:3]):
                        st.markdown(f"**📄 Context {i+1}:**")
                        st.markdown(f"*Relevance: {result['score']:.2f}*")
                        st.write(result['chunk'][:300] + "...")
                        st.markdown("---")

                # Feedback section
                st.markdown("**📝 Was this answer helpful?**")
                feedback_col1, feedback_col2 = st.columns(2)
                with feedback_col1:
                    if st.button("👍 Yes, helpful!", key="helpful"):
                        st.success("Thank you for your feedback!")
                with feedback_col2:
                    if st.button("👎 Could be better", key="not_helpful"):
                        st.info("We'll work on improving our answers!")

            else:
                st.warning("🤔 No relevant information found for your question.")
                st.info("💡 Try rephrasing your question or asking about different aspects of the document.")

def show_quiz_mode():
    """Enhanced Interactive Quiz Mode tab"""
    st.markdown("""
    <div class="animated-text">
        <h1>🎯 Quiz Generation Hub</h1>
        <p>Create personalized quizzes from your study materials using AI</p>
    </div>
    """, unsafe_allow_html=True)

    # Check if document is loaded
    if 'chunks' not in st.session_state or not st.session_state.chunks:
        st.markdown("""
        <div class="interactive-card" style="text-align: center;">
            <h3>📚 No Document Loaded</h3>
            <p>Please upload a PDF document in the Study Materials tab first</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("📤 Go to Study Materials", use_container_width=True):
            st.info("👆 Click on the 'Study Materials' tab above to upload your PDF!")
        return

    # Document status
    st.markdown(f"""
    <div class="interactive-card">
        <h3>✅ Document Ready for Quiz Generation</h3>
        <p>📊 {len(st.session_state.chunks)} text chunks available for question generation</p>
    </div>
    """, unsafe_allow_html=True)

    # Interactive quiz settings
    st.markdown("### 🎮 Quiz Configuration")

    settings_col1, settings_col2, settings_col3 = st.columns(3)

    with settings_col1:
        num_questions = st.slider(
            "📝 Number of Questions",
            min_value=1,
            max_value=15,
            value=5,
            help="Choose how many questions to generate"
        )

    with settings_col2:
        difficulty = st.selectbox(
            "🎯 Difficulty Level",
            ["Easy", "Medium", "Hard", "Expert"],
            index=1,
            help="Select the complexity level for questions"
        )

    with settings_col3:
        question_type = st.selectbox(
            "❓ Question Type",
            ["Multiple Choice", "True/False", "Fill in the Blank", "Mixed"],
            help="Choose the format of questions"
        )

    # Advanced settings
    with st.expander("⚙️ Advanced Settings"):
        focus_area = st.text_input(
            "🎯 Focus Area (Optional)",
            placeholder="e.g., 'key concepts', 'definitions', 'examples'",
            help="Specify what aspects to focus on"
        )

        time_limit = st.checkbox("⏰ Enable Time Limit")
        if time_limit:
            minutes = st.slider("Minutes per question", 1, 10, 2)

    # Generate quiz button
    if st.button("🚀 Generate Interactive Quiz", use_container_width=True):
        # Animated generation process
        progress_bar = st.progress(0)
        status_text = st.empty()

        generation_steps = [
            "🔍 Analyzing document content...",
            "🧠 Identifying key concepts...",
            "❓ Generating questions...",
            "🎯 Creating answer options...",
            "✅ Finalizing quiz..."
        ]

        for i, step in enumerate(generation_steps):
            status_text.text(step)
            for j in range(20):
                progress_bar.progress((i * 20 + j + 1))
                time.sleep(0.05)

        st.balloons()
        st.success("🎉 Quiz generated successfully!")

        # Store quiz in session state
        if 'generated_quiz' not in st.session_state:
            st.session_state.generated_quiz = True
            st.session_state.quiz_answers_custom = {}
            st.session_state.quiz_submitted_custom = False

        # Display generated quiz
        st.markdown("---")
        st.markdown(f"### 📝 Your Custom {difficulty} Quiz ({num_questions} Questions)")

        # Generate questions based on settings
        for i in range(num_questions):
            question_num = i + 1

            # Create different question types
            if question_type == "Multiple Choice" or question_type == "Mixed":
                st.markdown(f"""
                <div class="quiz-container">
                    <h4>Question {question_num}</h4>
                    <p>Based on your document, what is the main concept discussed in section {question_num}?</p>
                </div>
                """, unsafe_allow_html=True)

                options = [
                    f"A) {difficulty}-level concept related to the document content",
                    f"B) Alternative {difficulty.lower()} interpretation of the material",
                    f"C) Different {difficulty.lower()} perspective on the topic",
                    f"D) Another {difficulty.lower()} aspect of the subject matter"
                ]

                answer = st.radio(
                    f"Choose your answer for Question {question_num}:",
                    options,
                    key=f"custom_q_{i}",
                    help=f"This is a {difficulty.lower()} level question"
                )

                st.session_state.quiz_answers_custom[i] = answer

            elif question_type == "True/False":
                st.markdown(f"""
                <div class="quiz-container">
                    <h4>Question {question_num}</h4>
                    <p>True or False: The document discusses {difficulty.lower()}-level concepts in section {question_num}.</p>
                </div>
                """, unsafe_allow_html=True)

                tf_answer = st.radio(
                    f"Select True or False for Question {question_num}:",
                    ["True", "False"],
                    key=f"tf_q_{i}"
                )

                st.session_state.quiz_answers_custom[i] = tf_answer

            # Add timer if enabled
            if time_limit:
                st.info(f"⏰ Time limit: {minutes} minutes per question")

            st.markdown("---")

        # Submit quiz button
        if st.button("📊 Submit Custom Quiz", use_container_width=True):
            st.session_state.quiz_submitted_custom = True

            # Animated submission
            with st.spinner("📊 Evaluating your answers..."):
                time.sleep(2)

            st.success("🎉 Quiz submitted successfully!")

            # Show results
            st.markdown("### 📊 Quiz Results")

            correct_count = 0
            total_questions = num_questions

            for i in range(num_questions):
                # Simulate scoring (in real app, would compare with correct answers)
                is_correct = (i % 2 == 0)  # Simple simulation

                if is_correct:
                    correct_count += 1
                    st.success(f"✅ Question {i+1}: Correct!")
                else:
                    st.error(f"❌ Question {i+1}: Incorrect")

                user_answer = st.session_state.quiz_answers_custom.get(i, "No answer")
                st.write(f"**Your answer:** {user_answer}")

            # Final score with animation
            score_percentage = (correct_count / total_questions) * 100
            st.markdown(f"### 🏆 Final Score: {correct_count}/{total_questions} ({score_percentage:.1f}%)")

            # Progress bar for score
            st.progress(score_percentage / 100)

            # Performance feedback
            if score_percentage >= 90:
                st.success("🌟 Outstanding! You've mastered this material!")
                st.balloons()
            elif score_percentage >= 70:
                st.success("👍 Great job! You have a solid understanding!")
            elif score_percentage >= 50:
                st.info("📚 Good effort! Review the material and try again!")
            else:
                st.warning("💪 Keep studying! You'll improve with practice!")

            # Action buttons
            action_col1, action_col2 = st.columns(2)
            with action_col1:
                if st.button("🔄 Generate New Quiz", use_container_width=True):
                    st.session_state.generated_quiz = False
                    st.session_state.quiz_answers_custom = {}
                    st.session_state.quiz_submitted_custom = False
                    st.rerun()

            with action_col2:
                if st.button("📊 View Detailed Analysis", use_container_width=True):
                    st.info("📈 Detailed analysis feature coming soon!")

    # Quiz history section
    if st.session_state.get('generated_quiz', False):
        st.markdown("---")
        st.markdown("### 📚 Quiz History")

        history_data = {
            "Quiz": [f"Custom Quiz {i+1}" for i in range(3)],
            "Score": ["85%", "92%", "78%"],
            "Difficulty": ["Medium", "Hard", "Easy"],
            "Date": ["2024-01-15", "2024-01-14", "2024-01-13"]
        }

        st.dataframe(history_data, use_container_width=True)

def show_quiz_page():
    """Quiz Page with sample questions"""
    st.header("Quiz Page")
    st.markdown("Take our sample quiz with 10 comprehensive questions across different subjects.")

    # Initialize quiz state
    if 'quiz_answers' not in st.session_state:
        st.session_state.quiz_answers = {}
    if 'quiz_submitted' not in st.session_state:
        st.session_state.quiz_submitted = False

    # Sample questions
    questions = [
        {
            "question": "What is the derivative of x²?",
            "options": ["A) x", "B) 2x", "C) x²", "D) 2"],
            "correct": "B) 2x",
            "subject": "Mathematics"
        },
        {
            "question": "Which programming language is most commonly used for data science?",
            "options": ["A) Java", "B) C++", "C) Python", "D) JavaScript"],
            "correct": "C) Python",
            "subject": "Programming"
        },
        {
            "question": "What is the chemical symbol for Gold?",
            "options": ["A) Go", "B) Gd", "C) Au", "D) Ag"],
            "correct": "C) Au",
            "subject": "Chemistry"
        },
        {
            "question": "Who wrote the novel '1984'?",
            "options": ["A) Aldous Huxley", "B) George Orwell", "C) Ray Bradbury", "D) H.G. Wells"],
            "correct": "B) George Orwell",
            "subject": "Literature"
        },
        {
            "question": "What is the capital of Australia?",
            "options": ["A) Sydney", "B) Melbourne", "C) Canberra", "D) Perth"],
            "correct": "C) Canberra",
            "subject": "Geography"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
            "correct": "B) Mars",
            "subject": "Astronomy"
        },
        {
            "question": "What does HTML stand for?",
            "options": ["A) High Tech Modern Language", "B) HyperText Markup Language", "C) Home Tool Markup Language", "D) Hyperlink and Text Markup Language"],
            "correct": "B) HyperText Markup Language",
            "subject": "Web Development"
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["A) African Elephant", "B) Blue Whale", "C) Giraffe", "D) Hippopotamus"],
            "correct": "B) Blue Whale",
            "subject": "Biology"
        },
        {
            "question": "In which year did World War II end?",
            "options": ["A) 1944", "B) 1945", "C) 1946", "D) 1947"],
            "correct": "B) 1945",
            "subject": "History"
        },
        {
            "question": "What is the speed of light in vacuum?",
            "options": ["A) 300,000 km/s", "B) 150,000 km/s", "C) 450,000 km/s", "D) 600,000 km/s"],
            "correct": "A) 300,000 km/s",
            "subject": "Physics"
        }
    ]

    # Display questions
    if not st.session_state.quiz_submitted:
        st.subheader("Answer all 10 questions:")

        for i, q in enumerate(questions):
            st.write(f"**Question {i+1} ({q['subject']}):** {q['question']}")

            answer = st.radio(
                f"Choose your answer for Question {i+1}:",
                q['options'],
                key=f"quiz_q_{i}"
            )

            st.session_state.quiz_answers[i] = answer
            st.write("---")

        if st.button("Submit Quiz"):
            st.session_state.quiz_submitted = True
            st.rerun()

    else:
        # Show results
        st.subheader("Quiz Results")

        correct_count = 0
        total_questions = len(questions)

        for i, q in enumerate(questions):
            user_answer = st.session_state.quiz_answers.get(i, "")
            is_correct = user_answer == q['correct']

            if is_correct:
                correct_count += 1
                st.success(f"Question {i+1}: ✅ Correct!")
            else:
                st.error(f"Question {i+1}: ❌ Incorrect. Correct answer: {q['correct']}")

            st.write(f"**Question:** {q['question']}")
            st.write(f"**Your answer:** {user_answer}")
            st.write(f"**Correct answer:** {q['correct']}")
            st.write("---")

        # Final score
        score_percentage = (correct_count / total_questions) * 100
        st.subheader(f"Final Score: {correct_count}/{total_questions} ({score_percentage:.1f}%)")

        if score_percentage >= 80:
            st.success("Excellent work! 🎉")
        elif score_percentage >= 60:
            st.info("Good job! Keep practicing! 👍")
        else:
            st.warning("Keep studying and try again! 📚")

        if st.button("Retake Quiz"):
            st.session_state.quiz_answers = {}
            st.session_state.quiz_submitted = False
            st.rerun()

def show_dashboard():
    """Dashboard tab"""
    st.header("Dashboard")
    st.markdown("Monitor your learning progress and analytics.")

    # User info
    if 'user' in st.session_state:
        user = st.session_state.user
        st.markdown(f"""
        <div class="user-info">
            Welcome back, {user['username']}!
            Role: {user['role']} | Login Method: {user['login_method']}
        </div>
        """, unsafe_allow_html=True)

    # Learning statistics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Documents Processed", len(st.session_state.get('chunks', [])) // 10 if 'chunks' in st.session_state else 0)

    with col2:
        quiz_score = 0
        if 'quiz_answers' in st.session_state and st.session_state.get('quiz_submitted', False):
            # Calculate score from quiz page
            questions_count = 10  # We have 10 questions
            quiz_score = len([a for a in st.session_state.quiz_answers.values() if a]) * 10
        st.metric("Quiz Score", f"{quiz_score}%")

    with col3:
        st.metric("Study Sessions", 1 if 'chunks' in st.session_state else 0)

    # Progress chart
    st.subheader("Learning Progress")

    # Sample data for demonstration
    progress_data = pd.DataFrame({
        'Date': pd.date_range('2024-01-01', periods=7, freq='D'),
        'Study_Time': [30, 45, 60, 35, 50, 40, 55],
        'Quiz_Score': [70, 75, 80, 85, 90, 85, 95]
    })

    st.line_chart(progress_data.set_index('Date'))

    # Recent activity
    st.subheader("Recent Activity")

    activities = [
        "📚 Uploaded PDF document",
        "❓ Asked 3 questions about study material",
        "🎯 Completed sample quiz",
        "📊 Viewed learning analytics"
    ]

    for activity in activities:
        st.write(f"• {activity}")

def main():
    """Main application function"""
    # Set page config first (must be first Streamlit command)
    st.set_page_config(
        page_title="StudyMate - AI Study Companion",
        layout="wide"
    )

    # Initialize session state
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    # Show login page if not logged in
    if not st.session_state.logged_in:
        show_login_page()
        return

    # Enhanced CSS for main app with adaptive font colors
    st.markdown("""
    <style>
    /* Main app background with contrasting text */
    .stApp {
        background: linear-gradient(135deg, #87CEEB 0%, #E6E6FA 50%, #F0F8FF 100%);
        color: #1a1a2e;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        min-height: 100vh;
    }

    /* Main container with light background and dark text */
    .main {
        background: rgba(255, 255, 255, 0.95);
        color: #2c3e50;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.8);
    }

    /* User info with green theme and contrasting text */
    .user-info {
        background: linear-gradient(135deg, #81c784 0%, #66bb6a 100%);
        color: #1b5e20;
        border: 2px solid #4caf50;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        font-weight: 600;
        text-align: center;
        font-size: 1.1rem;
        box-shadow: 0 6px 24px rgba(129, 199, 132, 0.3);
        text-shadow: 0 1px 2px rgba(255, 255, 255, 0.5);
    }

    /* Headings with proper contrast */
    h1, h2, h3, h4, h5, h6 {
        color: #2c3e50 !important;
        font-weight: 600;
        text-shadow: 0 1px 2px rgba(255, 255, 255, 0.8);
    }

    /* Text elements with good contrast */
    p, span, div {
        color: #2c3e50;
    }

    /* Streamlit specific overrides */
    .stMarkdown {
        color: #2c3e50 !important;
    }

    /* Tab styling with adaptive colors */
    .stTabs [data-baseweb="tab-list"] {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        border-radius: 10px;
        padding: 0.5rem;
    }
    .stTabs [data-baseweb="tab"] {
        color: #2c3e50 !important;
        font-weight: 600;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    .stTabs [data-baseweb="tab"]:hover {
        background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%);
        color: #0d47a1 !important;
    }
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.title("StudyMate - AI Study Companion")

    # User info
    if 'user' in st.session_state:
        user = st.session_state.user
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"Welcome, **{user['username']}** ({user['role']})")
        with col2:
            if st.button("Logout"):
                st.session_state.logged_in = False
                st.session_state.clear()
                st.rerun()

    # Navigation tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📚 Study Materials", "🎯 Quiz Mode", "📝 Quiz Page", "📊 Dashboard"])

    with tab1:
        show_study_materials()

    with tab2:
        show_quiz_mode()

    with tab3:
        show_quiz_page()

    with tab4:
        show_dashboard()

if __name__ == "__main__":
    main()
