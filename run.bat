@echo off
REM AI Collective Agent - Quick Start Script for Windows

echo.
echo ======================================
echo AI Collective Agent - Starting...
echo ======================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo Setting up virtual environment...
python -m venv venv
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -q -r requirements.txt

echo.
echo ======================================
echo Starting AI Collective Agent
echo ======================================
echo.
echo Dashboard: http://localhost:8000
echo API: http://localhost:8000/api
echo.
echo Watching for request bubbles in current folder...
echo.

python -m agent
pause
