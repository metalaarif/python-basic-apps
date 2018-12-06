#!/usr/bin/python3
class Rockpaperscissor:
    '''
    Rock Paper Scissor Game creating via Class
    '''
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def printPlayer1(self):
        print("The Player1 is Winner")
    def printPlayer2(self):
        print("The Player2 is Winner")

print("Please select Rock or Paper or Scissor: \nRock == [r] \nPaper == [p] \nScissors == [s]")
r, p, s = "r", "p", "s"
player1 = input("Player1 Enter: ")
player2 = input("Player2 Enter: ")
obj = Rockpaperscissor(player1, player2)
if player1 == r and player2 == p:
    obj.printPlayer2()
elif player1 == r and player2 == s:
    obj.printPlayer1()
elif player1 == p and player2 == r:
    obj.printPlayer1()
elif player1 == p and player2 == s:
    obj.printPlayer2()
elif player1 == s and player2 == r:
    obj.printPlayer2()
elif player1 == s and player2 == p:
    obj.printPlayer1()
elif player1 == r and player2 == r or player1 == p and player2 == p or player1 == s and player2 == s:
    print("It is a Tie")
else:
    print("Opps Error")
