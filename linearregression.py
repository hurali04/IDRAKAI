# Task 7: Linear Regression
import pandas as pd
import matplotlib.pyplot as plt
import load_data
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
model = LinearRegression()
model.fit(load_data.X_train, load_data.y_train)
y_pred = model.predict(load_data.X_test)
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Feature names:", load_data.data.columns[:-1])  

