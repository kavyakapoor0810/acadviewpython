#question1

a=input("enter number")
b=input("enter float number")
c=input("enter complex number")
d=[]
d.append(a)
d.append(b)
d.append(c)
print(d)

#question2

i=["google","apple","facebook","microsoft","tesla"]
d.append(i)
print(d)

#queation3

j=[2,3,4,5,6,2,8]
print(j.count(2))

#question4

j.sort()
print(j)

#question5

p=[1,3,5,7,9]
q=[2,4,6,8,10]
r=(p+q)
r.sort()
print(r)

#question6

k=[1,"hello","kavya",12]
k.pop(1)
print(k)
k.insert(1,"my name is ")
print(k)
print("adding 10")
k.append(10)
print(k)

#optionalquestion
x={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
odd=0
even=0
for y in x:
        if not (y % 2):
    	     even=even+1
        else:
    	     odd=odd+1
print("Number of even numbers :",even)
print("Number of odd numbers :",odd)