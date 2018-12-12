import util

def play(start, transitions, generations):
	current = ["."]*20 + list(start[:]) + ["."]*generations
	f = open("ouput.txt","w")
	for gen in range(generations):
		f.write(''.join(current)+"\n")
		nextgen = ['.']*len(current)
		for i in range(len(current)-5):
			for match, state in transitions:
				if current[i:i+5] == match:
					nextgen[i+2]=state
		current = nextgen
	f.write(''.join(current)+"\n")
	return current

def part1(start, transitions):
	current = play(start, transitions, 20)
	util.Answer(1, sum(i - 20 for i,c in enumerate(current) if c =="#"))
		
def part2(start, transitions):
	current = play(start, transitions, 100)
	util.Answer(2, sum(i - 20 + 50000000000 - 100 for i,c in enumerate(current) if c =="#"))
	

def format_data(lines):
	start = lines[0][15:]
	transitions = []
	for line in lines[2:]:
		match,state = line.split(' => ')
		transitions.append((list(match[:]),state))
	return start, transitions

if __name__ == "__main__":
	testdata = """initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #""".split("\n")
	
	data = util.ReadPuzzle()
	start, transitions = format_data(data)
	#start, transitions = format_data(testdata)
	
	part1(start, transitions)
	part2(start, transitions)
