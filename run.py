from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("app_info.html")

@app.route("/home")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run()