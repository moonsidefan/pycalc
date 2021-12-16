#!/usr/bin/python

import sys

args = sys.argv[1:]
count = len(args)

number = 0
operator = "+"
operators = ["+", "-", "*", "/"]

# Reading arguments
def checkSyntax(chars):
	for i in range(len(chars)):
		if not(i % 2):
			checkNumber(chars[i])
		else:
			checkOperator(chars[i])

# Check for number syntax
def checkNumber(num):
	if num.isnumeric():
		doMath(int(num))
	else:
		print("Wrong Syntax. Type 'h' for help.")
		quit()

# Check for operator syntax
def checkOperator(oper):
	global operator
	if oper in operators:
		operator = oper
	else:
		print("Wrong Syntax. Type 'h' for help.")
		quit()

# Applying logic to the current result
def doMath(num):
	global number
	if operator == "/" and num == 0:
		print("Deviding by zero impossible, but JavaScript says it is equal to infinity.")
		quit()
	elif operator == "+":
		number += num
	elif operator == "-":
		number -= num
	elif operator == "*":
		number *= num
	elif operator == "/":
		number /= num
	else:
		input("Unknown error. Press key to exit...")
		quit()
	
# Start
if count == 1 and args[0] == "-h" or count == 1 and args[0] == "-help":
	print("The correct syntax is: number(0,1,2,3,4,5,6,7,8,9) operator(+,-,*,/) number(0,1,2,3,4,5,6,7,8,9) (and so on...)\n")
	print("Example: python pycalc.py 4000 + 6000\n")
	print("The result is: 10000\n")
	print("Note, that 'Punkt vor Strich' will be ignored since I am to lazy for that.\n")
elif count < 3:
	print("Type -h or -help for help.")
	quit()
else:
	checkSyntax(args)
	print("The result is: " + str(number))
	quit()
	
			