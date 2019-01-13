#Joshua Prpic
#tictactoe


import random

def chkWinner(board):
	winner = False
	
	for i in range(0, 3, 1):
		# print(i)
		if(board[i] == "x" and board[i + 3] == "x" and board[i + 6] == "x"):
			print ("x wins!")
			winner = True
			break
		
		if(board[i] == "o" and board[i + 3] == "o" and board[i + 6] == "o"):
			print ("o wins!")
			winner = True
			break
	
	for i in range(0, 9, 3):
		if(board[i] == "x" and board[i + 1] == "x" and board[i + 2] == "x"):
			print ("x wins!")
			winner = True
			break
		if(board[i] == "o" and board[i + 1] == "o" and board[i + 2] == "o"):
			print ("o wins!")
			winner = True
			break
			
	# if(winner):
		# return True
	
	if(board[0] == "x" and board[4] == "x" and board[8] == "x"):
		print ("x wins!")
		return True
	if(board[2] == "x" and board[4] == "x" and board[6] == "x"):
		print ("x wins!")
		return True
	
	if(board[0] == "o" and board[4] == "o" and board[8] == "o"):
		print ("o wins!")
		return True
	if(board[2] == "o" and board[4] == "o" and board[6] == "o"):
		print ("o wins!")
		return True

	return winner

def ai(board):
	
	# first iteration is checking win, second is to check blocks
	# 3 conditions per row x x o | x o x | o x x
	
	place = -1
	
	for i in range(0, 2, 1):
		turn = "o"
		
		if(i == 1):
			turn = "x"
		
		for j in range(0, 3, 1):
			# print(j)
			if(board[j] == turn and board[j + 3] == turn and empty(board, (j + 6))):
				place = j + 6
				break
			if(board[j] == turn and board[j + 6] == turn and empty(board, (j + 3))):
				place = j + 3
				break
			if(board[j + 3] == turn and board[j + 6] == turn and empty(board, j)):
				place = j
				break
			
		for j in range(0, 9, 3):
			# print(j)
			if(board[j] == turn and board[j + 1] == turn and empty(board, (j + 2))):
				place = j + 2
				break
			if(board[j] == turn and board[j + 2] == turn and empty(board, (j + 1))):
				place = j + 1
				break
			if(board[j + 1] == turn and board[j + 2] == turn and empty(board, j)):
				place = j
				break
		
		if(place == -1):
			if(board[0] == turn and board[4] == turn and empty(board, 8)):
				place = 8
			if(board[0] == turn and board[8] == turn and empty(board, 4)):
				place = 4
			if(board[4] == turn and board[8] == turn and empty(board, 0)):
				place = 0
			
			if(board[2] == turn and board[4] == turn and empty(board, 6)):
				place = 6
			if(board[2] == turn and board[6] == turn and empty(board, 4)):
				place = 4
			if(board[4] == turn and board[6] == turn and empty(board, 2)):
				place = 2
		
		if(place != -1):
			return place
	
	
	
	
	new = True
	while(new):
		num = random.randint(0,8)
		
		if(board[num] == "x" or board[num] == "o"):
			new = True
		else:
			new = False
	
	# print("Rand")
	return num
	
def empty(board, spot):
	taken = True
	
	if(board[spot] == "x" or board[spot] == "o"):
		taken = False
	
	return taken
	
print("Welcome to tick tack toe.")

board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

print(board[0] + " | " + board[1] + " | " + board[2])
print("---------")
print(board[3] + " | " + board[4] + " | " + board[5])
print("---------")
print(board[6] + " | " + board[7] + " | " + board[8] + "\n")

#turn: True -> x first 	False -> o first
turn = True

tie = True
count = 9

for x in range(count):
	
	if(turn):
		print("User: ")
		uInput = int(input())
		uInput -= 1
	else:
		uInput = ai(board)
		display = uInput + 1
		print("CPU: \n" + str(display))
	
	if(board[uInput] == "x" or board[uInput] == "o"):
		count += 1
	else:
		if(turn):
			board[uInput] = "x"
			turn = False
		else:
			board[uInput] = "o"
			turn = True
	
	print(board[0] + " | " + board[1] + " | " + board[2])
	print("---------")
	print(board[3] + " | " + board[4] + " | " + board[5])
	print("---------")
	print(board[6] + " | " + board[7] + " | " + board[8] + "\n")
	
	
	
	if(chkWinner(board)):
		# print("things")
		tie = False
		break
	
if(tie):
	print("Tie game")
	
