# Movie List

[![Build Status](https://travis-ci.com/bighelmet7/sennder.svg?token=qVuyqSjnTjTxdCoTkHDd&branch=master)](https://travis-ci.com/bighelmet7/immfly)    [![codecov](https://codecov.io/gh/bighelmet7/sennder/branch/master/graph/badge.svg)](https://codecov.io/gh/bighelmet7/sennder)

# Challenge

- Develop a Python application which serves a page on localhost:8000/movies/. This page should contain a plain list of all movies from the Ghibli API. For each movie the people that appear in it should be listed.
- Don’t have to worry about the styling of that page.
- The information on the page is not older than 1 minute when the page is loaded.

### Requirements

- git
- Docker and docker-compose

### Installation

```bash
git clone https://github.com/bighelmet7/sennder.git
cd sennder/
docker-compose build
docker-compose up # the application is configured for a DevelopmentConfig environment.
```

### TODO

- codecov badge ✅ 
- travis CI ✅ 
- https for api and web
- API test
- Worker test

### Stack

- Python 3.8
- Celery 4.4.7
- RabbitMQ (latest docker version)
- PostgreSQL (latest docker version)
- NodeJS (latest docker version) Also see the web/package.json for a more detail information about the packages.

### Structure
Main project
```text
+-----------------+     +-------------+   +---------+   +-------------------+    +------------+
|Studio Ghibli|API+---->+Celery Worker+-->+Database <--->API|/api/v1/movies/<---->Web|/movies |
+-----------------+     +-------------+   +---------+   +-------------------+    +------------+
```
It is based in a Celery worker that every minute is fetching the Studio Ghibli API and writting into the configured Database **(Caution: SQLite could perfom IntegrityError use it only in TestingConfig)**. In the other side we have the API service that is reading all the information from the Database. This service gets the Film and People models and merge them into a JSON response.

Finally the Web service will perfom every 3 seconds a GET request to /api/v1/movies, so the user can feel a real time application.

API: http://localhost:5000/api/v1/movies
Web: http://localhost:8000/

### Models

First of all it is worth mention that Film and People models are not complete (compare to the information stored in Studio Ghibli DB). The worker is requesting the necessary information for both objects.

- Film contains an ID, title and a backref to People called _peoples_
- People contains an ID, name and a list of Film called _films_
- movies it is a through table to have a many to many relation between Film and People.

### Test and Styling
Tests
```bash
python -m unittest
```

PEP8
```bash
pycodestyle --filename='*.py' --exclude='migrations/' .
```

### Others

- Avoiding the celery worker test: it does not return any value; the main task is to write into our database, so if a test is needed (because of specifications) we can create a dumb database and write into it.
