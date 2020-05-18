from os import system,name
import random
from copy import deepcopy
import argparse
import math
try:
    if name=="nt":
        import msvcrt as getch
    else:
        import getch
except ImportError:
        print("Importing module....")
        system('pip install getch')

def clearscreen():
    return system("cls") if name == "nt" else system("clear")

def random_generator(board_view):
    while 1:
        row = random.randint(0, board_size-1)
        column = random.randint(0, board_size-1)
        if board_view[row][column] == 0:
            board_view[row][column] = 2
            break;
    return board_view

def initial_setup():
    board_view = [[0 for j in range(board_size)] for i in range(board_size)]
    board_view = random_generator(board_view)
    return board_view

def display_game(board_view):
    return '\n\n'.join('\t'.join(str(element) for element in row) for row in board_view)

def shift_left(board_view):
    return shift_values(board_view)

def shift_right(board_view):
    flip_board_sideways = [[board_view[i][board_size-1-j] for j in range(board_size)] for i in range(board_size)]
    new_board_view = shift_values(flip_board_sideways)
    return [[new_board_view[i][board_size - 1 - j] for j in range(board_size)] for i in range(board_size)]

def shift_upwards(board_view):
    transpose_boardview = [[board_view[j][i] for j in range(board_size)] for i in range(board_size)]
    new_board_view = shift_values(transpose_boardview)
    return [[new_board_view[j][i] for j in range(board_size)] for i in range(board_size)]

def shift_downwards(board_view):
    transpose_flip_board = [[board_view[board_size - 1 - j][i] for j in range(board_size)] for i in range(board_size)]
    new_board_view = shift_values(transpose_flip_board)
    return [[new_board_view[j][board_size - 1 - i] for j in range(board_size)] for i in range(board_size)]

def move_zero_to_end(row):
    return [not_zero for not_zero in row if not_zero != 0] + [zero for zero in row if zero == 0]

def shift_values(board_view):
    for row_num, row in enumerate(board_view):
        if 0 in row:
            board_view[row_num] = move_zero_to_end(row)
        for index, value in enumerate(board_view[row_num][:-1]):
            if board_view[row_num][index] == board_view[row_num][index + 1]:
                board_view[row_num][index] *= 2
                board_view[row_num][index + 1] = 0
                board_view[row_num] = move_zero_to_end(board_view[row_num])
    return board_view

def empty_space(board_view):
    single_list = [value for row in board_view for value in row]
    return single_list.count(0) > 0

def check_move(board_view, MOVE):
    shift_operation = {"a": shift_left, "s": shift_downwards, "d": shift_right, "w": shift_upwards}
    if MOVE != 't':
        temp = deepcopy(board_view)
        board_view = shift_operation[MOVE.lower()](board_view)
        if temp == board_view:
            print("Try another move")
            return board_view
    if empty_space(board_view):
        if MOVE != 't':
            board_view = random_generator(board_view)
        return board_view
    else:
        count = 0
        temp = deepcopy(board_view)
        for move in "wdsa":
            if temp == shift_operation[move](board_view):
                count += 1
        if count == 4:
            return "Game lost"
        else:
            return temp

def game_play(board_view):
    board_view = check_move(board_view, 't')
    if board_view =="Game lost":
        return "Game lost"
    else:
        for row in board_view:
            if NUM_TO_WIN in row:
                return "\nGame Won"
        print("Enter w/a/s/d to play or e to exit: ")
        if name == "nt":
            operation = msvcrt.getch().decode("ASCII").lower()
        else:
            operation = getch.getch().lower()   
        if operation in "wasde":
            if operation == "e":
                return "\nGame over"
            clearscreen()
            board_view = check_move(board_view,operation)
            print(display_game(board_view))
            return game_play(board_view)
        else:
            print("Invalid Move")
            return game_play(board_view)

def is_power_of_two(number):
    if number == 2:
        return True
    log_base_two = math.log(number)
    return log_base_two.is_integer()

#taking input from command line
parser = argparse.ArgumentParser()
parser.add_argument('--n', type = int, action = 'store', dest = 'board_size', default = 5)
parser.add_argument('--x', type = int, action = 'store', dest = 'NUM_TO_WIN', default = 2048)
args = parser.parse_args()
board_size = args.board_size
NUM_TO_WIN = args.NUM_TO_WIN #if is_power_of_two(args.NUM_TO_WIN) else 2048
clearscreen()
print("You must get",NUM_TO_WIN,"to win")
#driver code
if board_size == 1 and  NUM_TO_WIN == 2:
    print("Game won")
else:
    initial_board=initial_setup()
    print(display_game(initial_board))
    print(game_play(initial_board))
