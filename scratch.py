import pandas as pd

nfl_data_set = pd.read_csv('nfl-play-by-play-2009-2018.csv')

# output the column names to a txt file
with open('column_names.txt', 'w') as f:
    for col in nfl_data_set.columns:
        f.write(col + '\n')