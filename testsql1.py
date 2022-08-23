from flask import Flask, request, jsonify
import mysql.connector as conn
app = Flask(__name__)   # create app in Flask() menthod
#establish database connection
mydb = conn.connect(host='localhost', user='root', passwd='susant123')
# create cursor object
cursor = mydb.cursor()
# create a database in sql
cursor.execute("create database if not exists api_db")
#cretae a table in apidb database
cursor.execute("create table if not exists api_db.employ_details(name varchar(30), number int)")

@app.route('/dbsql/insert', methods=['POST','GET'])
def insert():
    if request.method == 'POST':
        try:
            name1 = request.json['name']
            num1 = request.json['num']
            cursor.execute("insert into api_db.employ_details values(%s,%s)",(name1,num1))
            mydb.commit()
            return jsonify(str("one record inserted"))
        except exception as e:
            return jsonify(str(e))

@app.route('/dbsql/update', methods=['POST','GET'])
def update():
    if request.method == 'POST':
        try:
            name1 = request.json['name']
            cursor.execute("update api_db.employ_details set number = number * 100 where name=%s",(name1,))
            mydb.commit()
            return jsonify(str("one record updated successfully"))
        except exception as e:
            return jsonify(str(e))


@app.route('/sqldb/delete', methods=['POST','GET'])
def delete():
    if request.method=='POST':
        try:
            name1 = request.json['name']
            cursor.execute("delete from api_db.employ_details where name=%s",(name1,)) # name - column name in sql
            mydb.commit()
            return jsonify(str("one record deleted"))
        except Exception as e:
            return jsonify(str(e))

if __name__ == '__main__':
    app.run(port=5002)

