#!/usr/bin/python

import sys

count = len(sys.argv)
args = sys.argv
num1 = 1000001
num2 = 1000001
operator = ""
res = 0

if count == 1:
	print("Type -h for help")
	quit()
elif count > 2:
	print("Too many arguments. Type -h for help")
	quit()
else:
	if args[1] == "-h":
		print("To start the program type -s")
		quit()
	elif args[1] == "-s":
		while num1 < -1000000 or num1 > 1000000 or num2 < -1000000 or num2 > 1000000:
			print("Numbers must be between -1000000 and 1000000.")
			num1 = int(input("Value for number one: "))
			num2 = int(input("Value for number two: "))
		while operator not in ["+", "-", "*", "/", "c"]:
			print("For addition type '+', for subtraction type '-', for multiplication type '*', for devision type '/'. Type 'c' to exit")
			operator = input("Your choice: ")
		if operator == "c":
			print("Exiting...")
			quit()
		elif operator == "/" and num2 == 0:
			print("Deviding by zero impossible")
			quit()
		else:
			if operator == "+":
				res = num1 + num2
				print("The result is: " + str(res))
				quit()
			elif operator == "-":
				res = num1 - num2
				print("The result is: " + str(res))
				quit()
			elif operator == "*":
				res = num1 * num2
				print("The result is: " + str(res))
				quit()
			elif operator == "/":
				res = num1 / num2
				print("The result is: " + str(res))
				quit()
			else:
				input("Unknown error. Press key to exit...")
				quit()

			