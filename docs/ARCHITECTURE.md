# AI Collective Agent Architecture

## Overview

A modular, self-executing AI framework that:
- Coordinates multiple AI models
- Learns from task execution
- Connects to any external program
- Auto-executes from folder request bubbles

## Core Components

### 1. Orchestrator (`agent/orchestrator.py`)
Central decision-maker that:
- Routes tasks to appropriate AI models
- Manages execution pipeline
- Coordinates with external programs
- Triggers learning from results

### 2. Folder Executor (`agent/executor.py`)
Monitors designated folders for "request bubbles" (special JSON files) and:
- Detects `.request.json` files
- Parses task specifications
- Executes through the orchestrator
- Writes results back to the folder
- Auto-cleans up after execution

### 3. Model Abstraction Layer (`agent/models/`)
Unified interface for multiple AI providers:
- OpenAI models
- Anthropic models
- Local models
- Custom models

Each model implements:
- `initialize()` - setup
- `infer()` - single inference
- `stream()` - streaming results
- `get_capabilities()` - list features

### 4. Memory System (`agent/memory/`)

#### Short-Term Memory
- Current task context
- Session state
- Auto-expires after inactivity
- Cleared between sessions

#### Long-Term Memory
- Past task results
- Learned patterns
- Model performance ratings
- Tool effectiveness scores
- Persistent on disk

### 5. Tool System (`agent/tools/`)

#### Tool Registry
- Centralized tool management
- Tool discovery and listing
- Capability matching

#### Tool Executor
- Executes tools with error handling
- Logs execution results
- Supports:
  - API calls
  - CLI commands
  - Local scripts
  - Database queries
  - File operations

### 6. Connector Framework (`agent/connectors/`)
Universal interface for external programs:

```python
class BaseConnector:
    - initialize()        # Setup connection
    - authenticate()      # Authenticate if needed
    - list_capabilities() # What can it do?
    - execute_action()    # Run an action
    - read_data()         # Read state
    - write_data()        # Modify state
    - handle_error()      # Error recovery
```

## Request Bubble System (Self-Execution)

### How It Works

1. **User Creates Request Bubble**
   ```json
   // folder/.request.json
   {
     "request": "Analyze this data and create a report",
     "priority": 1,
     "context": {...}
   }
   ```

2. **Folder Watcher Detects File**
   - FolderWatcher (watchdog) detects new/modified `.request.json`
   - Triggers `execute_from_bubble()`

3. **Orchestrator Processes Task**
   - Task created with UUID
   - Model selected based on task type
   - Execution begins
   - Memory loads context

4. **Task Completes**
   - Result written to `.result-{task_id}.json`
   - Learning recorded in long-term memory
   - Bubble file cleaned up

5. **User Sees Results**
   - Result file appears in same folder
   - File contains task output and status

## Execution Flow

```
Request Bubble Created
    ↓
Folder Watcher Detects
    ↓
FolderExecutor.execute_from_bubble()
    ↓
Orchestrator.execute_task()
    ↓
┌─ Select Model
│  └─ Use learned preferences
├─ Prepare Context
│  └─ Load memory, tools, connectors
├─ Execute
│  ├─ Model inference
│  ├─ Tool execution
│  └─ Connector calls
├─ Gather Results
└─ Learn & Store
   ├─ Rate model performance
   ├─ Update patterns
   └─ Save to long-term memory
    ↓
Write Result File
    ↓
Cleanup Bubble
```

## Task Lifecycle

```
Task States:
  pending → running → completed/failed

Task Data:
  {
    id: UUID,
    description: str,
    priority: int,
    status: "pending" | "running" | "completed" | "failed",
    created_at: datetime,
    result: dict (on completion),
    error: str (on failure)
  }
```

## Learning System

The agent improves through:

1. **Model Rating**
   - Track accuracy for task types
   - Prefer high-performing models
   - Fallback to less-preferred if needed

2. **Pattern Learning**
   - Identify recurring task patterns
   - Store successful strategies
   - Reuse patterns for similar tasks

3. **Tool Effectiveness**
   - Rate tools by success rate
   - Prefer reliable tools
   - Detect tool failures

4. **Connector Optimization**
   - Track connector reliability
   - Cache successful operations
   - Learn retry strategies

## API Endpoints

```
POST   /api/tasks                 - Create and execute task
GET    /api/tasks/{id}            - Get task status
GET    /api/tasks                 - List all tasks
GET    /api/folders/results       - Get all folder results
GET    /api/folders/results/{id}  - Get specific folder result
GET    /api/health                - Health check
```

## Configuration

Environment variables (`.env`):
- `OPENAI_API_KEY` - OpenAI access
- `ANTHROPIC_API_KEY` - Claude access
- `GITHUB_TOKEN` - GitHub integration
- `SLACK_BOT_TOKEN` - Slack integration
- `WATCH_FOLDERS` - Folders to monitor
- `MEMORY_STORAGE_PATH` - Memory storage location

## Extending the System

### Add a New Connector
```python
class MyConnector(BaseConnector):
    async def initialize(self): ...
    async def authenticate(self, creds): ...
    async def list_capabilities(self): ...
    async def execute_action(self, action, params): ...
    # etc.
```

### Add a New Model
```python
class MyModel(BaseModel):
    async def initialize(self): ...
    async def infer(self, prompt, context): ...
    async def stream(self, prompt, context): ...
```

### Register a New Tool
```python
async def my_tool(param1, param2):
    # Implementation
    return result

registry.register_tool(
    "my_tool",
    "Description of what it does",
    my_tool,
    {"param1": "type", "param2": "type"}
)
```

## Future Enhancements

- [ ] Agent collaboration (swarm orchestration)
- [ ] Federated learning across agents
- [ ] Advanced pattern recognition
- [ ] Self-modifying code generation
- [ ] Distributed execution
- [ ] Web UI for task management
- [ ] Real-time monitoring dashboard
- [ ] Advanced error recovery
- [ ] Cost optimization
- [ ] Multi-language support
