.PHONY: build

lint:
	@pre-commit run --all-files
test:
	@python -m pytest

dev-docs:
	@source /opt/homebrew/opt/nvm/nvm.sh && nvm use && npm run dev

build-docs:
	@source /opt/homebrew/opt/nvm/nvm.sh && nvm use && npm run build
