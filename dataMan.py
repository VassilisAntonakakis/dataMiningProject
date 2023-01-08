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
#for column in sales: printarei thn kathe sthlh
#    print(sales[column])

arr = sales.to_numpy()
arrsum = salessum.to_numpy()
#arrsum = arr.empty_like(sales)
tmp = -1
for i in range(len(arr)):
    try:
        tmp = arr[i+1][0]
        k=0
        tmplist = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        while arr[k][0] == tmp:
            for j in range(len(arr)):
                try:
                    tmplist[1]= arr[k][1]
                    tmplist[2]= arr[k][2]
                    tmplist[3]= arr[k][3]
                    tmplist[j+3]= arr[k][j+3] + arr[k+1][j+3]
                    print(tmplist)
                except IndexError:
                    break
            k=k+1
            arrsum[k]=np.append(tmplist)
    except IndexError:
        break

dataCopy = pd.DataFrame(arrsum, columns=['Day','Month','day of week', 'angbutter', 'plain bread', 'jam', 'americano', 'croissant', 'caffe latte', 'tiramisu crossant', 'cacaou deep', 'pain au chocolat', 'almond croissant', 'croque monsieur', 'mad garlic', 'milk tea'])
dataCopy.to_csv('Bakery Sales.csv', index=False)
