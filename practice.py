from sklearn.preprocessing import StandardScaler
import pandas as pd

df = pd.DataFrame({
    'age': [20, 30, 40, 50, 60],
    'chol': [200, 220, 240, 260, 280]
})

scaler = StandardScaler()
scaled = scaler.fit_transform(df)

print(scaled)
