import json

def speichern(name, datum, beginn, ende, verantwortung, beteiligung):
	jahresplan = {}

	jahresplan[name] = {
		'datum' : datum, 
		'beginn' : beginn,
		'ende' : ende,
		'verantwortung' : verantwortung, 
		'beteiligung' : beteiligung
	}

	with open('data/data.json', 'a+', encoding = 'utf-8') as openfile: 
		json.dump(jahresplan, openfile, indent = 4)
		