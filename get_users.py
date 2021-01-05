#!/usr/bin/python3


import fileinput


with fileinput.input("/etc/passwd") as f_input:
	for line in f_input:
		fields = line.split(":")
		if int(fields[3]) >= 2000 and int(fields[3]) < 3000:
			print( fields[3], fields[0])
