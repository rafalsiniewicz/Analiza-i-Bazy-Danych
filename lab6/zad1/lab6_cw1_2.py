import numpy as np 
import matplotlib as mpl 
from mpl_toolkits.mplot3d import Axes3D 
import matplotlib.pyplot as plt 
import pandas as pd
  

df = pd.read_csv("exercise.csv")
df.columns = ['y','x1','x2']
#print(df.describe())
df = df.dropna()

x1 = df.iloc[:,df.columns == 'x1']
x2 = df.iloc[:,df.columns == 'x2']
y = df.iloc[:, 0]  

mpl.rcParams['legend.fontsize'] = 12
  
fig = plt.figure() 
ax = fig.gca(projection ='3d') 
  
ax.scatter(x1, x2, y, label ='y') 
ax.legend() 
ax.view_init(45, 0) 
  
plt.show() 
 