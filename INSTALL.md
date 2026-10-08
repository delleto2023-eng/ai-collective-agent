# Installation Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning)

## Quick Start

### On macOS/Linux:

```bash
cd ai-collective-agent
chmod +x run.sh
./run.sh
```

### On Windows:

```bash
cd ai-collective-agent
run.bat
```

### Manual Installation:

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows

# Install dependencies
pip install -r requirements.txt

# Run the agent
python -m agent
```

## Docker Installation

If you have Docker installed:

```bash
cd docker
docker-compose up
```

Then open http://localhost:8000

## Configuration

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your API keys:
   ```
   OPENAI_API_KEY=your_key_here
   ANTHROPIC_API_KEY=your_key_here
   GITHUB_TOKEN=your_token_here
   ```

## Verify Installation

Open your browser to:
- http://localhost:8000 - Web dashboard
- http://localhost:8000/api/health - API health check

## Troubleshooting

### Python not found
- Ensure Python 3.8+ is installed
- Add Python to your PATH

### Port 8000 already in use
- Edit `config/settings.py` and change `api_port`
- Or kill the process using port 8000

### Import errors
- Ensure virtual environment is activated
- Run `pip install -r requirements.txt` again

## Next Steps

1. Read [QUICK_START.md](docs/QUICK_START.md) to learn how to use the system
2. Check [ARCHITECTURE.md](docs/ARCHITECTURE.md) for technical details
3. Create your first request bubble in a folder
4. Monitor the results in real-time
