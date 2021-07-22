## First Time Set-Up (Development)

Install docker and docker-compose.

After cloning the repository, navigate to the same folder as the repository (ie `cd case-repository`) and simply run

```
docker-compose -f docker-compose.test.yml up --build
```

`-f docker-compose.test.yml` tells docker compose to use the development settings, as opposed to the production settings stored in `docker-compose.yml` (which would be used if you simpyl ran `docker-compose up --build`). 

There is no need to set any environmental variables (test environmental variables values are supplied in `docker-compose.test.yml` - note the production version instead *does* expect to read from a .env file) or to install any software - python, django, or postgres. 

Sample data is loaded from dump.json (a Django fixture; the output of `django-admin dumpdata`). Python libraries needed are kept in requirements.txt (the output of `pip freeze`).

### Adding New Python Dependencies

If you want to change the requirements.txt, it can be useful to have a virtual environment, pip install all existing requirement from the file, pip install the new requirements, and run pip freeze.

```
python3 -m venv venv
```

To set up a virtual environment for the first time, which will be ignored by git.

Then

```
pip install -r requirements.txt
pip install <DESIREDNEWDEPENDENCY>
pip freeze > requirements.txt
```

Alternatively, just directly edit the requirements.txt.