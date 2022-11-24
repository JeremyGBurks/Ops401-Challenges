# Author - Jeremy Burks
# Date Last Revised - 07/05/22
# Purpose - Automates the configuration of the monitor timeout parameter to 1 minute, then subsequently locks the workstation.

#This cmdlt changes the monitor timout to 1 minute. It can be ran with any automation script that is standing up endpoints to automate configurations
powercfg -change -monitor-timeout-dc 1
#This cmdlt is straightforward. It automatically locks the workstation
rundll32.exe user32.dll,LockWorkStation
