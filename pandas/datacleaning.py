import pandas as pd

read = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

print(read.isnull().sum())

read["Age"] = read["Age"].fillna(read["Age"].mean())
read["Fare"] = read["Fare"].fillna(read["Fare"].mean())
read["Embarked"] = read["Embarked"].fillna(read["Embarked"].mode()[0])

read = read.drop(columns=["Name", "Ticket", "Cabin"])

read["Survived"] = read["Survived"].astype("int")
read["Pclass"] = read["Pclass"].astype("int")
read["Age"] = read["Age"].astype("float")

print(read.dtypes)
print(read.isnull().sum())
