#!/usr/bin/python

import sys

def aggregateCommonChars(alist):
	total = len(alist)
	container = [0 for _ in xrange(128)]
	for word in alist:
		hs = set()
		for char in word:
			if char in hs:
				continue
			hs.add(char)
			container[ord(char)] += 1
	ans = ""
	for i in xrange(len(container)):
		if container[i] == total:
			ans += chr(i)
	return ans


def main(filename):
	f = open(filename)
	f.readline()
	output = open('ansComChar.txt', 'w')
	for line in f:
		ls_line = line.rstrip().split(' ')
		newline = aggregateCommonChars(ls_line)
		output.write(newline + '\n')
	return 0;

filename = "PracticeInput.txt"
main(filename)