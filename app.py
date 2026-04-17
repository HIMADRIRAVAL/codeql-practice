from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/search")
def search():
    name = request.args.get("name")
    conn = sqlite3.connect("test.db")
    cur = conn.cursor()

    query = "SELECT * FROM users WHERE name = '" + name + "'"
    cur.execute(query)

    return "done"

app.run()
