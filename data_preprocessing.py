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

    nfl_play_data: pd.DataFrame = pd.read_csv(file_path)

    # keep only the columns listed
    nfl_play_data = nfl_play_data[features_to_keep]

    # remove any plays where play_type not in ('pass', 'run')
    nfl_play_data = nfl_play_data[nfl_play_data['play_type'].isin(['pass', 'run'])]

    # convert the number of seconds to hours
    # nfl_play_data = nfl_play_data['quarter_seconds_remaining'] / 3600
    # nfl_play_data = nfl_play_data['half_seconds_remaining'] / 3600
    # nfl_play_data = nfl_play_data['game_seconds_remaining'] / 3600

    # convert the the following feature to a dummy variables
    # nfl_play_data = nfl_play_data['game_half'].get_dummies()
    # nfl_play_data = nfl_play_data['postteam'].get_dummies()
    # nfl_play_data = nfl_play_data['defteam'].get_dummies()

    play_outcomes: pd.Series = nfl_play_data.pop('play_type')

    return nfl_play_data, play_outcomes

def missing_data():
    nfl_play_data, play_outcomes = load_nfl_data('nfl-play-by-play-2009-2018.csv')
    print(nfl_play_data.columns)


    



missing_data()

