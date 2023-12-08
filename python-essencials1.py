from random import randrange

USER_SYMBOL = "O"
MACHINE_SYMBOL = "X"

board = [[1, 2, 3], [4, MACHINE_SYMBOL, 6], [7, 8, 9]]

fields = [
  (0,0),
  (0,1),
  (0,2),
  (1,0),
  (1,1),
  (1,2),
  (2,0),
  (2,1),
  (2,2)
]

win_combinations = [
  [(0, 0), (0, 1), (0, 2)],
  [(0, 0), (1, 0), (2, 0)],
  [(0, 0), (1, 1), (2, 2)],
  [(0, 1), (1, 1), (2, 1)],
  [(0, 2), (1, 2), (2, 2)],
  [(0, 2), (1, 1), (2, 0)],
  [(1, 0), (1, 1), (1, 2)],
  [(2, 0), (2, 1), (2, 2)]
]

def display_board():
  print("+-------+-------+-------+")
  print("|       |       |       |")
  print("|  ", board[0][0], "  |  ", board[0][1], "  |  ", board[0][2], "  |")
  print("|       |       |       |")
  print("+-------+-------+-------+")
  print("|       |       |       |")
  print("|  ", board[1][0], "  |  ", board[1][1], "  |  ", board[1][2], "  |")
  print("|       |       |       |")
  print("+-------+-------+-------+")
  print("|       |       |       |")
  print("|  ", board[2][0], "  |  ", board[2][1], "  |  ", board[2][2], "  |")
  print("|       |       |       |")
  print("+-------+-------+-------+")

def machine_move():
  free_fields = make_list_of_free_fields()
  current_value = MACHINE_SYMBOL
  while current_value == MACHINE_SYMBOL or current_value == USER_SYMBOL:
    free_random_field = free_fields[randrange(len(free_fields))]
    row = free_random_field[0]
    column = free_random_field[1]
    current_value = board[row][column]
  board[row][column] = MACHINE_SYMBOL

def user_move():
  try:
    user_move = int(input("Enter your move: "))
    if user_move not in range(1, len(fields) + 1):
      print("Please enter a movement between 1 and 9.")
      return
    position = fields[user_move - 1]
    current_value = board[position[0]][position[1]]
    if current_value == MACHINE_SYMBOL or current_value == USER_SYMBOL:
      print("This movement is not available.")
      return
    board[position[0]][position[1]] = USER_SYMBOL
  except ValueError:
    print("Please enter a valid movement.")

def make_list_of_free_fields():
  free_fields = []
  for field in fields:
    row = field[0]
    column = field[1]
    if board[row][column] != MACHINE_SYMBOL and board[row][column] != USER_SYMBOL:
      free_fields.append((row, column))
  return free_fields

def is_board_full():
  return not len(make_list_of_free_fields())

def make_list_of_movement_fields(symbol):
  movement_fields = []
  for field in fields:
    row = field[0]
    column = field[1]
    if board[row][column] == symbol:
      movement_fields.append((row, column))
  return movement_fields

def is_win_combination(movements):
  for combination in win_combinations:
    win_fields = []
    for position in combination:
      if position in movements:
        win_fields.append(True)
      else:
        win_fields.append(False)
    if False not in win_fields:
      return True
  return False
  
def victory_for(symbol):
  movements = make_list_of_movement_fields(symbol)
  if len(movements) < 3:
    return False
  return is_win_combination(movements)

display_board()

while len(make_list_of_free_fields()):
  current_number_of_free_fields = len(make_list_of_free_fields())
  while len(make_list_of_free_fields()) != current_number_of_free_fields - 1:
    user_move()
  display_board()
  if victory_for(USER_SYMBOL):
    print("You won!")
    break
  if len(make_list_of_free_fields()):
    machine_move()
    display_board()
    if victory_for(MACHINE_SYMBOL):
      print("You lose!")
      break
else:
  print("Game tied!")