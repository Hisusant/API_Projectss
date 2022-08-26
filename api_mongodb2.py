from flask import Flask, request, jsonify
import pymongo

client = pymongo.MongoClient("mongodb+srv://susant:susant123@cluster0.8beoc.mongodb.net/?retryWrites=true&w=majority")
database = client['api_db'] # creating database
collection = database['login_details'] # creating table

app = Flask(__name__) # app creation

@app.route('/mongo2/insert2', methods = ['POST',"GET"])
def insert1():
    if request.method == 'POST':
        try:

            user1 = request.json['user']
            pass1 = request.json['pass']
            collection.insert_one({user1:pass1})
            return jsonify(str("one record inserted"))
        except Exception as e:
            return jsonify(str(e))

if __name__=='__main__':
    app.run()