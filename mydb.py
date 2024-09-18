import mysql.connector
import os

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = os.environ.get('BD_PASSWORD')
)

cursorObject = dataBase.cursor()
cursorObject.execute('CREATE DATABASE crmapp')

print("Database created successfully!")