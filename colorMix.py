#!/usr/bin/python


def colorPredicator(alist):
	pallete = {"purple": ("red", "blue"),
				"green": ("blue", "yellow"),
				"orange": ("red", "yellow"),
				"red": ("blank", "red"),
				"yellow": ("blank", "yellow"),
				"blue": ("blank", "blue"),
				"blank": ("blank", "blank")
				}
	ans = ""
	prev = alist[0]
	ans += prev
	for i in xrange(1, len(alist)-1):
		curt = alist[i]
		choices = pallete[curt]
		if prev == choices[0]:
			nextColor = choices[1]
		else:
			nextColor = choices[0]
		ans += ' ' + nextColor
		prev = nextColor
	return ans



def main(filename):
	f = open(filename, 'r')
	output = open('ansColorMix.txt', 'w')
	for line in f:
		ls_colors = line.rstrip().split(' ')
		new_colors = colorPredicator(ls_colors)
		output.write(new_colors + '\n')
	output.close()

filename = "PracticeInput.txt"
main(filename)
