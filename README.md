# VVV

## Setup
* navigate to vvv -> create venv using
* ```python -m virtualenv --python C:\Path\To\Python\python.exe venv```
* activate venv
* install packages using ``` pip install -r requirements.txt```
* create .env file on manage.py level and copy environment variables from existing file elsewhere
* Create admin user with ```python manage.py createsuperuser```

## Restore DB
* place bench.csv on manage.py level
* python manage.py bench_from_csv --path bench.csv

## Maintenance
* Get outdated packages with ```pip list --outdated```
* Update files in requirements.txt