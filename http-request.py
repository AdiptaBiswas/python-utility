# Code to perform GET request from an online resource
# Use "requests" module for the purpose

import requests as req

resource = inp("Enter web link: ")
document = req.get(resource)    # Grabs the whole document
print(document.status_code, "\n")   # Returns '200' if request was successful
print(document.headers, "\n")   # Returns a dictionary of header objects; Key: value pairs
document = document.text    # Converts html document to text for parsing

for p in page.split():    # Parsing every html document lines
    print(p)
