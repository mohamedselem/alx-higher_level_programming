#!/bin/bash
# Bash script that take in a URL, sends a request to it.
curl -s "$1" | wc -c
