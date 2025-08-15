eval = lambda x: 1 if x == 'x' else (-1 if x == 'o' else 0)


def win_val(dic):
    for i in range(1, 5):
        for j in range(0, 6):
            sums = [0, 0, 0, 0]
            for k in range(0, 4):
                try:
                    sums[0] += eval(dic[i + k][j])
                except:
                    pass
                try:
                    sums[1] += eval(dic[i][j + k])
                except:
                    pass
                try:
                    sums[2] += eval(dic[i + k][j + k])
                except:
                    pass
                try:
                    sums[3] += eval(dic[i + k][j - k])
                except:
                    pass
            if 4 in sums:
                return 'x'
            elif -4 in sums:
                return 'o'
    return ' '