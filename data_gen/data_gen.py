import uuid
import json
import random

#Generate data packet
def data_gen(count,consumerID,producerID,errcode):
    '''
    This function generates a dummy data packet.
    >>PARAMS
    count: int
    consumerID: str
    producerID: str
    errcode: list[boolean] len()=3
    >>RETURNS
    json object
    '''
    #Selecting country name
    if errcode[0]==True:
        countryName = 123
    else:
        countryList = ["USA", "Paksitan", "Europe", "Japan"]
        countryName = random.choice(countryList)

    #Selecting player name
    playerList = [
  "Knight Lee",
  "Mcdowell Griffin",
  "Ora Marquez",
  "Fitzgerald Bonner",
  "Christian Bryant",
  "Sweeney Franks",
  "Katheryn Swanson",
  "Conrad Carr",
  "Robinson Emerson",
  "Lara French",
  "Sonja Gibson",
  "Lacey Morrison",
  "Trujillo Salinas",
  "Rojas Boone",
  "Lynch Evans",
  "Chan Kidd",
  "Juliet Orr",
  "Flynn Golden",
  "Vonda Watts",
  "Karla Snyder",
  "Weiss Fischer",
  "Anthony Rios",
  "Sharon Cortez",
  "Gwen Hogan",
  "Ola Webster",
  "Meagan Hendrix",
  "Jordan Battle",
  "Carney Haley",
  "Stokes Quinn",
  "Barr Newton",
  "Hewitt Buckner",
  "Maxwell Walton",
  "Monica Walsh",
  "Villarreal Dale",
  "Banks Strickland",
  "Patsy Higgins",
  "Benita Best",
  "Brewer Casey",
  "Louise Lowe",
  "Slater Parsons",
  "Hyde Britt",
  "Glover Richard",
  "Virginia Banks",
  "Fay Knowles",
  "Massey Porter",
  "Ann Rich",
  "Angeline Pickett",
  "Tamera Forbes",
  "Frank Ramsey",
  "Keisha Perkins"
]
    if errcode[1]==True:
        playerName = 123
    else:
        playerName = random.choice(playerList)
    
    #Selecting team name
    teamList = ["OakenShield", "Thorfinn", "D.D.D", "Sedated", "RiskyBoots", "Gandalves", "Griffindor", "Cthulhu", "RottyTop", "Sherlock", "Ritcher", "ShieldKnight"]
    if errcode[2]==True:
        teamName = 123
    else:
        teamName = random.choice(teamList)

    #Selecting isOUT isPlaying logic
    isOUT = random.choice([True,False])
    isPlaying = random.choice([True,False]) if isOUT==False else False

    return json.dumps({
            "_id": str(uuid.uuid4()),
            "packetID": count,
            "consumerID":consumerID,
            "producerID":producerID,
            "playerName": playerName,
            "team": teamName,
            "country": countryName,
            "individualScore": random.randrange(0, 40),
            "playerStatus": {
                "isOut": isOUT,
                "isPlaying": isPlaying
            }
        }, indent = 4)

# test code
# print([datagen(1,12,22),datagen(1,12,22),datagen(1,12,22),datagen(1,12,22)])

def data_create_err(count,consumerID,producerID,errCode):
    '''
    This function allows occasional errors while generating json data packets.
    >>PARAMS
    count: int
    consumerID: str
    producerID: str
    errCode: boolean
    >>RETURNS
    json object
    '''
    #random error generator
    if errCode==True:
        randErr = [random.choice([True,False]) for i in range(3)]
    else:
        randErr = [False,False,False]
    
    # generate data packet
    data = json.loads(data_gen(count,consumerID,producerID,randErr))
    return data

def data_create(count,consumerID,producerID,err):
    '''
    this funciton generates a predefined data packet with random occasional errors.
    >>PARAMS
    count: int
    consumerID: str
    producerID: str
    err: boolean
    >>RETURNS
    json object
    '''
    # calculating percentage chance for error to occur
    err_chance = [True]*err
    no_err_chance = [False]*(10 - len(err_chance))
    err_chance.extend(no_err_chance)
    errSignal = random.choice(err_chance)
    data = data_create_err(count,consumerID,producerID,errSignal)
    
    return data

#test
# print(data_create(7))
# print([data_create(7) for i in range(6)])