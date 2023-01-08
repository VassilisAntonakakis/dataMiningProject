import pandas as pd
from pandas import DataFrame
import numpy as np

data = pd.read_csv('Bakery Sales.csv')
sales = pd.DataFrame(data)
salesCopy = sales.copy
salessum = sales.iloc[0:0]
print(data)
#change the values Mon to 1, Tue to 2, Wed to 3, Thu to 4, Fri to 5, Sat to 6, Sun to 7 in the day of week column of the sales dataframe
data['day of week'] = data['day of week'].replace(['Mon', 'Tue', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun'], [1, 2, 3, 4, 5, 6, 7])

arr = sales.to_numpy()
arrsum = salessum.to_numpy()

finalSum = []

print(arr)
print ("------------")
DATE_IDX = 0
MONTH_IDX = 1
WEEKDAY_IDX = 2
tmpDay = -1
tmpMonth = -1
sumrow = None
for row in arr:
    if row[DATE_IDX] != tmpDay:
        tmpDay = row[DATE_IDX]
        tmpMonth = row[MONTH_IDX]
        if sumrow is not None:
            '''
                Craft a list out of the three first collumns
                and then append the sum of the rows that you
                want to sum as an extension.
                tmp -> holds the out line which can be appended
                on the final array
            '''
            tmp = [row[DATE_IDX], row[MONTH_IDX], row[WEEKDAY_IDX]]
            tmp.extend(sumrow)

            finalSum.append(tmp)
        sumrow = row[3:]

    if row[DATE_IDX] == tmpDay and row[MONTH_IDX] == tmpMonth:
        sumrow += row[3:]

print(finalSum)
dataCopy = pd.DataFrame(finalSum, columns=['Day','Month','day of week', 'angbutter', 'plain bread', 'jam', 'americano', 'croissant', 'caffe latte', 'tiramisu crossant', 'cacaou deep', 'pain au chocolat', 'almond croissant', 'croque monsieur', 'mad garlic', 'milk tea'])
dataCopy.to_csv('Bakery Sum Sales.csv', index=False)
