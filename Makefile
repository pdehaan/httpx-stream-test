main:
		uv run main.py

format: lint
		uv format

lint:
		uvx ruff check
