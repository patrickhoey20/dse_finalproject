import pandas as pd
import numpy as np

df = pd.read_csv("batters.csv")
df = df.replace(False, 0)
df = df.replace(True, 1)
df.replace([np.inf, -np.inf], np.nan, inplace=True)
batters_data = df[df.active_player ==1]


coeffs ={'years_played': 0.09402990080100215,
 'career_batting_average': 1.572602490493626,
 'career_hits': -0.0019317757644307042,
 'career_HRs': -0.013640325278365376,
 'career_WAR': 0.07128038775818683,
 'career_RBIs': 0.004488248685339582,
 'career_runs': 0.0016782873365918864,
 'career_OBP': 0.2346897688008183,
 'career_SLG': 1.812398993571799,
 'world_series_wins': 0.19498051893293256,
 'golden_glove_awards': -0.1522947453269327,
 'mvps': 0.36870874526017655,
 'career_hitting_titles': 0.4746181927642111,
 'silver_slugger_awards': -0.0990496667082874,
 'all_star_apps': 0.2504181461044138}
intercept = -8.34310917
HOF = []
HOF_cusp = []
HOF_work_to_do = []
for index, row in batters_data.iterrows():
    score = 0
    score = int(row['years_played'])*coeffs['years_played']+(row['career_batting_average'])*coeffs['career_batting_average']+ int(row['career_hits'])*coeffs['career_hits'] + int(row['career_HRs'])*coeffs['career_HRs']+ (row['career_WAR'])*coeffs['career_WAR']+int(row['career_RBIs'])*coeffs['career_RBIs']+int(row['career_runs'])*coeffs['career_runs']+(row['career_OBP'])*coeffs['career_OBP']+(row['career_SLG'])*coeffs['career_SLG']+int(row['world_series_wins'])*coeffs['world_series_wins']+int(row['golden_glove_awards'])*coeffs['golden_glove_awards']+int(row['mvps'])*coeffs['mvps']+int(row['career_hitting_titles'])*coeffs['career_hitting_titles']+int(row['silver_slugger_awards'])*coeffs['silver_slugger_awards']+int(row['all_star_apps'])*coeffs['all_star_apps'] + intercept
    if score > 1:
        HOF.append(str(row['name']))
    if score <=1 and score >= 0:
        HOF_cusp.append(str(row['name']))
    if score < 0 and score >= -1:
        HOF_work_to_do.append(str(row['name']))
print('Almost certainly Hall of Famers: ' + str(HOF))
print('On the cusp of being in the Hall of Fame: ' + str(HOF_cusp))
print('Likely Hall of Fame, but work to do: ' + str(HOF_work_to_do))
