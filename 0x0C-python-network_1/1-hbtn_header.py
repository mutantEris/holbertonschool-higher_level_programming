#!/usr/bin/python3
"""Python script that takes URL"""


from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        html = response.info()
    print(html.get("X-Request-Id"))
