from flask import Flask, request
import os
import socket
import mysql.connector as mariadb


conn = mariadb.connect(
          host='db',
          user='root',
          password='lukaskas22',
          database='data',
          port=3306)
cursor = conn.cursor()

app = Flask(__name__)

@app.route("/test")
def test():
    return f"ALIVE {socket.gethostname()}"

@app.route("/message", methods=['GET', 'POST'])
def message():
    if request.method == 'POST':
        return f"post"
    else:
        return f'{request.method}'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
