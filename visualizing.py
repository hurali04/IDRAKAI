import matplotlib.pyplot as plt
import load_data
import linearregression
# 1. Predictions vs True Values
plt.scatter(load_data.y_test, linearregression.y_pred, color='blue', alpha=0.5)
plt.xlabel('True Values')
plt.ylabel('Predictions')
plt.title('True Values vs Predictions')
plt.show()

# 2. Residuals Plot
residuals = (load_data.y_test) - (linearregression.y_pred)
plt.scatter(linearregression.y_pred, residuals, color='red', alpha=0.5)
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residuals Plot')
plt.axhline(y=0, color='black', linestyle='--')  
plt.show()
