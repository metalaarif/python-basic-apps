#!/usr/bin/python3
class RockPaperScissors:
    '''
    Rock Paper Scissor game using Class
    '''

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def printPlayer1(self):
        print("Player1 is the Winner")

    def printPlayer2(self):
        print("Player2 is the winner")

print("Choose \n1. Rock \n2. Paper \n3. Scissor ")
r = 1
p = 2
s = 3
player1 = int(input("Player1 choice: "))
player2 = int(input("Player2 choice: "))
game = RockPaperScissors(player1, player2)
if player1 == r and player2 == p:
    game.printPlayer2()
elif player1 == r and player2 == s:
    game.printPlayer1()
elif player1 == p and player2 == r:
    game.printPlayer1()
elif player1 == p and player2 == s:
    game.printPlayer2()
elif player1 == s and player2 == r:
    game.printPlayer2()
elif player1 == s and player2 == p:
    game.printPlayer1()
elif player1 == r and player2 == r or player1 == p and player2 == p or player1 == s and player2 == s:
    print("It is Tie")
else:
    print("Opps!! Error")