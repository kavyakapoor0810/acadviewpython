import time,os,datetime
#question1

''' t1=time.localtime()
print(time.asctime(t1))
when we run this we get time.struct_time(tm_year=2018, tm_mon=6, tm_mday=21, tm_hour=21, tm_min=52, tm_sec=42, tm_wday=3, tm_yday=172, tm_isdst=0)
there are 9 values in time tuple 
 index 0-8 can be used for varies fields 
 eg
 t2=time.localtime(0)
  print(time.asctime(t2)
  this will tell us year 1970 1st jan '''

#question2

t1=time.localtime()
print(time.asctime(t1))

#question3

from datetime import date
d=date.today()
print(d.month)

#question4

from datetime import date
d=date.today()
print(d.day)

#question5
d1=datetime.date.today()
d1.strftime("%d%m%y")
print(d1.day)

#question6

print(time.localtime())

#question7

import math
n=int(input("enter number"))
print(math.factorial(n))

#question8
x=int(input("enter number"))
y=int(input("enter number"))
print(math.gcd(x,y))

#question9
print(os.getcwd())

print(os.environ)