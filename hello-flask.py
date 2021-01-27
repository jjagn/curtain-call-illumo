from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "twelve of the clock and all is well"