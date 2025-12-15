from flask import Flask, request, jsonify
from datetime import datetime

app1 = Flask(__name__)

@app1.route('/')
def hello():
    return ("Привет, пользователь\n")

@app1.route('/hello/<name>')
def hello_n(name):
    return (f"Привет, {name}\n")

@app1.route('/square/<int:number>')
def square(number):
    return str(number ** 2)

@app1.route('/sum')
def sum():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return str(a+b)

@app1.route('/info')
def info():
    start_time = datetime.now()
    inf = {
        "version": "1.0",
        "author":"alspezza",
        "time": str(start_time)
    }
    return jsonify(inf)
