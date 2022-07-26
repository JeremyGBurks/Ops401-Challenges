#!/usr/bin/env python3

# Author - Jeremy Burks
# Date Last Revised - 07/21/22
# Purpose - Provides a menu and takes user input---encrypts and decrypts a file, encrypts and decrypts a message depending on user selection 

# import required module
from cryptography.fernet import Fernet
from pathlib import Path
import os
import sys

stringKey = Fernet.generate_key()
fernet = Fernet(stringKey)
def get_cryptic():
    prompt =  """
        **************************************
        **     Please choose an option:     **
        **      1 = Ecrypt a file           **
        **      2 = Decrypt a file          **
        **      3 = Encrypt a message       **
        **      4 = Decrypt a message       **
        **      q = Quit                    **
        **************************************
        #####################################################
            Please enter a number 1, 2, 3 or 4
    
        #####################################################
    """ 
    prompt = input(prompt)
    if prompt == str(1):
        file = input("please enter a file path for encryption.")
        path_exists = Path(file)
        if path_exists.is_file():
            encryptFile(file)
        else:
            print("please enter valid file path")
            get_cryptic()
    elif prompt == str(2):
        file = input("please enter a file path for decryption.")
        path_exists = Path(file)
        if path_exists.is_file():
            decryptFile(file)
            get_cryptic()
        else:
            print("please enter valid file path")
            get_cryptic()
    elif prompt == str(3):
        secrets = str(input("please enter a message for encryption:"))
        encryptString(secrets, fernet)
        get_cryptic()
    elif prompt == str(4):
        secrets = str(input("please enter a message for decryption:"))
        decryptString(fernet)
        get_cryptic()
    elif prompt == 'q' or prompt.lower == 'quit':
        sys.exit(0)
    else:
        print("please enter a valid response")
        get_cryptic()    
def encryptFile(file):
    key = Fernet.generate_key()
    filename = os.path.basename(file)
    uniquekey = "/Users/jeremyburks/Ops401-Challenges/" + filename + ".key"
    if os.path.isdir(file): 
        for item in os.listdir(file):
            decryptFile("/Users/jeremyburks/Ops401-Challenges/testfolder/" + item)
            print(item)
    else:
        with open(uniquekey, 'wb') as filekey:
            filekey.write(key)
        with open(uniquekey, 'rb') as filekey:
            master_key = filekey.read() 
        f = Fernet(master_key)
        with open(file, "rb") as fileread:
            readfile = fileread.read()
    
    encryptFile = f.encrypt(readfile)
    with open(file, "wb") as filewrite:
        filewrite.write(encryptFile)
    
    print("files encrypted")
    #get_cryptic()
def decryptFile(file):   
    filename = os.path.basename(file)
    unlockkey = "/Users/jeremyburks/Ops401-Challenges/" + filename + ".key"
    with open(unlockkey, 'rb') as filekey:
        master_key = filekey.read() 
  
    fernet = Fernet(master_key)
    
    with open(file, 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(file, 'wb') as dec_file:
        dec_file.write(decrypted)
    print("files decrypted")
def encryptString(message, fernet):
    encMessage = fernet.encrypt(message.encode())
    print("original string: ", message)
    print("encrypted string: ", encMessage)
    with open("secrets.txt", "wb") as f:
        f.write(encMessage)
    return encMessage
def decryptString(fernet):
    with open("secrets.txt", "rb") as f:
        message = f.read()
    decMessage = fernet.decrypt(message).decode()
    print("decrypted string: ", decMessage)
#get_cryptic()
thepath = Path("/Users/jeremyburks/Ops401-Challenges/testfolder")
for file in os.listdir(thepath):
    decryptFile("/Users/jeremyburks/Ops401-Challenges/testfolder/" + file)
    print(file)
