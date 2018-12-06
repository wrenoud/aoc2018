import util
		

def part1(data):
	x = sorted(data, key=lambda coord: coord[1][0])
	y = sorted(data, key=lambda coord: coord[1][1])
	for coord in x:
		print(coord)
	util.Answer(1, None)

		
def part2(data):
	util.Answer(2, None)


if __name__ == "__main__":
	data = util.ReadData(6)
	coords = []
	for i, line in enumerate(data):
		x, y = line.strip().split(', ')
		coords.append((i, (int(x),int(y))))
	part1(coords)
	part2(coords)
	
	
