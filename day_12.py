import util


def part1(start, transitions):
	current = list(start[:])
	next = list(start[:])
	for gen in range(20):
		for i in range(len(start)-5):
			for match, state in transitions:
				if current[i:i+5] == match:
					next[i+2]=state
		current = next
		print(''.join(current))
	util.Answer(1, None)

		
def part2(start, transitions):
	util.Answer(2, None)


if __name__ == "__main__":
	data = util.ReadPuzzle()
	start = data[0][15:]
	transitions = []
	for line in data[2:]:
		match,state = line.split(' => ')
		transitions.append((list(match[:]),state))
	part1(start, transitions)
	part2(start, transitions)
