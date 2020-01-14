import json

#load json for overview

def get_data(): 
	with open(data/data.json, 'r') as openfile: 
		data = json.load(openfile)
		print(data)

get_data()