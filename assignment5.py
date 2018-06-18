#question1

a=int(input("enter year"))
if(a%4==0 and a%100!=0 or a%400==0):
    print("leap year")
else:
    print("Not a leap year")

#question2

l=input("enter length")
b=input("enter breadth")

if(l==b):
    print("it's a square")
else:
    print("it's a rectangle")

#question3

c=input("enter age of 1st person")
d=input("enter age of 2nd person")
e=input("enter age of 3rd person")
if(c>=d and c>=e):
    print("c is oldest among all")
elif(d>=c and d>=e):
    print("d is oldest among all")
else:
    print("e is oldest among all")
if (c < d and c <e):
    print("c is youngest among all")
elif (d <c and d< e):
    print("d is youngest among all")
else:
    print("e is youngest among all")

#question4

k=int(input("enter your points out of 200"))
if(k>=1 and k<=50):
    print("Sorry! No prize this time.")
elif(k>=51 and k<=150):
    print("Congratulations! You won Wooden Dog!")
elif(k>=151 and k<=180):
    print("Congratulations! You won Book!")
elif (k >= 181 and k <= 200):
    print("Congratulations! You won Chocolates!")

#question5

j=int(input("enter the no. of units, one unit costs 100"))
sum=j*100
if(sum>=1000):
    b=(sum-(sum*10/100))
    print("Amount : " ,b)
else:
    print("Amount : " ,sum)
