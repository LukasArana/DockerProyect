from flask import Flask
from redis import Redis, RedisError
import os
import socket
import mariadb

conn = mariadb.connect(
         host='localhost',
         port= 3306,
         user='root',
         password='goldSTAR',
         database='movieDb')
# Connect to Redis
app = Flask(__name__)

cur = conn.cursor()
@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"
    html = "<h3>Hello {name}!</h3>" \
    "<b>Hostname:</b> {hostname}<br/>" \
    "<b>Visits:</b> {visits}"
    print(html)    
    return html.format(name=os.getenv("NAME", "world"),
hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
