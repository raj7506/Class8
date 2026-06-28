#Activity: Game Leader Board Analyzer
import pandas as pd
# Part 1 - Create a Panda Series of Top Player Scores
print("Part 1: Panda Series")
scores = [83621, 29158, 34910, 42201]
players = pd.Series(scores, index =['NightWolf','PixelHeart', 'GameMoney', 'StarFlower'])
print(players)

# Part 2 - Create a DataFrame of gaming starting
print()
print("Part 2: Pandas DataFrame")
data = {
    'Player': ['NightWolf', 'PixelHeart', 'GameMoney', 'StarFlower'],
    'Level': [42, 35, 16, 23],
    'Score': [83621, 29158, 34910, 42201],
    'Wins': [210, 185, 162, 140],
}
df =pd.DataFrames
print(df)

#Part 3 - Acess rows using .loc
print()
print("Part 3: Acessing rows")
print("row0(top player):")
print(df.loc[0])
print()
print("Rows 2 and 3:")
print(df.loc[2:3])

#Part 4 -Load leaderboard.csv and view the data
print()
print("Part 4: Reading a csv file")
full_df = pd.read_csv('leaderboard.csv')
print('First 5 rows(head): ')
print(full_df.head())
print()
print('Last 3 rows(tail):')
print(full_df.tail(3))
print("Dataset info:")
print(full_df.info())

#Part 5- Clean the Data
print()
print("Part 5- Clean Data")
print("Rows with missing values removed(dropna):")
clean_df = full_df.dropna()
print(clean_df.to_string())
print()
print('Missing values filled with 0(fillna)')
filled_df = full_df.fillna(0)
print(filled_df.to_string)