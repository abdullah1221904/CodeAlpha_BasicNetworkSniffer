from scapy.all import *

def packet_callback(packet):
    print("===================================")
    
    # Check if packet has IP layer
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        print(f"Protocol: {ip_layer.proto}")
    
    # Check for TCP
    if packet.haslayer(TCP):
        print("Protocol Type: TCP")
    
    # Check for UDP
    elif packet.haslayer(UDP):
        print("Protocol Type: UDP")
    
    # Check for ICMP
    elif packet.haslayer(ICMP):
        print("Protocol Type: ICMP")
    
    # Print Payload
    if packet.haslayer(Raw):
        print(f"Payload: {packet[Raw].load}")

# Start sniffing
print("Starting Network Sniffer...")
sniff(prn=packet_callback, count=10)