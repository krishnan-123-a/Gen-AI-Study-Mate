"""
Setup Script for StudyMate Application
Helps users install dependencies and configure the environment
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path


def print_banner():
    """Print welcome banner"""
    print("=" * 60)
    print("📚 StudyMate Setup - AI-Powered PDF Q&A System")
    print("=" * 60)
    print()


def check_python_version():
    """Check if Python version is compatible"""
    print("🐍 Checking Python version...")
    
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")
    return True


def install_dependencies():
    """Install required Python packages"""
    print("\n📦 Installing dependencies...")
    
    try:
        # Check if requirements.txt exists
        if not os.path.exists("requirements.txt"):
            print("❌ requirements.txt not found")
            return False
        
        # Install packages
        result = subprocess.run([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Dependencies installed successfully")
            return True
        else:
            print("❌ Failed to install dependencies")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Error installing dependencies: {str(e)}")
        return False


def setup_environment():
    """Setup environment configuration"""
    print("\n🔧 Setting up environment configuration...")
    
    # Check if .env already exists
    if os.path.exists(".env"):
        print("ℹ️ .env file already exists")
        return True
    
    # Copy .env.example to .env
    if os.path.exists(".env.example"):
        try:
            shutil.copy(".env.example", ".env")
            print("✅ Created .env file from template")
            print("⚠️ Please edit .env file with your IBM Watsonx AI credentials")
            return True
        except Exception as e:
            print(f"❌ Failed to create .env file: {str(e)}")
            return False
    else:
        print("❌ .env.example not found")
        return False


def verify_installation():
    """Verify that the installation is working"""
    print("\n🧪 Verifying installation...")
    
    try:
        # Try importing key modules
        import streamlit
        import fitz  # PyMuPDF
        import sentence_transformers
        import faiss
        import ibm_watsonx_ai
        
        print("✅ All required packages imported successfully")
        
        # Check if test script exists and run basic tests
        if os.path.exists("test_studymate.py"):
            print("ℹ️ Test script found. You can run 'python test_studymate.py' to test the system")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {str(e)}")
        print("Some packages may not be installed correctly")
        return False
    except Exception as e:
        print(f"❌ Verification error: {str(e)}")
        return False


def show_next_steps():
    """Show next steps to the user"""
    print("\n🎯 Next Steps:")
    print("1. Edit the .env file with your IBM Watsonx AI credentials:")
    print("   - IBM_API_KEY: Your IBM Cloud API key")
    print("   - IBM_PROJECT_ID: Your Watsonx project ID")
    print("   - IBM_URL: Your Watsonx service URL")
    print()
    print("2. Test the installation:")
    print("   python test_studymate.py")
    print()
    print("3. Start the application:")
    print("   streamlit run app.py")
    print()
    print("📖 For detailed instructions, see README.md")


def main():
    """Main setup function"""
    print_banner()
    
    # Check Python version
    if not check_python_version():
        return False
    
    # Install dependencies
    if not install_dependencies():
        return False
    
    # Setup environment
    if not setup_environment():
        return False
    
    # Verify installation
    if not verify_installation():
        return False
    
    print("\n🎉 Setup completed successfully!")
    show_next_steps()
    
    return True


if __name__ == "__main__":
    success = main()
    if not success:
        print("\n❌ Setup failed. Please check the errors above and try again.")
        sys.exit(1)
    else:
        print("\n✅ StudyMate is ready to use!")
        sys.exit(0)
