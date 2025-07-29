import pandas as pd

data = {
    'Name': ['Asad', 'Fahad', 'Hamza'],
    'Marks': [85, 80, 75],
    'City': ['Gujranwala', 'Sialkot', 'Rawalpindi']
}
dp = pd.DataFrame(data)
dp.index = ['a', 'b', 'c']

selected_columns = dp[['City', 'Marks']]
above_70 = dp[dp['Marks'] > 71]
to_2 = dp.iloc[:2]
to_0 = dp.iloc[0]
loc_1 = dp.loc['b']
loc_2 = dp.loc['a':'c']

print("Selected Columns:\n", selected_columns)
print("\nB Graders:\n", above_70)
print("\nFirst row with iloc:\n", to_0)
print("\nRow where Name is Fahad using loc with condition:\n", dp.loc[dp['Name'] == 'Fahad'])
print("\nRow with label 'b':\n", loc_1)
print("\nRows from label 'a' to 'c':\n", loc_2)
print("\nFull DataFrame:\n", dp)
