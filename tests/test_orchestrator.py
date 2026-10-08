"""Tests for orchestrator."""

import asyncio
import pytest
from agent.orchestrator import Orchestrator, Task


@pytest.fixture
async def orchestrator():
    """Create an orchestrator instance."""
    orch = Orchestrator()
    await orch.initialize()
    return orch


@pytest.mark.asyncio
async def test_orchestrator_initialization(orchestrator):
    """Test orchestrator initializes correctly."""
    assert orchestrator is not None
    assert isinstance(orchestrator.tasks, dict)


@pytest.mark.asyncio
async def test_task_execution(orchestrator):
    """Test task execution."""
    task = Task(
        id="test-1",
        description="Test task",
        priority=1
    )
    
    result = await orchestrator.execute_task(task)
    assert result is not None
    assert task.status in ["completed", "failed"]


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
