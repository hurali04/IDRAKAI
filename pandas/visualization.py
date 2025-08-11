import pandas as pd
import matplotlib.pyplot as plt

read = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
read["Age"] = read["Age"].fillna(read["Age"].mean())
read["Fare"] = read["Fare"].fillna(read["Fare"].mean())
read["Embarked"] = read["Embarked"].fillna(read["Embarked"].mode()[0])
read["Sex"] = read["Sex"].map({"male": 1, "female": 0})
read["FamilySize"] = read["SibSp"] + read["Parch"] + 1
read["AgeGroup"] = pd.cut(read["Age"], bins=[0, 12, 59, 100], labels=["Child", "Adult", "Senior"])

plt.hist(read["Age"], bins=30)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

survival_rate = read.groupby("Pclass")["Survived"].mean()
plt.bar(survival_rate.index, survival_rate.values)
plt.title("Survival Rate by Pclass")
plt.xlabel("Pclass")
plt.ylabel("Survival Rate")
plt.show()
