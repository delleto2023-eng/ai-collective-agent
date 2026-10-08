#!/bin/bash
# AI Collective Agent - Quick Start Script

echo "======================================"
echo "AI Collective Agent - Starting..."
echo "======================================"

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    exit 1
fi

echo "Setting up virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing dependencies..."
pip install -q -r requirements.txt

echo ""
echo "======================================"
echo "Starting AI Collective Agent"
echo "======================================"
echo ""
echo "Dashboard: http://localhost:8000"
echo "API: http://localhost:8000/api"
echo ""
echo "Watching for request bubbles in current folder..."
echo ""

python -m agent
