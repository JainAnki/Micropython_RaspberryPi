#to host a localhost web server

import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] == True

@app.route("/", methods=["GET"])
def home():
	hello = {"message":"Hello!"}
	return jsonify(hello)

app.run(host='0.0.0.0', port=8080, debug=True)
