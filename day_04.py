import util
from datetime import datetime, timedelta


def FormatData(inputs):
	data = []
	for line in inputs:
		d = datetime.strptime(line[1:17],"%Y-%m-%d %H:%M")
		m = line[19:].strip()
		data.append((d,m))
	return sorted(data, key=lambda v: v[0])


def part1(inputs):
	sleep = {}
	guard = None
	fell_asleep_time = None
	for t, message in inputs:
		if "Guard" in message:
			_, guard, _, _ = message.split(' ')
			if guard not in sleep:
				sleep[guard] = {}
		elif message == "falls asleep":
			fell_asleep_time = t
		elif message == "wakes up":
			minutes = int((t - fell_asleep_time).seconds/60)
			for i in range(minutes):
				sleep_minute = (fell_asleep_time + timedelta(minutes=i)).strftime("%H:%M")
				if sleep_minute not in sleep[guard]:
					sleep[guard][sleep_minute] = []
				sleep[guard][sleep_minute].append(minutes)
			fell_asleep_time = None
		else:
			assert False
	for guard, sleeptimes in sleep.items():
		t = list(sleeptimes.keys())[0]
		maxsleep = (t, len(sleeptimes[t]))
		totalsleep = 0
		for t, spans in sleeptimes.items():
			totalsleep += len(spans)
			if maxsleep[1] < len(spans):
				maxsleep = (t, len(spans))
		print(guard, maxsleep, totalsleep)

if __name__ == "__main__":
	test, answer = util.ReadTestData(4)
	inputs = FormatData(test)
	part1(inputs)
	print("---")
	inputs = FormatData(util.ReadData(4))
	part1(inputs)
	
