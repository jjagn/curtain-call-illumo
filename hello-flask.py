from flask import Flask
from gpiozero import Motor
app = Flask(__name__)

@app.route("/")
def hello():
    return "twelve of the clock and all is well"

@app.route("/open")
def open():
    motor.forward()
    sleep(5)
    motor.stop()

@app.route("/close")
def close():
    motor.backward()
    sleep(5)
    motor.stop()