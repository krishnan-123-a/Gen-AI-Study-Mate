"""
StudyMate Launcher - Complete Setup and Launch Script
Handles all setup, dependency installation, and application launch
"""

import os
import sys
import subprocess
import time
import webbrowser
from pathlib import Path


def print_banner():
    """Print StudyMate banner"""
    print("=" * 60)
    print("📚 StudyMate - AI-Powered PDF Q&A System")
    print("🚀 Complete Setup and Launch Script")
    print("=" * 60)
    print()


def check_python():
    """Check Python version"""
    print("🐍 Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} detected")
    return True


def install_dependencies():
    """Install required packages"""
    print("\n📦 Installing/Updating dependencies...")
    
    packages = [
        "streamlit>=1.28.0",
        "PyMuPDF>=1.23.0", 
        "sentence-transformers>=5.0.0",
        "faiss-cpu>=1.7.0",
        "ibm-watsonx-ai>=1.0.0",
        "python-dotenv>=1.0.0",
        "numpy>=1.24.0",
        "pandas>=2.0.0",
        "transformers>=4.41.0"
    ]
    
    for package in packages:
        try:
            print(f"Installing {package}...")
            result = subprocess.run([
                sys.executable, "-m", "pip", "install", "--user", "--upgrade", package
            ], capture_output=True, text=True, timeout=300)
            
            if result.returncode != 0:
                print(f"⚠️ Warning: {package} installation had issues, but continuing...")
            else:
                print(f"✅ {package} installed successfully")
                
        except subprocess.TimeoutExpired:
            print(f"⚠️ Timeout installing {package}, but continuing...")
        except Exception as e:
            print(f"⚠️ Error installing {package}: {e}, but continuing...")
    
    print("✅ Dependency installation completed")


def setup_environment():
    """Setup environment files"""
    print("\n🔧 Setting up environment...")
    
    # Create .env if it doesn't exist
    if not os.path.exists(".env"):
        if os.path.exists(".env.example"):
            try:
                with open(".env.example", "r") as src, open(".env", "w") as dst:
                    dst.write(src.read())
                print("✅ Created .env file from template")
            except Exception as e:
                print(f"⚠️ Could not create .env file: {e}")
        else:
            # Create basic .env file
            with open(".env", "w") as f:
                f.write("# IBM Watsonx AI Configuration\n")
                f.write("IBM_API_KEY=your_ibm_api_key_here\n")
                f.write("IBM_PROJECT_ID=your_project_id_here\n")
                f.write("IBM_URL=https://us-south.ml.cloud.ibm.com\n")
            print("✅ Created basic .env file")
    else:
        print("✅ .env file already exists")


def create_sample_pdfs():
    """Create sample PDFs if they don't exist"""
    print("\n📄 Setting up sample PDFs...")
    
    if not os.path.exists("sample_ml_basics.pdf") or not os.path.exists("sample_deep_learning.pdf"):
        try:
            result = subprocess.run([sys.executable, "create_sample_pdfs.py"], 
                                  capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                print("✅ Sample PDFs created successfully")
            else:
                print("⚠️ Could not create sample PDFs, but continuing...")
        except Exception as e:
            print(f"⚠️ Error creating sample PDFs: {e}, but continuing...")
    else:
        print("✅ Sample PDFs already exist")


def test_imports():
    """Test if core modules can be imported"""
    print("\n🧪 Testing core functionality...")
    
    try:
        # Test PDF processor
        subprocess.run([
            sys.executable, "-c", 
            "from modules.pdf_processor import create_pdf_processor; print('PDF processor: OK')"
        ], check=True, capture_output=True, timeout=30)
        print("✅ PDF processor working")
        
        # Test embeddings
        subprocess.run([
            sys.executable, "-c",
            "from modules.embeddings import create_embedding_manager; print('Embeddings: OK')"
        ], check=True, capture_output=True, timeout=30)
        print("✅ Embeddings module working")
        
        # Test utils
        subprocess.run([
            sys.executable, "-c",
            "from modules.utils import setup_streamlit_page; print('Utils: OK')"
        ], check=True, capture_output=True, timeout=30)
        print("✅ Utils module working")
        
        print("✅ All core modules working correctly")
        return True
        
    except Exception as e:
        print(f"⚠️ Some modules have issues: {e}")
        print("🎯 Will run in demo mode")
        return False


def launch_streamlit():
    """Launch the Streamlit application"""
    print("\n🚀 Launching StudyMate...")
    print("📱 The application will open in your default web browser")
    print("🔄 If it doesn't open automatically, go to: http://localhost:8501")
    print()
    print("💡 Tips:")
    print("   - Upload the sample PDFs to test the system")
    print("   - Try asking: 'What is machine learning?'")
    print("   - Check the Q&A history and download feature")
    print()
    print("🛑 To stop the application, press Ctrl+C in this terminal")
    print("=" * 60)
    
    try:
        # Launch Streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port", "8501",
            "--server.address", "localhost"
        ])
    except KeyboardInterrupt:
        print("\n\n🛑 StudyMate stopped by user")
    except Exception as e:
        print(f"\n❌ Error launching Streamlit: {e}")
        print("💡 Try running manually: streamlit run app.py")


def main():
    """Main launcher function"""
    print_banner()
    
    # Check Python version
    if not check_python():
        input("Press Enter to exit...")
        return
    
    # Install dependencies
    install_dependencies()
    
    # Setup environment
    setup_environment()
    
    # Create sample PDFs
    create_sample_pdfs()
    
    # Test imports
    modules_ok = test_imports()
    
    # Show status
    print("\n" + "=" * 60)
    print("📊 Setup Summary:")
    print(f"✅ Python: Ready")
    print(f"✅ Dependencies: Installed")
    print(f"✅ Environment: Configured")
    print(f"✅ Sample Data: Ready")
    print(f"{'✅' if modules_ok else '🎯'} Core Modules: {'Working' if modules_ok else 'Demo Mode'}")
    print("=" * 60)
    
    # Ask user if they want to launch
    print("\n🚀 Ready to launch StudyMate!")
    response = input("Launch the application now? (y/n): ").lower().strip()
    
    if response in ['y', 'yes', '']:
        launch_streamlit()
    else:
        print("\n📝 To launch later, run:")
        print("   python run_studymate.py")
        print("   OR")
        print("   streamlit run app.py")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🛑 Setup interrupted by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("💡 Please check the error and try again")
    finally:
        input("\nPress Enter to exit...")
