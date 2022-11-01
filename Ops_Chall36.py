#!/usr/bin/env python3

# Author - Jeremy Burks
# Date Last Revised - 10/31/22
# Purpose - a Python script that utilizes multiple banner grabbing approaches against a single target

import os
import socket
import sys
import telnetlib
import nmap


url = input("Please enter URL or IP address: ")
port = int(input("Please enter a port number: "))


def cat_net(url, port):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((url, port))
    nc = "nc" + url + " " + int(port)
    sock.sendall(nc.encode())
    time.sleep(0.5)
    sock.shutdown(socket.SHUT_WR)

    res = ""

    while TRUE:
        data = soc.recv(1024)
        if (not data):
            break
        res += data.decode()
    print(res)
    print("\033[A   \033[A")

    print ("Connection closed")
    soc.close()

def tell_thenet(url, port):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((url, port))
    telly = "telnet" + url + " " + int(port)
    sock.sendall(telly.encode())
    time.sleep(0.5)
    sock.shutdown(socket.SHUT_WR)

    res = ""

    while TRUE:
        data = soc.recv(1024)
        if (not data):
            break
        res += data.decode()
    print(res)

    print ("Connection closed")
    soc.close()

cat_net(url, port)
tell_thenet(url, port)
