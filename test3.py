import mysql.connector as conn
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/dbconn12', methods=['GET','POST'])
def mysql_dbconn():
    if (request.method=='POST'):
        try:
            mydb = conn.connect(host='localhost', user='root', passwd='susant123')
            #establish connection
            cursor = mydb.cursor()  # creating cursor object
            query1 = request.json['query_db'] # "query_db" : "create database if not exists API_DB"
            cursor.execute(query1)
            result = "database created"
            #mydb.close()
            return jsonify((str(result)))
        except Exception as e:
            return jsonify((str(e)))

@app.route('/abc1/root12', methods=['GET','POST'])
def root1():
    if (request.method == 'POST'):
        a = request.json['a1'] # a1 : 10
        b = request.json['b1']  # b1 : 5
        result = a ** b
        return jsonify((str(result)))

if __name__ == '__main__':
    app.run()
