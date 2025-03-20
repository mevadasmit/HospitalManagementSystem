from validations import (valid_name,valid_age,valid_gender,valid_number,valid_blood_group,valid_email)
from fetch import execute_query , fetch_one
from prettytable import PrettyTable
from database_query import (NURSE_PROFILE,VALIDATE_DOCTOR, DOCTOR_AVAILABEL,
                            VALIDATE_APPOINTMENT_ID, DELETE_APPOINTMENTS_BY_RE, CREATE_PATIENT, INSERT_PATIENT_TABLE,
                            CREATE_BILL, VALIDATE_BILL, UPDATE_BILL, DELETE_BILL , PATIENT_ID )
from admin import AdminFeatures
from nurse import NurseFeatures

from constant import (RECEPTIONIST_PROFILE, PROFILE_NOT_FOUND, PROFILE_FETCH_ERROR, DOCTOR_AVAILABILITY, DOCTOR_NO_SHIFT, DOCTOR_AVAILABILITY_ERROR,
                    APPOINTMENT_MENU, ENTER_CHOICE, INVALIDCHOICE, APPOINTMENT_VIEW,ENTER_DOCTOR_ID, PATIENT_ID,
                    ENTER_APPOINTMENT_ID, APPOINTMENT_DELETE, DELETION_ERROR , PATIENT_NAME , PATIENT_AGE , PATIENT_EMAIL , PATIENT_GENDER , PATIENT_ADDRESS ,
                    USER_BLOOD_GROUP, PATIENT_PHONE_NUMBER, PATIENT_REGISTRATION, RECEPTIONIST_BILL_MENU, RETURN_BACK, DELETE_BILL_ID
                    ,BILL_DELETION_ERROR, TOTAL_BILL_AMOUNT, BILL_CREATE_SUCCESS, BILL_CREATE_ERROR , BILL_ID ,NEW_BILL_AMOUNT, BILL_UPDATE_SUCCESS ,
                    BILL_UPDATE_ERROR, RECEPTIONIST_MENU , VALIDCHOICE , EXIT , DELETE_BILL, DOCTOR_ID_NOT_EXIST,
                    BILL_ID_NOT_FOUND, FIELD , DETAILS, FIELD_USER_ID, FIELD_EMAIL,
                    FIELD_NAME,FIELD_PHONE_NUMBER,FIELD_ADDRESS, FIELD_GENDER, FIELD_BLOOD_GROUP)

