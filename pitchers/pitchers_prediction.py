import pandas as pd
import numpy as np

df = pd.read_csv("pitchers.csv")
df = df.replace(False, 0)
df = df.replace(True, 1)
df.replace([np.inf, -np.inf], np.nan, inplace=True)
pitchers_data = df[df.active_player ==1]

# Coefficients from logistic regression pasted from pitchers_regression.ipynb file
coeffs = {'years_played': 0.0020428039642415513,
 'career_era': -1.1158026287597493,
 'career_whip': -1.9318618093573272,
 'career_ip': -0.0012619974204642326,
 'career_wl': -0.8934375712804276,
 'career_wins': 0.03778412738264687,
 'career_so': -0.0014222222823067736,
 'career_war': 0.0830667170029248,
 'career_saves': 0.00818862965699141,
 'world_series_wins': 0.30117298303976586,
 'cy_young_awards': 0.2982898970935313,
 'mvps': -0.5136674329481301,
 'era_titles': 0.3401397317783753,
 'all_star_apps': 0.28873683194134486}

intercept = -1.8893136
HOF = []
HOF_cusp = []
HOF_work_to_do = []
for index, row in pitchers_data.iterrows():
    score = 0
    score = int(row['years_played'])*coeffs['years_played']+(row['career_era'])*coeffs['career_era']+ int(row['career_whip'])*coeffs['career_whip'] + int(row['career_ip'])*coeffs['career_ip']+ (row['career_wl'])*coeffs['career_wl']+int(row['career_wins'])*coeffs['career_wins']+int(row['career_so'])*coeffs['career_so']+(row['career_war'])*coeffs['career_war']+(row['career_saves'])*coeffs['career_saves']+int(row['world_series_wins'])*coeffs['world_series_wins']+int(row['cy_young_awards'])*coeffs['cy_young_awards']+int(row['mvps'])*coeffs['mvps']+int(row['era_titles'])*coeffs['era_titles']+int(row['all_star_apps'])*coeffs['all_star_apps'] + intercept
    if score > 1:
        HOF.append(str(row['name']))
    if score <=1 and score >= 0:
        HOF_cusp.append(str(row['name']))
    if score < 0 and score >= -1:
        HOF_work_to_do.append(str(row['name']))
print('Almost certainly Hall of Famers: ' + str(HOF))
print('On the cusp of being in the Hall of Fame: ' + str(HOF_cusp))
print('Likely Hall of Fame, but work to do: ' + str(HOF_work_to_do))
