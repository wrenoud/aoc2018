import util
from blist import blist


def Play(players, marbles):
	board = blist([0])
	player = 0
	scores = [0]*players
	current = 0
	for marble in range(1,marbles):
		if marble % 23 == 0:
			current = (current-7) % len(board)
			scores[player] += marble + board[current]
			del board[current]
		else:
			current = (current+2) % len(board)
			#board = board[:current] + blist([marble,]) + board[current:]
			board.insert(current, marble)
		player = (player + 1) % players
		if marble % int(marbles/1000) == 0:
			print(marble/int(marbles/100), "%", marble, current)
	return max(scores)


def part1(players, marbles):
	util.Answer(1, Play(players, marbles))

		
def part2(players, marbles):
	util.Answer(2, Play(players, marbles))


if __name__ == "__main__":
	#print(Play(9, 25), 32)
	print(Play(13, 7999), 146373)

	players, marbles = util.ReadData(9)[0].split(" players; last marble is worth ")
	players, marbles = int(players), int(marbles.split()[0])
	print("Players:", players, "Marbles:", marbles)
	part1(players, marbles)
	part2(players, marbles*100)
