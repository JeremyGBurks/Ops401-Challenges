#!/usr/bin/env python3

# Author - Jeremy Burks
# Date Last Revised - 10/17/22
# Purpose - User selects an OS, then recursively scans each file and folder in the user input directory path and print it to the screen.
#Generate the file’s MD5 hash using Hashlib, assign the MD5 hash to a variable. Print the variable to the screen along with a timestamp, file name, file size, and complete file path

import os
import os.path
import hashlib 

def usermenu_os():
    method_menu = """
    **********************************
    **                              **
    *     Select an OS               *
    *    1. Windows                  *
    *    2. Linux                    *
    **                              **
    **********************************
    """
    os_type = input(method_menu) 
    # upon selection of option 1 or 2, the next output prompts the user for a filename, then a directory 
    user_file = input("please enter a file name that you'd like to find: ")
    user_dir = input("Please enter a directory path to search in: ")
    if os_type == '1':
        windows_select(user_dir, user_file)
    elif os_type == '2':
        linux_select(user_dir, user_file)
    else:
        print("Please choose a valid response!")
        usermenu_os()

def windows_select(directory, file):
    num_files = 0
    correct_files = 0
    fullpath = "C:\\" + directory 
    for filename in os.listdir(fullpath):
        num_files += 1
        if os.path.isdir(path):
            print(file + " has been located in " + directory + "!")
        else:
            num_files += 1
    print("There were " + str(correct_files) + " matching file names found and " + str(num_files) + " were searched in this directory.")

def linux_select(directory, file):
    num_files = 0
    correct_files = 0
    for filename in os.listdir(directory):
        num_files += 1
        if os.path.isdir(path):
            hash_path = path.encode('utf-8')
            hashed_path2 = hashlib.md5(hash_path)
            print(hashed_path2)
            print(file + " has been located in " + directory + "!")
        else:
            num_files += 1
    print("There were " + str(correct_files) + " matching file names found and " + str(num_files) + " were searched in this directory.")


usermenu_os()
