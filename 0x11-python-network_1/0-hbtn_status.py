#!/usr/bin/python3
""" Model to fetches https://alx-intranet.hbtn.io/status"""
from urllib import request


if __name__ == "__main__":
    ur = request.Request('https://alx-intranet.hbtn.io/status')
    with request.urlopen(ur) as req:
        str1 = req.read()
        print("Body response:")
        print("\t- type: {}".format(type(str1)))
        print("\t- content: {}".format(str1))
        print("\t- utf8 content: {}".format(str1.decode('utf-8')))
