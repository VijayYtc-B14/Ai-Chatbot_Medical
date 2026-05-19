@echo off
REM MediCare AI - Quick Start Script for Windows
REM This script helps you get started with MediCare AI

echo.
echo ==========================================
echo   MediCare AI - Quick Start Script
echo ==========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.11+ from https://python.org
    pause
    exit /b 1
)

echo [OK] Python is installed

REM Check if venv exists
if not exist venv (
    echo.
    echo Creating virtual environment...
    python -m venv venv
    echo [OK] Virtual environment created
) else (
    echo [OK] Virtual environment already exists
)

REM Activate virtual environment
echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo [OK] Virtual environment activated

REM Install requirements
echo.
echo Installing dependencies...
pip install -q -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)
echo [OK] Dependencies installed

REM Verify setup
echo.
echo Verifying setup...
python verify_setup.py
if %errorlevel% neq 0 (
    echo.
    echo Some checks failed. Please review the errors above.
    echo.
    echo Common fixes:
    echo 1. Check that .env file exists and has API keys
    echo 2. Run: pip install -r requirements.txt
    echo 3. Verify Python version: python --version (needs 3.11+)
    pause
    exit /b 1
)

REM Start the app
echo.
echo ==========================================
echo   Starting MediCare AI...
echo ==========================================
echo.
echo The app will open at: http://localhost:8501
echo.
echo Press Ctrl+C in the terminal to stop the app
echo.
pause

streamlit run app.py

pause
