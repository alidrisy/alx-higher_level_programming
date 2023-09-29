#!/usr/bin/python3
""" Model to fetches https://alx-intranet.hbtn.io/status using requests"""
import requests
from sys import argv

if __name__ == "__main__":
    resp = requests.get(argv[1])
    print(resp.headers['X-Request-Id'])
