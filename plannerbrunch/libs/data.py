import json
#json file inhalt laden, wenn kein inhalt vorhanden -> Struktur anlegen
def load_json(name):
    json_daten = {}
    
    try:
        with open("data/data.json") as open_file:
            json_daten = json.load(open_file)
    except FileNotFoundError:
        json_daten = {
            name: {
                }
            }
    return json_daten

#json file überschreiben mit neuem Inhalt
def save_json(data):
    with open("data/data.json", "w") as open_file:
        json.dump(data, open_file, ensure_ascii=False, indent=4)
    
#input werte in json file anfügen. 1. json file laden + Inhalt ausgeben 2. neuer Eintrag in vorhandenes dict anfügen 3. json file neu speichern
def aktivitaet_speichern(name, date, beginn, ende, verantwortung, beteiligung):
    json_daten = load_json(name)
    json_daten[name] = {
        "Aktivität": name, "Datum": date, "Beginn": beginn, "Ende": ende, "Verantwortung": verantwortung, "Stufe TN": beteiligung
        }
    save_json(json_daten)


#json file laden um Übersicht zu laden
def load_overview(): 
	try: 
		with open("data/data.json") as f: 
			data = json.load(f)
	except FileNotFoundError:
		print("Es sind noch keine Termine erfasst.")
	return data

