import tkinter as tk
from tkinter import ttk
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def get_ip_counts():
    conn = sqlite3.connect("db/traffic_log.db")
    cursor = conn.cursor()
    cursor.execute("SELECT src_ip, COUNT(*) FROM packets GROUP BY src_ip ORDER BY COUNT(*) DESC LIMIT 5")
    data = cursor.fetchall()
    conn.close()
    return data

def refresh_chart():
    data = get_ip_counts()
    ips = [row[0] for row in data]
    counts = [row[1] for row in data]

    ax.clear()
    ax.bar(ips, counts, color='skyblue')
    ax.set_title("Top IPs by Packet Count")
    ax.set_ylabel("Packets")
    ax.set_xlabel("Source IP")

    canvas.draw()

# GUI setup
root = tk.Tk()
root.title("Live Network Traffic Monitor")
root.geometry("700x500")

frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

fig, ax = plt.subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.get_tk_widget().pack()

btn = ttk.Button(root, text="Refresh Graph", command=refresh_chart)
btn.pack(pady=10)

refresh_chart()
root.mainloop()
 
