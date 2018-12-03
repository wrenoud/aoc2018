from typing import List
import util


def part1(inputs: List[int]):
	freq = 0
	for inp in inputs:
		freq += inp
	util.Answer(1, freq)


def part2(inputs: List[int]):
	freq = 0
	visited = {0:1}
	while visited[freq] == 1:
		for inp in inputs:
			freq += inp
			if freq in visited:
				visited[freq] += 1
				break
			visited[freq] = 1
	util.Answer(2, freq)
	

if __name__ == "__main__":
	inputs = [int(line) for line in util.ReadData(1)]
	part1(inputs)
	part2(inputs)
