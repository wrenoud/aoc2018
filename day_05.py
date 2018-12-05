import util


def dist(a,b):
	return abs(ord(a)-ord(b))


def react(letters):
	i = len(letters)
	tmp = letters[:]
	while i > 1:
		i-=1
		if dist(tmp[i], tmp[i-1]) == 32:
			del tmp[i]
			del tmp[i-1]
			if i > len(tmp): i = len(tmp)
	return tmp


def part1(letters):
	letters = react(letters)
	util.Answer(1, len(letters))


def part2(letters):
	letter = None
	length = None
	for v in range(ord('a'),ord('z')+1):
		t = chr(v)
		tmp = react(list(l for l in letters if l.lower() != t))
		if letter is None or len(tmp) < length:
			letter = t
			length = len(tmp)
		print(t,len(tmp))
	util.Answer(2, (letter, length))


if __name__ == "__main__":
	data, = util.ReadData(5)
	letters = list(c for c in data)
	part1(letters)
	part2(letters)
