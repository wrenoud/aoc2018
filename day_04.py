import util
from datetime import datetime


def ReadData():
	data = []
	for line in util.ReadData(4):
		d = datetime.strptime(line[1:17],"%Y-%m-%d %H:%M")
		m = line[19:].strip()
		data.append((d,m))
	return sorted(data, key=lambda v: v[0])


def part1(inputs):
	sleeps = {}
	guard = None
	for t, message in inputs:
		if "Guard" in message:
			_, guard, _, _ = message.split(' ')
			if guard not in sleeps:
				sleeps[guard] = {}

if __name__ == "__main__":
	inputs = ReadData()

	
