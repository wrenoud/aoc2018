import os
import json
from typing import List
import requests


def get_session():
	"""loads a adventofcode.com session cookie from env.json"""
	env = json.load(open('env.json'))	
	cookie = requests.cookies.create_cookie(name='session', value=env['session'])
	sess = requests.session()
	sess.cookies.set_cookie(cookie)
	return sess


def ReadData(day:int) -> List[str]:
	filepath = "./data/puzzle_{:02}.txt".format(day)
	
	if not os.path.exists(filepath):
		print("Downloading from adventofcode.com")
		url = "https://adventofcode.com/2018/day/{}/input".format(day)
		res = get_session().get(url)
		if res.status_code != 200:
			print("*** error downloading ***")
			return None
		puzzle = res.text.strip()
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
