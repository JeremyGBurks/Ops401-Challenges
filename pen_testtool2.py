#!/usr/bin/python3

# Author - Jeremy Burks
# Date of last revision - 11/21/2022
# Purpose - Python script that automates the use of nmap scanning commands

import subprocess
import nmap

# ip_addr = '127.0.0.1'

scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) Regular Scan  
                4) Ping Sweep  \n""")
print("You have selected option: ", resp)

range = input("Please enter a port range to scan: ")

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

if  resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sU')
    print(scanner.scaninfo()) 
    print("Ip Status: ", scanner[ip_addr].state())
    print("protocols:", scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]["udp"].keys())

elif resp == '3':
    scanner.scan(ip_addr)
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

elif resp >= '4':
    scanner.scan(hosts='192.168.1.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
    hosts_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]
    for host, status in hosts_list:
        print('{0}:{1}'.format(host, status))
