import util
		

class Task:
	def __init__(self, id):
		self.id = id
		self.child = set()
		self.parents = set()

	def __repr__(self):
		return "Task('{}',\n\tchild={},\n\tparents={})".format(self.id, self.child, self.parents)


def build_graph(data):
	tasks = {}
	for line in data:
		_, task, child = line.lower().split('step ')
		task_id=task[:1]
		child_id=child[:1]
		
		if task_id not in tasks:
			tasks[task_id]=Task(task_id)
		tasks[task_id].child.add(child_id)

		if child_id not in tasks:
			tasks[child_id] = Task(child_id)
		tasks[child_id].parents.add(task_id)
	return tasks


def part1(data, expected_answer):
	tasks = build_graph(data)
	completed = set()
	completing = []
	taskorder = ""
		
	while len(completed) < len(tasks):
		completing = []
		for task in tasks.values():
			if task.id not in completed and len(task.parents - completed) == 0:
				completing.append(task.id)
		
		completing.sort()
		completed.update(completing[0])
		taskorder += completing[0]
	assert taskorder.upper() == expected_answer
	util.Answer(1, taskorder.upper())


class Worker:
	def __init__(self, extra_time):
		self.extra_time = extra_time
		self.assign(None)
		
	def assign(self, task):
		self.task = task
		if task is None:
			self.time_to_completion = 0
		else:
			self.time_to_completion = ord(task.upper()) - ord("A") + 1 + self.extra_time

	def working(self):
		return self.time_to_completion > 0

	def work(self):
		"""return false on work finished"""
		if self.working():
			self.time_to_completion -= 1
		return self.working()

		
def part2(data, worker_count, extra_time, expected_answer=None):
	answer = expected_answer
	tasks = build_graph(data)
	completed = set()
	completing = []
	taskorder = ""
	elapsed = 0
	workers = []
	for i in range(worker_count):
		workers.append(Worker(extra_time))
		
	while len(completed) < len(tasks):
		# work work work
		working = sum(worker.working() for worker in workers)
		worker_stopped = False
		while working > 0 and not worker_stopped:
			elapsed += 1
			worker_stopped = (working != sum(worker.work() for worker in workers))

		# who finished working?		
		completing = []
		working = []
		for worker in workers:
			if not worker.working() and worker.task is not None:
				completing.append(worker.task)
				worker.assign(None)
			elif worker.working():
				working.append(worker.task)
		
		completing.sort()
		completed.update(completing)
		taskorder += "".join(completing)
		
		completing = []
		for task in tasks.values():
			if task.id not in completed \
				and task.id not in working \
				and len(task.parents - completed) == 0:
					completing.append(task.id)
		completing.sort()
		
		for worker in workers:
			if len(completing) > 0 and not worker.working():
				worker.assign(completing[0])
				completing = completing[1:]
		
	util.Answer(2, elapsed)
	assert elapsed == expected_answer
	

if __name__ == "__main__":
	print("*** Test Answers ***")
	testdata = [
		"Step C must be finished before step A can begin.",
		"Step C must be finished before step F can begin.",
		"Step A must be finished before step B can begin.",
		"Step A must be finished before step D can begin.",
		"Step B must be finished before step E can begin.",
		"Step D must be finished before step E can begin.",
		"Step F must be finished before step E can begin."]
	part1(testdata, "CABDFE")
	part2(testdata, 2, 0, 15)
	
	print("*** Puzzle Answers ***")
	data = util.ReadData(7)
	part1(data, "BFLNGIRUSJXEHKQPVTYOCZDWMA")
	part2(data, 5, 60, 880)
	
