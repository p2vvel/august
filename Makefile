format:
	ruff . --fix
	isort .
	black .

test:
	pytest .


images:
	python -m august.main images -s ~/Obrazy/ -d ~/Obrazy/augmented -n 20

audio:
	python -m august.main audio -s ~/Muzyka/ -d ~/Muzyka/augmented -n 20

text:
	python -m august.main text -s ~/Dokumenty/ -d ~/Dokumenty/augmented -n 20
