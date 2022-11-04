#!/usr/bin/env python3
# Author - 
# Date Last Revised - 
# Purpose -  This Python script receives cookies a site that a user specifies, then sends them back to the web server and saves the response to an HTML file.
# it then opens the file using firefox

import requests
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

targetsite = input("Enter target site:")
# "http://www.whatarecookies.com/cookietest.asp"
response = requests.get(targetsite)
cookie = response.cookies
senditback = requests.get(targetsite, cookie)
with open("response.html", "w") as file:
    file.write(senditback.text)

driver = webdriver.Firefox()
driver.get("/Users/jeremyburks/response.html")

def bringforthcookiemonster(): 
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.
                                ' '  0  0  0 |

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)
