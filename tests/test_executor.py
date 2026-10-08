"""Tests for folder executor."""

import asyncio
import json
import pytest
import tempfile
from pathlib import Path
from agent.executor import FolderExecutor, RequestBubble
from agent.orchestrator import Orchestrator


@pytest.fixture
async def executor():
    """Create an executor instance."""
    orch = Orchestrator()
    await orch.initialize()
    return FolderExecutor(orch)


def test_request_bubble_loading():
    """Test request bubble loads metadata correctly."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump({"request": "Test request", "priority": 1}, f)
        f.flush()
        
        bubble = RequestBubble(Path(f.name))
        assert bubble.get_task_description() == "Test request"
        assert bubble.get_priority() == 1
        
        Path(f.name).unlink()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
