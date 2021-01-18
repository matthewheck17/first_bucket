import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
import mysql.connector

conn = mysql.connector.connect(
  host="***",
  user="***",
  password="***",
  database="***"
)
mycursor = conn.cursor()

TEAM_ACRONYMS = ["atl", "bkn", "bos", "cha", "chi", "cle", "dal", "den", "det", "gs", "hou", "ind", "lac", "lal", "mem", "mia", "mil", "min", "no", "nyk", "okc", "orl", "phi", "phx", "por", "sac", "sas", "tor", "utah", "was"]

for selected_team in range(0, 30):
    print(selected_team)
    print(TEAM_ACRONYMS[selected_team])
    if selected_team == 19:
        #knicks logo is named incorrectly on espns site too lol
        TEAM_LOGO = "https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/ny.png&h=100&w=100"
    elif selected_team == 26:
        #spurs logo is named incorrectly on espns site too omegalul
        TEAM_LOGO = "https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/sa.png&h=100&w=100"
    elif selected_team == 29:
        #wiz logo is named incorrectly on espns site too omegalul
        TEAM_LOGO = "https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/wsh.png&h=100&w=100"
    else:
        TEAM_LOGO = "https://a.espncdn.com/combiner/i?img=/i/teamlogos/nba/500/" + TEAM_ACRONYMS[selected_team] + ".png&h=100&w=100" # insert team logo here

    #get link to each game a team has played
    schedule_page = requests.get("https://www.espn.com/nba/team/schedule/_/name/" + TEAM_ACRONYMS[selected_team]) #insert team schedule page here
    schedule_page_code = BeautifulSoup(schedule_page.text, 'html.parser')
    game_list = schedule_page_code.find_all('span', attrs = {'class': 'ml4'})

    game_link_list = []

    for game in game_list:
        link = game.find('a',)
        link_string = link['href']
        updated_link = link_string.replace("/game?", "/playbyplay?")
        game_link_list.append(updated_link)

    scorers = []

    #insert link to play-by-play and this will get the first scorers name as a string
    for link in game_link_list:
        game_id = link[42:]
        mycursor.execute("SELECT game_id FROM games WHERE team_id = '" + str(selected_team) + "'")
        game_ids = mycursor.fetchall()
        id_list = []

        for g in game_ids:
            g = str(g)[2:-3]
            id_list.append(g)

        if game_id in id_list:
            continue
        
        game_page = requests.get(link)
        game_page_code = BeautifulSoup(game_page.text, 'html.parser')
        all_scores = game_page_code.find_all('tr', attrs = {'class': 'scoring-play'})
        first_score = None
        found = False
        i=-1
        bucket_index = 0
        while found != True: #find first team score
            i += 1
            score_td = all_scores[i].find('td', attrs = {'class': 'game-details'})
            logo_td = score_td.previousSibling
            logo_img = logo_td.find('img')
            logo_src = logo_img['src']
            if "free throw" not in score_td.text: #if its not a free throw it counts
                if logo_src == TEAM_LOGO: #if it was a bucket made by the selected team
                    found = True
                    first_score = all_scores[i]
                else:
                    bucket_index += 1 #increment bucket_index so it is known that it is not the first overall bucket
            
        score_desc = first_score.find('td', attrs = {'class': 'game-details'})
        score_desc_list = score_desc.text.split()
        scorer = score_desc_list[0] + " " + score_desc_list[1]
        scorer = scorer.replace("'", "")

        if bucket_index == 0: 
            mycursor.execute("INSERT INTO games (game_id, first_scorer, overall, team_id) values ('" + game_id + "', '" + scorer +"', TRUE, '" + str(selected_team) +"')")
        else:
            mycursor.execute("INSERT INTO games (game_id, first_scorer, overall, team_id) values ('" + game_id + "', '" + scorer +"', FALSE, '" + str(selected_team) +"')")

    print("team success")


conn.commit()
