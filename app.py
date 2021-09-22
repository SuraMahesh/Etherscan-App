from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "Etherscan web app"

@app.route("/trans/<hash>")
def transaction(hash):
    return render_template("transaction.html")
