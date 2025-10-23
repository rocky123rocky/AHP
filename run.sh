#!/bin/bash

# COPP AHP Military Planner - Run Script
# This script starts the Streamlit application

echo "=========================================="
echo "  COPP AHP Military Planner"
echo "  Advanced Planning System"
echo "=========================================="
echo ""

# Check if we're in the right directory
if [ ! -d "Ver 6 23 Oct 25 - for CI" ]; then
    echo "Error: Application directory not found!"
    echo "Please run this script from the AHP repository root."
    exit 1
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed!"
    echo "Please install Python 3.8 or higher."
    exit 1
fi

# Check if required packages are installed
echo "Checking dependencies..."
if ! python3 -c "import streamlit" 2>/dev/null; then
    echo "Installing required dependencies..."
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "Error: Failed to install dependencies!"
        echo "Please run: pip install -r requirements.txt"
        exit 1
    fi
fi

echo "Starting AHP application..."
echo ""
echo "Default Credentials:"
echo "  - Control PIN: 9999"
echo "  - Force PINs: 0000"
echo ""
echo "The application will open in your default browser."
echo "Press Ctrl+C to stop the server."
echo ""

# Change to application directory and run
cd "Ver 6 23 Oct 25 - for CI"
streamlit run app.py
