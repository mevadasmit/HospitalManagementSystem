from constant import (USER_NOT_EXIST,SIGN_IN_ERROR)
from database_query import LOGIN_QUERY

class Authentication:

	def __init__(self,connection):
		
		self.connection = connection
		
	def login(self,email,passwd):
     
		try:
      
			self.connection.cursor_connection.execute(LOGIN_QUERY,(email,passwd))
			users = self.connection.cursor_connection.fetchone()
			
			if users:
				return {
					'id': users[0],
					'name':users[1],
					'role_name': users[2]
				}			
			else:
				print(USER_NOT_EXIST)

		except Exception as error:
			print(SIGN_DATABASE_INERTION_ERROR , error) 