from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello, World!"
@app.route('/json', methods=['GET'])
def send_json():
    json = {"h": "haaaloo"}
    return json
