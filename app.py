from flask import Flask
import os
import socket
import mysql.connector as mariadb
'''
conn = mariadb.connect(
         host='localhost',
         port= 3306,
         user='root',
         password='goldSTAR',
         database='movieDb')
cursor = conn.cursor()
'''
app = Flask(__name__)

@app.route("/test")
def test():
    return f"ALIVE {socket.gethostname()}"

@app.route("/message,methods = ['POST', 'GET']")
def message():
        
    if request.method == 'POST':
      frm = request.form['From']
      cont = request.form['Content']
      conn.execute('INSERT INTO posts (from, content, id) VALUES (?, ?, ?)',
                   (frm, cont, socket.gethostname()))
      conn.commit()
      conn.close()
      #return redirect(url_for('/index'))    # etzekit ea holakoik behardeken
    else:
      posts = conn.execute('SELECT * FROM posts').fetchall()
      conn.close()
      #return render_template('/index.html', posts=posts) # hau supongo behardekela


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
