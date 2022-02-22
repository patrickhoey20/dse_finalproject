from bs4 import BeautifulSoup
import requests
import sys
from string import ascii_lowercase

# Print header
print('link' + ',' + 'name' + ',' + 'hall_of_fame' + ',' + 'active_player' + ',' + 'years_played' + ',' + 'career_era' + ',' + 'career_whip' + ',' + 'career_ip' + ',' + 'career_wl' + ',' + 'career_wins' + ',' + 'career_so' + ',' + 'career_war' + ',' + 'career_saves' + ',' + 'world_series_wins' + ',' + 'cy_young_awards' + ',' + 'mvps' + ',' + 'era_titles' + ',' + 'all_star_apps')


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
            if elem.text == 'ERA':
                # NAME
                name = ''
                x = soup.body.find('h1',{'itemprop':'name'})
                x = x.span.text
                name = x
                # HALL OF FAME
                hall_of_fame = False
                x = soup.body.find('a',{"href": "/awards/hof.shtml"})
                if x.text == "Hall of Fame":
                    hall_of_fame = True
                # ACTIVE PLAYER
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
                # CAREER ERA
                career_era = 0
                x = soup.body.tfoot.tr
                x = x.find('td',{'data-stat':'earned_run_avg'})
                if not x == None:
                    career_era = x.text
                else:
                    career_era = ''
                # CAREER WHIP
                career_whip = 0
                x = soup.body.tfoot.tr
                x = x.find('td',{'data-stat':'whip'})
                if not x == None:
                    career_whip = x.text
                else:
                    career_whip = ''
                # CAREER IP
                career_ip = 0
                x = soup.body.tfoot.tr
                x = x.find('td',{'data-stat':'IP'})
                if not x == None:
                    career_ip = x.text
                else:
                    career_ip = ''
                # CAREER W-L PERCENTAGE
                career_wl = 0
                x = soup.body.tfoot.tr
                x = x.find('td',{'data-stat':'win_loss_perc'})
                if not x == None:
                    career_wl = x.text
                else:
                    career_wl = ''
                # CAREER WINS
                career_wins = 0
                x = soup.body.tfoot.tr
                x = x.find('td',{'data-stat':'W'})
                if not x == None:
                    career_wins = x.text
                else:
                    career_wins = ''
                # CAREER SO
                career_so = 0
                x = soup.body.tfoot.tr
                x = x.find('td',{'data-stat':'SO'})
                if not x == None:
                    career_so = x.text
                else:
                    career_so = ''
                # CAREER WAR
                career_war = 0
                x = soup.body.find('div',{'class':'stats_pullout'})
                z = x.find('div',{'class':'p1'})
                y = z.find('p')
                if not z == None:
                    career_war = y.text
                else:
                    career_war = ''
                # CAREER SAVES
                career_saves = 0
                x = soup.body.tfoot.tr
                x = x.find('td',{'data-stat':'SV'})
                if not x == None:
                    career_saves = x.text
                else:
                    career_saves = ''
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
                # CY YOUNG AWARDS
                cy_young_awards = 0
                x = soup.body.find('ul',{"id": "bling"})
                if not x == None:
                    z = x.find_all('li')
                    for elem in z:
                        if 'Cy Young' in elem.a.text:
                            if 'x' in elem.a.text:
                                if elem.a.text[1] == 'x':
                                    cy_young_awards = elem.a.text[0]
                                else:
                                    cy_young_awards = elem.a.text[0:2]
                            else:
                                cy_young_awards = 1
                # MVP AWARDS
                mvps = 0
                x = soup.body.find('ul',{"id": "bling"})
                if not x == None:
                    z = x.find_all('li')
                    for elem in z:
                        if 'MVP' in elem.a.text:
                            if 'x' in elem.a.text:
                                if elem.a.text[1] == 'x':
                                    mvps = elem.a.text[0]
                                else:
                                    mvps = elem.a.text[0:2]
                            else:
                                mvps = 1
                # ERA TITLES
                era_titles = 0
                x = soup.body.find('ul',{"id": "bling"})
                if not x == None:
                    z = x.find_all('li')
                    for elem in z:
                        if 'ERA Title' in elem.a.text:
                            if 'x' in elem.a.text:
                                if elem.a.text[1] == 'x':
                                    era_titles = elem.a.text[0]
                                else:
                                    era_titles = elem.a.text[0:2]
                            else:
                                era_titles = 1
                # ALL STAR APPEARANCES
                all_star_apps = 0
                x = soup.body.find('ul',{"id": "bling"})
                if not x == None:
                    z = x.find_all('li')
                    for elem in z:
                        if 'All-Star' in elem.a.text:
                            if elem.a.text[1] == 'x':
                                all_star_apps = elem.a.text[0]
                            else:
                                all_star_apps = elem.a.text[0:2]
                # INSERT ALL DATA
                print(link + ',' + str(name) + ',' + str(hall_of_fame) + ',' + str(active_player) + ',' + str(years_played) + ',' + str(career_era) + ',' + str(career_whip) + ',' + str(career_ip) + ',' + str(career_wl) + ',' + str(career_wins) + ',' + str(career_so) + ',' + str(career_war) + ',' + str(career_saves) + ',' + str(world_series_wins) + ',' + str(cy_young_awards) + ',' + str(mvps) + ',' + str(era_titles) + ',' + str(all_star_apps))

