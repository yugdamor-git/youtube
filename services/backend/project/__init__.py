from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/")
def hello_world():
    return jsonify(
        ip=os.environ.get("IP")
    )