.PHONY: help install run dev clean test

help:
	@echo "AI Collective Agent - Available Commands"
	@echo ""
	@echo "  make install   - Install dependencies"
	@echo "  make run       - Run the agent"
	@echo "  make dev       - Run with debug mode"
	@echo "  make clean     - Remove virtual environment and cache"
	@echo "  make test      - Run tests"

install:
	python -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

run:
	. venv/bin/activate && python -m agent

dev:
	. venv/bin/activate && DEBUG=true python -m agent

clean:
	rm -rf venv __pycache__ .pytest_cache .memory

test:
	. venv/bin/activate && python -m pytest tests/
