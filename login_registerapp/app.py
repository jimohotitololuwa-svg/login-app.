from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

app.run(debug=True)