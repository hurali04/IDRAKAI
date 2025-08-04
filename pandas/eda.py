import pandas as pd
import matplotlib.pyplot as plt

read = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

read["Age"] = read["Age"].fillna(read["Age"].mean())
read["Fare"] = read["Fare"].fillna(read["Fare"].mean())
read["Embarked"] = read["Embarked"].fillna(read["Embarked"].mode()[0])
read = read.drop(columns=["Cabin", "Name", "Ticket"])
read["Sex"] = read["Sex"].map({"male": 0, "female": 1})
read["FamilySize"] = read["SibSp"] + read["Parch"] + 1

print("Overall Survival Rate:", read["Survived"].mean())

print("Survival by Class:\n", read.groupby("Pclass")["Survived"].mean())

print("Survival by Gender:\n", read.groupby("Sex")["Survived"].mean())

read["Age"].hist(bins=30)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

print("Correlation Matrix:\n", read[["Age", "Fare", "FamilySize", "Survived"]].corr())
