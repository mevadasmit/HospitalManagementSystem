import psycopg2
from constant import DATABASE_CONNECTION_ERROR   

class DatabaseConnection:
    
    def __init__(self,config):

        self.database_connection = None
        self.cursor_connection = None
        self.config = config
        try:

            self.database_connection = psycopg2.connect(host = self.config.hostname, 
                dbname = self.config.database , user = self.config.username , 
                password = self.config.pwd , port = self.config.port_id)
            
            self.database_connection.autocommit = True

            self.cursor_connection = self.database_connection.cursor()

        except Exception as error:
            print(DATABASE_CONNECTION_ERROR,error)

    def close(self):

        try:

            if self.cursor_connection:
                self.cursor_connection.close()

            if self.database_connection:
                self.database_connection.close()

        except Exception as error:
            print(error)
