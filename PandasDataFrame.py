#Pandas - DataFrame's

#Hands on!

#let's import all the library we need 
import numpy as np
import pandas as pd 

df = pd.DataFrame({
    'Population':[35.467, 63.951, 80.94 , 60.665, 127.061, 64.511, 318.52],
    'GDP': [
        1785387,
        2833687,
        3874437,
        2167744,
        4602367,
        2950039,
        17348075
    ],
    'Surface Area': [
        9984670,
        640679,
        357114,
        301336,
        377930,
        242495,
        9525067
    ],
    'HDI': [
        0.913,
        0.888,
        0.916,
        0.873,
        0.891,
        0.907,
        0.915
    ],
    'Continent': [
         'America',
        'Europe',
        'Europe',
        'Europe',
        'Asia',
        'Europe',
        'America'
    ]
}, columns=['Population', 'GDP', 'Surface Area', 'HDI', 'Continent'])

#We can index it like a series
df.index =[
    'Canada',
    'France',
    'Germany',
    'Italy',
    'Japan',
    'United Kingdom',
    'United States',
] 
print(df)

#We can check the info data using this 
print(df.columns)
print(df.index)
print(df.info())
print(df.size)
print(df.shape)

# this describe the all the fundamental statistical detail
print(df.describe())

#to get a datatype of of data
print(df.dtypes)

#this function how much time which data contain detail
print(df.value_counts())

#Indexing, Selection and Slicing
print(df.loc['Canada'])
print(df.iloc[-1])
print(df['Population'])

#IF you're working on a notebook and want to see a more DataFrame-like format we can use the to_frame method:
print(df['Population'].to_frame())
print(df[['Population', 'GDP']])
print(df[1:3])

#using loc 
print(df.loc['Italy'])
print(df.loc['France': 'Italy'])
print(df.loc['France': 'Italy', 'Population'])
print(df.loc['France': 'Italy', ['Population', 'GDP']])

#using iloc
print(df.iloc[0])
print(df.iloc[-1])
print(df.iloc[[0,1,-1]])
print(df.iloc[1:3])
print(df.iloc[1:3,3])
print(df.iloc[1:3, [0,3]])
print(df.iloc[1:3, 1:3])

#Conditional selection (boolean arrays)
print(df['Population'] > 70)
print(df.loc[df['Population'] > 70])
print(df.loc[df['Population'] > 70, 'Population'])
print(df.loc[df['Population'] > 70, ['Population', 'GDP']])

#Dropping stuff


#Operation
print(df[['Population', 'GDP']] / 100)
print(pd.Series([-1_000_000, -0.3], index=['GdP', 'HDI']))
print(df[['GDP', 'HDI']])
crisis = pd.Series([-1_000_000, -0.3], index=['GDP', 'HDI'])
print(df[['GDP', 'HDI']] + crisis)

#Modifying DataFrames


