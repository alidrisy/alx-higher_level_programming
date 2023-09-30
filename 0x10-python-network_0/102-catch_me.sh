#!/bin/bash
# This script takes in a URL and displays all HTTP methods the server will accept.
curl -LX PUT -s 0.0.0.0:5000/catch_me_3 -H "Origin:School"
