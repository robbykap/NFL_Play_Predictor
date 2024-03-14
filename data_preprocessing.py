import pandas as pd


features_to_keep = [
    # 'home_teaplay_idm',  # not sure what this feature is
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
    'qb_dropback',
    'qb_scramble',
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

    print(len(nfl_play_data))

    # keep only the columns listed
    nfl_play_data = nfl_play_data[features_to_keep]

    # remove any plays where play_type not in ('pass', 'run')
    nfl_play_data = nfl_play_data[nfl_play_data['play_type'].isin(['pass', 'run'])]

    play_outcomes: pd.Series = nfl_play_data.pop('play_type')

    print(len(nfl_play_data))

    return nfl_play_data, play_outcomes
