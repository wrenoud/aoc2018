import util


def powerlevel(x,y,id):
	rackid = x+10
	p1 = rackid * y + id
	p2 = rackid * p1
	return int(str(p2)[-3])-5


def gridpower(x,y,cell,grid):
	return sum(sum(grid[x+ix-1][y-1:y+cell-1]) for ix in range(cell))


def makegrid(id):
	grid = []
	for x in range(1,301):
		grid.append([])
		for y in range(1,301):
			grid[-1].append(powerlevel(x,y,id))
	return grid


def part1(id):
	grid = makegrid(id)
	max = 0
	maxcell = None
	for x in range(1,302-3):
		for y in range(1,302-3):
			power = gridpower(x,y,3,grid)
			if power > max:
				max = power
				maxcell = (x,y)
	util.Answer(1, maxcell)

		
def part2(id):
	grid = makegrid(id)
	max = -9999999
	maxcell = None
	for cell in range(300,1,-1):
		for x in range(1,302-cell):
			for y in range(1,302-cell):
				power = gridpower(x,y,cell,grid)
				if power > max:
					max = power
					maxcell = (x,y,cell)
		print(cell, maxcell, max)
	util.Answer(1, maxcell)


if __name__ == "__main__":
	print(powerlevel(122,79,57),-5)
	print(powerlevel(217,196,39),0)
	
	data = int(util.ReadData(11)[0])
	part1(data)
	part2(data)
