from flask import Flask

app = Flask("Hello World")

@app.route('/chatz')
def hello_world():
	return 'Hello, World!'


if __name__ == "__main__":
	app.run(debug=True, port=5000)