class ReceptionistFeatures:

    def __init__(self, connection, user_id):
        self.connection = connection
        self.user_id = user_id

    def view_profile(self):
        """ Receptionist can view the profile details."""
        try:

            # Query to fetch receptionist details
            receptionist = fetch_one(self.connection , NURSE_PROFILE, (self.user_id,) )

            print(RECEPTIONIST_PROFILE)
            # Display profile details
            if receptionist:
                table = PrettyTable()
                table.field_names = [FIELD, DETAILS]
                table.add_row([FIELD_USER_ID, receptionist[0]])
                table.add_row([FIELD_NAME, receptionist[1]])
                table.add_row([FIELD_EMAIL, receptionist[2]])
                table.add_row([FIELD_PHONE_NUMBER, receptionist[3]])
                table.add_row([FIELD_ADDRESS, receptionist[4]])
                table.add_row([FIELD_GENDER, receptionist[5]])
                table.add_row([FIELD_BLOOD_GROUP, receptionist[6]])
                print(table)
                
            else:
                print(PROFILE_NOT_FOUND)
        except Exception as error:
            print(PROFILE_FETCH_ERROR, error)


        """ Receptionist can check availability of a specific doctor."""
        try:

            doctor_id = int(input(ENTER_DOCTOR_ID))
            
            # Validate Doctor ID
            doctor_exists = fetch_one(self.connection ,VALIDATE_DOCTOR, (doctor_id,))
            
            if not doctor_exists:
                print(DOCTOR_ID_NOT_EXIST)
                return    
            
            # Query to check the doctor shift
            self.connection.cursor_connection.execute(DOCTOR_AVAILABEL, (doctor_id,))
            doctor_availability = self.connection.cursor_connection.fetchall()
                        
            # Display the availability
            print(DOCTOR_AVAILABILITY)
            if doctor_availability:
                availability_table = PrettyTable()
                availability_table.field_names = ["Doctor Name", "Shift Day"]
                for doctor in doctor_availability:
                    availability_table.add_row(doctor)
                print(availability_table)
            else:
                print(DOCTOR_NO_SHIFT)
                
        except Exception as error:
            print(DOCTOR_AVAILABILITY_ERROR, error)

    def manage_appointments(self):

        while True:
            try:
                print(APPOINTMENT_MENU)

                choice = int(input(ENTER_CHOICE))

                if choice == 1:
                    NurseFeatures.view_appointments(self)
                elif choice == 2:
                    NurseFeatures.create_appointment(self)
                elif choice == 3:
                    NurseFeatures.update_appointment(self)
                elif choice == 4:
                    self.delete_appointments()
                elif choice == 5:
                    print(" \n ")
                    break
                else:
                    print(INVALIDCHOICE)    

            except Exception as error:
                print(error)

    def delete_appointments(self):

        """Using Appointment id receptionist can delete appointment. """
        try:
            appointment_id = int(input(ENTER_APPOINTMENT_ID))
            
            """ Check if the appointment exists """
            appointment = fetch_one(self.connection,VALIDATE_APPOINTMENT_ID, (appointment_id,))
            if not appointment:
                print(APPOINTMENT_VIEW)
                return
            
            # query to delete the appointments
            execute_query(self.connection , DELETE_APPOINTMENTS_BY_RE, (appointment_id,))
            
            print(APPOINTMENT_DELETE)
        except Exception as error:
            print(DELETION_ERROR , error)

    def patient_register(self):
        
        try:

            name = input(PATIENT_NAME)
            valid_name(name)

            age =  int(input(PATIENT_AGE))
            valid_age(age)

            gender = input(PATIENT_GENDER)
            valid_gender(gender)

            blood_group = input(USER_BLOOD_GROUP)
            valid_blood_group(blood_group)

            phone_number = input(PATIENT_PHONE_NUMBER)
            valid_number(phone_number)

            email = input(PATIENT_EMAIL)
            valid_email(email)

            address = input(PATIENT_ADDRESS)
            
            password = AdminFeatures.generate_random_password(self)
            
            created_by = updated_by = self.user_id
            
            role_id = 3

            insert_user_data = (name,age,gender,blood_group,phone_number,email,address,password,role_id,created_by , updated_by)
            execute_query(self.connection, CREATE_PATIENT, insert_user_data)

            user_id = self.connection.cursor_connection.fetchone()[0]

            execute_query(self.connection , INSERT_PATIENT_TABLE, (user_id,created_by,updated_by))
                
            patient_id = fetch_one(self.connection , PATIENT_ID , (user_id,))[0]

            print(PATIENT_REGISTRATION.format(name=name , user_id=user_id , patient_id = patient_id , password = password))
            
        except Exception as error:
            print(error) 

    def manage_bill(self):

        while True:
            try:
                print(RECEPTIONIST_BILL_MENU)
                choice = int(input(ENTER_CHOICE))

                if choice == 1:
                    AdminFeatures.view_bill(self)
                elif choice == 2:
                    self.create_bill()
                elif choice == 3:
                    self.update_bill()
                elif choice == 4:
                    self.delete_bill()
                elif choice == 5:
                    print(RETURN_BACK)
                    break
                else:
                    print(INVALIDCHOICE)    

            except Exception as error:
                print(error)        

    def create_bill(self):
        """ Create patient bill """

        try:
            
            NurseFeatures.view_appointments(self)
            appointment_id = int(input(ENTER_APPOINTMENT_ID))        
            total_amount = int(input(TOTAL_BILL_AMOUNT))
            
            # Check if the appointment exists
            appointment = fetch_one(self.connection ,VALIDATE_APPOINTMENT_ID, (appointment_id,) )
            
            if not appointment:
                print(APPOINTMENT_VIEW)
                return
            
            # Fetch the user ID of the receptionist
            created_by = updated_by = self.user_id 

            # Insert the bill into the database
            execute_query(self.connection, CREATE_BILL, (appointment_id, total_amount, created_by, updated_by))

            print(BILL_CREATE_SUCCESS)
        except Exception as error:
            print(BILL_CREATE_ERROR, error)

    def update_bill(self):

        """ Update patient bill """

        try:
            AdminFeatures.view_bill(self)
            # Get the Bill ID to update
            bill_id = int(input(BILL_ID))
            bill = fetch_one(self.connection , VALIDATE_BILL , (bill_id, ))
            
            if not bill:
                print(BILL_ID_NOT_FOUND)
                return
            
            new_total_amount = int(input(NEW_BILL_AMOUNT))
            # Update the bill
            execute_query(self.connection , UPDATE_BILL, (new_total_amount, self.user_id, bill_id))

            print(BILL_UPDATE_SUCCESS.format(bill_id = bill_id))
        except Exception as error:
            print(BILL_UPDATE_ERROR, error)

    def delete_bill(self):

        """Delete the bill  """
        
        try:
            
            AdminFeatures.view_bill(self)
            # Get the Bill ID to delete
            bill_id = int(input(BILL_ID))
            bill = fetch_one(self.connection , VALIDATE_BILL , (bill_id, ))
            
            if not bill:
                print(BILL_ID_NOT_FOUND)
                return

            # Delete the bill
            execute_query(self.connection , DELETE_BILL, (bill_id,))
            print(DELETE_BILL_ID.format(bill_id = bill_id))
        except Exception as error:
            print(BILL_DELETION_ERROR, error)
  
    def receptionist_menu(self):

        while True:

            print(RECEPTIONIST_MENU)

            try:

                choice = int(input(ENTER_CHOICE))

                if choice == 1:
                    self.view_profile()

                elif choice == 2:
                    NurseFeatures.doctor_avalibility(self)

                elif choice == 3:
                    self.manage_appointments()
                
                elif choice == 4:
                    self.patient_register()
                
                elif choice == 5:
                    self.manage_bill()

                elif choice == 6:
                    print(EXIT)
                    break
                else:
                    print(INVALIDCHOICE)

            except ValueError:
                print(VALIDCHOICE)