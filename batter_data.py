from bs4 import BeautifulSoup
import requests
import sys
from string import ascii_lowercase

print('link' + ',' + 'name' + ',' + 'hall_of_fame' + ',' + 'active_player' + ',' + 'years_played' + ',' + 'career_batting_average' + ',' + 'career_hits' + ',' + 'career_HRs' + ',' + 'career_WAR' + ',' + 'career_RBIs' + ',' + 'career_runs' + ',' + 'career_OBP' + ',' + 'career_SLG' + ',' + 'career_OPS' + ',' + 'world_series_wins' + ',' + 'golden_glove_awards' + ',' + 'mvps' + ',' + 'career_hitting_titles' + ',' + 'silver_slugger_awards'+','+ 'all_star_apps')


# Get links for all player pages
linklist = []
for i in ascii_lowercase:
    url = "https://www.baseball-reference.com/players/" + i + "/"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    x = soup.body
    x = x.find('div',{"class": "section_content"})
    z = x.find_all('a')
    for j in z:
        link = "http://www.baseball-reference.com" + j['href']
        linklist.append(link)
for link in linklist:
    url = link
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    x = soup.body.find('div',{"class": "stats_pullout"})
    if not x == None:
        z = x.find_all('strong')
        for elem in z:
        	if elem.text == 'SB':
        		#NAME
        		name = ''
        		x = soup.body.find('h1',{'itemprop':'name'})
        		x = x.span.text
        		name = x
        		#HALL OF FAME
        		hall_of_fame = False
        		x = soup.body.find('a',{"href": "/awards/hof.shtml"})
        		if x.text == "Hall of Fame":
        			hall_of_fame = True
        		#ACTIVE
        		active_player = False
        		x = soup.body.find('div',{"class": "stats_pullout"})
        		z = x.find_all('strong')
        		for elem in z:
        			if elem.text == "2021":
        				active_player = True
        		# YEARS PLAYED
        		years_played = 0
        		x = soup.body.find('th',{"data-stat": "player_stats_summary_explain"}).text
        		if x[1] == ' ':
        			years_played = x[0]
        		else:
        			years_played = x[0:2]
        		# Career Battin Average
        		batting_average = 0
        		x = soup.body.tfoot.tr
        		x = x.find('td',{'data-stat':'batting_avg'})
        		if not x == None:
        			batting_average = x.text
        		else:
        			batting_average = ''
        		# Career Hits
        		x = soup.body.tfoot.tr
        		x = x.find('td',{'data-stat':'H'})
        		hits = 0
        		if not x == None:
        			hits = x.text
        		else:
        			hits = ''
        		# Career HRs
        		x = soup.body.tfoot.tr
        		x = x.find('td',{'data-stat':'HR'})
        		hr = 0
        		if not x == None:
        			hr = x.text
        		else:
        			hr = ''
        		# CAREER WAR
        		career_war = 0
        		x = soup.body.find('div',{'class':'stats_pullout'})
        		z = x.find('div',{'class':'p1'})
        		y = z.find_all('p')
        		if not z == None:
        			if active_player == True:
        				career_war = y[1].text
        			else:
        				career_war = y[0].text
        		else:
        			career_war = ''
        		# Career RBIs
        		x = soup.body.tfoot.tr
        		x = x.find('td',{'data-stat':'RBI'})
        		RBI = 0
        		if not x == None:
        			RBI = x.text
        		else:
        			RBI = ''
        		#  Career Runs
        		x = soup.body.tfoot.tr
        		x = x.find('td',{'data-stat':'R'})
        		Runs = 0
        		if not x == None:
        			Runs = x.text
        		else:
        			Runs = ''
        		#  Career OBP
        		x = soup.body.tfoot.tr
        		x = x.find('td',{'data-stat':'onbase_perc'})
        		OBP = 0
        		if not x == None:
        			OBP = x.text
        		else:
        			OBP = ''
        		#  Career SLG
        		x = soup.body.tfoot.tr
        		x = x.find('td',{'data-stat':'slugging_perc'})
        		SLG = 0
        		if not x == None:
        			SLG = x.text
        		else:
        			SLG = ''
        		x = soup.body.tfoot.tr
        		x = x.find('td',{'data-stat':'onbase_plus_slugging'})
        		OPS = 0
        		if not x == None:
        			OPS = x.text
        		else:
        			OPS = ''
        		# WORLD SERIES WINS
        		world_series_wins = 0
        		x = soup.body.find('ul',{"id": "bling"})
        		if not x == None:
        			z = x.find_all('li')
        			for elem in z:
        				if 'World Series' in elem.a.text:
        					if 'x' in elem.a.text:
        						if elem.a.text[1] == 'x':
        							world_series_wins = elem.a.text[0]
        						else:
        							world_series_wins = elem.a.text[0:2]
        					else:
        							world_series_wins = 1
        		# Golden GLOVE WINS
        		gold_glove = 0
        		x = soup.body.find('ul',{"id": "bling"})
        		if not x == None:
        			z = x.find_all('li')
        			for elem in z:
        				if 'Gold Glove' in elem.a.text:
        					if 'x' in elem.a.text:
        						if elem.a.text[1] == 'x':
        							gold_glove = elem.a.text[0]
        						else:
        							gold_glove = elem.a.text[0:2]
        					else:
        							gold_glove = 1
        		# MVPs
        		mvp = 0
        		x = soup.body.find('ul',{"id": "bling"})
        		if not x == None:
        			z = x.find_all('li')
        			for elem in z:
        				if 'MVP' in elem.a.text and 'AS' not in elem.a.text:
        					if 'x' in elem.a.text:
        						if elem.a.text[1] == 'x':
        							mvp = elem.a.text[0]
        						else:
        							mvp = elem.a.text[0:2]
        					else:
        							mvp = 1
        		# Career hitting titles
        		hitting_title = 0
        		x = soup.body.find('ul',{"id": "bling"})
        		if not x == None:
        			z = x.find_all('li')
        			for elem in z:
        				if 'Batting Title' in elem.a.text:
        					if 'x' in elem.a.text:
        						if elem.a.text[1] == 'x':
        							hitting_title = elem.a.text[0]
        						else:
        							hitting_title = elem.a.text[0:2]
        					else:
        							hitting_title = 1
        		# Silver Slugger
        		silver = 0
        		x = soup.body.find('ul',{"id": "bling"})
        		if not x == None:
        			z = x.find_all('li')
        			for elem in z:
        				if 'Silver Slugger' in elem.a.text:
        					if 'x' in elem.a.text:
        						if elem.a.text[1] == 'x':
        							silver = elem.a.text[0]
        						else:
        							silver = elem.a.text[0:2]
        					else:
        							silver = 1
        		# All Star apps
        		allstar = 0
        		x = soup.body.find('ul',{"id": "bling"})
        		if not x == None:
        			z = x.find_all('li')
        			for elem in z:
        				if 'All-Star' in elem.a.text:
        					if 'x' in elem.a.text:
        						if elem.a.text[1] == 'x':
        							allstar = elem.a.text[0]
        						else:
        							allstar = elem.a.text[0:2]
        					else:
        							allstar = 1
        		print(link +',' + str(name)+','+ str(hall_of_fame)+"," +str(active_player) +"," + str(years_played) +"," + str(batting_average) +"," + str(hits) + ',' + str(hr) + ',' + str(career_war) + ',' + str(RBI)+ ',' + str(Runs) + ',' + str(OBP) + ',' + str(SLG) + ',' + str(OPS) + ',' + str(world_series_wins) + ',' + str(gold_glove) + ',' + str(mvp) + ',' + str(hitting_title) + ',' + str(silver) + ',' + str(allstar))
    
