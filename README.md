# 🛰️ Network Packet Sniffer with Alert System

## 🎯 Objective
Build a **real-time network traffic sniffer** in Python with anomaly detection, email alerts, database logging, and GUI visualization.

---

## 🧰 Tools & Technologies Used

- Python 🐍
- `scapy` for packet sniffing
- `SQLite3` for logging traffic
- `matplotlib` for plotting graphs
- `smtplib` and `email` for sending alerts
- Command Line Interface (CLI) + optional GUI

---

## 📂 Project Structure

network-sniffer/
│
├── main.py # Starts packet sniffing and handles alerts
├── alert.py # Checks high traffic & sends email
├── gui_graph.py # Shows traffic graph from database
├── test_requests.py # Sends requests to generate traffic
├── view_logs.py # Displays last 10 packets
├── db/
│ └── traffic_log.db # SQLite database for logs
├── screenshots/
│ ├── main_running.png
│ ├── email_alert.png
│ ├── view_logs.png
│ └── graph_output.png


---

## 🚀 How to Run

### 1. Install Requirements
```bash
pip install scapy matplotlib
```
Start the Sniffer
``` bash
python main.py
```
Generate Traffic (in another terminal)
```
python test_requests.py
```
View Last 10 Logs
``` bash
python view_logs.py
```
GUI Graph of Traffic
``` bash
python gui_graph.py
```

🔔 Email Alert Feature
If traffic from a single IP exceeds 10 packets in 10 seconds, an email alert is triggered.

Alerts are printed in the terminal and also sent to your Gmail.

✅ Make sure you've enabled "Less Secure Apps" or App Password in Gmail settings.

📊 GUI Graph Feature
Launches a window showing a real-time line graph of packet counts.

Helps visualize how much traffic was observed in recent time windows.
