# This file contain game board diplaying.
# 🙌 Good job

def print_board(dict_1):
    print('| ' + ' | '.join(dict_1[1] + [' '] * (5 - len(dict_1[1]))) + ' |')
    print('| ' + ' | '.join(dict_1[2] + [' '] * (5 - len(dict_1[2]))) + ' |')
    print('| ' + ' | '.join(dict_1[3] + [' '] * (5 - len(dict_1[3]))) + ' |')
    print('| ' + ' | '.join(dict_1[4] + [' '] * (5 - len(dict_1[4]))) + ' |')
    print('| ' + ' | '.join(dict_1[5] + [' '] * (5 - len(dict_1[5]))) + ' |')
    print('| ' + ' | '.join(dict_1[6] + [' '] * (5 - len(dict_1[6]))) + ' |')
    print('| ' + ' | '.join(dict_1[7] + [' '] * (5 - len(dict_1[7]))) + ' |')
        
def start ():    
    input("Enter any key to start...")
    print("start ")
    player_1 = input("player1: enter your name:")
    player_2 = input("player2: enter your name:")






