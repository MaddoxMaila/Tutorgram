from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello() :
	return 'Hello world'

@app.route('/home/')

def home() :

	return 'Im Home Guys'