from pymongo import MongoClient
from datetime import datetime

connection = MongoClient("mongodb+srv://username: password@ekatietokanta.7dk9tsm.mongodb.net/?retryWrites=true&w=majority")
db = connection.taloudenhallinta
collection = db.taloudenhallinta

def yhdista_mongoon():
    try:
        CONNECTION_STRING="mongodb+srv://<temp>:<temp>@ekatietokanta.7dk9tsm.mongodb.net/?retryWrites=true&w=majority"
        connection = MongoClient(CONNECTION_STRING)
        print("yhteys ok")
        return connection["taloudenhallinta"]

    except Exception:
        print("Ei voida yhdistää Mongoon")

def tallenna_tiedot(nimi:str, summa:float, paivamaara:datetime):
    collection.insert_one(
        {
            "nimi": nimi,
            "summa":summa,
            "paivamaara": paivamaara
        }
    )

def nayta_tiedot():
    tiedot = []
    for rivi in collection.find():
        tiedot.append(
            rivi["nimi"] + 
            ": " +
            str(rivi["summa"])+ 
            ", " +
            (rivi ["paivamaara"]).strftime("%d.%m.%Y %H:%M")

        )
    
    return tiedot

db = yhdista_mongoon()
