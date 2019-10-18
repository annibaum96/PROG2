from datetime import datetime
import json

def speichern(datei, key, value):
	try:
		with open(datei) as open_file:
			datei_inhalt = json.load(open_file)
	except FileNotFoundError:
		datei_inhalt = {}

	datei_inhalt[str(key)] = value

	print(datei_inhalt)

	with open(datei, "w") as open_file:
		json.dump(datei_inhalt, open_file)

def termin_abspeichern(termin):
	datei_name = "termine.json"
	zeitpunkt = datetime.now()
	speichern(datei_name, zeitpunkt, termin)
	return zeitpunkt, termin

def termine_laden():
	datei_name = "termine.json"
	try:
		with open(datei_name) as open_file: 
			datei_inhalt = json.load(open_file)
	except FileNotFoundError:
		datei_inhalt = {}

	return datei_inhalt


