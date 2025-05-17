
## How to Install MySQL and Python connector
Download MySQL community edition
### add to path - to see which shell are we running:
echo $SHELL  
nano .zshrc  
export PATH=${PATH}:/usr/local/mysql/bin  
source .zshrc  

###  Create virutual env
python3 -m venv mysql-workspace  
cd mysql-workspace  
activate  

### Install DB Connector 
pip4 install mysql-connector-python  
pip3 install sqlalchemy  

### Create  DB and depdendent tables via MySQL shell:
sudo mysql -u root -p      
mysql>CREATE DATABASE projects;  
mysql> use projects;  
mysql> CREATE TABLE projects (project_id INT(11) NOT NULL AUTO_INCREMENT, title VARCHAR(30), description VARCHAR(255), PRIMARY KEY(project_id);  
mysql> CREATE TABLE tasks (tasks_id INT(11) NOT NULL AUTO_INCREMENT, project_id INT(11) NOT NULL, description VARCHAR(255), PRIMARY KEY(task_id), 
FOREIGN KEY (project_id) REFERENCES projects(project_id));  
mysql> show tables;  
mysql> SELECT * FROM projects;   

## Connet Python app to MySQL DB
python3 01_connect_db.py



 






