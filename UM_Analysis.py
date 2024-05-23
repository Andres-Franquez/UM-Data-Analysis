import pandas as pd
import seaborn as sns

df = pd.read_csv("TWO_CENTURIES_OF_UM_RACES.csv", low_memory=False)

#clean up data
#ONLY USA RACES, 50KM OR 50MI, 2020
#STEP 1 SHOW 50mi OR 50km

df[df['Event distance/length'] == '50mi']

#combine 50km/50mi with isin
df[df["Event distance/length"].isin(['50km','50mi'])]

#Add the year of event 
df[(df["Event distance/length"].isin(['50km','50mi'])) & (df['Year of event'] == 2020)]

#Combine with USA
df[df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA']


df2 = df[(df["Event distance/length"].isin(['50km','50mi'])) & (df['Year of event'] == 2020) & (df['Event name'].str.split('(').str.get(1).str.split(')').str.get(0) == 'USA')]

#df2 = df[(df["Event distance/length"].isin(['50km','50mi'])) & (df['Year of event'] == 2020) & (df['Event name'].str.split(')').str.get(1))]
#remove USA from event name

df2['Event name'] = df2['Event name'].str.split('(').str.get(0)

print(df2)