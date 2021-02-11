import pandas as pd


data = pd.read_csv(r'C:\Users\tuca_\Desktop\vitao\teste\temp\athlete_events.csv')

#Getting unique values from csv
seasons = data['Season'].unique()
cities  = data['City'].unique()
sports  = data['Sport'].unique()
teams   = data['Team'].unique()
names   = data['Name'].unique()

