#!/usr/bin/python3
""" Model to fetches https://alx-intranet.hbtn.io/status"""
from urllib import request

if __name__ == "__main__":
    ur = request.Request('https://alx-intranet.hbtn.io/status')
    with request.urlopen(ur) as req:
        str1 = req.read()
    print("Body response:")
    print(f"   - type: {type(str1)}")
    print(f"   - content: {str1}")
    print(f"   - utf8 content: {str1.decode('ascii')}")
