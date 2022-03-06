The following repo is organized into three directories: batters, pitchers, and project. The batters and pitchers directories are in charge of collecting and analyzing data on batters and pitchers, respectively. Both of these directories are organized in the following way:

1. batter_data.py / pitcher_data.py -- scrape the data off of baseball-reference.com
2. batters.csv / pitchers.csv -- the output of batter_data.py and pitcher_data.py, respectively
3. batters_regression.ipynp / pitchers_regression.ipynb -- code that runs logistic regression on batters.csv and pitchers.csv, respectively (we used Jupyter Notebook for simplicity)
4. batters_prediction.py / pitchers_prediction.py -- using the coefficients found from regression, these scripts finds the players most likely to be inducted into the Hall of Fame based on our model
5. batters_prediction.txt / pitchers_regression.txt -- the output of batters_prediction.py and pitchers_prediction.py, respectively