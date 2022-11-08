#!/usr/bin/env python3

# Author:      Abdou Rockikz
# Description: XSS vulnerability scanner
# Date:        11/07/2022
# Modified by: Jeremy Burks 

import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# This function is making a request to the user provided URL. It takes the contents of the reposnse which is HTML looking for
# the form tag--it is returning everything within the form tags. The form is used to create HTML for user input. 
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

# This function gets the type of form that is found in the get_all_forms function above. It is looking for the method being used in the form
# The input type the form takes, it is putting the details about the form into a dictionary and returning the dictionary. 
def get_form_details(form):
    details = {}
    #curly braces are creating a dictionary with key value pairs
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    #creating a key called action
    details["method"] = method
    #creating a key called method
    details["inputs"] = inputs
    #creating a key called inputs
    return details
    
# This function is checking to see if the form type is text or search type form, if so it takes the input at the value field and sets it to the js_script alert tag
# It creats a dictionary of forms that have both an input name and input value
# It is checking to see if the form is using a post method, if so it makes a post request to the given URL. If it does not take a post request it makes a "get" request
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

# This is the main XSS scanning function that calls the anove functions and defines the js script that it will be injecting
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = "<script>javascript:alert(12345)</script>" 
    # Above is the java script that triggers a pop-up 
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        # above we are passing in the javascript alert into the submut form function where the function will inject the code into any forms that natch the required form type
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main
# this calls the functions against the user's URL
if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:") 
    print(scan_xss(url))



# Below is the output for a positive vulnerability detection:

# Enter a URL to test for XSS:https://xss-game.appspot.com/level1/frame
# [+] Detected 1 forms on https://xss-game.appspot.com/level1/frame.
# [+] XSS Detected on https://xss-game.appspot.com/level1/frame
# [*] Form details:
# {'action': '',
#  'inputs': [{'name': 'query',
#              'type': 'text',
#              'value': '<script>javascript:alert(12345)</script>'},
#             {'name': None, 'type': 'submit'}],
#  'method': 'get'}
# True


# Below is the output for a negative vulnerability detection:

# Enter a URL to test for XSS:http://dvwa.local/login.php
# [+] Detected 1 forms on http://dvwa.local/login.php.
# False
