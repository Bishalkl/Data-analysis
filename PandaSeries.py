#first importing lib
import pandas as pd
import numpy as np 

# creaing panda series
g7_pop = pd.Series([35.467, 63.951, 80.940, 60.665, 127.061, 64.511, 318.523])
print(g7_pop)

# giving a name of panda series
g7_pop.name = "G7 Population in millions"
print(g7_pop)

# checking a datatype of series
print(g7_pop.dtype)

# checking the value of panda series in array form
print(g7_pop.values)

# checking the value type
print(type(g7_pop.values))

#now A Series has an index, that's similar to the automatic index assigned to Python's lists:
print(g7_pop[0])
print(g7_pop[1])

# Checking the range and detail of index
print(g7_pop.index)

#we can explicitly define the index:
g7_pop.index = [
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States',
]
print(g7_pop)

#We can say that Series look like "ordered dictionaries". We can actually create Series out of dictionaries:
g8_pop = pd.Series({
    'canada' : 34.563,
    'France' : 63.951,
    'Italy': 60.665,
    'Japan': 127.061,
    'United Kingdom': 64.511,
    'United States': 318.523
}, name= "G8 Population in millions")
print(g8_pop)

#We can also create a panda series dividing arrays and naming and indexing 
g9_pop = pd.Series([35.467, 63.951, 80.94, 60.665, 127.061, 64.511, 318.523], index=['Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom','United States'], name= 'G9 Population in millions')
print(g9_pop)


# in this if there is no value of spain then defalut value would be Nan
modified_g7_pop = pd.Series(g9_pop, index=['France', 'Germany', 'Italy', 'Spain'])
print(modified_g7_pop) 

#Indexing 
#Indexing works similarly to lists and dictionaries, you use the index of the element you're looking for:
print(g9_pop['Canada'])
print(g9_pop['Japan'])

#Numeric position can also be used, with the iloc attribute 
print(g9_pop.iloc[0])
print(g9_pop.iloc[-1])

#Selecting multiple elements at once:
print(g9_pop[['Italy', 'France']])
print(g9_pop.iloc[[0, 1]])

#slicing also works, but important, in Pandas, the upper limit is also in included:
print(g9_pop['Canada': 'Italy'])

#not working with iloc, the upper limit is not going to be in included
print(g9_pop[0:-1])

#Conditional selection (boolean arrays)
print(g9_pop > 70) #it will give boolean value 
print(g9_pop[g9_pop > 70]) #it will give the value according to the boolean rule 

#give the value of mean 
print(g9_pop[g9_pop > g9_pop.mean()])

print(g9_pop.std())

#doing more complex and long condtional boolean
print(g7_pop[(g7_pop > g7_pop.mean() - g7_pop.std() / 2) | (g7_pop > g7_pop.mean() + g7_pop.std() / 2)])

# Operations and method 
print(g9_pop * 1000000)
print(g9_pop.mean())
print(np.log(g9_pop))
print(g9_pop['France': 'Italy'].mean())
print(g9_pop)

#Boolean arrays
#(working in the same way as numpy)
print(g9_pop)
print(g9_pop > 80) 
print(g9_pop[g9_pop > 80])
print(g7_pop[(g7_pop > 80) | (g7_pop < 40)])
print(g7_pop[(g7_pop > 80) & (g7_pop < 200)])

#Modifying series
g7_pop['Canada'] = 40.5
print(g7_pop)
g7_pop.iloc[-1] = 500
print(g7_pop)
print(g7_pop[g7_pop<70])
g7_pop[g7_pop < 70] = 99.99
print(g7_pop)















