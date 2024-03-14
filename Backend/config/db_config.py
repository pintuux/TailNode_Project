import mysql.connector

# MySQL Database Configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Pintu@28',
    'database': 'Users'
}
# Connect to MySQL Database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

