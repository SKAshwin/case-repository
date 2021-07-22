## First Time Set-Up (Development)

Install docker and docker-compose.

After cloning the repository, navigate to the same folder as the repository (ie `cd case-repository`) and simply run

```
docker-compose -f docker-compose.test.yml up --build
```

`-f docker-compose.test.yml` tells docker compose to use the development settings, as opposed to the production settings stored in `docker-compose.yml` (which would be used if you simpyl ran `docker-compose up --build`). 

There is no need to set any environmental variables (test environmental variables values are supplied in `docker-compose.test.yml` - note the production version instead *does* expect to read from a .env file) or to install any software - python, django, or postgres. 

Sample data is loaded from dump.json (a Django fixture; the output of `django-admin dumpdata`). Python libraries needed are kept in requirements.txt (the output of `pip freeze`). To add new Python dependencies (or upgrade to a newer version), modify the requirements.txt with the name and version number of the library you wish to install (e.g. add a line `Django==3.2.6`)

## First Time Set-Up (Production)

Unlike in development, production uses a persistent database (not loaded from `dump.json`), and so postgres doesn't appear in the docker-compose and does need to be separately installed and set up. 

Then, a .env file needs to be created with all the correct values of the environmental variables (most database log in information, as well as a randomly generated Django secret key and the domain name of the production server; see `docker-compose.yml` for what environmental variables are expected). This needs to be placed in the topmost folder (ie, same folder as `docker-compose.yml`). Run

```
docker-compose up --build -d
```

To run the production server in headless mode (so you can close the terminal and it will continue running). This will hide the logs from you, so make sure to run `docker-compose logs` if you need to inspect if something went wrong. `docker-compose down` to shutdown the production server.

## The Stack

Django is used to write the web application, and static files are served up within the docker container via `collectstatic`.

Gunicorn is a server which passes requests to the Django application (but it cannot handle static files)

Caddy is a reverse proxy which listens to ports :80 and :443, and serves up static files for all requests beginning with /static/ and otherwise passes requests to gunicorn (on an internal Docker network).

All three technologies are run off docker. Postgres is used for the database, and the Django application makes requests with the Postgres database using the environmental variables supplied.