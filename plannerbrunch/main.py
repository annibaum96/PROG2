from flask import Flask, render_template, request, flash
from libs import data
import datetime

app = Flask("Planner")
app.secret_key = 'kn/Ujlkm#[sdfnop]jnnq/km*'

#Startseite
@app.route('/index', methods = ['POST', 'GET'])
@app.route('/')
def startseite():
	if request.method == 'POST':
		result=request.form['name']
		return render_template('index.html',result = result)
	else:
		return render_template('index.html')


#Seite um eine Aktivität nach der anderen zu erfassen
@app.route('/erfassen', methods = ['POST', 'GET'])
def erfassen():
	if request.method == 'POST':
		flash('Die Aktivität wurde erfolgreich erfasst.')
		akt=request.form['aktivitaet']
		date=request.form['datum']
		time=request.form['beginn']
		time2=request.form['ende']
		who=request.form['verantwortung']
		who2=request.form.getlist('beteiligt')
		jahresplan = data.aktivitaet_speichern(akt, date, time, time2, who, who2)
		return render_template('termin_erfassen.html', len=len, akt=akt, who2=who2)

	else:
		return render_template('termin_erfassen.html', len=len)

#Hier können alle erfassten Daten geprüft und gegebenenfalls gelöscht werden
@app.route('/uebersicht', methods = ['POST', 'GET'])
def overview():
	if request.method == 'POST':
		flash('Die Aktivität wurde erfolgreich gelöscht.')
		return render_template('overview_termine.html',result = result)
	else:
		jahresplan = data.load_overview()
		return render_template('overview_termine.html', jahresplan = jahresplan)

# @app.route('/delete/<aktivitaet>')
# def delete_aktivitaet(aktivitaet):



#Seite um gesamte erfassten Daten in Kalender zu exportieren
@app.route('/kalender', methods = ['POST', 'GET'])
def kalender():
	if request.method == 'POST':
		result=request.form['name']
		return render_template('kalender_export.html',result = result)
	else:
		return render_template('kalender_export.html')




if __name__ == "__main__":
    app.run(debug=True, port=5000)