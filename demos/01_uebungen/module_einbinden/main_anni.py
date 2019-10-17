from flask import Flask
from rabatte import preise_b
from rabatte.preise_b import grosser_r


app = Flask("module")

@app.route('/<preis>')
def rabatte(preis): # Argument in Funktion darf nicht vergessen gehen. Muss hier, sowie im eingebundenen Modul angesprochen sein
	# preis_weniger_rabatt = preise_a.berechnung(int(preis)) --> Diese Option, wenn gesamtes Modul importiert wird
	preis_weniger_rabatt = berechnung(int(preis)) #Diese Option, wenn gezielt die Funktion importiert wurde
	
	return "Der neue Preis ist: " + str(preis_weniger_rabatt)

@app.route('/grosser_r/<preis>')
def grosser_rabatt(preis):
	preis_weniger_rabatt = grosser_r(int(preis))
	return "Der neue Preis, mit grossem Rabatt beträgt: " + str(preis_weniger_rabatt)


if __name__ == "__main__":
	app.run(debug=True, port=5000)

