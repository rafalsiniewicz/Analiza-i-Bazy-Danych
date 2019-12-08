import numpy as np

import statsmodels.api as sm

import statsmodels.formula.api as smf

import pandas as pd

import matplotlib.pyplot as plt

from numpy.polynomial.polynomial import polyfit
import plotnine as p9


exercise=pd.read_csv("exercise.csv")
exercise = exercise.dropna()
#print(exercise)

results = smf.ols('y ~ x1 + x2', data=exercise).fit()
wyn=results.params
#print(results.summary())
#exercise.plot.scatter('x1', 'x2')

'''predictions = results.predict(exercise.get('x1','x2'))
plt.plot(predictions)
plt.plot(exercise.get('y'))'''

exercise=pd.read_csv("exercise.csv")

predictions = results.predict(exercise[['x1','x2']])
plt.plot(predictions, '-o')
plt.plot(exercise.get('y'), '-o')
plt.show()



