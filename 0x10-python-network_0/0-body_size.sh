#!/bin/bash
# This script takes in a URL, sends a request to that URL, and displays the size of the body of the response
echo "$(echo "$(curl -Is "$1" | grep Content-Length)" | cut --complement -d " " -f1)"
