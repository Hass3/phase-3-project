import sqlite3

CONN = sqlite3.connect('health.db')
CURSOR = CONN.cursor()
