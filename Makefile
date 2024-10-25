.PHONY: build

lint:
	@pre-commit run --all-files
test:
	@python -m pytest
