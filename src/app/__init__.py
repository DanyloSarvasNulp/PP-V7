from flask import Flask

app = Flask(__name__)


@app.route("/api/v1/hello-world-7")
def index():
    return "Hello World 7"