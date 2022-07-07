from re import L
from flask import Flask, render_template
from flask_sock import Sock

app = Flask(__name__)
sock = Sock(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/click')
def click():
    return render_template('click.html')

@sock.route('/control')
def control(sock):
    while True:
        data = sock.receive()
        sock.send(data)