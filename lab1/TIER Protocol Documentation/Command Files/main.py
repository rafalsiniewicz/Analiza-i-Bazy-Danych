from pandas import *
df = read_csv('drinks.csv')
print(df)
df = melt(df, id_vars =['country'], 
	value_vars =['beer_servings', 'spirit_servings', 'wine_servings', 'total_litres_of_pure_alcohol'],
	var_name ='type',
	value_name ='litres') 
print(df)