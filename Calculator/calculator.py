def calc(number1,number2,ops):
	if ops not in "+-/*":
		return "Only +-/*  !!"
	if ops == "+":
		return(str(number1) + " " + ops + " " + str(number2) + " = " + str(number1+number2))
	elif ops == "-":
		return(str(number1) + " " + ops + " " + str(number2) + " = " + str(number1-number2))
	elif ops == "/":
		return(str(number1) + " " + ops + " " + str(number2) + " = " + str(number1/number2))
	elif ops == "*":
		return(str(number1) + " " + ops + " " + str(number2) + " = " + str(number1*number2))

while True:

	number1 = int(input("Please enter first number: "))
	number2 = int(input("Please enter second number: "))
	ops = input("Choose between +,-,/,* ")

	print(calc(number1,number2,ops))


