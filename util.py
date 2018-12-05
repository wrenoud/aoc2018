import os
import json
from typing import List
import requests


def get_session():
	env = json.load(open('env.json'))	
	cookie = requests.cookies.create_cookie(name='session', value=env['session'])
	sess = requests.session()
	sess.cookies.set_cookie(cookie)
	return sess


def ReadData(day:int) -> List[str]:
	filepath = "./data/puzzle_{:02}.txt".format(day)
	
	if not os.path.exists(filepath):
		url = "https://adventofcode.com/2018/day/{}/input".format(day)
		puzzle = get_session().get(url).text.strip()
		with open(filepath, 'w') as f:
			f.write(puzzle)
		return puzzle.split('\n')
		
	with open(filepath) as f:
		return f.read().split('\n')


def Answer(part, answer):
	print("Part {} answer:".format(part), answer)


class AdventOfCodeDay:
	pass


if __name__ == "__main__":
	
	print(ReadData(1))
