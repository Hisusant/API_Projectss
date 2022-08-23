from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)
# connecting to mongoDB application server
client = pymongo.MongoClient("mongodb+srv://susant:susant123@cluster0.8beoc.mongodb.net/?retryWrites=true&w=majority")

database = client['api_db'] # creating database
collection = database['user_login'] # creating table

@app.route('/mongo1/insert', methods = ['POST',"GET"])
def insert():
    try:

        if request.method == 'POST':
            username = request.json['uname']
            passwd = request.json['pwd']
            collection.insert_one({username:passwd})
            return jsonify(str("one record inserted to mongodb"))
    except Exception as e:
        return jsonify(str(e))

@app.route('/mongo1/update', methods = ['POST',"GET"])
def update():
    try:

        if request.method == 'POST':
            username = request.json['uname']
            passwd = request.json['pwd']
            collection.update_one({'susant':'bbsr'},{'$set':{username:passwd}})
            return jsonify(str("one record updated"))
    except Exception as e:
        return jsonify(str(e))

@app.route('/mongo1/delete', methods = ['POST',"GET"])
def delete():
    try:
        if request.method == 'POST':
            username = request.json['uname']
            passwd = request.json['pwd']
            collection.delete_one({username:passwd})
            return jsonify(str("one record deleted"))
    except Exception as e:
        return jsonify(str(e))

@app.route('/mongo1/fetch', methods = ['POST',"GET"])
def fetch():
    try:
        if request.method == 'POST':
            l = []
            for i in collection.find(): # To fetch all records
                l.append(i)
            return jsonify(str(l))
    except Exception as e:
        return jsonify(str(e))

if __name__ == "__main__":
    app.run(port=5001)

