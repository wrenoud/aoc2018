from typing import List


def ReadData(day:int) -> List[str]:
	with open("./data/day_{:02}.txt".format(day)) as f:
		return f.readlines()


def Answer(part, answer):
	print("Part {} answer:".format(part), answer)


class AdventOfCodeDay:
	pass

if __name__ == "__main__":
	print(ReadData(3))
