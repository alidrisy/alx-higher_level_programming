#!/usr/bin/python3
""" Model to takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        data = {'q': sys.argv[1]}
    else:
        data = {'q': ""}
    resp = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        js_r = resp.json()
        if js_r != {}:
            print("[{}] {}".format(js_r['id'], js_r['name']))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
