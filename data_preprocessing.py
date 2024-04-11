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
    'epa',
    'previous_play1',
    'previous_play2',
    'previous_play3'
]


def set_previous_play1(row):
    if row['drive'] != row['previous_drive1']:
        return 'new_team'
    else:
        return row['previous_play1']


def set_previous_play2(row):
    if row['drive'] != row['previous_drive2']:
        return 'new_team'
    else:
        return row['previous_play2']


def set_previous_play3(row):
    if row['drive'] != row['previous_drive3']:
        return 'new_team'
    else:
        return row['previous_play3']


def load_nfl_data(file_path) -> [pd.DataFrame, pd.Series]:

    nfl_play_data: pd.DataFrame = pd.read_csv(file_path)

    # jank
    nfl_play_data[f'previous_play1'] = nfl_play_data['play_type'].shift(1)
    nfl_play_data[f'previous_drive1'] = nfl_play_data['drive'].shift(1)

    nfl_play_data[f'previous_play2'] = nfl_play_data['play_type'].shift(2)
    nfl_play_data[f'previous_drive2'] = nfl_play_data['drive'].shift(2)

    nfl_play_data[f'previous_play3'] = nfl_play_data['play_type'].shift(3)
    nfl_play_data[f'previous_drive3'] = nfl_play_data['drive'].shift(3)

    # add column for previous play(s)
    nfl_play_data['previous_play1'] = nfl_play_data.apply(set_previous_play1, axis=1)
    nfl_play_data['previous_play2'] = nfl_play_data.apply(set_previous_play2, axis=1)
    nfl_play_data['previous_play3'] = nfl_play_data.apply(set_previous_play3, axis=1)

    # keep only the columns listed
    nfl_play_data = nfl_play_data[features_to_keep]

    # remove any plays where play_type not in ('pass', 'run')
    nfl_play_data = nfl_play_data[nfl_play_data['play_type'].isin(['pass', 'run'])]

    nfl_play_data = nfl_play_data.dropna()

    # convert the number of seconds to hours
    nfl_play_data['quarter_seconds_remaining'] = nfl_play_data['quarter_seconds_remaining'] / 3600
    nfl_play_data['half_seconds_remaining'] = nfl_play_data['half_seconds_remaining'] / 3600
    nfl_play_data['game_seconds_remaining'] = nfl_play_data['game_seconds_remaining'] / 3600

    play_outcomes = pd.get_dummies(nfl_play_data.pop('play_type'))

    nfl_play_data = pd.get_dummies(nfl_play_data)

    return nfl_play_data, play_outcomes



def old_load_nfl_data(file_path) -> [pd.DataFrame, pd.Series]:

    nfl_play_data: pd.DataFrame = pd.read_csv(file_path, nrows=1000)
    nfl_play_data: pd.DataFrame = pd.read_csv(file_path)

    # keep only the columns listed
    nfl_play_data = nfl_play_data[features_to_keep]

    nfl_play_data = nfl_play_data.dropna()

    # remove any plays where play_type not in ('pass', 'run')
    nfl_play_data = nfl_play_data[nfl_play_data['play_type'].isin(['pass', 'run'])]

    nfl_play_data['half_seconds_remaining'] = nfl_play_data['half_seconds_remaining'] / 3600
    nfl_play_data['game_seconds_remaining'] = nfl_play_data['game_seconds_remaining'] / 3600


    play_outcomes = pd.get_dummies(nfl_play_data.pop('play_type'))

    nfl_play_data = pd.get_dummies(nfl_play_data)

    return nfl_play_data, play_outcomes

# features_not_found =   ['date',
#                         'home_team',
#                         'game_date',
#                         'time',
#                         'qb_scrumble',
#                         'tackler1_player_id',
#                         'tackler1_player_name',
#                         'tackler2_player_id',
#                         'tackler2_player_name',
#                         'field_goal_kicker_player_id',
#                         'field_goal_kicker_player_name',
#                         'punter_player_name',
#                         'punter_player_id',
#                         'kicker_player_name',
#                         'kicker_player_id',
#                         'own_kickoff_recovery_player_id',
#                         'own_kickoff_recovery_player_name',
#                         'blocked_player_id',
#                         'blocked_player_name']
