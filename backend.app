from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(_name_)
CORS(app)

@app.route("/")
def home():
    return jsonify({"status": "Backend funcionando correctamente"})

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
