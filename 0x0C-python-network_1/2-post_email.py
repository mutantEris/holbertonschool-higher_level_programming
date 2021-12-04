#!/usr/bin/python3
"""Sends Email Address"""

import urllib
from urllib import request, parse
from sys import argv



if __name__ == "__main__":

    values = {'email' : argv[2] }
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        html = response.read()
        html = html.decode('utf-8')
        print(html)
