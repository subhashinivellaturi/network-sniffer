import sqlite3
from datetime import datetime
import os

db_path = "db/traffic_log.db"
os.makedirs("db", exist_ok=True)

conn = sqlite3.connect(db_path, check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS packets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    src_ip TEXT,
    dst_ip TEXT,
    src_port INTEGER,
    dst_port INTEGER,
    protocol TEXT
)''')
conn.commit()

def log_packet(src, dst, sport, dport, proto):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO packets (timestamp, src_ip, dst_ip, src_port, dst_port, protocol) VALUES (?, ?, ?, ?, ?, ?)",
                   (timestamp, src, dst, sport, dport, proto))
    conn.commit()
