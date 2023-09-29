#!/usr/bin/python3
""" Model to takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""
import requests
import sys


if __name__ == "__main__":
    url = f"https://api.github.com/users/{sys.argv[1]}"
    arg = f"Bearer {sys.argv[2]}"
    header = {'Authorization': arg, 'accept': "application/vnd.github+json"} 
    resp = requests.get(url, headers=header)
    try:
        js_r = resp.json()
        if js_r != {}:
            print(js_r['id'])
        else:
            print("None")
    except Exception:
        print("None")
