# Python3 program to find the next optimal move for a player
from ast import Str
import os

clear = lambda: os.system('cls')

player, opponent = 'o', 'x'

# This function returns true if there are moves
# remaining on the board. It returns false if
# there are no moves left to play.
def isMovesLeft(board) :

	for i in range(3) :
		for j in range(3) :
			if (board[i][j] == ' ') :
				return True
	return False

# This is the evaluation function as discussed
# in the previous article ( http://goo.gl/sJgv68 )
def evaluate(b) :

	# Checking for Rows for X or O victory.
	for row in range(3) :	
		if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :	
			if (b[row][0] == player) :
				return 10
			elif (b[row][0] == opponent) :
				return -10

	# Checking for Columns for X or O victory.
	for col in range(3) :
	
		if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) :
		
			if (b[0][col] == player) :
				return 10
			elif (b[0][col] == opponent) :
				return -10

	# Checking for Diagonals for X or O victory.
	if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :
	
		if (b[0][0] == player) :
			return 10
		elif (b[0][0] == opponent) :
			return -10

	if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :
	
		if (b[0][2] == player) :
			return 10
		elif (b[0][2] == opponent) :
			return -10

	# Else if none of them have won then return 0
	return 0

# This is the minimax function. It considers all
# the possible ways the game can go and returns
# the value of the board
def minimax(board, depth, isMax) :
	score = evaluate(board)

	# If Maximizer has won the game return his/her
	# evaluated score
	if (score == 10) :
		return score

	# If Minimizer has won the game return his/her
	# evaluated score
	if (score == -10) :
		return score

	# If there are no more moves and no winner then
	# it is a tie
	if (isMovesLeft(board) == False) :
		return 0


	# If this maximizer's move
	if (isMax) :	
		best = -1000

		# Traverse all cells
		for i in range(3) :		
			for j in range(3) :
			
				# Check if cell is empty
				if (board[i][j]==' ') :
				
					# Make the move
					board[i][j] = player

					# Call minimax recursively and choose
					# the maximum value
					best = max( best, minimax(board,
											depth + 1,
											not isMax) )

					# Undo the move
					board[i][j] = ' '
		return best

	# If this minimizer's move
	else :
		best = 1000

		# Traverse all cells
		for i in range(3) :		
			for j in range(3) :
			
				# Check if cell is empty
				if (board[i][j] == ' ') :
				
					# Make the move
					board[i][j] = opponent

					# Call minimax recursively and choose
					# the minimum value
					best = min(best, minimax(board, depth + 1, not isMax))
				
					# Undo the move
					board[i][j] = ' '
		return best

# This will return the best possible move for the player
def findBestMove(board) :
	bestVal = -1000
	bestMove = (-1, -1)

	# Traverse all cells, evaluate minimax function for
	# all empty cells. And return the cell with optimal
	# value.
	for i in range(3) :	
		for j in range(3) :
		
			# Check if cell is empty
			if (board[i][j] == ' ') :
			
				# Make the move
				board[i][j] = player

				# compute evaluation function for this
				# move.
				moveVal = minimax(board, 0, False)

				# Undo the move
				board[i][j] = ' '

				# If the value of the current move is
				# more than the best value, then update
				# best/
				if (moveVal > bestVal) :			
					bestMove = (i, j)
					bestVal = moveVal
	return bestMove
# Driver code


def startGame():
	clear()
	print("The game has started")
	board = [
		[ ' ', ' ', ' ' ],
		[ ' ', ' ', ' ' ],
		[ ' ', ' ', ' ' ]
	]
	while(1):
		printBoard(board)
		if not (isMovesLeft):
			print("No moves left")
			return
		# Take user's input
		print("Enter your move: ")
		move = input()
		board = drawUsersMove(board,move,'x')
		# Evaluate the board
		if evaluate(board) == 10:
			print("You lost")
			return
		elif evaluate(board) == -10:
			printBoard(board)
			print("You won")
			return 
		# Check if moves left for ai
		if not (isMovesLeft(board)):
			print("It's a tie")
			return
		# Play ai's turn
		bestmove = findBestMove(board)
		board = drawUsersMove(board, bestmove[0] * 3 + bestmove[1] + 1,'o')
		# Evaluate the board
		if evaluate(board) == 10:
			print("You lost")
			return
		elif evaluate(board) == -10:
			printBoard(board)
			print("You won")
			return 
		# Check if moves left for user
		if not (isMovesLeft(board)):
			print("It's a tie")
			return
			

def printBoard(board):
	# clear()
	print(board[0][0] + "|" + board[0][1] +  "|" + board[0][2])
	print("_|_|_")
	print(board[1][0] + "|" + board[1][1] +  "|" + board[1][2])
	print("_|_|_")
	print(board[2][0] + "|" + board[2][1] +  "|" + board[2][2])

def drawUsersMove(board,move,userType):
	if(isinstance(move,str)):
		move = int(move)
	if(move == 1):
		board[0][0] = userType
	elif(move == 2):
		board[0][1] = userType
	elif(move == 3):
		board[0][2] = userType
	elif(move == 4):
		board[1][0] = userType
	elif(move == 5):
		board[1][1] = userType
	elif(move == 6):
		board[1][2] = userType
	elif(move == 7):
		board[2][0] = userType
	elif(move == 8):
		board[2][1] = userType
	elif(move == 9):
		board[2][2] = userType
	return board

startGame()	

