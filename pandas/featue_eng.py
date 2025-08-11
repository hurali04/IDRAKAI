import pandas as pd

read = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

read["Age"] = read["Age"].fillna(read["Age"].mean())
read["Fare"] = read["Fare"].fillna(read["Fare"].mean())
read["Embarked"] = read["Embarked"].fillna(read["Embarked"].mode()[0])

read["AgeGroup"] = pd.cut(read["Age"], bins=[0, 12, 59, 100], labels=["Child", "Adult", "Senior"])

read["Sex"] = read["Sex"].map({"male": 1, "female": 0})

read["FamilySize"] = read["SibSp"] + read["Parch"] + 1

print(read[["Age", "AgeGroup", "Sex", "FamilySize"]].head())
