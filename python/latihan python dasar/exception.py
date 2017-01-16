#How to utilize exception in python

number = 19

try:
    print number/0
except:
    print "Failed Calculation"
print "this process still working"

try:
    print number/0
except ZeroDivisionError, e:
    print "Failed Calculation because of ", e
print "This process still working"

#print number/0

print "Is this process still working?" #no exception

#Index Error and Key Error in tuple, list and dictionary
list = ["merah", "kuning", "hijau"]
tuple = (1,2,3,4,5)
dictionary = {"name":"masMAY", "job":"Teaching/Frelancer"}

#utilize index error
try:
    print list[6]
except IndexError,e:
    print "Failed process because of", e
print "This process still working"

#utilize key Error
try:
    print dictionary['gender']
except KeyError,e:
    print "Failed process because of", e
print "This process still working"


#Utilize Attribute Exception
class rectangle:
    length = 0
    width = 0
    def __init__(self, p,l):
        self.length = p
        self.width = l

test_rectangle = rectangle(10,5)

try:
    print "length is :", test_rectangle.length
    print "width is :", test_rectangle.width
    print "hight is ", test_rectangle.hight
except AttributeError,e:
    print "Calling the attribute is failed because of",e

print "This process still working"

#IOE exception to handle input, process and file operation
try:
    f=open('test.txt')
except IOError,e:
    print "Open file process failed because of",e
print "This process still working"

#multiple excep
try:
    number1 = int(raw_input('input first number :'))
    number2 = int(raw_input('input second number :'))

    print "Calculation Result num1/num2 :", number1/number2
except ZeroDivisionError,e:
    print "Failed division process because of:",e
except ValueError,e:
    print "Failed division process because of :",e

print "This process still working"


#multiple exception
try:
    number1 = float(raw_input('input first number :'))
    number2 = float(raw_input('input second number :'))

    print "Calculation Result num1/num2 :", number1/number2
except (ZeroDivisionError,ValueError,TypeError),e:
    print "Failed division process because of:",e

print "This process still working"

#nested try-exception
try:
    number1 = float(raw_input('input first number :'))
    number2 = float(raw_input('input second number :'))
    try:
        print "Calculation Result num1/num2 :", number1/number2
    except ZeroDivisionError,e:
        print "Failed division process because of:", e

except ValueError,e:
    print "Failed division process because of:",e

print "This process still working"



#Creating Own Exception
#Exception negative value

class NegativeValueError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        s = "Don't accept value < 0" + str(self.value)
        return s

def checkValue(number):
    if number < 0:
        raise NegativeValueError(number)

try:
    test_number = int(raw_input("Input a number :"))
    checkValue(test_number)
except (NegativeValueError,TypeError),e:
    print "Failed process because of :",e



#Finally exception --> last decion event exception is working or not
try:
    number1 = float(raw_input('input first number :'))
    number2 = float(raw_input('input second number :'))
    try:
        print "Calculation Result num1/num2 :", number1/number2
    except ZeroDivisionError,e:
        print "Failed division process because of:", e

except ValueError,e:
    print "Failed division process because of:",e

finally:
    print "Caution your input,please!"

print "This process still working"
    