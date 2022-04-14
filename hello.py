from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1> Hello Dewa </h1>"

@app.route("/works")
def it_works():
    return "IT Works"