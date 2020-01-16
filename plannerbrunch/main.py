""" 
Summary: 
    Main python file. Includes app routes and their functions.
Attributes:
    app: Description.
    app.secret_key: Description. Needed for flash messages. 
"""

from flask import Flask, render_template, request, flash
from libs import data
from datetime import datetime

app = Flask("Planner")
app.secret_key = 'kn/Ujlkm#[sdfnop]jnnq/km*'

#Startseite
@app.route('/index', methods = ['POST', 'GET'])
@app.route('/')
def startseite():
	"""
    Summary: 
    Starts webpage. 
    From there a User can navigate to "Eintrag erfassen", "Übericht" or "Export Calendar".   
        
    Returns:
    Index.html, which shows only NavBar and a Message. 
    """
	if request.method == 'POST':
		result=request.form['name']
		return render_template('index.html',result = result)
	else:
		return render_template('index.html')


#Seite um eine Aktivität nach der anderen zu erfassen
@app.route('/erfassen', methods = ['POST', 'GET'])
def erfassen():
	"""
    Summary: 
    Page to add a new activity/date. User needs to fill in Input forms.
    The details will be saved in a json file.
    If User presses the "Speichern"-Button, it will flash a Message as Confirmation.

    Returns:
    variables.  
    """
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
	"""
    Summary: 
    Shows table of all activites entered (saved in json file). 
    Possibility to delete an entry --> will flash a message. 
            
    Returns:
    Overview.  
    """
	if request.method == 'POST':
		flash('Die Aktivität wurde erfolgreich gelöscht.')
		jahresplan = data.load_overview()
		result=request.form['eintrag']
		del jahresplan[result]
		data.save_json(jahresplan)
		return render_template('overview_termine.html', jahresplan = jahresplan)
	else:
		jahresplan = data.load_overview()
		return render_template('overview_termine.html', jahresplan = jahresplan)

# def darstellung(): 
# 	jahresplan = data.load_overview()
# 	aktivitaeten = []
# 	for eintrag in jahresplan:
# 		aktivitaeten.append(eintrag)

# 	for a in aktivitaeten:
# 		eintrag = jahresplan[a]["Stufe TN"]
# 		for stufe in eintrag:
# 			stufe = stufe.capitalize()
# 			return stufe
# 			return render_template('overview_termine.html', stufe = stufe)

#Seite um gesamte erfassten Daten in Kalender zu exportieren
@app.route('/kalender', methods = ['POST', 'GET'])
def kalender():
	"""
    Summary: 
    This page is coming soon. Should give possibility to export saved informations into calendar via link. 

    Returns:
    link.  
    """
	if request.method == 'POST':
		result=request.form['name']
		return render_template('kalender_export.html',result = result)
	else:
		return render_template('kalender_export.html')




if __name__ == "__main__":
    app.run(debug=True, port=5000)