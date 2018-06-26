#! /usr/bin/python
# File name: readfile.py
# Author: Joe Burton
# Date created: 6/24/18
# Date last modified: 6/24/18
# Python Version: 3.6
import time

i = 0
ts = time.time()
with open("output.txt", "a+") as of:
	with open("data.txt", "r") as mf:
		for line in mf:
			of.write(line)
tf = time.time()
time = (tf-ts)/60
print("Finished in: " + str(time) + " Minutes. Read " + str(i) + " lines.")