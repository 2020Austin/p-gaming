import requests, time, os, csv, pandas as pd
from dotenv import load_dotenv


# 20 requests every 1 seconds(s)
# 100 requests every 2 minutes(s)

# Summonername=eStarAstral

# Getting summoners in the diamond one level through League V4

def getD1summoners():
  payload = {}
  load_dotenv()
  api_key = os.environ.get("Api_Key", None)
  payload["api_key"]=api_key
  r = requests.get("https://na1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/GOLD/I?page=8", params=payload)
  print("people =", r.url) #League V4
  time.sleep(2)
  return r.json()

summoners = getD1summoners()


# Getting match id
def reqMatchId(puuid, start, count):
  payload = {'start': start, 'count': count}
  load_dotenv() 
  api_key = os.environ.get("Api_Key", None) #Extracting API key from .env file
  payload["api_key"]=api_key
  r=requests.get("https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/"+puuid+'/ids?queue=420&type=ranked', params=payload)
  print("Generated URL=", r.url)
  return r.json()


payload = {}
load_dotenv() 
api_key = os.environ.get("Api_Key", None) #Extracting API key from .env file
payload["api_key"]=api_key


# Creating function using requests library to get match url and return a json of matches

def reqMatchData(matchId):
  payload = {}
  load_dotenv() 
  api_key = os.environ.get("Api_Key", None) #Extracting API key from .env file
  payload["api_key"]=api_key
  r = requests.get('https://americas.api.riotgames.com/lol/match/v5/matches/'+matchId, params=payload) 
  time.sleep(1)
  #print(matchId)
  return r.json()

# creating CSV header (column names)

header = ['matchNum', 'summoner', 'matchId', 'blueKills-redKills','blueAssists-redAssists', 'blueGold-redGold', 'blueAvgLevel-redAvgLevel', 'blueDamageToTurrets-redDamageToTurrets', 'blueDragonKills-redDragonKills', 'gameLength', 'numPlayers','outcome'] # Gold deficit

with open('Newest_league_dataset1.csv', 'w', encoding='UTF8', newline='') as f:
  writer = csv.writer(f)

  # write the header
  writer.writerow(header)

  matchnum=1


  for summoner in summoners:
    summonerName=summoner['summonerName'] # Getting the summoner name
    r = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName, params = payload)
    print("SUMMONERURL=", r.url)
    summonerJson = r.json()
    #print("summonerJson=", summonerJson)
    print("summonerPuuid=", summonerJson['puuid']) # Getting the puuid
    matches=reqMatchId(summonerJson['puuid'], "0", "50")

    print("matches=", matches) # Getting the matches of the summoner

    for matchId in matches:
      #print("matchid=", matchid)
      #print("match data=",  reqMatchData(matchid))
      
      matchinfo=reqMatchData(matchId)
      numPlayers=len(matchinfo['metadata']['participants'])

      i = 0
      blueAssists = 0
      redAssists = 0

      blueGold = 0
      redGold = 0

      blueKills = 0
      redKills = 0

      blueAvgLevel = 0
      redAvgLevel = 0

      redDamageToTurrets = 0
      blueDamageToTurrets = 0
      
      redDragonKills = 0
      blueDragonKills = 0

      halfPlayers=numPlayers/2

      while i<numPlayers/2: # because not all games has the same number of participants - first half are blue team # num_participants/2
        blueAssists+=matchinfo['info']['participants'][i]['assists'] # total number of assists by blue team
        blueGold+=matchinfo['info']['participants'][i]['goldEarned'] # total number of gold
        blueKills+=matchinfo['info']['participants'][i]['kills'] # total number of kills
        blueAvgLevel+=matchinfo['info']['participants'][i]['champLevel']/(halfPlayers) #Average champion level on blue team
        blueDamageToTurrets+=matchinfo['info']['participants'][i]['damageDealtToTurrets'] # total damage dealt to turrets on blue team
        blueDragonKills+=matchinfo['info']['participants'][i]['dragonKills'] # total blue dragon kills
        i+=1

      while i>=numPlayers/2 and i<numPlayers:
        redAssists+=matchinfo['info']['participants'][i]['assists']
        redGold+=matchinfo['info']['participants'][i]['goldEarned']
        redKills+=matchinfo['info']['participants'][i]['kills']
        redAvgLevel+=matchinfo['info']['participants'][i]['champLevel']/(halfPlayers)
        redDamageToTurrets+=matchinfo['info']['participants'][i]['damageDealtToTurrets'] 
        redDragonKills+=matchinfo['info']['participants'][i]['dragonKills'] 
        i+=1

      if matchinfo['info']['participants'][0]['win'] == True: # if first player wins, then blue team won that match
        outcome=1 # 1 means blue team win
      else:
        outcome=0 # 0 means red team win

      gamelength=matchinfo['info']['gameDuration'] # finding length of game

      print("Total blueKills in Match", matchnum, "=", blueKills)
      print("Total redKills in Match", matchnum, "=", redKills)
        
      print("Total blueAssists in Match", matchnum, "=", blueAssists)
      print("Total redAssists in Match", matchnum, "=", redAssists)


      print("Total blueGold in Match", matchnum, "=", blueGold)
      print("Total redGold in Match", matchnum, "=", redGold)

      print("Average Blue Champion Level in Match", matchnum, "=", "{:.1f}".format(blueAvgLevel))
      print("Average Red Champion Level in Match", matchnum, "=", "{:.1f}".format(redAvgLevel))
      

      print("Total Blue Damage Teal to Turrets", matchnum, "=", blueDamageToTurrets)
      print("Total Red Damage Teal to Turrets", matchnum, "=", redDamageToTurrets)

      print("Total Blue Dragon Kills", matchnum, "=", blueDragonKills)    
      print("Total Blue Dragon Kills", matchnum, "=", redDragonKills)
    
      print("num_participants=", numPlayers)

      print("Game Duration in Match", matchnum, "=",   gamelength)
      print("Outcome in Match", matchnum, "=",   outcome)

      print("-----------------------------------------------------------------")

      data=[matchnum, summonerName, matchId, blueKills-redKills, blueAssists-redAssists, blueGold-redGold, "{:.1f}".format(blueAvgLevel-redAvgLevel), blueDamageToTurrets-redDamageToTurrets, blueDragonKills-redDragonKills, gamelength, numPlayers, outcome] # indicating what to write as data
      # print("data=", data)
      # positive goldDiff value means blue has more gold, negative goldDiff value means red has more gold

      matchnum+=1 # iterating through next match
      writer.writerow(data) # writing data into CSV

      time.sleep(1)


