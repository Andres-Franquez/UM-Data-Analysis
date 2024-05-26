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

#remove USA from event name
df2['Event name'] = df2['Event name'].str.split('(').str.get(0)


#clean up athlete age

df2['athlete_age'] = 2020 - df2['Athlete year of birth']

#remove h from athlete performane

df2['Athlete performance'] = df2['Athlete performance'].str.split('(').str.get(0)

#drop columns Athlete club, athlete country, athlete year of birth, athlete age category

df2 = df2.drop(['Athlete club', 'Athlete country', 'Athlete year of birth', 'Athlete age category'], axis = 1)

#clean up null values 

df2.isna().sum()

#look at examples
df2[df2['athlete_age'].isna()==1]

#drop the rows 

df2 = df2.dropna()

#check for duplicates 

df2[df2.duplicated() == True]

#reset the index

df2.reset_index(drop = True)

#fix the types 
#df2.dtypes

df2['athlete_age'] = df2['athlete_age'].astype(int)
df2['Athlete average speed'] = df2['Athlete average speed'].astype(float)

#renaming columns for efficiency 
df2 = df2.rename(columns = {
    "Year of event":'year',
    'Event dates':'race_day',
    'Event name':'race_name',
    'Event distance/length':'race_length',
    'Event number of finishers': 'race_number_of_finishers',
    'Athlete performance' : 'athlete_performance',
    'Athlete gender': 'athlete_gender',
    'Athlete average speed': 'athlete_average_speed',
    'Athlete ID': 'athlete_id'
})

#reordering for preference
df3 = df2[['race_day', 'race_name', 'race_length', 'race_number_of_finishers', 'athlete_id', 'athlete_gender', 'athlete_age', 'athlete_performance', 'athlete_average_speed', 'year']]

#charts and graphs 
sns.histplot(df3['race_length'])

