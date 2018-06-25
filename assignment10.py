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

class cop()
    def __init__(self,name,age,work_experience,designation):
        self.n=name
        self.a=age
        self.w_e=work_experience
        self.d=designation

    def add(self):
        n=input("enter your name")
        a=input("enter age")
        w_e=input("enter your work experience")
        d=input("enter designation")

    def update(self):
        pass
class Mission(cop)

