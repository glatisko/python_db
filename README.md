# https://github.com/LinkedInLearning/advanced-python-working-with-databases-4365479

# git remote add origin git@github.com:glatisko/python_db.git

# Download latest python
https://www.python.org/downloads/

# Check installed interpreters
where python
C\:\Users\glatisko\AppData\Local\Programs\Python\Python312\python.exe
C:\Users\glatisko\AppData\Local\Microsoft\WindowsApps\python.exe

# Select python interpreter in VS
Ctrl+Shift+P


####################################
# Create virtual environment
python3 -m venv .venv

# Check you select correct interpreter:
Ctrl+Shift+P
Python 3.12.1 venv .venv

# Restat terminal with activated Virtual Environment
(.venv) PS C:\SOURCE\python> 

OR
cd  .venv/Scripts
activate
deactivate

####################################
# ORM - SQLAlchemy - with venv acivated
pip install sqlalchemy

# run example:
python filter_sqlalchemy_core.py




