from flask import Flask, request
import os
import socket
import mysql.connector as mariadb


conn = mariadb.connect(
          host='db',
          user='lukashasier',
          password='lukashasier',
          database='lana',
          port=3306)

app = Flask(__name__)

@app.route("/test")
def test():
    return f"ALIVE {socket.gethostname()}"

@app.route("/message", methods=['GET', 'POST'])
def message():
    cursor = conn.cursor()
    if request.method == 'POST':
      req = request.json
      cursor.execute('INSERT INTO datuak (fro, CONTENT, id) VALUES (%s, %s, %s)',
                   (req["From"], req["Content"], socket.gethostname()))
      conn.commit()
      cursor.close()
      return req
    else:
      cursor.execute('SELECT * FROM datuak')
      data = cursor.fetchall()
      cursor.close()
      return data


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
