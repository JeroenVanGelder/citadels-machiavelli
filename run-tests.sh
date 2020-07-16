#!/bin/bash

coverage run -m unittest discover -s tests --pattern test_*.py
coverage report --omit "*/.local/lib/python3.6/site-packages/*","tests/*","/usr/lib/python3/*" -m
coverage xml
