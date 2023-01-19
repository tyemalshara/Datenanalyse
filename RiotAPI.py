import requests 
import ast

api_key  = 'RGAPI-3ffd65f3-9941-4b1c-b2d2-f963fad8771f'
puuid = 'Hy0nU-qjR3oCqkR3cXma1o-Xk82M0gDQ16D6hknxIY-APLcU33F0ZAWZULTGaCj2UG2PnqMbqX69ag'
Number_of_match_ids = 100
# match_id = 'EUW1_6215274778'

ListofMatchIds_by_Puuid = f'https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count={Number_of_match_ids}&api_key={api_key}'
# Match_by_Id = f'https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54",
    "Accept-Language": "de,de-DE;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Riot-Token": api_key,
    "Origin": "https://developer.riotgames.com"
    }
ListofMatchIds_by_Puuid = requests.get(ListofMatchIds_by_Puuid, headers=headers)
s = ListofMatchIds_by_Puuid.text
# Use ast.literal_eval() to parse the string as a literal value
ListofMatchIds_by_Puuid = ast.literal_eval(s)
anfangsklammer = 0
for match_id in ListofMatchIds_by_Puuid:
    response = requests.get(f'https://europe.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={api_key}', headers=headers)
    # If the request is successful (response code is 200)
    if response.status_code == 200:
        # Open a file for writing in binary mode
        with open(f"match_data{Number_of_match_ids}.json", "ab") as f:
            # if anfangsklammer==0:
            #     f.write("[")
            #     anfangsklammer = anfangsklammer+1
            # Write the response data to the file
            f.write(response.content)
            f.write(b",")   # add comma to separate JSON objects from each other. These brackets: [] are added manually one at the beginning and one at the very end
    else:
        print(f"Failed to retrieve match data. Status code: {response.status_code}")

