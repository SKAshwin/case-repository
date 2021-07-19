## First Time Set-Up

After cloning the repository, navigate to the same folder as the repository (ie `cd case-repository`) and run

```
python3 -m venv venv
```

This creates a python virtual environment. 

Before running any files (at any time - not just first set up), make sure to run

```
source venv/bin/activate
```

This activates the virtual environment. 

After activating the virtual environment, install the required python dependencies by running 

```
pip install -r requirements.txt
```

You will also need to do this after every git pull, if someone else changed the dependencies since your last pull.

If you ever pip-install another dependency, update the requirements.txt file by running

```
pip freeze
```

To run the development server on port 8000 of your current system,
run

```
python manage.py runserver
```