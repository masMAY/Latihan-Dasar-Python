#function is declare by def as follow : -> def functionname :

#function without paramater
print 'function without parameter'

def function_without_parameter():
    for j in range(10,1,-2):
        print 'looping without parameter at ',j

print 'function with parameter'

def function_parameter(akhir, langkah):
    for i in range(1,akhir, langkah):
        print 'looping with parameter at', i

#utilize function that we declared
print 'example of utilize function '
print 'Result', function_without_parameter()
print 'Result', function_parameter(10,3)


#return function -->function will give the result return to caller
print "Return function below :"

def ret_func_no_param():
    result = 0
    for j in range (1,10):
        result += j
    return result

def ret_func_param(akhir, langkah):
    result = 0
    for i in range(20,akhir,langkah):
        result+=i
    return result

#utilize return function that we declared
print 'Result return function without parameter :', ret_func_no_param()
print 'Result return function without parameter :', ret_func_no_param()
print 'Result return function include parameter', ret_func_param(1,-3)
print 'Result return function include parameter', ret_func_param(5,-10)

#Default Argument in python --> we have declared value in inital function

print 'Example of default argument in biodata function'
def print_biodata(name, city, age=17):
    print "Name : ", name
    print "City :", city
    print "Age :", age
    return

print "Calling the function without default argument"
print_biodata("Muhamad Arief Yulianto", "Jepara", 15)

print "Calling the function with default argument"
print_biodata("masMAY", "Jepara")

#Variabel length argument -->it can be handled n argumen --> def name(arg1,arg2,*narg)
#note : it should be declared use * and put in the last argument

def print_rapot(name, id, *scores):
    print "Name :", name
    print "Id :", id
    print "Record Score :"
    j = 1
    for score in scores :
        print "score at %d :%d" %(j,score)
        j= j+1
    return

print "utilize variabel length"
print_rapot("Muhamad Arief Y",14336,100,89,39,50,78,98,100)


#Keyword argument --> namefunc("name"="value")
#it shout be assign when you call the function as a random parameter

#Keyword-length argument in function --> it can be handled additional argument --> def name(arg1,arg2,**narg)
#note : it should be store in dictionary form

def print_report(name,id,**add_data):
    print "Name :", name
    print "Id :", id
    print "Record other data :"
    j=1
    for data in add_data:
        print "%s:%s"%(data,add_data[data]) #parsing add argument via looping


    return

#utilize function with full fill all parameter
print "keyword length argment, the other document will be handle in dictionary :"
print_report("Muhamad Arief y",143687,email="masMAY@gmail.com", telp = "0812-9989-1234", facebook = "www.facebook.com/masmay")

#Pass by Reference and pass by value in function --> in python all value will pass by reference, it means if we will change argument
#in the function so the argument value in the function will change too.

def list_func(list):
    list = [1,2,3,4,5]
    print list

def other_list_func(list):
    list.append([10,20,30])
    print list

test_list = [10,20,30]
list = [100,200,300]

print "Does test_list change?"
print test_list
list_func(test_list)
print test_list
print test_list
other_list_func(test_list)
print test_list


print "Does list change?"
print list
list_func(list)
print list
print list
other_list_func(list)
print list


#scope variable --> variable that can be accessed as universal or local
# global namevar

def test_func():
    number = 10
    print "The number in this function is :", number

def global_var_func():
    global number
    number = 15
    print "The number in this function is :", number

number = 1000

#no global argument
print "The number value before call function :", number
test_func()
print "The number value after call function :", number

#utilize global argument
print "The number value before call function :", number
global_var_func()
print "The number value after call function :", number