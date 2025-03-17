from google.cloud import firestore
from flask import Flask, request, jsonify
from flask_cors import CORS

db = firestore.Client.from_service_account_json("firebase_credentials.json")
app = Flask(__name__)
CORS(app, origins="http://localhost:3000")

@app.route("/", methods=["GET"])
def test():
    return 'ALIVE!'

@app.route("/all", methods=["GET"])
def get_all_posts():
    bufferjson = {}
    post_ref = db.collection("Posts").stream()
    for doc in post_ref:
        bufferjson[doc.id] = doc.to_dict()
    return jsonify(bufferjson)

@app.route("/<userId>", methods=["GET"])
def get_user_posts(userId):
    bufferjson = {}
    post_ref = db.collection("Posts").where("userId", "==", userId).stream()
    for doc in post_ref:
        bufferjson[doc.id] = doc.to_dict()
    return jsonify(bufferjson)

def get_all_posts():
    bufferjson = {}
    post_ref = db.collection("Posts").stream()
    for doc in post_ref:
        bufferjson[doc.id] = doc.to_dict()
    return jsonify(bufferjson)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

