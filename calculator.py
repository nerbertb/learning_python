

x = float(input("Enter the first number: "))
operator = input ("Enter the operator you want to use: ")
y = float(input ("Enter the second number: "))

def calc (x, y):
	if operator == "+":
		return x + y
	elif operator == "-":
		return x - y
	elif operator == "/":
		return x / y
	elif operator == "*":
		return x * y
	else:
		print ("Invalid Operator!")



result = calc (x, y)
print ("The result is: ", result)