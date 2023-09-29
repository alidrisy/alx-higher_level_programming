#!/usr/bin/python3
""" Model to takes in a URL, sends a request to the URL and displays
displays the body of the response (decoded in utf-8) and manage
urllib.error.HTTPError exceptions"""
from urllib import request, error
from sys import argv


if __name__ == "__main__":
    ur = request.Request(argv[1])
    try:
        with request.urlopen(ur) as req:
            print(req.read().decode('utf-8'))
    except error.HTTPError as er:
        print("Error code: {}".format(er.code))
