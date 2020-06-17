DOCKER_IMAGE_NAME ?= travelperk-university-backend
APP_PORT ?= 8000
.DEFAULT_GOAL := help
.PHONY: help

dep: ## Runs linting test to the code.
	pip3 install -r requirements.txt

lint: ## Runs linting test to the code.
	flake8 .

test: ## Runs project tests.
	python3 manage.py test

validate: lint test ## Run linting and unit tests.

run: ## Starts django server and listen to port `{APP_PORT}` or `8000`.
	python3 manage.py runserver 0.0.0.0:$(APP_PORT)

run-migrate: ## Runs db migrations to the database.
	python3 manage.py migrate

migration: ## Builds db migrations.
	python3 manage.py makemigrations

docker: ## Builds the docker image with tag `{DOCKER_IMAGE_NAME}` or `travelperk-university-backend`
	docker build -t $(DOCKER_IMAGE_NAME) .

docker-test: docker ## Builds docker image (see docker target) and run tests.
	docker run -t $(DOCKER_IMAGE_NAME) validate

docker-push: ## Tags and pushes with the required name:tag `{DOCKER_REMOTE_IMAGE}`.
	docker tag $(DOCKER_IMAGE_NAME) $(DOCKER_REMOTE_IMAGE)
	docker push $(DOCKER_REMOTE_IMAGE)

sh: ## Starts sh session(for docker debugging).
	@sh

# Godly script by: https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help: ## Prints this page.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
