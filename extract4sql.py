#! /usr/bin/python
# File name: extract4sql.py
# Author: Joe Burton
# Date created: 6/24/18
# Date last modified: 6/24/18
# Python Version: 3.6
import time
import csv

ts = time.time()

with open("output.txt", "a+") as o:
	with open("data.txt", "r") as f:
		reader = csv.reader(f, delimiter="\t")
		for row in reader:
			if row[0] == "101011":
				o.write(','.join(row)+"\n")

tf = (time.time() - ts)/60
print("Finished in: " + str(tf) + " Minutes.")