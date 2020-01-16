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

def table(aktivitaet):
    jahresplan = load_overview()
    eintrag = jahresplan[aktivitaet]["Stufe TN"]
    for d in eintrag:
        print(d)

table("Leiterhöck 1")


"""

def darstellung():
    jahresplan = load_overview()
    aktivitaeten = []
    for eintrag in jahresplan:
        aktivitaeten.append(eintrag)
    
    
    for a in aktivitaeten: 
        eintrag = jahresplan[a]["Stufe TN"]
        for stufe in eintrag:
            stufe = stufe.capitalize()
            return(stufe)

darstellung()
"""
 


"""
    eintrag = jahresplan[aktivitaet]["Stufe TN"]
    for data in eintrag:
        stufe = data.capitalize() 



def delete_aktivitaet(aktivitaet):
    jahresplan = load_overview()
    eintrag = jahresplan[aktivitaet]
    print(eintrag)

delete_aktivitaet("Winterplausch")
    
def overview():
    jahresplan = load_overview()
    for data in jahresplan.values():
        tn = data["Stufe TN"]
        print(*tn, sep = "\n")
       

overview()
"""