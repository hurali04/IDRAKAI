import pandas as pd

read = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

print("Information: ", read.info())
print("Using Describe Function: ", read.describe())
print("Using Head Function: ", read.head())
print(read.isnull().sum())

read = read.drop(columns=["Cabin"])
read["Age"] = read["Age"].fillna(read["Age"].mean())
read["Embarked"] = read["Embarked"].fillna(read["Embarked"].mode()[0])

print(read.isnull().sum())
