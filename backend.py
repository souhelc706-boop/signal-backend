from flask import Flask
import os

app = Flask(_name_)

@app.route("/")
def home():
    return "Backend funcionando!"

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
