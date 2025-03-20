from database_connection import DatabaseConnection
from constant import DATABASE_SUCCESS,DB_ERROR

class DatabaseSetup():

    def __init__(self,connection):

        self.connection = connection

    def create_table(self):

        try:

            # self.connection.cursor_connection.execute('''DROP TABLE IF EXISTS roles CASCADE''')
            # self.connection.cursor_connection.execute('''DROP TABLE IF EXISTS department_details CASCADE''')
            # self.connection.cursor_connection.execute('''DROP TABLE IF EXISTS shift CASCADE''')
            # self.connection.cursor_connection.execute('''DROP TABLE IF EXISTS users CASCADE''')
            # self.connection.cursor_connection.execute('''DROP TABLE IF EXISTS patients_detail CASCADE''')
            # self.connection.cursor_connection.execute('''DROP TABLE IF EXISTS doctors_detail CASCADE''')
            # self.connection.cursor_connection.execute('''DROP TABLE IF EXISTS shift_manage CASCADE''')
            # self.connection.cursor_connection.execute('''DROP TABLE IF EXISTS appointments CASCADE''')
            # self.connection.cursor_connection.execute('''DROP TABLE IF EXISTS bill CASCADE''')
            # self.connection.cursor_connection.execute('''DROP TABLE IF EXISTS report CASCADE''')
            # self.connection.cursor_connection.execute('''DROP TABLE IF EXISTS report_type CASCADE''')
            # self.connection.cursor_connection.execute('''DROP TABLE IF EXISTS hospital_staff_details CASCADE''')


            create_role_table = '''CREATE TABLE IF NOT EXISTS roles(id SERIAL NOT NULL PRIMARY KEY,
                                                        role_name varchar(50)) '''

            create_department_table = ''' CREATE TABLE IF NOT EXISTS department_details(id SERIAL NOT NULL PRIMARY KEY,
                                                        department_name varchar(50))'''

            create_shift_table = ''' CREATE TABLE IF NOT EXISTS shift(id SERIAL NOT NULL PRIMARY KEY, 
                                                        day_name varchar(20))'''

            create_user_table = '''CREATE TABLE IF NOT EXISTS users(id SERIAL NOT NULL PRIMARY KEY,
                                                        name varchar(20), age int,
                                                        gender varchar(20), blood_group varchar(10),
                                                        phone_number bigint, email varchar(200),
                                                        address text , password varchar(20), 
                                                        role_id int NOT NULL REFERENCES roles(id),
                                                        created_at TIMESTAMP DEFAULT NOW(),
                                                        updated_at TIMESTAMP DEFAULT NOW(),
                                                        created_by int REFERENCES users(id) ON DELETE CASCADE,
                                                        updated_by int REFERENCES users(id) ON DELETE CASCADE)'''

            create_patient_table = '''CREATE TABLE IF NOT EXISTS patients_detail(id SERIAL NOT NULL PRIMARY KEY,
                                                        user_id int NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                                                        created_at TIMESTAMP DEFAULT NOW(),
                                                        updated_at TIMESTAMP DEFAULT NOW(),
                                                        created_by int REFERENCES users(id) ON DELETE CASCADE,
                                                        updated_by int REFERENCES users(id) ON DELETE CASCADE)'''

            create_doctors_table = ''' CREATE TABLE IF NOT EXISTS doctors_detail(id SERIAL NOT NULL PRIMARY KEY,
                                                        user_id int NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                                                        joining_date date , consultation_fees int , 
                                                        department_id int NOT NULL REFERENCES department_details(id) ON DELETE CASCADE,
                                                        created_at TIMESTAMP DEFAULT NOW(),
                                                        updated_at TIMESTAMP DEFAULT NOW(),
                                                        created_by int REFERENCES users(id) ON DELETE CASCADE,
                                                        updated_by int REFERENCES users(id) ON DELETE CASCADE)'''


            create_shift_manage_table = ''' CREATE TABLE IF NOT EXISTS  shift_manage(id SERIAL NOT NULL PRIMARY KEY,
                                                        shift_id int NOT NULL REFERENCES shift(id) ON DELETE CASCADE,
                                                        doctors_detail_id int NOT NULL REFERENCES doctors_detail(id) ON DELETE CASCADE)'''
            
            create_appointment_table = ''' CREATE TABLE IF NOT EXISTS appointments(id SERIAL NOT NULL PRIMARY KEY,
                                                        doctors_detail_id int NOT NULL REFERENCES doctors_detail(id) ON DELETE CASCADE,
                                                        patients_detail_id int NOT NULL REFERENCES patients_detail(id) ON DELETE CASCADE,
                                                        appointment_details varchar(200),appointment_date date,
                                                        created_at TIMESTAMP DEFAULT NOW() ,
                                                        updated_at TIMESTAMP DEFAULT NOW(),
                                                        created_by int REFERENCES users(id) ON DELETE CASCADE,
                                                        updated_by int REFERENCES users(id) ON DELETE CASCADE)'''
            
            create_bill_table = ''' CREATE TABLE IF NOT EXISTS bill(id SERIAL NOT NULL PRIMARY KEY,
                                                        appointment_id int NOT NULL REFERENCES appointments(id) ON DELETE CASCADE,
                                                        total_amount int,
                                                        created_at TIMESTAMP DEFAULT NOW(),
                                                        updated_at TIMESTAMP DEFAULT NOW(),
                                                        created_by int REFERENCES users(id) ON DELETE CASCADE,
                                                        updated_by int REFERENCES users(id) ON DELETE CASCADE)'''
            
            create_report_table = ''' CREATE TABLE IF NOT EXISTS report(id SERIAL NOT NULL PRIMARY KEY,
                                                        appointment_id int NOT NULL REFERENCES appointments(id) ON DELETE CASCADE,
                                                        created_at TIMESTAMP DEFAULT NOW(),
                                                        updated_at TIMESTAMP DEFAULT NOW(),
                                                        created_by int REFERENCES users(id) ON DELETE CASCADE,
                                                        updated_by int REFERENCES users(id) ON DELETE CASCADE)'''

            create_report_type_table = ''' CREATE TABLE IF NOT EXISTS report_type(id SERIAL NOT NULL PRIMARY KEY,
                                                        report_id int NOT NULL REFERENCES report(id) ON DELETE CASCADE,
                                                        report_name varchar(100),
                                                        report_description varchar(250),
                                                        created_at TIMESTAMP DEFAULT NOW(),
                                                        updated_at TIMESTAMP DEFAULT NOW(),
                                                        created_by int REFERENCES users(id) ON DELETE CASCADE,
                                                        updated_by int REFERENCES users(id) ON DELETE CASCADE)'''

            create_hospital_staff_table = ''' CREATE TABLE IF NOT EXISTS hospital_staff_details(id SERIAL NOT NULL PRIMARY KEY,
                                                        shift_id int NOT NULL REFERENCES shift(id) ON DELETE CASCADE,
                                                        user_id int NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                                                        created_at TIMESTAMP DEFAULT NOW(),
                                                        updated_at TIMESTAMP DEFAULT NOW(),
                                                        created_by int REFERENCES users(id) ON DELETE CASCADE,
                                                        updated_by int REFERENCES users(id) ON DELETE CASCADE)'''


            # self.connection.cursor_connection.execute(create_role_table)
            # self.connection.cursor_connection.execute(create_department_table)
            # self.connection.cursor_connection.execute(create_shift_table)
            # self.connection.cursor_connection.execute(create_user_table)
            # self.connection.cursor_connection.execute(create_patient_table)
            # self.connection.cursor_connection.execute(create_doctors_table)
            # self.connection.cursor_connection.execute(create_shift_manage_table)
            # self.connection.cursor_connection.execute(create_appointment_table)
            # self.connection.cursor_connection.execute(create_bill_table)
            # self.connection.cursor_connection.execute(create_report_table)
            # self.connection.cursor_connection.execute(create_report_type_table)
            # self.connection.cursor_connection.execute(create_hospital_staff_table)


            create_tables = [
                create_role_table, create_department_table, create_shift_table, create_user_table,
                create_patient_table, create_doctors_table, create_shift_manage_table, create_appointment_table,
                create_bill_table, create_report_table, create_report_type_table, create_hospital_staff_table
            ]

            for create_table in create_tables:
                self.connection.cursor_connection.execute(create_table)

            
            print(DATABASE_SUCCESS)

        except Exception as error:
            print(DB_ERROR,error)

    def insert_data(self):

        try:

            insert_role = ''' INSERT INTO roles(id,role_name) VALUES (%s,%s)'''
            insert_values = [(1,'Admin'),(2,'Doctor'),(3,'Patient'),(4,'Nurse'),(5,'Receptionist')]

            for record in insert_values:
                self.connection.cursor_connection.execute(insert_role,record)

            insert_shift = ''' INSERT INTO shift(id,day_name) VALUES (%s,%s)'''
            insert_values = [(1,'Monday'),(2,'Tuesday'),(3,'Wednesday'),(4,'Thursday'),(5,'Friday'),(6,'Saturday'),(7,'Sunday')]

            for record in insert_values:
                self.connection.cursor_connection.execute(insert_shift,record)

            insert_department = ''' INSERT INTO department_details(id,department_name) VALUES(%s,%s)'''
            insert_values = [(1,'General Surgery'),(2,'Orthopedics'),(3,'Cardiology'),(4,'Neurology'),(5,'Physiotherapy')]

            for record in insert_values:
                self.connection.cursor_connection.execute(insert_department,record)

            insert_user = '''INSERT INTO users(name,age,gender,blood_group,phone_number,email,address,password,role_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
            insert_values = [('Kaushal Raval',28,'Male', 'B+', 9859685485, 'kaushal12@gmail.com','5-Modi nagar palanpur','kaushal12',3)]

            for record in insert_values:
                self.connection.cursor_connection.execute(insert_user,record)

        except Exception as error:
            print(error)

