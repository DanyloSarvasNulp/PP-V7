from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)


@app.route("/api/v1/hello-world-7")
def index():
    return "Hello World 7!"
