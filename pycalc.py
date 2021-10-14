#!/usr/bin/python

import sys

count = len(sys.argv)
args = sys.argv
num1 = 0
num2 = 0
limit = 2**64
operator = ""
res = 0

def MainProgram():
	num1 = int(input("Value for number one: "))
	num2 = int(input("Value for number two: "))
	if CheckNumbers(num1, num2):
		print("For addition type '+', for subtraction type '-', for multiplication type '*', for devision type '/'. Type 'e' to edit numbers")
		operator = input("Your choice: ")
		if CheckSyntax(operator):
			Calculate(num1, num2, operator)


def CheckNumbers(num1, num2):
	if abs(num1) > limit or abs(num2) > limit:
		print("Numbers exceed the limit (2**64)")
		return False
	else:
		return True

def CheckSyntax(operator):
	if operator == "e":
		MainProgram()
	elif operator not in ["+", "-", "*", "/"]:
		print("Operators must be ")
		return False
	else:
		return True

def Calculate(num1, num2, operator):
	if operator == "/" and num2 == 0:
		print("Deviding by zero impossible")
		quit()
	elif operator == "+":
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
		MainProgram()
	
			
