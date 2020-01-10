from flask import Flask, render_template, request

app = Flask("Planner")

@app.route('/index', methods = ['POST', 'GET'])
def startseite():
	if request.method == 'POST':
		result=request.form['name']
		return render_template('header.html',result = result)
	else:
		return render_template('header.html')

@app.route('/erfassen', methods = ['POST', 'GET'])
def erfassen():
	if request.method == 'POST':
		akt=request.form['aktivitaet']
		date=request.form['datum']
		time=request.form['beginn']
		time2=request.form['ende']
		who=request.form['verantwortung']
		who2=request.form.getlist('beteiligt')
		print(akt, date, time, time2, who, who2)
		return render_template('termin_erfassen.html', len=len, akt=akt, who2=who2)
	else:
		return render_template('termin_erfassen.html', len=len)

if __name__ == "__main__":
    app.run(debug=True, port=5000)