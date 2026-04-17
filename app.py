import os
import subprocess
import sqlite3

user = input("Name: ")
query = "SELECT * FROM users WHERE name='" + user + "'"

conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute(query)

cmd = input("Command: ")
os.system(cmd)
