#tuples

#question1

a=(1,2,3,'s','d',"hello")
print(len(a))

#question2

b=(1,2,4,5,7,9,3)
print("max=" ,max(b))
print("min=" ,min(b))

#question3

c=(1*2*4*5*6*7)
print(c)

#set

#question1
p=set([1,2,3,4,5,6,7,8,9,10])
q=set([1,3,5,7,9])
print("difference", p-q)
print("Is q a subset of p?", q<=p)
print("Is p a superset of q?", p>=q)
print("intersection", p&q)

#dictionary

#question1

k=input(' enter your name')
l=input('enter your marks')
d={'name' : k,
   'marks' : l}
print(d)

#question3 MISSISSIPPI

m=['m','i','s','s','i','s','s','i','p','p','i']
n={'M' : m.count('m'),
   'I' : m.count('i'),
   'S': m.count('s'),
   'p': m.count('p')}
print(n)


#question2

 #tried using for loop

'''x= input("Please enter number of students:")
print ("you entered %s students" %(x))
for i in x:
       name=input("enter you name")
       marks=input("enter your marks")
      z={'name' : name ,
         'marks' : marks}
      print(z)



name=input("enter you name")
marks=input("enter your marks")
e={'name' : name,'marks' : marks}
for i in range(10):

print(e)
'''







