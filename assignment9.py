#question1
class circle():
    def __init__(self,radius):
        self.radius=radius
    def getArea(self):
        a=3.14*self.radius*self.radius
        print("area : " , a)

    def getCircumfrence(self):
        b=2*3.14*self.radius
        print("circumfrence : ",b)

radius=int(input("enter radius "))
c=circle(radius)
c.getArea()
c.getCircumfrence()

#question2

class Student:
    def __init__(self,name,rollno):
        self.rollno=rollno
        self.name=name
    def display(self):
        print(self.rollno)
        print(self.name)
name=input("enter name")
rollno=input("enter rollno")

s=Student(rollno, name)
s.display()

#question3
class Temp():
    def  convertFahrenhiet(self,C):
        return (C * 9/5) + 32
    def convertCelsius(self,F):
        return (F - 32) * 5/9
t=Temp()
c = t.convertFahrenhiet(100)
f = t.convertCelsius(98.4)
print("Celsius :  ",c )
print("Fahrenhiet :" ,f)

#question4

class Movie():
    def _init_(self, name, artist, year, ratings):
        self.name = name
        self.artist = artist
        self.year = year
        self.ratings = ratings

    def display(self):
         print("The", self.name, "starring", self.artist, "has been released                     in", self.year,
                 "with the ratings", self.ratings)

    def update(self):
         name = input("Enter movie name: ")
self.name = name
artist = input("Enter artist name: ")
self.artist = artist
year = input("Enter year of release: ")
self.year = year
ratings = input("Enter ratings: ")
self.ratings = ratings
print("The", self.name, "starring", self.artist, "has been released in", self.year, "with the ratings", self.ratings)

movie = Movie('IronMan', 'Robert Downey Jr', 2008, 7.9)
movie.display()
movie.update()


#question5

class Expenditure:
    def __init__(self,savings,expenditure):
        self.savings=savings
        self.expenditure=expenditure
    def display_expense(self):
        print(self.expenditure)
        print(self.savings)
    def cal_salary(self):
        total = self.savings + self.expenditure
        print("The total salary is", total)

savings = input("Enter savings: ")
expen = input("Enter expenditure: ")
exp = Expenditure(savings, expen)
exp.display_expense()
exp.cal_salary()
