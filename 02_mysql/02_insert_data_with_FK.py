import mysql.connector as mysql

def connect(db_name):
	try:
		return mysql.connect(host="localhost",
							 database=db_name,
							 user='root',
							 password="password")
	except Error as e:
		print(e)

# INPUT PARAMS
# cursor
# project title -> table PROJECTS
# project description -> table PROJECTS
# tasks - list of tasks to be added to table TASKS
def add_project(cursor, project_title, project_description, tasks):
    
	project_data = (project_title, project_description) #create single tuple for insert into table PROJECTS
	cursor.execute('''INSERT INTO projects(title, description) VALUES (%s, %s)''', project_data)
 
	tasks_data = [] #tasks list
	for task in tasks:
		task_data = (cursor.lastrowid, task) # single tuple from tasks list
		tasks_data.append(task_data) #list of tuples
	cursor.executemany('''INSERT INTO tasks(project_id, description) 
		VALUES(%s, %s)''', tasks_data)

if __name__ == '__main__':
    
	db = connect("projects")
	cursor = db.cursor()
	tasks = ["Clean bathroom", "Clean kitchen", "Clean living room"] 
 
	add_project(cursor, "Clean house", "Clean house by room", tasks)
	db.commit()

	cursor.execute("SELECT * FROM projects")
	project_records = cursor.fetchall()
	print(project_records)

	cursor.execute("SELECT * FROM tasks")
	tasks_records = cursor.fetchall()
	print(tasks_records)