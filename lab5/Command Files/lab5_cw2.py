import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
weather=pd.read_csv('weather_tidy.csv',delimiter=',')

#print(weather.to_string())

#print(weather)

######## najwieksza roznica temp ###########
weather['diff'] = weather['tmax'] - weather['tmin']
print(weather.loc[weather['diff'].idxmax()])


######## najblizsza tmax do sredniej tmax ##########################################
weather = weather.dropna()
print(weather.iloc[(weather['tmax'] - weather['tmax'].mean()).abs().argsort()[:1]])
print(weather['tmax'].mean())

######## najblizsza tmin do sredniej tmin ##########################################
print(weather.iloc[(weather['tmin'] - weather['tmin'].mean()).abs().argsort()[:1]])
print(weather['tmin'].mean())