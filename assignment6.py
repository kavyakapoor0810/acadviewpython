#question1
'''for i in range(1,11):
    x=input("enter your name")
    print(x)

#question2
b=5
while(b>0):
    print(b)

#question3
l=[]
k=[]
for i in range(1,5):
    c=int(input("enter number"))
    l.append(c)
    k.append(c*c)
print(l)
print(k)

#question4
s=[1,"sakshi",3.5,2,5,"hello",2.4,2.6,"hey"]
p=[]
q=[]
r=[]
for i in s:
    if(isinstance(i,int)):
        p.append(i)
    elif (isinstance(i,str)):
        q.append(i)
    else:
        r.append(i)
print("list: ",s)
print("Integer: ", p)
print("String: ", q)
print("Float: ", r)

#question5
even=[]
odd=[]
for I in range(1,101):
    if(I%2==0):
        even.append(I)
    else:
        odd.append(I)
print("The even list",even)
print("The odd list",odd)

#question6
for I in range(0,4):
    for I in range(0,I+1):
        print("*",end="")
    print()
'''
#question7

D={'name':'kav',
   'age':20}
for i in D:
    D.get(i)
    print(i)

#question8

e=[]
for i in range(0,5):
    f=int(input("enter number"))
    e.append(f)
print(e)
z=print("enter index of number to be deleted: ")
#e = [x for x in e if x != z]

try:
    g=e.index(z)
    del e[g]
except:
    pass
print(e)





