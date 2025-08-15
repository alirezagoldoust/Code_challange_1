user1 = input()
user2 = input()
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

        user1_value = int(input())

        stack.append(user1_value)

        cur_list = dict[user1_value]

        cur_list.append("x")

    elif stack and stack.pop() == "o" :

        user2_value = int(input())

        stack.append(user2_value)

        cur_list = dict[user2_value]

        cur_list.append("o")
    else :

        user1_value = int(input())

        stack.append(user1_value)

        cur_list = dict[user1_value]

        cur_list.append("x")
