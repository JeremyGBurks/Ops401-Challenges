#!/usr/bin/env python3

# Author - Jeremy Burks
# Date Last Revised - 10/20/22
# Purpose - User selects an OS, then recursively scans each file and folder in the user input directory path and print it to the screen.
# Generate the file’s MD5 hash using Hashlib, assign the MD5 hash to a variable. Print the variable to the screen along with a timestamp, file name, file size, and complete file path

import os
import os.path
import hashlib 
import datetime

def usermenu():
    user_dir = input("Please enter a directory path to search in: ")
    if os.path.exists(user_dir):
        directory_search(user_dir)
    else:
        print('Please enter a valid path')
        usermenu()

def directory_search(file):
    for filename in os.listdir(file):
        filepath = os.path.abspath(file)
        fullpath = filepath + "/" + filename
        if os.path.isdir(filename):
            directory_search(fullpath)
        else:
            hash = hashing(fullpath)
            file_size = os.path.getsize(fullpath)
            time = datetime.datetime.now()
            print(hash + 'filename ' + filename, time, file_size, fullpath)
            

def hashing(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    return hasher.hexdigest()

usermenu()

