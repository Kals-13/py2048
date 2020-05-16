import os
import random
from sys import argv

def clearscreen():
    return os.system("cls") if os.name == "nt" else os.system("clear")

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

def is_shift_possible(row):
    for index, value in enumerate(row[:-1]):
        if value == 0 and row[index + 1] != 0:
            return True
        elif value == row[index + 1] and value != 0:
            return True
    else:
        return False

def process_shift(board_view):
    return any(is_shift_possible(row) for row in board_view) == 1
#print(process_shift([[0,2],[0,0]]))

def shift_left(board_view):
    return shift_values(board_view) if process_shift(board_view) else False

def shift_right(board_view):
    flip_board_sideways = [[board_view[i][board_size-1-j] for j in range(board_size)] for i in range(board_size)]
    if process_shift(flip_board_sideways):
        new_board_view = shift_values(flip_board_sideways)
        return [[new_board_view[i][board_size - 1 - j] for j in range(board_size)] for i in range(board_size)]
    else:
        return False

def shift_upwards(board_view):
    transpose_boardview = [[board_view[j][i] for j in range(board_size)] for i in range(board_size)]
    if process_shift(transpose_boardview):
        new_board_view = shift_values(transpose_boardview)
        return [[new_board_view[j][i] for j in range(board_size)] for i in range(board_size)]
    else:
        return False

def shift_downwards(board_view):
    transpose_flip_board = [[board_view[board_size - 1 - j][i] for j in range(board_size)] for i in range(board_size)]
    if process_shift(transpose_flip_board):
        new_board_view = shift_values(transpose_flip_board)
        return [[new_board_view[j][board_size - 1 - i] for j in range(board_size)] for i in range(board_size)]
    else:
        return False

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

#board_size = 2
#print((shift_right([[0,2],[0,0]])))
def empty_space(board_view):
    single_list = [value for row in board_view for value in row]
    return single_list.count(0) > 0
def nand(board_view):
    situation = []
    for move in "wdsa":
        situation.append(shift_operation[move.lower()](board_view))
    return situation.count(0) == 4
def check_move(board_view, MOVE):
    shift_operation = {"a": shift_left, "s": shift_downwards, "d": shift_right, "w": shift_upwards}

    new_board_view = shift_operation[MOVE.lower()](board_view)

    if new_board_view == False:
        return "Invalid input"
    else:
        if empty_space(new_board_view):
            updated_board_view = random_generator(new_board_view)
            return updated_board_view
        else:
            return new_board_view
#shift_operation = {"a": shift_left, "s": shift_downwards, "d": shift_right, "w": shift_upwards}

#board_size=2
#print(check_move([[0,2],[0,0]],[[0,2],[0,0]],"d"))
#print(display_game(check_move([[0,0],[2,2]],"a"))
#print(display_game(check_move([[2,2,2,], [2,2,0,], [4,0,2,]],"s")))

# def game_play(board_view, operation):
#    if operation  in "wasde":
#        if operation == "e":
#            return "Game over"
#        for row in board_view:
#            if NUM_TO_WIN in row:
#                return "Game Won"
#        print(display_game(board_view))
#        operation = input("Enter w/a/s/d to play, e to exit ")
#        board_view = check_move(board_view, operation)
#        if check_move(board_view, operation) == "Game lost":
#            return "Game lost"
#        return game_play(board_view,operation)
#    else:
#        return "Invalid Move"
def game_play(board_view, operation):
    if operation in "wasde":
        if operation == "e":
            return "Game over"
        for row in board_view:
            if NUM_TO_WIN in row:
                return "Game won"
        temporary_board_view = check_move(board_view, operation)
        if temporary_board_view == "Invalid input":
            if nand(temporary_board_view):
                return "Game lost"
            else:
                print("Please enter another number!")
                operation = input("Enter w/a/s/d to play or e to exit: ")
                return game_play(board_view, operation)
        elif temporary_board_view == "Game lost":
            return "Game lost"
        else:
            new_board_view = temporary_board_view
            print(display_game(new_board_view))

            operation = input("Enter w/a/s/d to play or e to exit: ")
            return game_play(new_board_view, operation)
    else:
        print("Invalid input")
        operation = input("Enter w/a/s/d to play or e to exit: ")
        return game_play(board_view, operation)
shift_operation = {"a": shift_left, "s": shift_downwards, "d": shift_right, "w": shift_upwards}

NUM_TO_WIN = 16
board_size = 2
initial_board_view = initial_setup()
print(display_game(initial_board_view))
operation = input("Enter w/a/s/d to play or e to exit: ")
print(game_play(initial_board_view, operation))
#board_size = int(argv[2])
#NUM_TO_WIN = int(argv[4])
#print(display_game(board_view))
#print("Enter w/a/s/d")
#n=input()
#clearscreen()
#print(display_game(check_move(board_view, board_size,NUM_TO_WIN,n)))
