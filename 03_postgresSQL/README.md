# Install / configure
## Download latest PostgresSQL
## Add to path
nano .zshrc  
export PATH=${PATH}:/Library/PostgresSQL/15/bin  
source .zshrc  
## Login/Create DB
psql -U postgres
CREATE DATABASE red30;
## To list databases
\l
## To connect to database
\c red30;
## To See tables
\dt
## Create Venv and install dependencies
python3 -m venv postgres-workspace
cd postgres-workspace
activate
pip3 install psycopg2-binary

# Connect/create/insert into table 
python3 01_insert_tuple.py

# Insert via dictionary
python3 02_insert_dynamic.py




