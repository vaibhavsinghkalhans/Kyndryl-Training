from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to my first REST API"
    })

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return jsonify({
        "id": user_id,
        "name": "Vaibhav Singh",
        "role": "Infrastructure Specialist"
    })

if __name__ == "__main__":
    app.run(debug=True)