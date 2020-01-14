import json
import datetime

def speichern(datum):
    list = datum.split("-")
    print(list)

def load_overview():
    try: 
        with open("data/data.json") as f: 
            data = json.load(f)
    except FileNotFoundError:
        print("Es sind noch keine Termine erfasst.")
    return data

def eintrag_loeschen(name):
    daten = load_overview()
    for d in daten:
        if d == name:
            
    







"""
def overview():
    jahresplan = load_overview()
    for data in jahresplan.values():
        tn = data["Stufe TN"]
        print(*tn, sep = "\n")
       

overview()
"""