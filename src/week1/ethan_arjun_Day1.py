import requests

api_key = "RGAPI-302819dc-bd09-414a-b18b-ef84ed8540ac"

def requestSummonerData (region, summoner_name):
    URL = "https://" + region + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name + "?api_key=" + api_key
    response = requests.get(URL)
    # print (response)
    return response.json()


# def matchStats (matchID):
#     URL = 


# def requestRankedData(region, parsed_name):
#     URL = "https://" + region + ".api.riotgames.com/lol/league/v4/entries/by-summoner/" + parsed_name + "?api_key=" + api_key


def get_puuid():
    # region = (str) (input("what region bro (all lower e.g. na1): "))
    # summoner_name = (str) (input("what ur name: "))

    response_JSON = requestSummonerData(region, summoner_name)
    return response_JSON['puuid']
    # ID = response_JSON[summoner_name]['id']
    # ID = str[ID]
    # return ID

def get_match():
    if region == 'br1' or region == 'na1' or region == 'la1' or region == 'la2':
        the_region = 'americas'
    elif region == 'eun1' or region == 'euw1' or region == 'tr1':
        the_region = 'europe'
    else:
        the_region = 'asia'
    URL = 'https://' + the_region + '.api.riotgames.com/lol/match/v5/matches/by-puuid/' + get_puuid() + '/ids?start=0&count=20&api_key=' + api_key
    response = requests.get(URL)
    our_response = response.json()
    match_ID = our_response[0]
    return match_ID


def num_kills_blue():
    global region
    global summoner_name
    region = (str) (input("what region bro (all lower e.g. na1): "))
    summoner_name = (str) (input("what ur name: "))

    if region == 'br1' or region == 'na1' or region == 'la1' or region == 'la2':
        the_region = 'americas'
    elif region == 'eun1' or region == 'euw1' or region == 'tr1':
        the_region = 'europe'
    else:
        the_region = 'asia'

    URL = "https://" + the_region + ".api.riotgames.com/lol/match/v5/matches/" + get_match() + "?api_key=" + api_key
    response = requests.get(URL)
    our_response = response.json()
    num_kills = 0
    for i in range(4):
        num_kills = our_response['info']['participants'][i]['kills'] + num_kills
    return num_kills


def num_kills_red():
    if region == 'br1' or region == 'na1' or region == 'la1' or region == 'la2':
        the_region = 'americas'
    elif region == 'eun1' or region == 'euw1' or region == 'tr1':
        the_region = 'europe'
    else:
        the_region = 'asia'

    URL = "https://" + the_region + ".api.riotgames.com/lol/match/v5/matches/" + get_match() + "?api_key=" + api_key
    response = requests.get(URL)
    our_response = response.json()
    num_kills = 0
    for i in range(5,9):
        num_kills = our_response['info']['participants'][i]['kills'] + num_kills
    return num_kills


# def main():
    # my_dictionary = getDictionary
    # puuid = getDictionary['puuid']
    # return puuid


print ("blue team kills: " + str(num_kills_blue()))
print ("red team kills: " + str(num_kills_red()))

