#question1
import pandas as pd
import numpy as np

d={'name':pd.Series(['Kavya','Kashish','Uday','Dhruv']),
   'age':pd.Series([20,19,20,15]),
   'mail':pd.Series(['kavyakapoor0810@gmail.com','kashish.gpt.k@gmail.com','udaychopra20@gmail.com','dhruvkapoor1202@gmail.com']),
   'phoneno':pd.Series([9849754454,3243432443,2332143455,341232434])}
df=pd.DataFrame(d,index=[1,2,3,4])
print(df)
print(df.axes)
print(df.dtypes)
print(df.shape)
print(df.values)

#question2

df=pd.read_csv('question2-20.csv')
print(df.head(5))
print(df.head(10))
print("mean",df.mean)
print("describe",df.describe())
print(df.tail(10))
print(df['MinTemp'].describe())


print("Count ",df['MinTemp'].count())
print("Min ",df['MinTemp'].min())
print("Max ",df['MinTemp'].max())
print("Mean ",df['MinTemp'].mean())
print("Median ",df['MinTemp'].median())
print("Mode ",df['MinTemp'].mode())