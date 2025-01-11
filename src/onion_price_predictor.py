from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/forecast", methods = ["GET"])
def forecast():
    return render_template("forecast.html")


if __name__ == "__main__":
    app.run(debug = True)