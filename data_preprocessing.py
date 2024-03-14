import pandas as pd


features_to_keep = [
    'posteam',
    'defteam',
    'yardline_100',
    'quarter_seconds_remaining',
    'half_seconds_remaining',
    'game_seconds_remaining',
    'game_half',
    'quarter_end',
    'drive',
    'sp',
    'qtr',
    'down',
    'ydstogo',
    'ydsnet',
    'play_type',
    'posteam_timeouts_remaining',
    'defteam_timeouts_remaining',
    'posteam_score',
    'defteam_score',
    'score_differential',
    'ep',
    'epa'
]


def load_nfl_data(file_path) -> [pd.DataFrame, pd.Series]:

    nfl_play_data: pd.DataFrame = pd.read_csv(file_path, nrows=1000)

    # keep only the columns listed
    nfl_play_data = nfl_play_data[features_to_keep]

    # remove any plays where play_type not in ('pass', 'run')
    nfl_play_data = nfl_play_data[nfl_play_data['play_type'].isin(['pass', 'run'])]

    # convert the number of seconds to hours
    nfl_play_data['quarter_seconds_remaining'] = nfl_play_data['quarter_seconds_remaining'] / 3600
    nfl_play_data['half_seconds_remaining'] = nfl_play_data['half_seconds_remaining'] / 3600
    nfl_play_data['game_seconds_remaining'] = nfl_play_data['game_seconds_remaining'] / 3600

    play_outcomes = pd.get_dummies(nfl_play_data.pop('play_type'))

    nfl_play_data = pd.get_dummies(nfl_play_data)

    return nfl_play_data, play_outcomes

def missing_data():
    nfl_play_data, play_outcomes = load_nfl_data('nfl-play-by-play-2009-2018.csv')
    print(play_outcomes.head())

    



    



missing_data()

