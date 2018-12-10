import re
import util


class Point:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __add__(self, rhs):
		return Point(self.x+rhs.x, self.y+rhs.y)
	def __sub__(self, rhs):
		return Point(self.x-rhs.x, self.y-rhs.y)
	def __mul__(self, rhs):
		return Point(self.x*rhs, self.y*rhs)
	def __repr__(self):
		return f"Point({self.x},{self.y})"


class PointWithVelocity:
	def __init__(self,x,y,dx,dy):
		self.pos=Point(x,y)
		self.vel=Point(dx,dy)
	def Step(self, count=1):
		self.pos+=self.vel*count
	def __repr__(self):
		return f"{self.pos},{self.vel}"


def parsedata(data):
	points=[]
	for line in data:
		vals = re.findall('\=\<\s*([0-9\-]+),\s*([0-9\-]+)\>',line)
		if len(vals) > 0:
			x,y,dx,dy = [int(v) for pair in vals for v in pair]
		else:
			print('error parsing:',line)
		points.append(PointWithVelocity(x,y,dx,dy))
	return points


def Range(points):
	x = [p.pos.x for p in points]
	y = [p.pos.y for p in points]
	return max(x),min(x),max(y),min(y)


if __name__ == "__main__":
	with open("data/puzzle_10_test.txt") as f:
		testdata = f.read().split('\n')
	testdata = parsedata(testdata)
	
	data = util.ReadData(10)
	points=parsedata(data)
	
	seconds = 0
	maxx, minx, maxy, miny = Range(points)
	lastxrange = maxx-minx+1	
	while lastxrange > maxx-minx:
		lastxrange = maxx-minx
		for p in points:
			p.Step()
		seconds+=1
		maxx, minx, maxy, miny = Range(points)
	
	for p in points:
		p.Step(-1)
				
	orig = Point(minx, miny)
	for p in points:
		p.pos -= orig

	text=[]
	for i in range(maxy-miny+1):
		text.append([" "]*(maxx-minx+1))

	for p in points:
		text[p.pos.y][p.pos.x] = "#"
	
	for line in text:
		print("".join(line))
	
	util.Answer(2, seconds-1)
