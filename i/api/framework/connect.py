import pymysql
import json

 # Class To Help Work With MySQL Database Much Easier

class Query :

	Connection = None

	query = None

	def __init__(self) :

		try:
			
			# Connect To The Database
			self.Connection = pymysql.connect(host = 'localhost', user = 'root', password = '', database = 'tutorgram')

			# Create A Cursor From The Connection Variable
			self.query = self.Connection.cursor()

			# Now We Can Use The Cursor To Make Database Queries

		except Exception as e:
			
			# Handle The Exception By Printing It Out
			print(json.dumps({'error': True, 'message': e }))

	# End Of Constructor

	# Method To Return The Cursor
	def cursor(self) :

		return self.query

	# End Of Cursor()