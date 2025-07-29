from scapy.all import sniff, IP, TCP
from sniffer.logger import log_packet
from sniffer.alert import check_alerts

def process_packet(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet.proto if hasattr(packet, "proto") else "Unknown"

        if packet.haslayer(TCP):
            sport = packet[TCP].sport
            dport = packet[TCP].dport
        else:
            sport = dport = None

        log_packet(ip_src, ip_dst, sport, dport, proto)
        check_alerts(ip_src)

def start_sniffing():
    sniff(prn=process_packet, store=0)
