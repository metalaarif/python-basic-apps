#!/usr/bin/python3
# London Academy of IT
# Python Exercise 23
'''
Write a program that gives information about James Bond Films. The program gives 4 chances to name an actor who has played
Bond and then say whether you are right or not. They should use the text below in the messages output (up to the names of the actors and so
films given). Finally they should print how well you did giving a score out of 4.
'''

movies = {"Sean Connery" : "From Russia with Love",
          "Roger Moore": "Live and let Die",
          "Pierce Brosnan": "Die Another Day",
          "Daniel Craig": "Skyfall"}

print("Try and name 4 actors who have played James Bond.")
i = 1
b = 0
while i <= 4:
    a = input("Attemp {} - Name an actor: ".format(i))
    if a in movies:
        print("Well Done! {}, was in {}".format(a, movies.get(a)))
        b += 1
    else:
        print("Sorry {}, hasn't played any James Bond movies".format(a))
    i += 1
print("You got {} out of 4".format(b))
