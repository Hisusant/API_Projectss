from flask import Flask, request, jsonify
app = Flask(__name__)
import mysql.connector as conn

@app.route('/getfun')
def getfun():
    return "Hello , welcome to flask url programming"
    # run ulr - 127.0.0.1:5003/getfun

@app.route('/search1')
def get1():
    name1 = request.args.get('name') # pass in server url - 127.0.0.1:5003/search1?name=susant kumar
    return "Helllo {}".format(name1)

@app.route('/search2')
def search22():
    name1 = request.args.get('name')
    num1 = request.args.get('num')
    email1 = request.args.get('email')
    #pass data in url - 127.0.0.1:5003/search2?name=susant kumar &num=9438528988 &email=spsu@gmail.com
    return "Hello {} {} {} ".format(name1,num1,email1)

@app.route('/searchdb')
def searchdbdata():
    try:

        mydb = conn.connect(host='localhost', user='root', passwd='susant123', database='api_db')
        cursor = mydb.cursor()
        #dbname1 = request.args.get('dbname')
        table1 = request.args.get('table')
        #return "{} {}".format(dbname1, table1)
        #pass data in url - 127.0.0.1:5003/searchdb?dbname=api_db &table=employ_details
        cursor.execute(f"select * from {table1}")
        records = cursor.fetchall()
        mydb.commit()
        return jsonify(str(records))
    except Exception as e:
        return jsonify(str(e))


if __name__ == '__main__':
    app.run(port=5003)