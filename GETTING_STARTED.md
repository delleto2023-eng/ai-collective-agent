# Getting Started with AI Collective Agent

## What is This?

AI Collective Agent is a **self-executing AI orchestration system** that:
- Monitors folders for task requests ("request bubbles")
- Routes tasks to multiple AI models
- Learns from execution to improve over time
- Connects to any external program or API
- Automatically runs tasks and writes results back to folders

## The Core Idea

Instead of manually running AI tasks, you:
1. Create a task folder
2. Drop a request file (`.request.json`)
3. The system auto-detects it, runs it, and saves results
4. You review the results in the same folder

## Start Here

### 1. Install

**Windows:**
```bash
run.bat
```

**macOS/Linux:**
```bash
./run.sh
```

### 2. Open Dashboard

Go to: http://localhost:8000

### 3. Create Your First Request Bubble

Create a folder anywhere on your computer:
```bash
mkdir my-ai-tasks
cd my-ai-tasks
```

Create a file named `.request.json`:
```json
{
  "request": "Analyze this folder and suggest the next best action",
  "priority": 1
}
```

### 4. Watch It Execute

The system will:
- Detect the `.request.json` file
- Process the request
- Write results to `.result-{task-id}.json`
- Clean up the request file

You can view the result immediately in the same folder.

## API Endpoints

You can also submit tasks via the API:

```bash
curl -X POST http://localhost:8000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"description": "Summarize this project", "priority": 1}'
```

## How It Works

```
You create a request bubble (.request.json)
         ↓
Folder watcher detects it
         ↓
Orchestrator chooses best AI model
         ↓
Task executes with tools & connectors
         ↓
System learns from results
         ↓
Results written to .result-{id}.json
         ↓
You view the results
```

## Configuration

Edit `.env` to add API keys:

```bash
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GITHUB_TOKEN=ghp_...
```

## System Architecture

- **Orchestrator**: Decides which AI to use for each task
- **Models**: Multiple AI providers (OpenAI, Anthropic, local)
- **Memory**: Learns from past executions
- **Tools**: Perform actions (file operations, API calls, etc.)
- **Connectors**: Integrate with external programs
- **Watcher**: Monitors folders for request bubbles

## Examples

### Example 1: Code Review

```json
{
  "request": "Review the code in this folder and provide feedback",
  "priority": 2,
  "context": {
    "file_types": ["py", "js"],
    "focus_on": "performance"
  }
}
```

### Example 2: Data Analysis

```json
{
  "request": "Analyze the data.csv file and create a summary report",
  "priority": 1
}
```

### Example 3: Project Planning

```json
{
  "request": "Read the README and propose a development roadmap",
  "priority": 1
}
```

## Next Steps

1. **Read the docs**: Check `docs/` folder for detailed guides
2. **Explore the code**: Browse `agent/` to understand the system
3. **Add connectors**: Integrate with your favorite tools (Slack, GitHub, etc.)
4. **Customize models**: Swap in your preferred AI providers
5. **Build automations**: Create workflows that auto-execute

## Troubleshooting

**Not detecting request bubbles?**
- Ensure file is named `.request.json`
- Check that the folder is being watched (see `.env` WATCH_FOLDERS)
- Review logs in the terminal

**API not responding?**
- Check http://localhost:8000/api/health
- Verify port 8000 is not in use
- Check your firewall settings

**Results not being generated?**
- Verify API keys are set in `.env`
- Check the web dashboard for task status
- Review the server logs

## Support

- **Documentation**: See `docs/` folder
- **Issues**: Report on GitHub
- **Examples**: Check `examples/` folder
