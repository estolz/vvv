# VVV

## Setup
* Navigate to vvv -> create venv using
* ```python -m virtualenv --python C:\Path\To\Python\python.exe venv```
* Activate venv
* Install packages using ``` pip install -r requirements.txt```
* Create .env file on manage.py level and copy environment variables from existing file elsewhere
* Create admin user with ```python manage.py createsuperuser```

## Restore DB
* Place bench.csv on manage.py level
* ```python manage.py bench_from_csv --path bench.csv```

## Maintenance
* Get outdated packages with ```pip list --outdated```
* Update files in requirements.txt

## Deploy
* Go to console and run ```source env/bin/activate```
* Navigate to vvv with ```cd vvv```
* Pull changes with ```git pull```
* If there have been updates to requirements.txt run ```pip install -r VVV/requirements.txt```