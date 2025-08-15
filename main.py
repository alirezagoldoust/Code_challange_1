from display import *
from update import *

stack = []
board_dict = {
    1 : [], 
    2 : [],
    3 : [],
    4 : [],
    5 : [],
    6 : [],
    7 : [],
}

start()

while True :

    if stack and stack.pop() == "x" :
        player1_value = int(input())
        stack.append('o')
        cur_list = board_dict[player1_value]
        cur_list.append("o")
        ret = win_val(board_dict)

    elif stack and stack.pop() == "o" :
        player2_value = int(input())
        stack.append('x')
        cur_list = board_dict[player2_value]
        cur_list.append("x")
        ret = win_val(board_dict)

    else :
        player1_value = int(input())
        stack.append('x')
        cur_list = board_dict[player1_value]
        cur_list.append("x")
        ret = win_val(board_dict)

    if ret == 'x':
        print('x wins')
        break

    elif ret == 'o':
        print('o wins')
        break

    print_board(board_dict)