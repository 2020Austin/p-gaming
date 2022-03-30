import requests, time, os, pandas as pd
from dotenv import load_dotenv


def reqSummoner(name): 
 
  payload = {}
  load_dotenv() # Searches for .env file in root directory
  api_key = os.environ.get("Api_Key", None) # Extracting the API Key from the .env file, returns None if there is nothing with this name there
  payload["api_key"]=api_key

  r = requests.get('https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+name, params=payload) 
  return r.json()

def reqMatch(matchId):
  payload = {}
  load_dotenv() 
  api_key = os.environ.get("Api_Key", None)
  payload["api_key"]=api_key

  r = requests.get('https://americas.api.riotgames.com/lol/match/v5/matches/'+matchId, params=payload) 
  return r.json()

match1=reqMatch("NA1_3999297248")
print("match1=", match1['info'])
df=pd.json_normalize(match1['info']['participants']) # Source: https://stackoverflow.com/questions/47242845/pandas-io-json-json-normalize-with-very-nested-json

df.to_csv(r"/Users/sophia/Desktop/P-ai/matchV5.csv")
