import requests, time, os, csv
from dotenv import load_dotenv


# 20 requests every 1 seconds(s)
# 100 requests every 2 minutes(s)

# Summonername=eStarAstral

# Getting summoners in the diamond one level through League V4

def get_summoners():
  payload = {}
  load_dotenv()
  api_key = os.environ.get("Api_Key", None)
  payload["api_key"]=api_key
  r = requests.get("https://na1.api.riotgames.com/lol/league/v4/entries/RANKED_SOLO_5x5/DIAMOND/I?page=9", params=payload)
  print("people =", r.url) #League V4
  return r.json()

summoners = get_summoners()


# Getting match id
def get_match_id(puuid, start, count):
  payload = {'start': start, 'count': count}
  load_dotenv() 
  api_key = os.environ.get("Api_Key", None) #Extracting API key from .env file
  payload["api_key"]=api_key
  r=requests.get("https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/"+puuid+'/ids?queue=420&type=ranked', params=payload)
  
  return r.json()


payload = {}
load_dotenv() 
api_key = os.environ.get("Api_Key", None) #Extracting API key from .env file
payload["api_key"]=api_key


# Creating function using requests library to get match url and return a json of matches

def get_match_timeline(matchId):
  payload = {}
  load_dotenv() 
  api_key = os.environ.get("Api_Key", None) #Extracting API key from .env file
  payload["api_key"]=api_key
  r = requests.get('https://americas.api.riotgames.com/lol/match/v5/matches/'+matchId + "/timeline", params=payload) #now pulling from the timeline api
#   print("Generated URL=", r.url)
  return r.json()

def reqMatchData(matchId):
  payload = {}
  load_dotenv() 
  api_key = os.environ.get("Api_Key", None) #Extracting API key from .env file
  payload["api_key"]=api_key
  r = requests.get('https://americas.api.riotgames.com/lol/match/v5/matches/'+matchId, params=payload) 
  #print(matchId)
#   print(r.url)
  return r.json()

# creating CSV header (column names)

header = ['matchNum', 'summoner', 'matchId', 'blueGold-redGold','blueDamage-redDamage', 'numPlayers', 'outcome'] # dont forget outcome

with open('Newest_league_dataset.csv', 'w', encoding='UTF8', newline='') as f:
  writer = csv.writer(f)

  # write the header
  writer.writerow(header)

  matchnum=1

  n = 0

  for summoner in summoners:
    if n == 20:
      break
    else:
      n += 1
    summonerName = summoner['summonerName'] # Getting the summoner name
    r = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName, params = payload)
    summonerJson = r.json()
    # print("summonerPuuid=", summonerJson['puuid']) # Getting the puuid
    matches=get_match_id(summonerJson['puuid'], "0", "50")
    # print("matches=", matches) # Getting the matches of the summoner

    for matchId in matches:
      #print("matchid=", matchid)
      #print("match data=",  reqMatchData(matchid))
      try:
        matchtimelineinfo=get_match_timeline(matchId)
        matchinfo=reqMatchData(matchId)
        
        if matchinfo['info']['gameDuration'] > 900:
            numPlayers=len(matchinfo['metadata']['participants'])
            i = 0

            blueGold = 0
            redGold = 0


            redDamage = 0
            blueDamage = 0


            halfPlayers=numPlayers/2

            while i<numPlayers/2: # because not all games has the same number of participants - first half are blue team # num_participants/2
                
                blueGold+=matchtimelineinfo['info']['frames'][6]['participantFrames'][str(i+1)]['totalGold'] #done gold so far
                blueDamage+=matchtimelineinfo['info']['frames'][6]['participantFrames'][str(i+1)]['damageStats']["totalDamageDoneToChampions"] #damage done to champs so far
                i+=1        

            while i>=numPlayers/2 and i<numPlayers:
                redGold+=matchtimelineinfo['info']['frames'][6]['participantFrames'][str(i+1)]['totalGold'] #done gold so far
                redDamage+=matchtimelineinfo['info']['frames'][6]['participantFrames'][str(i+1)]['damageStats']["totalDamageDoneToChampions"] #damage done to champs so far
                i+=1

            if matchinfo['info']['participants'][0]['win'] == True: # if first player wins, then blue team won that match
                outcome=1 # 1 means blue team win
            else:
                outcome=0 # 0 means red team win

            #   gamelength=matchinfo['info']['gameDuration'] # finding length of game

            #   print("Total blueKills in Match", matchnum, "=", blueKills)
            #   print("Total redKills in Match", matchnum, "=", redDamage)
                
            #   print("Total blueAssists in Match", matchnum, "=", blueAssists)
            #   print("Total redAssists in Match", matchnum, "=", redAssists)


            print("Total blueGold in Match", matchnum, "=", blueGold)
            print("Total redGold in Match", matchnum, "=", redGold)

            #   print("Average Blue Champion Level in Match", matchnum, "=", "{:.1f}".format(blueAvgLevel))
            #   print("Average Red Champion Level in Match", matchnum, "=", "{:.1f}".format(redAvgLevel))
            

            print("Total Blue Damage Teal to Turrets", matchnum, "=", blueDamage)
            print("Total Red Damage Teal to Turrets", matchnum, "=", redDamage)

            #   print("Total Blue Dragon Kills", matchnum, "=", blueDragonKills)    
            #   print("Total Blue Dragon Kills", matchnum, "=", redDragonKills)
            
            #   print("num_participants=", numPlayers)

            #   print("Game Duration in Match", matchnum, "=",   gamelength)
            print("Outcome in Match", matchnum, "=",   outcome)

            print("-----------------------------------------------------------------")

            data=[matchnum, summonerName, matchId, blueGold-redGold, blueDamage-redDamage, outcome] # indicating what to write as data
            # print("data=", data)
            # positive goldDiff value means blue has more gold, negative goldDiff value means red has more gold

            matchnum+=1 # iterating through next match
            writer.writerow(data) # writing data into CSV

            time.sleep(.5)
      except:
          print("oops")

