import linearregression
import load_data
from sklearn.metrics import mean_squared_error, r2_score
mse = mean_squared_error(load_data.y_test,linearregression.y_pred)

# Calculate R²
r2 = r2_score(load_data.y_test,linearregression.y_pred)

print(f"MSE: {mse}")
print(f"R²: {r2}")
