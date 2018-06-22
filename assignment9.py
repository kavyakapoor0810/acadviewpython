#question1
class circle():
    radius=6

    def getArea(self):
        a=3.14*self.radius*self.radius
        print("area : " , a)

    def getCircumfrence(self):
        b=2*3.14*self.radius
        print("circumfrence : ",b)


c=circle()
c.getArea()
c.getCircumfrence()

#question2
class Student():
    def __init__(self,name,rollnumber):
        self.n=name
        self.r=rollnumber

    s=Student(x,y)
    x=input("name= ")
    y=input("rollnumber= ")
print(s.n)
print(s.r)
