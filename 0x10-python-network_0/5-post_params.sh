#!/bin/bash
# This script takes in a URL, sends a POST request and parameters to the passed URL, and displays the body of the response
curl -sX POST -d "email: test@gmail.com", "subject: I will always be here for PLD" "$1"
