import util
import string

def same(a, b):
	return a.lower() == b.lower()
	
def will_react(a,b):
	return a != b and same(a,b)


def react(letters):
	i = len(letters)
	tmp = letters[:] # create a local copy
	while i > 1:
		i -= 1
		if will_react(tmp[i], tmp[i-1]):
			del tmp[i]
			del tmp[i-1]
			if i > len(tmp): i -= 1
	return tmp


def part1(letters):
	util.Answer(1, len(react(letters)))


def part2(letters):
	letters = react(letters) # start from the reacted string
	
	letter = None
	length = None
	for c in string.ascii_lowercase:
		tmp = list(l for l in letters if not same(l, c))
		count = len(react(tmp))
		if letter is None or count < length:
			letter = c
			length = count
	util.Answer(2, (letter, length))


if __name__ == "__main__":
	assert will_react('a', 'A')
	assert will_react('A', 'a')
	assert not will_react('a', 'a')

	assert same('a', 'A')
	assert same('A', 'a')
	assert same('a', 'a')
	
	data, = util.ReadData(5)
	letters = list(c for c in data) # bust the string out into a list
	
	part1(letters)
	part2(letters)
