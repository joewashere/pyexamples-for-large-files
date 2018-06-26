#! /usr/bin/python
# File name: genfile.py
# Author: Joe Burton
# Date created: 6/24/18
# Date last modified: 6/24/18
# Python Version: 3.6
import time
import random

string = "101010	12	this is some file data	34	some more data	12	1	12\n"
altstring1 = "101011	12	this is some file data	34	some more data	12	1	12\n"
altstring2 = "101012	12	this is some file data	34	some more data	12	1	12\n"
altstring3 = "101013	12	this is some file data	34	some more data	12	1	12\n"
altstring4 = "101014	12	this is some file data	34	some more data	12	1	12\n"

strings = [string, altstring1, altstring2, altstring3, altstring4]



i = 0

ts = time.time()
with open("data.txt", "a+") as myfile:
	while 14000000 > i:
		myfile.write(random.choice(strings))
		i = i + 1
tf = time.time()
time = (tf-ts)/60
print("Finished in: " + str(time) + " Minutes.")