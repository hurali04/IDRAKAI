import pandas as pd

read = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

read["Age"] = read["Age"].fillna(read["Age"].mean())
read["Fare"] = read["Fare"].fillna(read["Fare"].mean())
read["Embarked"] = read["Embarked"].fillna(read["Embarked"].mode()[0])
read["Sex"] = read["Sex"].map({"male": 1, "female": 0})
read["FamilySize"] = read["SibSp"] + read["Parch"] + 1
read["AgeGroup"] = pd.cut(read["Age"], bins=[0, 12, 59, 100], labels=["Child", "Adult", "Senior"])

fare_by_class = read.groupby("Pclass")["Fare"].mean()
print("Average Fare per Class:\n", fare_by_class)

survival_by_agegroup = read.groupby("AgeGroup")["Survived"].mean()
print("Survival Rate by Age Group:\n", survival_by_agegroup)

survival_by_familysize = read.groupby("FamilySize")["Survived"].mean()
print("Survival Rate by Family Size:\n", survival_by_familysize)
