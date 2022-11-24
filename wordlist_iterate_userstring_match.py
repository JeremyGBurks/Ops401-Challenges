#!/usr/bin/env python3

# Author - Jeremy Burks
# Date Last Revised - 08/24/22
# Purpose - User menu with two modes: one iterates through a provided wordlist in a filepath and prints the contents
# to the terminal. The second mode searches line by line in a selected wordlist to find a match to a user string they input. 

import time, getpass

# The iteration function that goes through and prints the values in the rovided word list
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
3 - Exit
        Please enter a number: 
""")
        if (mode == "1"):
            iterator()
        elif (mode == "2"):
            check_password()
        elif (mode == '3'):
            break
        else:
            print("Invalid selection...") 
