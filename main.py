from searchNumber import searchNumber
from textRecognition import getText
import os
from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Recognition MAIN</h1>"

@app.route("/recognition", methods=["POST"])
def recognition():
    file = request.files['file']
    file.save(os.path.join('./img', "image.jpg"))
    imgNumber = searchNumber("image.jpg")
    if imgNumber:
        text = getText("image.jpg")
        return jsonify({"number": text})
    else:
        return jsonify({"error": "Номер не найден"})
    

app.run(host="0.0.0.0", port="5000")