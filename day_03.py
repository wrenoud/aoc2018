from typing import List

import util

def ReadData():
	data = []
	for line in util.ReadData(3):
		patch, claim = line.split(" @ ")
		coord, dim = claim.split(": ")
		coordx,coordy = coord.split(",")
		dimx, dimy = dim.split("x")
		data.append(((int(coordx), int(coordy)), (int(dimx), int(dimy)), patch))
	return data

def part1(inputs):
	patches = {}
	fabric = {}
	for (coordx, coordy), (dimx, dimy), patch in inputs:
		patches[patch] = {}
		for x in range(dimx):
			for y in range(dimy):
				inch = str(coordx+x) + "x" + str(coordy+y)
				if inch not in fabric:
					fabric[inch] = []
				fabric[inch].append(patch)
				patches[patch][inch] = fabric[inch]
	#print(patches)
	total = 0
	for v in fabric.values():
		if len(v) >= 2:
			total += 1
	util.Answer(1, total)
	
	for patch, inches in patches.items():
		if sum(1 for inch in inches.values() if len(inch) > 1) == 0:
			util.Answer(2, patch)
			break
			

def part2(inputs):
	pass

if __name__ == "__main__":
	inputs = ReadData()
	#inputs = [((1,3),(4,4), "#1"),((3,1), (4,4), "#2"),((5,5), (2,2), "#3")]
	part1(inputs)
	part2(inputs)
