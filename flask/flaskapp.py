# flaskapp.py

from flask import Flask

app = Flask(__name_)

@app.route("/")

def flask_main():
    return "<h1>Hello World of Flask and Python</h1>"