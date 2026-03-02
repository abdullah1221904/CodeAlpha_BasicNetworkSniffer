from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        print("Source IP:", src_ip)
        print("Destination IP:", dst_ip)
        print("Protocol:", protocol)

        if TCP in packet:
            print("Protocol Type: TCP")
        elif UDP in packet:
            print("Protocol Type: UDP")

        print("-" * 40)

# Capture 10 packets
sniff(prn=packet_callback, count=10)