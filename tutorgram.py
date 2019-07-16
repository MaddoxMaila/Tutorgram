import sys
import os
sys.path.append('i/api/framework')

from login import Login

from flask import Flask, request, session


app = Flask(__name__)

@app.route('/')

def home() :

	return str(session.get('id'))

@app.route('/i/api/', methods=['GET'])

def do_login() :

	# Check If The Requests Fields Aren't Empty
	if request.form.get('email') != '' and request.form.get('password') != '' :

		# Create Login Object

		user_login = Login(request.args.get('email'), request.args.get('password'))

		# Check If Login

		if user_login.login() :

			# Set Session ID

			session['id'] = user_login.get_id()

			return 'Loggeedd In'

		else :

			session['id'] = 0
			return 'Not Logged IN'

	else :

		return 'They Not Set'


if __name__ == '__main__' :

	app.secret_key = os.urandom(12)
	app.run(debug=True)



