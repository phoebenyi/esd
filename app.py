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
    try:
        doc_ref = db.collection("Posts").document(userId).get()

        if not doc_ref.exists:
            return jsonify({"error": "Document not found"}), 404

        return jsonify(doc_ref.to_dict()), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/upload", methods=["POST"])
def upload_post():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400

        if "userId" not in data:
            return jsonify({"error": "Missing 'id' field in request data"}), 400

        doc_id = data["userId"]
        del data["userId"]

        db.collection("Posts").document(doc_id).set(data)

        return jsonify({"success": True, "userId": doc_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

