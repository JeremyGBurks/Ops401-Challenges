#!/usr/bin/python3

# Author - Jeremy Burks
# Date Revised - 11/30/22 
# Purpose - Port scanner that only uses python3 to determine if a port is open or closed


import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockmod.settimeout(5)

hostip = input("Enter IP to scan: ")
portno = int(input("Enter a port to scan: "))

def portScanner(portno):
    if sockmod.connect_ex((hostip, portno)): 
        print("Port closed")
    else:
        print("Port open")

portScanner(portno)
