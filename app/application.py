from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def index():
    return f"Hola desde {socket.gethostname()}"

@app.route("/status")
def status():
    return {
        "instancia": socket.gethostname(),
        "estado": "OK"
    }