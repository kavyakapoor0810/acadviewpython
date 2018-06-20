#question1

r=float(input("enter radius"))
def area(r):
    area=3.14*r*r
    return area
A=area(r)
print(A)

#question2

n=6

def perfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if(sum==n):
         return True
    else:
        return False
print(perfect(n))
for i in range(1, 1001):
    if (perfect(i)==True):
        print(i)

#question3

def mult(k,j=1):
    print("12*"+str(j)+"=" , k*j)
    if j!=10:
        mult(k,j+1)
mult(12)

#question4

x = int(input("enter number"))
y = int(input("enter power"))
def power(x,y):
    if y==1:
        return x
    else:
        return (x*pow(x,y-1))
pow=power(x,y)
print(pow)

#question5

l={}
def factorial(i):
    if(i==1):
        return 1
    else:
        f=i*factorial(i-1)
        return (f)
m=int(input("enter a number"))
F=factorial(m)
l[m]=F
print("Dict ",l)
