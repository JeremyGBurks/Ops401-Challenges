#!/usr/bin/env python3

# Author - Jeremy Burks
# Date Last Revised - 07/06/22
# Purpose - Sends ping requests every 2 seconds, evaluates the response and adds a timestamp.

import subprocess
import time
import datetime

def pinging():
    status = ""

    for ping in range(7,9):
        address = "8.8.8." + str(ping)
        #subprocess.call Stop after sending (and receiving) count(-c) 2 packets
        res = subprocess.call(['ping', '-c', '2', address])
        # subprocess.call will return a 0 return code upon success, a 2 for no response, or a 3 for failed response
        ct = str(datetime.datetime.now())
        if res == 0:
            status = "succcess"
            print(ct + ": ping to "+ address + " OK! " + status)
        elif res == 2:
            status = "failed"
            print(ct + ": no response from " + address + ". Ping has " + status)
        else:
            status = "failed"
            print(ct + ": ping to " + address + " " + status)

def two_second_ping():
    for i in range(1,3):
        print("Ping attempt number " + str(i))
        pinging()
        time.sleep(2)

two_second_ping()
