from flask import Flask, render_template, request

app = Flask("Hello World")

@app.route('/brunch', methods = ['POST', 'GET'])
def formular():
	if request.method == 'POST':
		result=request.form['name']
		return render_template('index.html',result = result)
	else:
		return render_template('index.html')


if __name__ == "__main__":
	app.run(debug=True, port=5000)