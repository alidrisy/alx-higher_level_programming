#!/bin/bash
# This script takes in a URL as an argument, sends a GET request with X-School-User-Id: 98 header variable to the URL
curl -sH "X-School-User-Id: 98" "$1"
