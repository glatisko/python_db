
## How to Install MySQL and Python connector
Download MySQL community edition
### add to path - to see which shell are we running:
echo $SHELL  
nano .zshrc  
export PATH=${PATH}:/usr/local/mysql/bin  
source .zshrc  

###  Create virtual env and DB Connector 
python3 -m venv mysql-workspace  
cd mysql-workspace  
activate  
pip3 install mysql-connector-python  


### Create  DB and depdendent tables via MySQL shell:
sudo mysql -u root -p      
mysql>CREATE DATABASE projects;  
mysql> use projects;  
mysql> CREATE TABLE projects (project_id INT(11) NOT NULL AUTO_INCREMENT, title VARCHAR(30), description VARCHAR(255),  
PRIMARY KEY(project_id);  
mysql> CREATE TABLE tasks (tasks_id INT(11) NOT NULL AUTO_INCREMENT, project_id INT(11) NOT NULL, description VARCHAR(255),  
PRIMARY KEY(task_id),  
FOREIGN KEY (project_id) REFERENCES projects(project_id));  
mysql> show tables;  
mysql> SELECT * FROM projects;   

## Connect Python app to MySQL DB
python3 01_connect_db.py


## Insert into MySQL DB Dependent data
python3 02_insert_data_with_FK.py

## SQL Alchemy Setup
python3 -m venv mysql-sqlalchemy-workspace  
cd mysql-sqlalchemy-workspace  
activate  
pip3 install mysql-connector-python  
pip3 install sqlalchemy 


## SQLAlchemy create/insert/select
python3 03_SQLAlchemy.py  



 






