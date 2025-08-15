from display import *

start()

stack = []
dict = {
    1 : [], 
    2 : [],
    3 : [],
    4 : [],
    5 : [],
    6 : [],
    7 : [],

}

while True :

    if stack and stack.pop() == "x" :

        player1_value = int(input())

        stack.append(player1_value)

        cur_list = dict[player1_value]

        cur_list.append("x")

    elif stack and stack.pop() == "o" :

        player2_value = int(input())

        stack.append(player2_value)

        cur_list = dict[player2_value]

        cur_list.append("o")
    else :

        player1_value = int(input())

        stack.append(player1_value)

        cur_list = dict[player1_value]

        cur_list.append("x")

print_board(dict)