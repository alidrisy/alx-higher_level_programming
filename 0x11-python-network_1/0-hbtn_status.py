#!/usr/bin/python3
""" Model to fetches https://alx-intranet.hbtn.io/status"""
from urllib import request


if __name__ == "__main__":
    ur = request.Request('https://alx-intranet.hbtn.io/status')
    with request.urlopen(ur) as req:
        str1 = req.read()
        print("Body response:")
        print(f"\t- type: {type(str1)}")
        print(f"\t- content: {str1}")
        print(f"\t- utf8 content: {str1.decode('ascii')}")
