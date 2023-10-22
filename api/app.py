from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello BUILD X2 World!"


@app.route("/query")
def query():
    qz = request.args.get('q')
    return process_query(qz)


def process_query(q: str):
    if q == "dinos":
        return "dinos are great"

    return "what"
