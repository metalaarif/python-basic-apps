password = "dragon"
counter = 1
# i = 0
while counter < 5:
	passwd = input("Enter your password please: ")

	if passwd != password:
		print("Please try again, this is your {} try".format(counter))
	else:
		print("Your {} attempt was the right password".format(counter))
		break
	counter += 1