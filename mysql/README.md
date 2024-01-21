# https://github.com/LinkedInLearning/advanced-python-working-with-databases-4365479
# https://github.com/glatisko/python_db

# Download MySQL community edition

# add to path
export PATH=

# MySQL Workbeanch - official GUI

# Create MySQL DB/tables

mysql -u root -p password

CREATE DATABASE projects;

use projects;
CREATE TABLE projects (project_id INT(11) NOT NULL AUTO_INCREMENT, title VARCHAR(30), description VARCHAR(255), PRIMARY KEY(project_id);

CREATE TABLE tasks (tasks_id INT(11) NOT NULL AUTO_INCREMENT, project_id INT(11) NOT NULL, description VARCHAR(255), PRIMARY KEY(task_id), FOREIGN KEY (project_id) REFERENCES projects(project_id));

show tables;


# Install DB Connector in venv
pip install mysql-connector-python
pip install sqlalchemy 






