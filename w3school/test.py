#!/bin/python3
def func(fname, lname):
	print("Welcome {} {} to the world of Python!". format(fname, lname))

def main():
	a = input("What is your firstname: ")
	b = input("What is your lastname: ")
	func(a, b)

main()
