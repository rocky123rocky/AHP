@echo off
REM COPP AHP Military Planner - Run Script for Windows
REM This script starts the Streamlit application

echo ==========================================
echo   COPP AHP Military Planner
echo   Advanced Planning System
echo ==========================================
echo.

REM Check if we're in the right directory
if not exist "Ver 6 23 Oct 25 - for CI" (
    echo Error: Application directory not found!
    echo Please run this script from the AHP repository root.
    pause
    exit /b 1
)

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH!
    echo Please install Python 3.8 or higher.
    pause
    exit /b 1
)

REM Check if required packages are installed
echo Checking dependencies...
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo Installing required dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo Error: Failed to install dependencies!
        echo Please run: pip install -r requirements.txt
        pause
        exit /b 1
    )
)

echo Starting AHP application...
echo.
echo Default Credentials:
echo   - Control PIN: 9999
echo   - Force PINs: 0000
echo.
echo The application will open in your default browser.
echo Press Ctrl+C to stop the server.
echo.

REM Change to application directory and run
cd "Ver 6 23 Oct 25 - for CI"
streamlit run app.py
