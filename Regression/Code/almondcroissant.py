import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model, metrics
import csv
import pandas as pd


data = pd.read_csv('Bakery Sales.csv')

# defining feature matrix(X) and response vector(y)
X = data[['Day','Month']]
y = data['almond croissant']

# splitting X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4,
													random_state=1)

# create linear regression object
reg = linear_model.LinearRegression()

# train the model using the training sets
reg.fit(X_train, y_train)

# regression coefficients
print('Coefficients: ', reg.coef_)

# variance score: 1 means perfect prediction
print('Variance score: {}'.format(reg.score(X_test, y_test)))

r_sq = reg.score(X_train, y_train)
print(f"coefficient of determination: {r_sq}")

a = input('Enter a Date value for prediction\nDay (1-30): ')
b = input('Month (1-12):')
c = np.array([int(a), int(b)])
plist = c.reshape(1, -1)
df=pd.DataFrame(plist,columns=['Day','Month'])
x_pred = df
y_pred = reg.predict(x_pred)
print('Predicted value:')
print(y_pred)