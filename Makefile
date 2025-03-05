.DEFAULT_GOAL := help

test-python: ## Run tests on Python files.
	@echo "---> running python tests"
	tox p

.PHONY: lint
lint: ## Lint code.
	pre-commit run -a

.PHONY: test
test: lint test-python

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
