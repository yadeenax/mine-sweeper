# mine-sweeper
mine sweeper 
import random

# Constants
BOARD_SIZE = 10
NUM_MINES = 10

# Create an empty board
board = []
for i in range(BOARD_SIZE):
  row = []
  for j in range(BOARD_SIZE):
    row.append(0)
  board.append(row)

# Place the mines randomly on the board
mines_placed = 0
while mines_placed < NUM_MINES:
  i = random.randint(0, BOARD_SIZE - 1)
  j = random.randint(0, BOARD_SIZE - 1)
  if board[i][j] != "X":
    board[i][j] = "X"
    mines_placed += 1

# Calculate the number of mines in each square's neighbors
for i in range(BOARD_SIZE):
  for j in range(BOARD_SIZE):
    if board[i][j] != "X":
      # Check all 8 neighbors
      for ii in range(i - 1, i + 2):
        for jj in range(j - 1, j + 2):
          if ii >= 0 and ii < BOARD_SIZE and jj >= 0 and jj < BOARD_SIZE and board[ii][jj] == "X":
            board[i][j] += 1

# Print the board
for row in board:
  print(row)
