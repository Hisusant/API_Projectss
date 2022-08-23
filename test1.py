from flask import Flask, request, jsonify
import mysql.connector as conn
app = Flask(__name__)

mydb = conn.connect
@app.route('/abcd', methods=['GET','POST'])
def test():
    if (request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a+b
        return jsonify((str(result)))

@app.route('/abc1/multiplication', methods=['GET','POST'])
def multiplication1():
    if (request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a*b
        return jsonify((str(result)))

@app.route('/abc1/division1', methods=['GET','POST'])
def div1():
    if (request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a/b
        return jsonify((str(result)))

@app.route('/abc1/exponent1', methods=['GET','POST'])
def expo1():
    if (request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a%b
        return jsonify((str(result)))

@app.route('/abc1/root12', methods=['GET','POST'])
def root1():
    if (request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a**b
        return jsonify((str(result)))


@app.route('/dbconn1', methods=['GET','POST'])
def mysql_dbconn():
    if (request.method=='POST'):
        try:
            mydb = conn.connect(host='localhost', user='root', passwd='susant123')
            #establish database connection
            cursor = mydb.cursor()  # creating cursor object
            query1 = request.json['query_db'] # "query_db" : "create database if not exists API_DB"
            cursor.execute(query1)
            result = "database created"
            #mydb.close()
            return jsonify((str(result)))
        except Exception as e:
            return jsonify((str(e)))


@app.route('/db/insert', methods=['GET','POST'])
def mysql_insert1():
    if (request.method=='POST'):
        try:
            mydb = conn.connect(host='localhost', user='root',passwd='susant123',database='API_DB' )
            #establish database connection
            cursor = mydb.cursor()  # creating cursor object
            name1 = request.json['name']
            age1 = request.json['age']
            sal1 = request.json['sal']
            dept1 = request.json['dept']
            insert1 = "insert into employ_info values(%s,%s,%s,%s)",(name1,age1,sal1,dept1)
            cursor.execute(insert1)
            mydb.commit()
            #mydb.close()
            result = "one record inserted"
            return jsonify((str(result)))
        except Exception as e:
            return jsonify((str(e)))

if __name__ == '__main__':
    app.run()