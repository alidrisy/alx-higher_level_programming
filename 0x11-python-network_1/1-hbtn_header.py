#!/usr/bin/python3
""" Model to fetches https://alx-intranet.hbtn.io/status"""
from urllib import request
from sys import argv


if __name__ == "__main__":
    ur = request.Request(argv[1])
    with request.urlopen(ur) as req:
        print(req.headers['X-Request-Id'])
