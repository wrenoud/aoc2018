import util
from datetime import datetime


def ReadData():
	data = []
	for line in util.ReadData(4):
		d = datetime.strptime(line[1:17],"%Y-%m-%d %H:%M")
		m = line[19:].strip()
		data.append((d,m))
	return data

if __name__ == "__main__":
	inputs = ReadData()
	print(inputs)
