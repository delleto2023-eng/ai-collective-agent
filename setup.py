from setuptools import setup, find_packages

setup(
    name="ai-collective-agent",
    version="0.1.0",
    description="Self-executing AI agent that learns automatically and connects to any program",
    author="delleto2023-eng",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "fastapi==0.104.1",
        "uvicorn==0.24.0",
        "pydantic==2.5.0",
        "pydantic-settings==2.1.0",
        "watchdog==3.0.0",
        "aiofiles==23.2.1",
        "httpx==0.25.2",
        "openai==1.3.0",
        "anthropic==0.8.0",
        "python-dotenv==1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "ai-agent=agent.main:run",
        ],
    },
)
