from typing import List

def ReadData():
	data = []
	with open("./data/day_02.txt", "r") as f:
		for line in f:
			data.append(line.strip())
	return data

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

	print(two, three, two*three)

def part2(inputs):
	for left in inputs:
		for right in inputs:
			if left == right:
				continue
			diff = 0
			for i in range(len(left)):
				if left[i] != right[i]:
					diff += 1
				if diff >=2:
					break
			if diff == 1:
				print(left,right)
				return

if __name__ == "__main__":
	inputs = ReadData()
	part1(inputs)
	part2(inputs)