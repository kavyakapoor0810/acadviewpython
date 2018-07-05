#question1

import numpy as np

abc=np.random.random((10,1))
print(abc)
print("Mean of 10 random no. :",abc.mean())
print("Mean of 10 random no. :",np.mean(abc))

#question2

a=np.random.rand(20,1)
print(a)
print("Variance :", a.var())
print("Standard Deviation :",a.std())

#question3

A=np.random.random((10,20))
B=np.random.random((20,25))
C=np.dot(A,B)
print("Matrix",C)
print("Shape",C.shape)
print("Sum",np.sum(C))

#question4

def kav(k):
    return (1/(1+(np.exp(-k))))
A=np.random.rand(10,1)
print("OLD array :",A)
B=kav(A)
print("NEW array :",B)