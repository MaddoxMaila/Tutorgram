from connect import Query


# Class To Log Users In
# Login Class Inherits Query Class

class Login(Query) :

	Email = None
	Password = None
	Id = None

	# Constructor To Accept, Email & Password
	def __init__(self, email, password) :

		
		# Call The Constructor Of The Parent Class To Initialize The Database Connection
		Query.__init__(self)

		self.Email = email
		self.Password = password

		

	# End Of Login Constructor

	# Login Method To Actually Log The User In

	def login(self) :

		# Login Query
		self.cursor().execute("SELECT user_id FROM users WHERE email = '{}' AND user_pass = '{}'".format(self.Email, self.Password))

		# Check If A Row Was Returned Or Not

		if self.cursor().rowcount == 1 :

			# A Row Was Returned
			self.Id = list(self.cursor().fetchone())[0]

			return True

		else :

			# A Row Was Not Returned
			return False

	# End Of Login Method

	# Method To Return The Id After Login

	def get_id(self) :

		# Return The Id

		return self.Id

	# End Of get_id Method
