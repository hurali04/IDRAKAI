import pandas as pd
data = {
    'Class': [1, 2, 3, 1, 2, 3],
    'Fare': [100, 50, 20, 120, 60, 25],
    'Age': [30, 25, None, 45, None, 22]
}
df = pd.DataFrame(data)
df_sorted = df.sort_values('Fare', ascending=False)
avg_fare = df.groupby('Class')['Fare'].mean()
missing = df.isnull().sum()

print("Sorted DataFrame:\n", df_sorted)
print("\nAverage Fare per Class:\n", avg_fare)
print("\nMissing Values:\n", missing)