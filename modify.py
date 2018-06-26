#! /usr/bin/python
# File name: modify.py
# Author: Joe Burton
# Date created: 6/24/18
# Date last modified: 6/24/18
# Python Version: 3.6
import time
import csv

ts = time.time()

nummy = 101011

with open("output2.txt", "a+") as o:
	with open("output.txt", "r") as f:
		reader = csv.reader(f, delimiter=",")
		for row in reader:
			nummy += 1
			row[0] = str(nummy)
			o.write(','.join(row)+"\n")

tf = (time.time() - ts)/60
print("Finished in: " + str(tf) + " Minutes.")