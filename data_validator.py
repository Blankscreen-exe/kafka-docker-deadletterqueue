from data_gen.data_gen import data_create
import json
import random

#taking settings into account
settings = open("settings.json")
setting = json.loads(settings.read())

def data_validate(data):
    
    # validation report variables
    playerNameErr = False
    countryNameErr = False
    teamNameErr = False

    # check for all three instances
    if not isinstance(data['playerName'], str):
        playerNameErr = True
    if not isinstance(data['country'], str):
        countryNameErr = True
    if not isinstance(data['team'], str):
        teamNameErr = True

    # validation err messages   
    playerErrMsg = "player name not of STR type"
    countryErrMsg = "country name not of STR type"
    teamErrMsg = "team name not of STR type"

    if not any([playerNameErr,countryNameErr,teamNameErr]):
        # if all good
        # send it to status checker
        return data
    else:
        # if something is wrong
        # attach headers
        return {
            "playerErr" : playerErrMsg if playerNameErr else None,
            "countryErr": countryErrMsg if countryNameErr else None,
            "teamErr": teamErrMsg if teamNameErr else None,
            "recievedData": data
            }

#test 
# print(data_validate(data_create(1,2,3,setting["dataGeneratorSettings"]["errFrequency"])))