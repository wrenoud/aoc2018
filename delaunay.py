import util
import math


class point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def cross(self, other):
		return self.x*other.y - self.y*other.x
	
	def __sub__(self, other):
		return point(self.x - other.x, self.y - other.y)
	
	def __len__(self):
		return abs(self.x) + abs(self.y)
	
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y
	
	def __repr__(self):
		return "point({}, {})".format(self.x, self.y)


def SameSide(p1:point, p2:point, a:point, b:point):
	"""tests if p1 and p2 are on the same side of line ab"""
	# http://blackpawn.com/texts/pointinpoly/
	return (b-a).cross(p1-a) * (b-a).cross(p2-a) >= 0
    

class triangle:
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
		self.fix()

	def fix(self):
		"""ensure clockwise rotation of points"""
		if (self.b - self.a).cross(self.b - self.c) < 0:
			self.a, self.c = self.c, self.a

	def inside(self, pt):
		return SameSide(pt, self.a, self.b, self.c) and SameSide(pt, self.b, self.a, self.c) and SameSide(pt, self.c, self.a, self.b)
	
	def __repr__(self):
		return "triangle({}, {}, {})".format(self.a, self.b, self.c)
		

class delaunay:
	def __init__(self):
		self.triangles = []
		self.points = []

	def add_point(self, pt):
		self.points.append(pt)
		if len(self.points) == 3:
			self.triangles.append(triangle(*self.points))
			for point in self.points:
				point.triangles = [self.triangles[-1],]
		elif len(self.points) > 3:
			


if __name__ == "__main__":
	import unittest
	
	class TestSameSide(unittest.TestCase):
		def testSameSide(self):
			self.assertTrue(SameSide(point(1,1), point(1,2), point(0,0), point(-1,2)))
		def testNotSameSide(self):
			self.assertFalse(SameSide(point(1,1), point(-1,-2), point(0,0), point(-1,2)))

	class TestTriangle(unittest.TestCase):
		def testNoFix(self):
			t = triangle(point(1,2), point(0,0), point(-1,2))
			self.assertEqual(t.a, point(1,2))
		def testFixed(self):
			t = triangle(point(-1,2), point(0,0), point(1,2))
			self.assertEqual(t.a, point(1,2))
			self.assertEqual(t.c, point(-1,2))
		def testInside(self):
			t = triangle(point(1,2), point(0,0), point(-1,2))
			self.assertTrue(t.inside(point(0,0)))
			self.assertTrue(t.inside(point(0,1)))
			self.assertFalse(t.inside(point(0,3)))

	unittest.main()
