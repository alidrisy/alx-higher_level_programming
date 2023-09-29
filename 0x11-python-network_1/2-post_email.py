#!/usr/bin/python3
""" Model to takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the
body of the response (decoded in utf-8)"""
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    data = parse.urlencode({"email": argv[2]})
    data = data.encode('utf-8')
    ur = request.Request(argv[1])
    with request.urlopen(ur) as req:
        print(req.read().decode("utf-8"))
