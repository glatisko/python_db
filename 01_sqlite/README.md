
## Create SQLite DB, create table, insert and filter 
python3 01_create_insert_filter_data.py


## SQLAlchemy
### Set up a virtual env for SQLAlchemy
python3 -m venv sqlalchemy-workspace   
cd sqlalchemy-workspace\Scripts
activate
cd sqlalchemy-workspace
pip3 install sqlalchemy
deactivate

### Execute query with SQLAlchemy
cd sqlalchemy-workspace\Scripts
activate
python3 02_filter_sqlalchemy.py


## Import data from CSV file into a SQLite Table
python3 03_csv2sqlite.py

## Insert using SQLAlchemy
python3 04_insert_sqlalchemy.py