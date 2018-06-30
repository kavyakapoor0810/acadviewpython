#question1

f = open("first.txt", "r")
print(f)
for line in reversed(list(open("first.txt", "r"))):
    print(line.rstrip())
print(f.readlines())
n = input("Enter number of last lines to be read: ")
f = open("first.txt")
lines=f.readlines()
print("Last lines :", lines[0:n-1])


#question2
import re
import string
word=input("enter word ")
roar=0

with open("first.txt",'r',encoding="utf8") as f:
    for line in f:
        words=line.split()
        for i in words:
            if(i==word):
                roar=roar+1
print("no. of times the word appeared :",roar)

#question3

with open("first.txt","r") as f:
    with open("red.txt", "w") as f1:
        f1.write("hello my name is kavya")
        for line in f:
            f1.write(line)

#question4
with open(“first.txt”,"r") as fh1, open(“red.txt”."r") as fh2:
    for l1, l2 in zip(fh1, fh2):
    print(l1 + l2)

#question5
import random

with open("random.txt", "w") as f:
    for i in range(int(input('How many random numbers? '))):
        line = str(random.randint(1, 100))
        f.writelines(line + '\n')
        print(line)

with open("random.txt") as f1, open("random1.txt", "w") as f2:
    lines = f1.read().splitlines()
lines.sort()

for l in lines:
    f2.write(str(l) + '\n')

