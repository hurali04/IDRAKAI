import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Name': ['Asad', 'Fahad', 'Hamza', 'Asad', 'Hamza', 'Fahad'],
    'Marks': [85, 80, 75, 88, 70, 65],
    'City': ['Gujranwala', 'Sialkot', 'Rawalpindi', 'Gujranwala', 'Rawalpindi', 'Sialkot']
}
df = pd.DataFrame(data)
df['Marks'].plot(kind='hist', title='Histogram of Marks')
plt.xlabel('Marks')
plt.show()
df['City'].value_counts().plot(kind='bar', title='City Count')
plt.xlabel('City')
plt.ylabel('Count')
plt.show()
