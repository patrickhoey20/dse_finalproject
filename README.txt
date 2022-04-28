The following project uses logistic regression to predict which active Major League Baseball players will eventually be inducted into the National Baseball Hall of Fame. Our model used historical data (from over 22,000 players) to assess which statistics/awards are most important in determining a player's Hall of Fame chances, and used those weights to predict which active players will be in the Hall one day. Since batters and pitchers have different measures that their performance is judged on, we analyzed the two groups separately. All of the data was gathered using web scrapping techniques (mainly BeautifulSoup) from baseball-reference.com.

The following repo is organized into three directories: batters, pitchers, and project. The batters and pitchers directories are in charge of collecting and analyzing data on batters and pitchers, respectively. Both of these directories are organized in the following way:

1. batter_data.py / pitcher_data.py -- scrape the data off of baseball-reference.com
2. batters.csv / pitchers.csv -- the output of batter_data.py and pitcher_data.py, respectively
3. batters_regression.ipynp / pitchers_regression.ipynb -- code that runs logistic regression on batters.csv and pitchers.csv, respectively (we used Jupyter Notebook for simplicity)
4. batters_prediction.py / pitchers_prediction.py -- using the coefficients found from regression, these scripts finds the players most likely to be inducted into the Hall of Fame based on our model
5. batters_prediction.txt / pitchers_regression.txt -- the output of batters_prediction.py and pitchers_prediction.py, respectively
