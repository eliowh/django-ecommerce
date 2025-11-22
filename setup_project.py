#!/usr/bin/env python
"""
Quick setup script for Django E-commerce Project
IT 403 WMAD - Elective 5 (WST 3)
Bulacan State University

This script automates the initial setup process for the project.
"""

import os
import sys
import subprocess
import platform

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n🔄 {description}...")
    try:
        if platform.system() == "Windows":
            result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        else:
            result = subprocess.run(command.split(), check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error in {description}: {e}")
        print(f"Command output: {e.output}")
        return False

def main():
    """Main setup function"""
    print("=" * 60)
    print("🚀 Django E-commerce Project Setup")
    print("IT 403 WMAD - Elective 5 (WST 3)")
    print("Bulacan State University")
    print("=" * 60)

    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("❌ Error: manage.py not found. Please run this script from the project root directory.")
        sys.exit(1)

    # Install dependencies
    if not run_command("python -m pip install --upgrade pip", "Upgrading pip"):
        sys.exit(1)
    
    if not run_command("python -m pip install -r requirements.txt", "Installing dependencies"):
        sys.exit(1)

    # Run migrations
    if not run_command("python manage.py migrate", "Running database migrations"):
        sys.exit(1)

    # Populate sample data
    if not run_command("python manage.py populate_sample_data", "Populating sample data"):
        print("⚠️  Warning: Sample data population failed. You can run it manually later.")

    # Final instructions
    print("\n" + "=" * 60)
    print("🎉 Setup completed successfully!")
    print("=" * 60)
    print("\n📋 Next Steps:")
    print("1. Run the development server:")
    print("   python manage.py runserver")
    print("\n2. Access the application:")
    print("   Main App: http://127.0.0.1:8000/")
    print("   Admin Panel: http://127.0.0.1:8000/admin/")
    print("\n🔑 Login Credentials:")
    print("   Admin: username=admin, password=admin123")
    print("   Customer: username=john_doe, password=testpass123")
    print("\n📚 Documentation:")
    print("   Check the docs/ directory for complete documentation")
    print("   README.md contains setup and usage instructions")
    print("\n✅ All IT 403 deliverables are ready for submission!")

if __name__ == "__main__":
    main()