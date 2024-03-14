# Flask API for Fetching User Data and Posts
This Flask application serves as an API for fetching user data and posts from the Dummy API and storing them into a MySQL database. The application consists of the following endpoints:

## 1. Root Endpoint (/):
Method: GET

Description: Returns a message indicating that the server is running.

## 2. /getdata Endpoint:
Method: GET

Description: Fetches user data from the Dummy API and inserts it into the TailNodeUser table in the MySQL database.
## 3. /post Endpoint:

Method: GET

Description: Fetches user IDs from the TailnodeUser table in the MySQL database, then uses these IDs to fetch posts for each user from the Dummy API. The posts are inserted into the post table in the MySQL database. Tags associated with each post are also inserted into the tags table.

## Installation
Clone the repository to your local machine:

git clone <repository_url>

# Install the required dependencies:

1. pip install Flask requests mysql-connector-python

2. Set up the MySQL database and update the config/db_config.py file with your MySQL database connection details.

3. Run the Flask application:

python app.py

# Usage
Access the API endpoints using the provided URLs (e.g., http://localhost:5000/getdata, http://localhost:5000/post) to fetch and store user data and posts.

## Dependencies
Flask: A lightweight web framework for Python.

requests: A library for making HTTP requests.

mysql-connector-python: A connector library for MySQL databases.

## Contributors
Pintu Kumar

## License
This project is licensed under the MIT License - see the LICENSE file for details.
