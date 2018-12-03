from typing import List

def ReadData():
	data = []
	with open("./data/day_03.txt", "r") as f:
		for line in f:
			coord, dim = line.split(" @ ")[1].split(": ")
			coordx,coordy = coord.split(",")
			dimx, dimy = dim.split("x")
			data.append(((int(coordx), int(coordy)), (int(dimx), int(dimy))))
	return data

def part1(inputs):
	patches = {}
	for (coordx, coordy), (dimx, dimy) in inputs:
		for x in range(dimx):
			for y in range(dimy):
				patch = str(coordx+x) + "x" + str(coordy+y)
				if patch not in patches:
					patches[patch] = 0
				patches[patch] += 1
	print(len(patches))
	total = 0
	for v in patches.values():
		if v >= 2:
			total += 1
	print(total)

def part2(inputs):
	pass

if __name__ == "__main__":
	inputs = ReadData()
	#inputs = [((1,3),(4,4)),((3,1), (4,4)),((5,5), (2,2))]
	print(inputs)
	part1(inputs)
	part2(inputs)