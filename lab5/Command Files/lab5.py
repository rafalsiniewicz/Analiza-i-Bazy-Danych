import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
drinks=pd.read_csv('result_drinks.csv',delimiter=',')
print(drinks.head())
print(drinks.info())
print(drinks.describe(include='all'))

#wywolaj dla kazdej zmiennej describe() i wykres i histogram ( dla kazdej osobno)


drinks =drinks.rename(columns={'Unnamed: 0':'country'})
print(drinks.query("~(type == 'country')").head())


print(drinks.loc[:, ["type"]].head())


print(drinks.agg({"litres": [np.mean, np.max]}))

print(drinks.assign(mean_beer_servings_by_country = lambda x: x.loc[:,["country", "beer_servings"]].groupby(["country"]).transform(np.mean)).head())


drinks=pd.read_csv('drinks.csv',delimiter=',')

drinks.plot.scatter(x='beer_servings', 
	y='wine_servings',
	marker='o' 
	)
plt.show()


fig, ax = plt.subplots()
for c, df_ in drinks.groupby('country'):
    ax.scatter(df_['beer_servings'], df_['spirit_servings'], label=c)
ax.legend()
plt.show()


fig_tip_hist=px.histogram(drinks, x='beer_servings')
fig_tip_hist.show()

fig_tip_hist=px.histogram(drinks, x='spirit_servings')
fig_tip_hist.show()

fig_tip_hist=px.histogram(drinks, x='wine_servings')
fig_tip_hist.show()


fig_tip_box=px.box(drinks, 
                   x="wine_servings",
                   points='all',
                   orientation='h')

fig_tip_box.show()







