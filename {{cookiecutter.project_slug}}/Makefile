install-poetry:
	@if ! python -c "import poetry" &> /dev/null; then \
		pip install poetry; \
	fi

install-common-deps: install-poetry
	poetry install --no-dev

install-deps: install-poetry
	poetry install

test: install-deps
	poetry run src/manage.py test

lint: install-deps
	echo $(which python)
	poetry run flake8 src

bandit: install-deps
	poetry run bandit src

isort: install-deps
	poetry run isort src

black: install-deps
	poetry run black src

mypy: install-deps
	poetry run mypy src


format-source-code: isort black

analyze-source-code: lint bandit mypy
