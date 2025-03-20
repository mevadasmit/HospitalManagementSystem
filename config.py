import psycopg2

class Config():

	def __init__(self):

		self.hostname = "localhost"
		self.database = "hospital_management_system"
		self.username = "postgres"
		self.pwd = "<Your Password>"
		self.port_id = 5432