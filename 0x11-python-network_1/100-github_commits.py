#!/usr/bin/python3
""" Model to takes 2 arguments in order to list 10 commits"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"\
            .format(sys.argv[2], sys.argv[1])
    resp = requests.get(url)
    try:
        js_r = resp.json()
        for i in range(10):
            com = js_r[1]
            print("{}: {}".format(com.get('sha'), com.get('commit')
                                  .get('author').get('name')))
    except Exception:
        pass
