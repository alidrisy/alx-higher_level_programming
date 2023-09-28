#!/bin/bash
# This script takes in a URL, sends a request to that URL, and displays the size of the body of the response

x=$(curl -Is "$1" | grep Content-Length)
s=$(echo "$x" | cut --complement -d " " -f1)
echo "$s"
