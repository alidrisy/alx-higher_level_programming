#!/usr/bin/python3
""" Model to takes 2 arguments in order to list 10 commits"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits?per_page=10"\
            .format(sys.argv[1], sys.argv[2])
    resp = requests.get(url)
    try:
        js_r = resp.json()
        if js_r != {}:
            for com in js_r:
                print(com['sha'], end=": ")
                print(com['commit']['author']['name'])
        else:
            print("None")
    except Exception:
        print("None")
