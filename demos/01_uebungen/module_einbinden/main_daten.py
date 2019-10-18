from flask import Flask
import daten

app = Flask("Persistente Daten")

@app.route("/speichern/<termin>")
def speichern(termin):
	zeitpunkt, termin = daten.termin_abspeichern(termin)

	return "Folgender Termin wurde gespeichert: " + termin + str(zeitpunkt)

@app.route("/agenda")
def auflistung():
	termine = daten.termine_laden()

	agenda = ""
	for key, value in termine.items():
		zeile = str(key) + ": " + value + "<br>"
		agenda += zeile

	return agenda
	 

if __name__ == "__main__":
	app.run(debug=True, port=5000)