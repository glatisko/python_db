
# Install MySQL
Download MySQL community edition
## add to path
echo $SHELL
nano .zshrc
export PATH=${PATH}:/usr/local/mysql/bin
source .zshrc

## Create MySQL DB/tables
sudo mysql -u root -p password

mysql>CREATE DATABASE projects;

mysql> use projects;
mysql> CREATE TABLE projects (project_id INT(11) NOT NULL AUTO_INCREMENT, title VARCHAR(30), description VARCHAR(255), PRIMARY KEY(project_id);

mysql> CREATE TABLE tasks (tasks_id INT(11) NOT NULL AUTO_INCREMENT, project_id INT(11) NOT NULL, description VARCHAR(255), PRIMARY KEY(task_id), FOREIGN KEY (project_id) REFERENCES projects(project_id));

mysql> show tables;


##  Install DB Connector in venv
pip install mysql-connector-python
pip install sqlalchemy
 






