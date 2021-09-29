## First Time Set-Up (Development)

Install docker and docker-compose.

After cloning the repository, navigate to the same folder as the repository (ie `cd case-repository`) and simply run

```
docker-compose -f docker-compose.test.yml up --build -d
```

`-f docker-compose.test.yml` tells docker compose to use the development settings, as opposed to the production settings stored in `docker-compose.yml` (which would be used if you simpyl ran `docker-compose up --build`). The option `-d` tells docker to run the command without occupying your terminal (so you can run further commands).

There is no need to set any environmental variables (test environmental variables values are supplied in `docker-compose.test.yml` - note the production version instead *does* expect to read from a .env file) or to install any software - python, django, or postgres. 

Sample data must be loaded in separately, from `dump.sql`. The `install_dump.sh` script does this. Simply run `sh install_dump.sh`.

Sample data is loaded from dump.json (a Django fixture; the output of `django-admin dumpdata`). Python libraries needed are kept in requirements.txt (the output of `pip freeze`). To add new Python dependencies (or upgrade to a newer version), modify the requirements.txt with the name and version number of the library you wish to install (e.g. add a line `Django==3.2.6`)

## First Time Set-Up (Production)

Unlike in development, production uses a persistent database (not loaded from `dump.json`), and so postgres doesn't appear in the docker-compose and does need to be separately installed and set up. 

Then, a .env file needs to be created with all the correct values of the environmental variables (most database log in information, as well as a randomly generated Django secret key and the domain name of the production server; see `docker-compose.yml` for what environmental variables are expected). This needs to be placed in the topmost folder (ie, same folder as `docker-compose.yml`). Run

```
docker-compose up --build -d
```

To run the production server in headless mode (so you can close the terminal and it will continue running). This will hide the logs from you, so make sure to run `docker-compose logs` if you need to inspect if something went wrong. `docker-compose down` to shutdown the production server.

## Updating the schema and dump.sql

If there is a change in `model.py`, new migrations need to be added to `caseapi/migrations` and the `dump.sql` needs to be changed (for use on your local system). After running `docker-compose -f docker-compose.test.yml up -d --build`, (and installing the existing data dump via `sh install_dump.sh`) enter the docker container running django by running `docker exec -it django bash`. Within the container, run `python manage.py makemigrations` which should add the new migrations in the `caseapi/migrations` folder *of the container*. Then run `python manage.py migrate` for the migrations to be applied to the database.

Then, assuming the migration is called XXX_something.py, exit the docker container (ctrl+D usually) and run `docker cp django:/app/caseapi/migrations/XXX_something.py caseapi/migrations/` to copy the migration file over to your local system (where it can then be committed to the git repository). Finally, run `docker exec -it db pg_dump -a -U caseapi_test -d caserepo > dump.sql` to update the SQL dump with the migrated data. Note the `-a` flag tells `pg_dump` to only export the INSERT statements - constructing the tables is handled by `python manage.py migrate` and is not the responsibility of `dump.sql`.

## The Stack

Django is used to write the web application, and static files are served up within the docker container via `collectstatic`.

Gunicorn is a server which passes requests to the Django application (but it cannot handle static files)

Caddy is a reverse proxy which listens to ports :80 and :443, and serves up static files for all requests beginning with /static/ and otherwise passes requests to gunicorn (on an internal Docker network).

All three technologies are run off docker. Postgres is used for the database, and the Django application makes requests with the Postgres database using the environmental variables supplied.