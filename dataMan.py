import pandas as pd
from pandas import DataFrame

data = pd.read_csv('Bakery Sales.csv')
sales = pd.DataFrame(data)
salesCopy = sales.copy
print(sales)
salessum = sales.iloc[0:0]
print(salessum)
#change the values Mon to 1, Tue to 2, Wed to 3, Thu to 4, Fri to 5, Sat to 6, Sun to 7 in the day of week column of the sales dataframe
data['day of week'] = data['day of week'].replace(['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun'], [1, 2, 3, 4, 5, 6, 7])
for ind in data.index:
    if data['day of week'][ind] == data['day of week'][ind+1]:
        temp = data[ind]['angbutter'] + data[ind+1]['angbutter']
        salessum.loc['angbutter'] = temp
        print(salessum)
data.to_csv('Bakery Sales.csv', index=False)