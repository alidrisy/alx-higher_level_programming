#!/usr/bin/python3
""" Model to takes in a URL, sends a request to the URL and an
email address, sends a POST request"""
import requests
from sys import argv


if __name__ == "__main__":
    resp = requests.post(argv[1], data={'email': argv[2]})
    print(resp.text)
