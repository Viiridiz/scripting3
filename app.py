from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Home!"

client = MongoClient("mongodb+srv://amashkashareef:ys3mNrQNsek5Wux6@cluster0.3dinr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client['Scripting3']
users_collection = db['Users']

print(users_collection)

@app.route('/users' , methods=['GET'])
def get_users():
    users = []
    for user in users_collection.find():
        user['_id'] = str(user['_id'])
        users.append(user)
    return jsonify(users)

@app.route('/print_collection', methods=['GET'])
def print_collection():
    return "Check your console for the printed collection!"

if __name__ == '__main__':
    app.run(debug=True)
