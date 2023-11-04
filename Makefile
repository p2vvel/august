format:
	ruff . --fix
	isort .
	black .

test:
	pytest .