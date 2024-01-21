import sqlite3
import pandas as pd
  
# Connect to SQLite database
connection = sqlite3.connect(r'names-sqlite.db')

file_name='test.csv'
read_data = pd.read_csv(file_name)

# Write the data to a sqlite table
read_data.to_sql('NAMES', connection, if_exists='append', index=False)

# Print data from table  
cursor = connection.cursor()
cursor.execute("SELECT * FROM NAMES")
print(cursor.fetchall())


connection.close()