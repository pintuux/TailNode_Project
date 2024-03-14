from flask import Flask, jsonify
import requests
import config.db_config as db

app = Flask(__name__)

# Define a route to retrieve data from the database
@app.route('/')
def TailNodeServer():
    return 'Server is running'
@app.route('/post',methods=['GET'])
def posts():
    try:
        sql = 'SELECT Id FROM TailnodeUser'
        db.cursor.execute(sql)
        user_ids = db.cursor.fetchall()
        # db.cursor.close()
        # print(user_ids)
        user_id_list = [id[0] for id in user_ids]
        # print(type(user_id_list))
        posts = list(map(upload_into_database,user_id_list))
        # print(posts[0]['data'])
        for post in (posts[0]['data']):
            sql = "INSERT IGNORE INTO  post (p_id,owner_id,publish_date,image,likes,text) VALUES (%s,%s,%s,%s,%s,%s)"
            values = (post['id'],post['owner']['id'],post['publishDate'],post['image'],post['likes'],post['text'])
            db.cursor.execute(sql,values)
            for tag in post['tags']:
                sql2 = 'INSERT IGNORE INTO tags (p_id,taged_people) VALUES(%s,%s)'
                values2 = (post['id'],tag)
                db.cursor.execute(sql2,values2)
        db.connection.commit()
        db.cursor.close()
        db.connection.close()
        return jsonify({'message': 'User_id fetched and post inserted into database successfully!'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/getdata',methods=['GET'])
def get_data():
    try:
        app_id = '65f1a4ede5c046667c0375cc'
        headers = {'app-id':app_id}
        response = requests.get('https://dummyapi.io/data/v1/user',headers = headers)
        
        if response.status_code == 200:
            data = response.json()
            
            for i in data['data']:
                # print(i)
                id = i['id']
                title = i['title']
                first_name = i['firstName']
                last_name = i['lastName']
                picture = i['picture']

                # Insert data into the table
                sql = "INSERT IGNORE INTO TailNodeUser (Id, Title, FirstName, LastName, Picture) VALUES (%s, %s, %s, %s, %s) "
                values = (id, title, first_name, last_name, picture)
                db.cursor.execute(sql,values)
                db.connection.commit()
            db.cursor.close()
            db.connection.close()    
            return jsonify({'message': 'Data fetched and inserted into Database successfully!'})
        else:
            return jsonify({'error': f"Error: {response.status_code}"}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500
def upload_into_database(user_id):
    try:
        # print(type(user_id))
        app_id = '65f1a4ede5c046667c0375cc'
        headers = {'app-id':app_id}
        url = f'https://dummyapi.io/data/v1/user/{user_id}/post'
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            post_data = response.json()
            # print(post_data)
            return post_data
        else:
            return jsonify({'error': f"Error: {response.status_code}"}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500    
if __name__ == '__main__':
    app.run(debug=True)
