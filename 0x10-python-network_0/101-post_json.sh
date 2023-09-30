#!/bin/bash
# This script takes in a URL and displays all HTTP methods the server will accept.
curl -sH "Content-Type: application/json" -X POST --data $"cat $2" "$1"
