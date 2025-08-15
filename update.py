

def win_val(dic):
    x_list = 0
    o_list = 0

    for i in range(len(1, 8)):
        for j in range(len(1, 6)):
            if dic[j] == "o":
                o_list += 1
            elif dic[i] == "x":
                x_list += 1
                o_list = 0
            else:
                pass

    for j in range(7, 0, -1):
        for i in range(1, 8):
            if dic[i] == "o":
                o_list += 1
            elif dic[i] == 'x':
                o_list = 0
                x_list += 1
            else:
                pass

    for i in range(1, 8):
        for j in range(1, 6):
            if (dic[i + 1]) and (dic[j + 1]) == 'o':
                o_list += 1
            elif (dic[i + 1]) and (dic[j + 1]) == 'x':
                x_list += 1
                o_list = 0
            else:
                pass

    for i in range(1, 8):
        for j in range(1, 6):
            if (dic[i - 1]) and (dic[j - 1]) == 'o':
                o_list += 1
            elif (dic[i - 1]) and (dic[j - 1]) == 'x':
                x_list += 1
                o_list = 0
            else:
                pass

    if x_list == 4:
        return (print("x_ user is the winner"))
    elif o_list == 4:
        return (print(" O_ user is the winner"))
    else:
        return (print("game over "))
