"""
Summary: 
Imports json, as the data will be saved in a json file.

To save a new enty, it will: 
1. Open or create json file
2. Load content
3. Add new entry
4. Overwrite old json-content with new one.     
Also used for only loading content. 
Returns:
New json file, content of json file.
"""
import json

"""
Summary: 
Loads the json file, if non existent creates a file, with the needed dictionary.    
    
Returns:
json_daten 
"""
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

"""
save_json()
Summary: 
Saves new dict, with added content. 

Returns:
json file 
"""
def save_json(data):
	with open("data/data.json", "w") as open_file:
		json.dump(data, open_file, ensure_ascii=False, indent=4)
    
def aktivitaet_speichern(name, date, beginn, ende, verantwortung, beteiligung):
    """
    Summary: 
    Gets added content for new entry and adds it to dict in json file.    
        
    Returns:
    current json file.  
    """
    #split date for nice format
    date = date.split("-")
    DD = str(date[2])
    MM = str(date[1])
    YYYY = str(date[0])
    date = DD + "." +  MM + "." + YYYY
	#reformat list from 'beteiligung' for nice output
    seperator = ", "
    beteiligung = seperator.join(beteiligung)

    name = name.capitalize()

    json_daten = load_json(name)
    json_daten[name] = {
        "Aktivität": name, "Datum": date, "Beginn": beginn, "Ende": ende, "Verantwortung": verantwortung, "Stufe TN": beteiligung
        }
    save_json(json_daten)


def load_overview(): 
	"""
    Summary: 
    Used for overview_termine.html to fill table, as there is no variable "name" given on this page.    
        
    Returns:
    json_daten 
    """
	try: 
		with open("data/data.json") as f: 
			data = json.load(f)
	except FileNotFoundError:
		print("Es sind noch keine Termine erfasst.")
	return data

def count_entrys():
	"""
	Summary: 
	Function for adding up the entrys.

	return: 
	amount of entrys in current dict. 
	"""
	jahresplan = load_overview()
	eintraege = [] 
	for a in jahresplan:
		eintraege.append(a)

	anz = int(len(eintraege))
	return anz