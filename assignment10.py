#question1

class Animal():
    def animal_attribute(self):
        print("method animal atrribute")
class Tiger(Animal):
    print("tiger class")
animal=Animal()
tiger=Tiger()
tiger.animal_attribute()

#question2

class A:
    def f(self):
        return self.g()
    def g(self):
        return 'A'
class B(A):
    def g(self):
        return 'B'
a=A()
b=B()
print(a.f(),b.f()) #A B
print(a.g(),b.g()) #A B

#question3
'''
class Cop():
    def add(self):
        self.name=input("enter name :")
        self.age=int(input("enter age :"))
        self.work_experience=input("work experience :")
        self.designation=input("designation :")

    def update(self):
        self.name = input("enter your name")
        self.age = int(input("enter age"))
        self.work_experience = input("enter your work experience")
        self.designation = input("enter designation")

    def display(self):
        print(self.name,self.age,self.work_experience,self.designation)
class Mission(Cop):
    def mission_details(self):
        self.details=input("enter mission name :")
    def mission_display(self):
        print("name of officer is %s whose age is %d with work experience %s and designation of %s going on mission %s" % (self.name,self.age
                                                                                                        ,self.work_experience,self.designation,self.mission_details()))
C=Cop()
M=Mission()
M.add()
M.update()
M.display()
M.mission_display()
'''
#question4

class shape():
    def input(self):
        self.l = int(input("enter length"))
        self.b = int(input("enter breadth"))
class rectangle(shape):
    def Area(self):
        self.input()
        self.A=self.l*self.b
        print("AREA OF RECTANGLE : ",self.A)
class square(shape):
    def Area(self):
        self.input()
        if(self.l==self.b):
             self.B=self.l*self.b
             print("AREA OF SQUARE : ",self.B)
        else:
            print("enter same l & b")
r=rectangle()
s=square()
r.Area()
s.Area()
