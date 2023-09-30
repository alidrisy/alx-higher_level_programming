#!/bin/bash
# This script takes in a URL and displays all HTTP methods the server will accept.
curl -LX PUT -i 0.0.0.0:5000/catch_me -H "Origin:School" ; echo ""
