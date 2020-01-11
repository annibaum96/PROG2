import json

# Struktur Dictionary

def aktivitaet_speichern(name, datum, beginn, ende, verantwortung, beteiligung):
	data = {}
	data['Aktivitaet'] = []
	data['Aktivitaet'].append({
	    'name': name,
	    'datum': datum,
	    'beginn': beginn,
	    'ende': ende,
	    'verantwortung': verantwortung,
	    'beteiligung': beteiligung
	})

	with open('data.txt', 'w') as outfile:
	    json.dump(data, outfile)

def load_json():
    json_daten = {}
    try:
        with open('data/data.json') as open_file:
            json_daten = json.load(open_file)
    
    except FileNotFoundError:    
        print("File not found")

    return json_daten

def save_to_json(daten):
    with open('data/data.json', "w", encoding="utf-8") as open_file:
        json.dump(daten, open_file)