#!/usr/bin/python3
""" Model to fetches https://alx-intranet.hbtn.io/status using requests"""
import requests


if __name__ == "__main__":
    resp = requests.get('https://alx-intranet.hbtn.io/status')
    respond = resp.text
    print('Body response:')
    print("\t- type: {}".format(type(respond)))
    print("\t- content: {}".format(respond))
