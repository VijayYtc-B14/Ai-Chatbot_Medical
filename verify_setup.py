#!/usr/bin/env python
"""
Setup Verification Script for MediCare AI

This script verifies that all required files and dependencies are in place.
Run this before starting the application.
"""

import os
import sys

def check_files():
    """Check if all required files exist."""
    required_files = [
        'app.py',
        'chatbot.py',
        '.env',
        'requirements.txt',
        'README.md',
        'DEPLOYMENT_GUIDE.md',
    ]
    
    required_pages = [
        'pages/1_About.py',
        'pages/2_Services.py',
        'pages/3_Medicine_Search.py',
        'pages/4_AI_Chatbot.py',
        'pages/5_Order_Tracking.py',
        'pages/6_Contact.py',
        'pages/7_FAQ.py',
        'pages/8_Upload_Medicine.py',
    ]
    
    print("🔍 Checking required files...")
    all_exist = True
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - MISSING")
            all_exist = False
    
    print("\n🔍 Checking page files...")
    for page in required_pages:
        if os.path.exists(page):
            print(f"✅ {page}")
        else:
            print(f"❌ {page} - MISSING")
            all_exist = False
    
    return all_exist

def check_env():
    """Check if .env file has required keys."""
    print("\n🔍 Checking environment variables...")
    
    if not os.path.exists('.env'):
        print("❌ .env file not found")
        return False
    
    with open('.env', 'r') as f:
        content = f.read()
    
    if 'GEMINI_API_KEY' in content and 'GEMINI_API_KEY=' in content:
        if content.split('GEMINI_API_KEY=')[1].split('\n')[0].strip():
            print("✅ GEMINI_API_KEY configured")
        else:
            print("❌ GEMINI_API_KEY is empty")
            return False
    else:
        print("❌ GEMINI_API_KEY not found")
        return False
    
    if 'OPENAI_API_KEY' in content and 'OPENAI_API_KEY=' in content:
        if content.split('OPENAI_API_KEY=')[1].split('\n')[0].strip():
            print("✅ OPENAI_API_KEY configured")
        else:
            print("❌ OPENAI_API_KEY is empty")
            return False
    else:
        print("❌ OPENAI_API_KEY not found")
        return False
    
    return True

def check_packages():
    """Check if required packages are installed."""
    print("\n🔍 Checking installed packages...")
    
    required_packages = [
        'streamlit',
        'python-dotenv',
        'google.genai',
        'openai',
        'PIL',
    ]
    
    all_installed = True
    
    for package in required_packages:
        try:
            if package == 'PIL':
                __import__('PIL')
            elif package == 'google.genai':
                __import__('google.genai')
            else:
                __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - NOT INSTALLED")
            all_installed = False
    
    return all_installed

def main():
    """Run all checks."""
    print("=" * 50)
    print("🏥 MediCare AI - Setup Verification")
    print("=" * 50)
    
    files_ok = check_files()
    env_ok = check_env()
    packages_ok = check_packages()
    
    print("\n" + "=" * 50)
    print("📋 Verification Summary")
    print("=" * 50)
    
    if files_ok and env_ok and packages_ok:
        print("\n✅ All checks passed! Ready to run:")
        print("\n   streamlit run app.py\n")
        return 0
    else:
        print("\n❌ Some checks failed. Please fix the issues above.")
        print("\nTo install dependencies:")
        print("   pip install -r requirements.txt")
        print("\nTo configure environment:")
        print("   # Create .env file with:")
        print("   GEMINI_API_KEY=your_key_here")
        print("   OPENAI_API_KEY=your_key_here\n")
        return 1

if __name__ == "__main__":
    sys.exit(main())
