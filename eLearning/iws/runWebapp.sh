#!/bin/bash
# Author: Rohtash Lakra
echo
#if [ $# -gt 0 ]; then
if [ "$1" == "production" ]; then
  gunicorn -c gunicorn.conf.py wsgi:app
else
  flask run --host=0.0.0.0
fi
echo

