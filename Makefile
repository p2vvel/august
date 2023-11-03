format:
	ruff . --fix
	black .

test:
	pytest .