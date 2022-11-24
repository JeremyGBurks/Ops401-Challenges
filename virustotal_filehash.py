#!/usr/bin/env python3

# Author - Jeremy Burks
# Date Last Revised - 10/20/22
# Purpose - takes a hash of a file and runs it aginst virustotal site using an API key that is set as an environmental variable. 
# the output of this search is then put into a txt file.

# The below demo script works in tandem with virustotal-search.py from https://github.com/eduardxyz/virustotal-search, which must be in the same directory.
# Set your environment variable first to keep it out of your script here.

import os
from dotenv import load_dotenv
import requests


load_dotenv()

apikey = os.getenv('API_KEY_VIRUSTOTAL') # Set your environment variable before proceeding. You'll need a free API key from virustotal.com so get signed up there first.
hash = '99017f6eebbac24f351415dd410d522d' # Set your hash here. 

# This concatenates everything into a working shell statement that gets passed into virustotal-search.py
query = 'python3 virustotal-search.py -k ' + apikey + ' -m ' + hash

data = {
    'apikey': apikey,
    'resource': '99017f6eebbac24f351415dd410d522d',
}

response = requests.post('https://www.virustotal.com/vtapi/v2/file/report', data=data)
data=response.content

with open('virus_total_report.txt', 'wb') as outfile:
    outfile.write(data)

os.system(query)
