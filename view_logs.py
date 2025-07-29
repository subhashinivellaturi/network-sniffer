import sqlite3

conn = sqlite3.connect("db/traffic_log.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM packets ORDER BY id DESC LIMIT 10")
rows = cursor.fetchall()

print("\nLast 10 packets captured:\n")
for row in rows:
    print(row)
 
