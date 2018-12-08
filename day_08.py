import util


class Node:
	def __init__(self):
		self.meta = None
		self.children = []
		self._value = None
	
	def value(self):
		if self._value is None:
			if len(self.children) == 0:
				print('leaf!')
				self._value = sum(self.meta)
			else:
				self._value = 0
				for m in self.meta:
					if m <= len(self.children):
						self._value += self.children[m-1].value()
		return self._value


def ReadNode(data, offset=0, metasum=0):
	children = data[offset]
	offset += 1
	metacount = data[offset]
	offset +=1
	
	root=Node()
	for i in range(children):
		child, offset, metasum = ReadNode(data, offset, metasum)
		root.children.append(child)
	
	root.meta = data[offset:offset+metacount]
	offset += metacount
	metasum += sum(root.meta)
	
	return root, offset, metasum

def part1(data):
	_, _, metasum = ReadNode(data)
	util.Answer(1, metasum)

		
def part2(data):
	root, _, _ = ReadNode(data)
	util.Answer(2, root.value())


if __name__ == "__main__":
	testdata = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split(' ')
	testdata = list(int(v) for v in testdata)
	part1(testdata)
	part2(testdata)
	
	data = util.ReadData(8)[0].split(' ')
	data = list(int(v) for v in data)
	part1(data)
	part2(data)
	
	
