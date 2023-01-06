import json
import pandas as pd
studentsList = []
blueteamId = 0
# print("Started Reading JSON file which contains multiple JSON document")
with open('match_data.json') as f:
    for jsonObj in f:
        studentDict = json.loads(jsonObj)
        studentsList.append(studentDict)
data = []
[studentsList] = studentsList   # remove-the-outer-list-of-a-double-list [[]] -> []
# print("Printing each JSON Decoded Object")
for student in studentsList:
    mydict = {}
    BlueTeam_assists = 0
    RedTeam_assists = 0
    BlueTeam_goldEarned = 0
    RedTeam_goldEarned = 0
    BlueTeam_championLevel = 0 
    RedTeam_championLevel = 0
    # print(student['info']['gameId'])
    gameId = student['info']['gameId']
    # mydict['gameId'] = gameId
    for participant in student['info']['participants']:
        if participant['summonerName']=='Timoschka17':
            # print(participant['summonerName'],participant['teamId'])    # get teamId since we need to know to team Timoschka belongs and based on that Timoschka's team is gonna be the Blue Team
            blueteamId = participant['teamId']
    for participant in student['info']['participants']: # get blue/red team total assists
        if participant["teamId"] == blueteamId & participant["teamId"] != 0:
            # Add the participant's assists to the BlueTeam assists
            BlueTeam_assists += participant['assists']
            
        if participant["teamId"] != blueteamId & participant["teamId"] != 0:
            # Add the participant's assists to the RedTeam assists
            RedTeam_assists += participant['assists']
    # mydict['blueAssists'] = BlueTeam_assists
    # mydict['redAssists'] = RedTeam_assists
    for participant in student['info']['participants']: # get blue/red team total gold earned
        if participant["teamId"] == blueteamId & participant["teamId"] != 0:
            # Add the participant's total gold to the BlueTeam total gold
            BlueTeam_goldEarned += participant['goldEarned']
            
        if participant["teamId"] != blueteamId & participant["teamId"] != 0:
            # Add the participant's total gold to the RedTeam total gold
            RedTeam_goldEarned += participant['goldEarned']
            
    # mydict['blueTotalGold'] = BlueTeam_goldEarned
    # mydict['redTotalGold'] = RedTeam_goldEarned
    redGoldDiff = RedTeam_goldEarned - BlueTeam_goldEarned
    # mydict['redGoldDiff'] = redGoldDiff
    blueGoldDiff = BlueTeam_goldEarned - RedTeam_goldEarned
    # mydict['blueGoldDiff'] = blueGoldDiff
    for participant in student['info']['participants']: # get blue/red team Average level
        if participant["teamId"] == blueteamId & participant["teamId"] != 0:
            # Add the participant's Average level to the BlueTeam Average level
            BlueTeam_championLevel += participant['champLevel']
        if participant["teamId"] != blueteamId & participant["teamId"] != 0:
            # Add the participant's Average level to the RedTeam Average level
            RedTeam_championLevel += participant['champLevel']
    BlueTeam_AvgLevel = BlueTeam_championLevel/5
    # mydict['blueAvgLevel'] = BlueTeam_AvgLevel
    RedTeam_AvgLevel = RedTeam_championLevel/5
    # mydict['redAvgLevel'] = RedTeam_AvgLevel
    for team in student['info']['teams']:        
        if team['teamId']==blueteamId:
            # print('This is BlueTeam kills: ')
            # print(team['objectives']['champion']['kills'],team['teamId'])   # get champkills of the team with the corresponding teamId. if teamId == teamId of Timoschka, then champkills are Blue team champion kills
            BlueteamKills = team['objectives']['champion']['kills']
            # mydict['blueKills'] = BlueteamKills
            # print('This is BlueTeam Firstblood: ')
            # print(team['objectives']['champion']['first'],team['teamId'])
            BlueTeamfirstblood = team['objectives']['champion']['first']
            # mydict['blueFirstBlood'] = BlueTeamfirstblood
            # print('BlueTeam Win: ',team['win'])
            BlueTeamWin = team['win']   # ersetzen mit '0' anstatt 'false/true' blueWins
            if BlueTeamWin == False:
                BlueTeamWin = 0
            if BlueTeamWin == True:
                BlueTeamWin = 1
            # mydict['blueWins'] = BlueTeamWin
        else:
            # print('This is RedTeam kills: ')
            # print(team['objectives']['champion']['kills'],team['teamId'])
            RedteamKills = team['objectives']['champion']['kills']
            # mydict['redKills'] = RedteamKills
            # print('This is RedTeam Firstblood: ')
            # print(team['objectives']['champion']['first'],team['teamId'])
            RedTeamfirstblood = team['objectives']['champion']['first']
            # mydict['redFirstBlood'] = RedTeamfirstblood
            # print('RedTeam Win: ',team['win'])
            RedTeamWin = team['win']
    mydict['gameId'] = gameId
    mydict['blueAssists'] = BlueTeam_assists
    mydict['redAssists'] = RedTeam_assists
    mydict['blueTotalGold'] = BlueTeam_goldEarned
    mydict['redTotalGold'] = RedTeam_goldEarned
    mydict['redGoldDiff'] = redGoldDiff
    mydict['blueGoldDiff'] = blueGoldDiff
    mydict['blueAvgLevel'] = BlueTeam_AvgLevel
    mydict['redAvgLevel'] = RedTeam_AvgLevel
    mydict['blueKills'] = BlueteamKills
    mydict['blueFirstBlood'] = BlueTeamfirstblood
    mydict['blueWins'] = BlueTeamWin
    mydict['redKills'] = RedteamKills
    mydict['redFirstBlood'] = RedTeamfirstblood
    data.append(mydict)

# Create a dataframe from the list of dictionaries
df = pd.DataFrame(data)
# Print the dataframe
print(df)