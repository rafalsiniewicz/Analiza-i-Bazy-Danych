import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("exercise.csv")
df.columns = ['y','x1','x2']
#print(df.describe())
df = df.dropna()

X = df.iloc[:,df.columns != 'y']
Y = df.iloc[:, 0]
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state= 0)

model = linear_model.LinearRegression()
model.fit(X_train, Y_train)

coeff_df = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
#print(coeff_df)

y_pred = model.predict(X_test)
df = pd.DataFrame({'Actual': Y_test, 'Predicted': y_pred})
print(df.head(10))

df.plot(kind='bar',figsize=(10,8))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()

# Root Mean Squared Deviation
rmsd = np.sqrt(mean_squared_error(Y_test, y_pred))      
r2_value = r2_score(Y_test, y_pred)                     

print("Intercept: \n", model.intercept_)
print("Root Mean Square Error \n", rmsd)
print("R^2 Value: \n", r2_value)
