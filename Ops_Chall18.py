#!/usr/bin/env python3

# Author - Jeremy Burks
# Date Last Revised - 09/01/22
# Purpose - User menu with four modes: one iterates through a provided wordlist in a filepath and prints the contents
# to the terminal. The second mode searches line by line in a selected wordlist to find a match to a user string they input. The third enables a brute force atatack using a wordlist
# The fourth menu function brute force attacks an encrypted Zipfile

import time, getpass
import paramiko, sys, os, socket
global host, username, line, input_file

# The iteration function that goes through and prints the values in the provided word list
def iterator ():
    filepath = input("Enter your dictionary filepath:\n")
    #filepath = /Users/jeremyburks/Desktop/rockyou.txt
    
    file = open(filepath, encoding = "ISO-8859-1")
    line = file.readline()
    while line:
        line = line.rstrip()
        word = line
        print(word)
        time.sleep(1)
        line = file.readline()
    file.close()


# the check password function looks within a user defined wordlist for a password they are promted for. The script reads the wordlist
# line by line and prints out a success statement if their provided string was found.
def check_password():
    file_path = input("Please enter a wordlist filepath: ")
    word_choice = input("Please enter a password to search for: ")
    file = open(file_path, encoding = "ISO-8859-1") # address encoding problem
    line = file.readline()
    word_in_file = 0
    while line:
        line = line.rstrip()
        if line == word_choice:
            print("Your password was in the file!")
            word_in_file = 1
            break
    if  word_in_file == 0:
        print("Your password was not in the file")

    file.close()


# User menu
if __name__ == "__main__": # when my computer runs this file...do this stuff
    while True:
        mode = input("""
Brue Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - SSH Brute Force attack
4-  Brute Force ZipFIle
5 - Exit
        Please enter a number: 
""")
        if (mode == "1"):
            iterator()
        elif (mode == "2"):
            check_password()
        elif (mode == '3'):
            ssh_brute()
        elif (mode == '4'):
            break
        else:
            print("Invalid selection...") 

def ssh_collect():
    line = "\n----------------------------------------------------------\n"
    try:
        host = raw_input("[*] Enter attack target address: ")
        username = raw_input("[*] Enter SSH username: ")
        input_file = raw_input("[*] Enter password filepath: ")

        if os.path.exists(input_file) == false:
            print ("\n[*] File Path Does Not Exist !!!")
            sys.exit(4)
    except KeyboardInterrupt:
        print ("\n\n[*] User Requested An Interrupt")
        sys.exit(3)

def ssh_brute(password, code = 0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(host, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        #[*] Authentication Failed ...
        code = 1
    except socket.error. e:
        #[*] Connection Failed ... Host Down
        code = 2
    
    ssh.close()
    return code

def zip_brute():
    from zipfile import ZipFile
    zip_file = 
    password = 

    with ZipFile(zip_file) as zf:
        zf.extractall(pwd=bytes(password,'utf-8'))
