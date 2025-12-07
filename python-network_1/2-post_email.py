#!/usr/bin/python3
"""
Sends a POST request to the given URL with an email parameter
and displays the body of the response (decoded in utf-8).
"""

import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({"email": email}).encode("ascii")
    req = urllib.request.Request(url, data=data)

    with urllib.request.urlopen(req) as response:
        body = response.read().decode("utf-8")
        print(body)

