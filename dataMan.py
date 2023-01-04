import pandas as pd
from pandas import DataFrame

data = pd.read_csv('mockSalesData.csv')
sales = pd.DataFrame(data)
salesCopy = sales.copy()

#add a new column to the dataframe that shows the total sales for each product

salesCopy["totalSales"] = salesCopy.groupby('itemId').sum()
print(salesCopy)