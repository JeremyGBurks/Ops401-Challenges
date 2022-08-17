#!/usr/bin/env python3

# Author - Jeremy Burks
# Date Last Revised - 08/16/22
# Purpose - function scans ports on a host, uses random to obfuscate source of scan. Ping scans a defined netowork

import random
from scapy.all import ICMP, IP, sr1, TCP
from ipaddress import IPv4Network

def user_menu():
    print("1. TCP Port Scanner")
    print("2. ICMP Ping Sweep")
    user_menu = input("Please choose an option: ")
    return user_menu


def portscanner():
# Define end host and TCP port range
    host = "192.168.1.9"
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

network = "192.168.1.0/29"
addresses = IPv4Network(network)


def ping_sweep():
    live_count = 0
# Send ICMP ping request, wait for answer
    for host in addresses:
        if (host in (addresses.network_address, addresses.broadcast_address)):
            continue
        resp = sr1(
            IP(dst=str(host))/ICMP(),
            timeout=2,
            verbose=0,
        )

        if resp is None:
            print(f"{host} is down or not responding.")
        elif (
            int(resp.getlayer(ICMP).type)==3 and
            int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
        ):
            print(f"{host} is blocking ICMP.")
        else:
            print(f"{host} is responding.")
            live_count += 1
    print(f"{live_count}/{addresses.num_addresses} hosts are online.")

user_menu = user_menu()
if user_menu == ("1"):
    portscanner()

if user_menu == ("2"):
    ping_sweep()
