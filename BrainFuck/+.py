#!/usr/bin/python
import sys
try:
    import pyperclip
except:
    print("You need pyperclip (pip install pyperclip)")
    exit(1)

if len(sys.argv) != 2:
	print("Usage: %s <n>" % sys.argv[0])
	exit(2)

if not sys.argv[1].isnumeric():
	print("Usage: %s <n>" % sys.argv[0])
	exit(3)

n = int(sys.argv[1])
pyperclip.copy("+"*n)