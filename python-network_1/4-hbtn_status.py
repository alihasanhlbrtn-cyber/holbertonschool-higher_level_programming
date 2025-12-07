#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using requests
and displays the body in a specific format.
"""
import requests
if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    body = response.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
