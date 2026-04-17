import sqlite3
import subprocess

user = input("Enter username: ")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

query = "SELECT * FROM users WHERE name = '" + user + "'"
cursor.execute(query)

cmd = input("Enter command: ")
subprocess.call(cmd, shell=True)
