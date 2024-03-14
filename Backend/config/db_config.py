import mysql.connector

# MySQL Database Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Your MySql Password',
    'database': 'Users'
}
# Connect to MySQL Database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

