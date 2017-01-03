#!/usr/bin/python


def findMissingInts(alist):
	ans = ""
	if len(alist) <= 2:
		return ans

	head = 2 ** 31 - 1
	tail = - 2 ** 31
	for s in alist:
		if int(s) < head:
			head = int(s)
		if int(s) > tail:
			tail = int(s)

	intsExist = [False for _ in xrange(tail - head + 1)]

	for i in xrange(len(alist)):
		idx = int(alist[i]) - head
		intsExist[idx] = True
	for i in xrange(len(intsExist)):
		if intsExist[i]:
			continue
		ans += str(i + head) + ' '
#	print intsExist
#	print ans
	return ans


def main(filename):
	f = open(filename, 'r')
	output = open("ansMissInt.txt", 'w')
	f.readline()
	for line in f:
		ls_nums = line.rstrip().split(' ')
		new_nums = findMissingInts(ls_nums)
		output.write(new_nums.rstrip(' ') + '\n')
	output.close()

filename = "PracticeInput.txt"
main(filename)

#print findMissingInts(['6', '9', '8', '7', '3', '2'])