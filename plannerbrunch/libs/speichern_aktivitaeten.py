import json

# Struktur Dictionary

def aktivitaet_speichern(name, datum, beginn, ende, verantwortung, beteiligung):	
	
	jahresplan_daten = load_json()
	aktivitaeten = jahresplan_daten.get("jahresplan", {})

	aktivitaet = {
	    'name': name,
	    'datum': datum,
	    'beginn': beginn,
	    'ende': ende,
	    'verantwortung': verantwortung,
	    'beteiligung': beteiligung
	}

	save_json(aktivitaeten)	

def load_json():
    jahresplan = {}
    # jahresplan['aktivitaet'] = []
    try:
        with open('data/data.json') as open_file:
            json_daten = json.load(open_file)
    
    except FileNotFoundError:    
        json_daten = {
        	'jahresplan': {
        		'aktivitaet': {

        		}
        	}
        }

    return json_daten

def save_json():
   with open('data/data.json', 'w', encoding = "utf-8") as open_file:
	    json.dump(jahresplan, aktivitaeten, indent = 2)


# import json

# # Struktur Dictionary

# def aktivitaet_speichern(name, datum, beginn, ende, verantwortung, beteiligung):	
	
# 	jahreplan_daten = load_json()
# 	aktivitaeten = jahresplan_daten.get("aktivitaet", {})

# 	jahresplan['aktivitaet'].append({
# 	    'name': name,
# 	    'datum': datum,
# 	    'beginn': beginn,
# 	    'ende': ende,
# 	    'verantwortung': verantwortung,
# 	    'beteiligung': beteiligung
# 	})




	

# def load_json():
#     jahresplan = {}
#     # jahresplan['aktivitaet'] = []
#     try:
#         with open('data/data.json') as open_file:
#             json_daten = json.load(open_file)
    
#     except FileNotFoundError:    
#         json_daten = {
#         	'aktivitaet': {

#         	}
#         }

#     return json_daten

# def save_to_json():
#    with open('data/data.json', 'w', encoding = "utf-8") as jahresplan_data:
# 	    json.dump(jahresplan, jahresplan_data, indent = 2)