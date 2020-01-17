""" 
Summary: 
    Main python file. Includes app routes and their functions.
Attributes:
    app: Name.
    app.secret_key: Needed for flash messages. 
"""

from flask import Flask, render_template, request, flash
from libs import data
from datetime import datetime

app = Flask("Planner")
app.secret_key = 'kn/Ujlkm#[sdfnop]jnnq/km*'

#Startseite
@app.route('/index')
@app.route('/')
def startseite():
	"""
    Summary: 
    Starts webpage. No input.
    From there a User can navigate to "Eintrag erfassen", "Übericht" or "Export Calendar".   
        
    Returns:
    Index.html, which shows only NavBar and a Message. 
    """
	return render_template('index.html')


#Seite um eine Aktivität nach der anderen zu erfassen
@app.route('/erfassen', methods = ['POST', 'GET'])
def erfassen():
	"""
    Summary: 
    Page to add a new activity/date. 

    Input: 
    User fills in the details for event, will be saved in a json file.
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
    Shows table of all activites entered (saved in json file) including current amount of entrys in json-file. 
    If non existing file or emtpy file = empty table.

    Input:
    Possibility to delete an entry --> will flash a message, update number of current entrys in json-file, update table.
            
    Returns:
    Overview.  
    """
	if request.method == 'POST':
		flash('Die Aktivität wurde erfolgreich gelöscht.')
		jahresplan = data.load_overview()
		result=request.form['eintrag']
		del jahresplan[result]
		data.save_json(jahresplan)
		anzahl = data.count_entrys()
		return render_template('overview_termine.html', jahresplan = jahresplan, anzahl = anzahl)
	else:
		jahresplan = data.load_overview()
		anzahl = data.count_entrys()
		return render_template('overview_termine.html', jahresplan = jahresplan, anzahl = anzahl)

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