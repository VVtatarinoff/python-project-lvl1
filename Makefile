install:
	poetry install
brain-games:
	poetry run brain-games
brain-calc:
	poetry run brain-calc
brain-even:
	poetry run brain-even
brain-progression:
	poetry run brain-progression
brain-prime:
	poetry run brain-prime
brain-gcd:
	poetry run brain-gcd
build:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
package-uninstall:
	python3 -m pip uninstall hexlet-code
lint:
	poetry run flake8 brain_games
.PHONY: install brain-games build publish package-install
