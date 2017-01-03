#!/usr/bin/python

class Node(object):
	def __init__(name, neighbor, time):
		self.name = name
		self.neighbor = neighbor
		self.time = time


class Task(object):
	def __init__(start, destination, pathsNum, maxTime):
		self.start = start
		self.destination = destination
		self.pathsNum = pathsNum
		self.maxTime = maxTime


def build_graph(alist):
	graph = []
	for path in alist:
		parsed = path.split(' ')
		node = Node(parsed[0], parsed[1], parsed[2])
		graph.append(node)
	return graph


def parseInput(content):
	pathsIdx = 1
	while pathsIdx < len(content):
		pathsNum = content[pathsIdx]
		firstLine = content[pathsIdx - 1].rstrip().split(' ')
		start = firstLine[0]
		destination = firstLine[1]
		ls_paths = []
		for i in xrange(pathsNum):
			ls_paths.append(content[pathsIdx + 1 + i])
		graph = build_graph(ls_paths)
		maxTime = content[pathsIdx + pathsNum + 1]
		pathsIdx = pathsIdx + pathsNum + 1 + 2
	

def main(filename):
	f = open(filename, 'r')
	output = open('ansRoadMap.txt', 'w')
	f.readline() # skip the first line
	ls_tasks = parseInput(f.readlines())

