#!/usr/bin/env python3
"""
Verification script for COPP AHP Military Planner
This script checks if all dependencies and files are correctly set up.
"""

import sys
import os
from pathlib import Path

def print_header(text):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60)

def check_mark(success):
    """Return checkmark or X based on success"""
    return "✅" if success else "❌"

def verify_python_version():
    """Check Python version"""
    print_header("Checking Python Version")
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major == 3 and version.minor >= 8:
        print(f"{check_mark(True)} Python version is compatible (3.8+)")
        return True
    else:
        print(f"{check_mark(False)} Python 3.8 or higher required")
        return False

def verify_dependencies():
    """Check if required packages are installed"""
    print_header("Checking Dependencies")
    
    required_packages = {
        'streamlit': 'Streamlit',
        'plotly': 'Plotly',
        'pandas': 'Pandas',
        'openpyxl': 'OpenPyXL'
    }
    
    all_installed = True
    for package, name in required_packages.items():
        try:
            __import__(package)
            version = __import__(package).__version__
            print(f"{check_mark(True)} {name} is installed (version {version})")
        except ImportError:
            print(f"{check_mark(False)} {name} is NOT installed")
            all_installed = False
    
    if not all_installed:
        print("\nTo install missing dependencies, run:")
        print("  pip3 install -r requirements.txt")
    
    return all_installed

def verify_files():
    """Check if required files and directories exist"""
    print_header("Checking Files and Directories")
    
    required_items = {
        'Ver 6 23 Oct 25 - for CI': 'dir',
        'Ver 6 23 Oct 25 - for CI/app.py': 'file',
        'Ver 6 23 Oct 25 - for CI/ahp_backend.py': 'file',
        'Ver 6 23 Oct 25 - for CI/projects': 'dir',
        'requirements.txt': 'file',
        'run.sh': 'file',
        'README.md': 'file',
    }
    
    all_exist = True
    for item, item_type in required_items.items():
        path = Path(item)
        exists = path.exists()
        
        if item_type == 'dir':
            exists = exists and path.is_dir()
            item_desc = f"Directory: {item}"
        else:
            exists = exists and path.is_file()
            item_desc = f"File: {item}"
        
        print(f"{check_mark(exists)} {item_desc}")
        all_exist = all_exist and exists
    
    return all_exist

def verify_app_syntax():
    """Check if the main app has valid Python syntax"""
    print_header("Checking Application Syntax")
    
    app_path = Path('Ver 6 23 Oct 25 - for CI/app.py')
    
    if not app_path.exists():
        print(f"{check_mark(False)} app.py not found")
        return False
    
    try:
        import py_compile
        py_compile.compile(str(app_path), doraise=True)
        print(f"{check_mark(True)} app.py syntax is valid")
        return True
    except py_compile.PyCompileError as e:
        print(f"{check_mark(False)} app.py has syntax errors:")
        print(f"  {e}")
        return False

def verify_data_files():
    """Check if sample data files exist"""
    print_header("Checking Data Files")
    
    data_files = {
        'Ver 6 23 Oct 25 - for CI/forces.json': 'Forces configuration',
        'Ver 6 23 Oct 25 - for CI/ahp_team.json': 'Team information',
    }
    
    all_exist = True
    for file_path, description in data_files.items():
        path = Path(file_path)
        exists = path.exists() and path.is_file()
        print(f"{check_mark(exists)} {description}: {file_path}")
        all_exist = all_exist and exists
    
    # Check if projects directory has sample data
    projects_dir = Path('Ver 6 23 Oct 25 - for CI/projects')
    if projects_dir.exists():
        project_files = list(projects_dir.glob('*.json'))
        print(f"{check_mark(len(project_files) > 0)} Sample project data: {len(project_files)} project files found")
    
    return all_exist

def main():
    """Main verification function"""
    print("\n" + "🦉" * 30)
    print("  COPP AHP Military Planner - Setup Verification")
    print("  'To War With Wisdom'")
    print("🦉" * 30)
    
    results = []
    
    # Run all verifications
    results.append(("Python Version", verify_python_version()))
    results.append(("Dependencies", verify_dependencies()))
    results.append(("Files & Directories", verify_files()))
    results.append(("Application Syntax", verify_app_syntax()))
    results.append(("Data Files", verify_data_files()))
    
    # Summary
    print_header("Verification Summary")
    
    all_passed = True
    for name, passed in results:
        status = "PASSED" if passed else "FAILED"
        print(f"{check_mark(passed)} {name}: {status}")
        all_passed = all_passed and passed
    
    print("\n" + "=" * 60)
    
    if all_passed:
        print("✅ All checks passed! The application is ready to run.")
        print("\nTo start the application, run:")
        print("  ./run.sh        (Linux/Mac)")
        print("  run.bat         (Windows)")
        print("\nOr manually:")
        print("  cd 'Ver 6 23 Oct 25 - for CI'")
        print("  streamlit run app.py")
        print("\nDefault credentials:")
        print("  Control PIN: 9999")
        print("  Force PINs: 0000")
        return 0
    else:
        print("❌ Some checks failed. Please review the issues above.")
        print("\nCommon fixes:")
        print("  1. Install dependencies: pip3 install -r requirements.txt")
        print("  2. Ensure you're in the correct directory")
        print("  3. Check that all files were properly cloned")
        return 1

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\nVerification cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Unexpected error during verification: {e}")
        sys.exit(1)
