from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Backend funcionando correctamente en Render!"})

@app.route("/sumar", methods=["POST"])
def sumar():
    data = request.get_json()
    a = data.get("a", 0)
    b = data.get("b", 0)
    return jsonify({"resultado": a + b})

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=10000)
