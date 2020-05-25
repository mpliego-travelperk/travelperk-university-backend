DOCKER_IMAGE_NAME ?= travelperk-university-backend
APP_PORT ?= 8000
.DEFAULT_GOAL := help
.PHONY: help

test: ## Runs project tests.
	python3 manage.py test

run: ## Starts django server and listen to port `{APP_PORT}` or `8000`.
	python3 manage.py runserver 0.0.0.0:$(APP_PORT)

build-migrations: ## Builds db migrations.
	python3 manage.py makemigrations

migrate: ## Runs db migrations to the database.
	python3 manage.py migrate

docker: ## Builds the docker image with tag `{DOCKER_IMAGE_NAME}` or `travelperk-university-backend`
	docker build -t $(DOCKER_IMAGE_NAME) .

# Godly script by: https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help: ## Prints this page.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
