#!/bin/bash
# This script sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -si "$1" | grep HTTP | cut --complement -d " " -f1 | cut -d " " -f1
