#! /usr/bin/python
# File name: process.py
# Author: Joe Burton
# Date created: 6/24/18
# Date last modified: 6/24/18
# Python Version: 3.6
import time
import csv
import pymysql.cursors
import pymysql
from sys import stdout

connection = pymysql.connect(host="localhost",
							user = "root",
							password = "",
							db = "tpstest",
							charset = "utf8",
							cursorclass=pymysql.cursors.DictCursor)


sql = "SELECT `prodcode` FROM `products` WHERE `prodcode`=%s"
i = 0
c = 0
try:
	with connection.cursor() as cursor:
		ts = time.time()
		with open("data.txt", "r") as f:
			reader=csv.reader(f, delimiter="\t")
			for row in reader:
				cursor.execute(sql, (row[0]))
				result = cursor.fetchone()
				if bool(result):
					#print(str(result["prodcode"]) + " <> " + str(row[0]))
					if str(row[0]) == str(result["prodcode"]):
						#print(row[0])
						c += 1

				i += 1
				print("Read lines: " + str(i))

		tf = (time.time() - ts)/60
		print("Finished in: " + str(tf) + " Minutes.")


finally:
	connection.close()

