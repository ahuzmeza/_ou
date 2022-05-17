import mysql.connector
from flask_login import UserMixin
from sqlalchemy.sql import func
import uuid

my_db = mysql.connector.connect( 
    host='localhost', 
    user='root', 
    password='', 
)

my_cursor = my_db.cursor()

# creaye db 
DB_NAME = '_ou_db'

my_cursor.execute("SHOW DATABASES LIKE '{}'".format(DB_NAME))
if my_cursor.fetchone():
    print("\n Database {} Already exists\n".format(DB_NAME))
else: 
    my_cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(DB_NAME))
    
my_cursor.execute("SHow DATABASES")
for db in my_cursor:
    print(db)
    
my_cursor.execute("Use {}".format(DB_NAME))
# Create table
my_cursor.execute("CREATE TABLE IF NOT EXISTS User (uuid INT PRIMARY KEY AUTO_INCREMENT, username VARCHAR(80) UNIQUE, email VARCHAR(120) UNIQUE, password VARCHAR(120), is_admin BOOLEAN DEFAULT FALSE)")