# Travelperk University Backend Exercise

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

In the _"/src"_ directory run for each case:

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