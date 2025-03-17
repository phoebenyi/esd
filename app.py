from google.cloud import firestore
from flask import Flask, request, jsonify
from flask_cors import CORS

db = firestore.Client.from_service_account_json("firebase_credentials.json")
app = Flask(__name__)
CORS(app, origins="http://localhost:3000")

@app.route("/", methods=["GET"])
def test():
    return 'ALIVE!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

