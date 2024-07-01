from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

con = sqlite3.connect("tutorial.db",check_same_thread=False)
cur = con.cursor()
try:
    cur.execute("CREATE TABLE movie(title, year, score)")
except:
    pass

res=[]
@app.route('/')
def hello():
    for row in cur.execute("SELECT * FROM movie"):
        res.append(row)
    return jsonify(res)

@app.route('/add')
def add():
    cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
    con.commit()
    return 'add'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
