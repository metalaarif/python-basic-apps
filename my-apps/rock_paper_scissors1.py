#!/usr/bin/python3
# Rock Paper and Scissors Game
'''
Write a Rock, Paper and Scissors game where, we need to take two user input and whenever user wins, Print Winner.
And ask if they want to continue or end the game. It is Draw, its draw.
'''
print("We are playing Rock, Paper Scissors Game, Choose one:")
player1 = input("Player 1: What is your name: ")
player2 = input("Player 2: What is your name: ")
R, P, S, Y = "R", "P", "S", "Y"

while True:
    user_1 = input("Rock[R] \nPaper[P] \nScissors[S] \n{} Choose: ".format(player1))
    user_2 = input("Rock[R] \nPaper[P] \nScissors[S] \n{} Choose: ".format(player2))

    if (user_1 == R and user_2 == S
        or user_1 == S and user_2 == P
        or user_1 == P and user_2 == R):
        print("{} is Winner".format(player1))
        ask = input("Do you want to play again [Y / N]: ")
        if Y == ask:
            continue
        else:
            break
    elif user_1 == user_2:
        print("It is a Draw")
        ask = input("Do you want to play again [Y / N]: ")
        if Y == ask:
            continue
        else:
            
            break
    elif (user_2 == R and user_1 == S
        or user_2 == S and user_1 == P
        or user_2 == P and user_1 == R):
        print("{} is Winner".format(player2))
        ask = input("Do you want to play again [Y / N]: ")
        if Y == ask:
            continue
        else:
            break
    else:
        print("Opps! Error")
        ask = input("Do you want to play again [Y / N]: ")
        if Y == ask:
            continue
        else:
            break
