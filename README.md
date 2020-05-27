# Travelperk University Backend Exercise

## Installation 

Latest image version can be retrieved directly from
the Github Docker repository.

First step is to authenticate with a personal
authentication token. The instruction are located in 
[Github's Documentation Site](https://help.github.com/es/packages/using-github-packages-with-your-projects-ecosystem/configuring-docker-for-use-with-github-packages).

Once authenticated run the following commands to run
the application in localhost port 8000

```shell
export IMAGE_NAME=docker.pkg.github.com/mpliego/travelperk-university-backend/backend:latest
docker pull $IMAGE_NAME
docker run -it -p 8000:8000 --rm $IMAGE_NAME run-migrate run
```

## Uses (with curl)

The following commands should be run with an empty database.

```shell
## Add new recipe
curl -X "POST" "http://127.0.0.1:8000/v1/recipe/" \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d $'{
  "name": "Recipe",
  "description": "Recipe Description"
}'
## Add new ingredient to recipe
curl -X "POST" "http://127.0.0.1:8000/v1/recipe/1/add-ingredient/" \
     -H 'Content-Type: application/json; charset=utf-8' \
     -d $'{
  "name": "Ingredient 1"
}'
## Renove ingredient from recipe
curl -X "DELETE" "http://127.0.0.1:8000/v1/ingredient/1/" \
     -H 'Content-Type: application/json; charset=utf-8'
```

## Development (with docker)

In the _"/src"_ directory run for each case:

### Run Tests

```shell
docker-compose run backend test 
```

### Run Django Migrations

```shell
## Generate migration files.
docker-compose run backend migration
## Run migration files into DB.
docker-compose run backend run-migrate 
```

### Start Django server

```shell
docker-compose up
## or
docker-compose run backend 
```

## Development (without docker)

In the _"/src"_ directory run for each case.

It is highly recommended to run the application inside a 
virtual environment some IDE helps in the creation and use
but in case it not available run the following commands to
create and run the venv:

```shell
python3 -m venv --clear .venv
source .venv/bin/activate
```

### Run Tests

```shell
make test 
```

### Run Django Migrations

```shell
## Generate migration files.
make migration
## Run migration files into DB.
make run-migrate 
```

### Start Django server

```shell
docker-compose up
## or
docker-compose run backend 
```