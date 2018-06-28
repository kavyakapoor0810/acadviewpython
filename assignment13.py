#question1

'''
a=3
if a<4:
    a=a/(a-3)
    print(a)'''

    #ZeroDivisionError

#question2

'''l=[1,2,3]
print(l[3])'''

#IndexError

#question3
'''
class NameError(Exception):
    pass
try:
    raise NameError("Hi there")
except NameError:
    print("An exception")
'''
#an Exception will print

#question4

'''
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
'''
#-5.0
#a/b result in 0 will print

#question5

try:
    import yourname
    a=[1,2,3,4]
    print(a[4])
except ZeroDivisionError:
    print("no. is divided by zero")
except IndexError:
    print("index does not exist")
except ImportError:
    print("import file does not exit")

#question6

class AgeToSmallError(Exception):
    pass
try:
    a=int(input("enter age"))
    if(a<18):
        raise AgeToSmallError
        print("you are not eligible")
except ValueError:
    print("please enter int value")
else:
    print("you are eligible")
finally:
    print("thankyou")
