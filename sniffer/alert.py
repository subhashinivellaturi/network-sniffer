from datetime import datetime, timedelta
import sqlite3
import smtplib
from email.mime.text import MIMEText

conn = sqlite3.connect("db/traffic_log.db", check_same_thread=False)
cursor = conn.cursor()

def send_email_alert(ip, count):
    sender = "lakshmisubhashini.ai@gmail.com"
    password = "ctzc lpze xukj vxcv"  # or Gmail password (not secure)
    receiver = "lakshmisubhashini.ai@gmail.com"

    msg = MIMEText(f"High traffic detected from IP: {ip} ({count} packets in 10s)")
    msg['Subject'] = "Network Alert: Suspicious Traffic"
    msg['From'] = sender
    msg['To'] = receiver

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print(f"[EMAIL SENT] Alert sent to {receiver}")
    except Exception as e:
        print(f"[EMAIL ERROR] {e}")

def check_alerts(ip):
    now = datetime.now()
    ten_seconds_ago = (now - timedelta(seconds=10)).strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute("SELECT COUNT(*) FROM packets WHERE src_ip = ? AND timestamp > ?", (ip, ten_seconds_ago))
    count = cursor.fetchone()[0]

    if count > 10:
        print(f"[ALERT] High traffic from {ip} ({count} packets in 10s)")
        send_email_alert(ip, count)
