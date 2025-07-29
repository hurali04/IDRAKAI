import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {
    'Age': [22, 45, 30, 35, 28, 40, 25, None, 32, 38],
    'Class': ['First', 'Second', 'Third', 'First', 'Second', 'Third', 'First', 'Second', 'Third', 'First']
}
df = pd.DataFrame(data)

# Histogram of numerical column (Age)
df['Age'].plot(kind='hist', bins=5, edgecolor='black', title='Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Bar chart of categorical counts (Class)
df['Class'].value_counts().plot(kind='bar', color='skyblue', edgecolor='black', title='Passenger Class Counts')
plt.xlabel('Class')
plt.ylabel('Count')
plt.show()