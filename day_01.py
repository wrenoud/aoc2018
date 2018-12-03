from typing import List

def ReadData():
	data = []
	with open("./data/day_01.txt", "r") as f:
		for line in f:
			data.append(int(line.strip()))
	return data

def part1(inputs: List[int]):
	freq = 0
	for inp in inputs:
		freq += inp

	print(freq)

def part2(inputs: List[int]):
	freq = 0
	visited = {}
	while True:
		for inp in inputs:
			freq += inp
			if freq in visited:
				return freq
			visited[freq] = 1

if __name__ == "__main__":
	inputs = ReadData()
	part1(inputs)
	print(part2(inputs))