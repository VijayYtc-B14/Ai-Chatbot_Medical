#!/bin/bash
# MediCare AI - Quick Start Script for macOS/Linux
# This script helps you get started with MediCare AI

echo ""
echo "=========================================="
echo "  MediCare AI - Quick Start Script"
echo "=========================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is not installed"
    echo "Please install Python 3.11+ from https://python.org"
    exit 1
fi

echo "[OK] Python is installed: $(python3 --version)"

# Check if venv exists
if [ ! -d "venv" ]; then
    echo ""
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "[OK] Virtual environment created"
else
    echo "[OK] Virtual environment already exists"
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source venv/bin/activate
echo "[OK] Virtual environment activated"

# Install requirements
echo ""
echo "Installing dependencies..."
pip install -q -r requirements.txt
if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to install dependencies"
    exit 1
fi
echo "[OK] Dependencies installed"

# Verify setup
echo ""
echo "Verifying setup..."
python verify_setup.py
if [ $? -ne 0 ]; then
    echo ""
    echo "Some checks failed. Please review the errors above."
    echo ""
    echo "Common fixes:"
    echo "1. Check that .env file exists and has API keys"
    echo "2. Run: pip install -r requirements.txt"
    echo "3. Verify Python version: python3 --version (needs 3.11+)"
    exit 1
fi

# Start the app
echo ""
echo "=========================================="
echo "  Starting MediCare AI..."
echo "=========================================="
echo ""
echo "The app will open at: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the app"
echo ""

streamlit run app.py
