#!/usr/bin/env python3

# Author - Jeremy Burks
# Date Last Revised - 08/10/22
# Purpose - function scans ports on a host, uses random to obfuscate source of scan.

import random
from scapy.all import ICMP, IP, sr1, TCP

def portscanner():
# Define end host and TCP port range
    host = "192.168.1.106"
    port_range = [22, 23, 80, 443, 3389]

# Send SYN with random Src Port for each Dst port
    for dst_port in port_range:
        src_port = random.randint(1025,65534)
        resp = sr1(
            IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1, 
    verbose=0,
        )

    if resp is None:
        print(f"{host}:{dst_port} is not responding")

    elif(resp.haslayer(TCP)):
        if(resp.getlayer(TCP).flags == 0x12):
            # Send a gratuitous RST to close the connection
            send_rst = sr(
                IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="r"), 
                timeout=1, 
                verbose=0,
            )
            print(f"{host}:{dst_port} is open!")

        elif (resp.getlayer(TCP).flags ==0x14):
                print(f"{host}:{dst_port} is closed!")

portscanner()
#end 
