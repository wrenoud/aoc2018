from typing import List

import util

def part1(inputs):
	two = 0
	three = 0
	for inp in inputs:
		counts = {}
		for l in inp:
			if l not in counts:
				counts[l] = 0
			counts[l] += 1
		hasTwo = False
		hasThree = False
		for count in counts.values():
			hasTwo |= (count == 2)
			hasThree |= (count == 3)

		two += hasTwo
		three += hasThree

	util.Answer(1, two*three)

def part2(inputs):
	for left in inputs:
		for right in inputs:
			if left == right:
				continue
			common = []
			for i in range(len(left)):
				if left[i] == right[i]:
					common.append(left[i])
				if len(common) < i:
					break
			if len(common) == len(left) - 1:
				util.Answer(2, "".join(common))
				return

if __name__ == "__main__":
	inputs = util.ReadData(2)
	part1(inputs)
	part2(inputs)
