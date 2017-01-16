print "Input two numbers .."
print "You will check the relation of both numbers"

number1 = raw_input("Input first number :")
number1 = int (number1)
number2 = raw_input("Input second number :")
number2 = int (number2)

if number1 == number2:
	print "%i is equal %d" %(number1, number2)
elif number1 != number2:
	print "%i is not equal %d" %(number1, number2)
elif number1 < number2:
	print "%i is less than %d" %(number1, number2)
elif number1 > number2:
	print "%i is more than %d" %(number1, number2)
elif number1 <= number2:
	print "%i is less than equal to %d" %(number1, number2)
elif number1 >= number2:
	print "%i is more than equal to %d" %(number1, number2)






