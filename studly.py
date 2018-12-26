#!/usr/bin/python3

'''
Convert a string to "StUDly CaPS"
<https://en.wikipedia.org/wiki/Studly_caps>
2018-10-09
Henry Hedden <henry@hedden.net>

This program can be imported as a Python module,
or invoked directly from the command-line.
'''

import sys
import random as r

HELP = """Usage: studly [-h] [-f [file]] [-t [text]]

Example: studly -f awesome.txt
  -h	display this message
  -f	read from file, or when file is -, read stdin
  -t	read from command-line argument"""

INVALID = """Invalid command-line arguments!
(Use `studly -h` for help)"""

'''
Converts a string to "stuDlY cAPs"
Parameter: a string
Returns: the same text in "stuDlY cAPs"
'''
def studly(s):
	r.seed()
	return "".join([c.upper() if r.randint(0,1) else c.lower() for c in s])

'''
Main method (used if invoked directly from command-line)
'''
if __name__ == "__main__":
	if len(sys.argv) > 1:
		if sys.argv[1] == "-h": # Show help
			print(HELP)
		elif sys.argv[1] == "-t": # Read command-line argument
			try:
				print(studly(sys.argv[2].strip("\"'")))
			except IndexError:
				print(INVALID)
				sys.exit(1)
		elif sys.argv[1] == "-f": # Read file
			try:
				infile = (sys.stdin if sys.argv[2]=='-' else open(sys.argv[2]))
			except IndexError:
				print(INVALID)
				sys.exit(1)
			except IOError:
				print("Failed to open file: " + sys.argv[2])
				sys.exit(2)
			for line in infile:
				print(studly(line), end="")
		else: # Generic error message
			print(INVALID)

