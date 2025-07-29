import pandas as pd
data={'Name':['Asad','Fahad','Hamza'],
      'Marks':[85,80,75],
      'City':['Gujranwala','Sialkot','Rawalpindi'],
      }
display=pd.DataFrame(data)
print("Display First Row",display.head(1))
print("Display Last Row",display.tail())
print("Shape of Column",display.shape)
print("Column Names",display.columns.tolist())
print("Data types of each column: ",display.dtypes)