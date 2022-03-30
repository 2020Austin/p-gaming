from anyio import get_current_task
import requests
from time import sleep

API_KEY = "RGAPI-e32a4f70-cca9-47d2-bcb7-1a5342b8ddd3"
matchID_list = ["NA1_4239217057","NA1_4239184967","NA1_4239231527"]
matchID_list_remaining=["NA1_4238423652","NA1_4238398893","NA1_4238375243","NA1_4238381841","NA1_4238338934","NA1_4238325902","NA1_4238312355","NA1_4238310102","NA1_4235518597","NA1_4235486177","NA1_4235493914","NA1_4235501001","NA1_4235198850","NA1_4234501679","NA1_4234468356","NA1_4234465571","NA1_4234462496","NA1_4234379485","NA1_4232551972","NA1_4231357883","NA1_4231324473","NA1_4231299548","NA1_4231297124","NA1_4229040266","NA1_4228968086","NA1_4228975393","NA1_4228982405","NA1_4227110211","NA1_4226974709","NA1_4224264963","NA1_4224309782","NA1_4224206500","NA1_4224145397","NA1_4221222873","NA1_4221183581","NA1_4219512389","NA1_4219509807","NA1_4218445928","NA1_4218423116","NA1_4218449829","NA1_4218396685","NA1_4218353931","NA1_4218361572","NA1_4218299448","NA1_4218336565","NA1_4217623886","NA1_4217207541"]

#blue: kills, assists, goldEarned

def funct0():
    result=[]
    for i in range(len(matchID_list)):
        matchID = matchID_list[i]
        URL = f"https://americas.api.riotgames.com/lol/match/v5/matches/{matchID}?api_key={API_KEY}"
        match_dict = requests.get(URL)
        match_dict = match_dict.json()
        for key, value in match_dict.items():
            if key == 'info':
                info_dict = value
                for key, value in info_dict.items():
                    if key == 'participants':
                        participant_list = value
                        for i in range(len(participant_list)): 
                            individual_participant_dict = participant_list[i]
                            for key, value in individual_participant_dict.items():
                                if key == 'teamId':
                                    if value == 100:
                                        for key, value in individual_participant_dict.items():
                                            if key == 'kills':
                                                blue_kills=value

#red: kills, assists, goldEarned

def funct1():
    for i in range(len(matchID_list)):
        matchID = matchID_list[i]
        URL = f"https://americas.api.riotgames.com/lol/match/v5/matches/{matchID}?api_key={API_KEY}"
        match_dict = requests.get(URL)
        match_dict = match_dict.json()
        for key, value in match_dict.items():
            if key == 'info':
                info_dict = value
                for key, value in info_dict.items():
                    if key == 'participants':
                        participant_list = value
                        for i in range(len(participant_list)): 
                            individual_participant_dict = participant_list[i]
                            for key, value in individual_participant_dict.items():
                                if key == 'teamId':
                                    if value == 200:
                                        for key, value in individual_participant_dict.items():
                                            if key == 'goldEarned':
                                                print(value)

#gameDuration

for i in range(len(matchID_list)):
    matchID = matchID_list[i]
    URL = f"https://americas.api.riotgames.com/lol/match/v5/matches/{matchID}?api_key={API_KEY}"
    match_dict = requests.get(URL)
    match_dict = match_dict.json()
    for key, value in match_dict.items():
        if key == 'info':
            info_dict = value
            for key, value in info_dict.items():
                if key == 'gameDuration':
                    print(value)

#win/loss

for i in range(len(matchID_list)):
    matchID = matchID_list[i]
    URL = f"https://americas.api.riotgames.com/lol/match/v5/matches/{matchID}?api_key={API_KEY}"
    match_dict = requests.get(URL)
    match_dict = match_dict.json()
    for key, value in match_dict.items():
        if key == 'info':
            info_dict = value
            for key, value in info_dict.items():
                if key == 'teams':
                    team_info_list=value
                    blue_info_dict=team_info_list[0]
                    red_info_dict=team_info_list[1]
                    for key, value in blue_info_dict.items():
                        if key=='win':
                            if value==False:
                                print(0)
                            if value==True:
                                print(1)