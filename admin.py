'''

(" Admin features : ")
(" 1.View and Update Patient info.")
(" 2.Create , Update , View and delete hospital staff.(Doctor , Nurse , Receptionist)")
(" 3.Create , Update , View and delete Bill management (Patients).")
(" 4.Create , Update , View and delete departments (Doctor).")
(" 5.Manage the shifts , (Doctor , View , Delete , Update ) (Nurse , Doctor , Receptionist )")

'''
from constant import (ADMIN_PATIENT_MENU, ENTER_CHOICE, RETURN_BACK, INVALIDCHOICE, OPERATION_CHOICE, LIST_PATIENT, NO_PATIENT_FOUND, PATIENT_VIEW_ERROR,
                      PATIENT_ID, PATIENT_NAME, PATIENT_AGE, PATIENT_GENDER, USER_BLOOD_GROUP, PATIENT_PHONE_NUMBER, PATIENT_EMAIL, PATIENT_ADDRESS, PATIENT_UPDATE,
                      HOSPITAL_STAFF_NOT_FOUND, DATABASE_ERROR, USER_NAME , USER_AGE , USER_GENDER, USER_PHONE_NUMBER, USER_EMAIL, USER_ADDRESS,UPDATE_STAFF_MENU,
                      ENTER_ROLE_NAME, ROLE_NOT_FOUND, ROLE_REGISTER, USER_REGISTRATION_ERROR , SHIFT_AVAILABLE, SHIFT_ID, INVALID_SHIFT_ID, HOSPITAL_STAFF_ADDED,
                      ADMIN_MAIN_MENU, EXIT, DOCTOR_JOINING_DATE, CONSULTANT_FEE, DEPARTMENT_NAME, NO_DEPARTMENT, DEPARTMENT,
                      DOCTOR_REGISTER,DELETION_ERROR, MANAGE_SHIFT, NO_SHIFT,FIELD_DAY, FIELD_SHIFT_ID, SHIFT_SUCCESS, ERROR_SHIFT_ASSIGN, VIEW_SHIFT,STAFF_DUPLICATE_SHIFT,
                      NO_SHIFT_ASSIGN, DOCTOR_SHIFT, ERROR_FETCH_SHIFT, DEPARTMENT_MENU, DEPARTMENT_CREATE_SUCESS, DEPARTMENT_DELETE_SUCESS, BILL_MENU, BILL, BILL_NOT_FOUND,
                      BILL_ERROR, NEW_BILL_AMOUNT, BILL_ID, BILL_UPDATE_SUCCESS, BILL_UPDATE_ERROR,DELETE_BILL_ID, BILL_DELETION_ERROR,STAFF_DATA_NOT_EXIST,
                      HOSPITAL_STAFF_MEMBER,PATIENT_ID_NOT_FOUND,DELETE_DOCTOR_ID, DOCTOR_ID_NOT_EXIST, DOCTOR_DATA_NOT_EXIST,DOCTORS,STAFF,STAFF_ID_NOT_FOUND,
                      USER_ID, BILL_ID_NOT_FOUND, DOCTOR_UPDATE, ENTER_DOCTOR_ID, USERS_PASSWORD,DEPARTMENT_Id,DEPARTMENT_EXIST , USER_ID_NOT_FOUND,FIELD_DOCTOR_ID,
                      DEPARTMENT_NOT_EXIST, FIELD_DEPARTMENT_ID, FIELD_DEPARTMENT_NAME, HOSPITAL_STAFF_MENU , FIELD_NAME , FIELD_AGE , FIELD_GENDER , FIELD_BLOOD_GROUP,
                      FIELD_PATIENT_ID, FIELD_PHONE_NUMBER , FIELD_USER_ID, FIELD_ROLE , FIELD_DOCTOR, FIELD_NURSE, FIELD_RECEPTIONIST , FIELD_PATIENT_NAME,DUPLICATE_SHIFT,
                      FIELD_APPOINTMENT_ID, FIELD_BILL_ID, FIELD_TOTAL_AMOUNT, FIELD_APPOINTMENT_DETAILS, FIELD_CONSULTATION_FEES,FIELD_JOINING_DATE, HOSPITAL_STAFF_UPDATED)

from prettytable import PrettyTable
from validations import (valid_name,valid_age,valid_gender,valid_number,valid_blood_group,valid_email)
import random
import string

from fetch import execute_query, fetch_one, fetch_all


from database_query import (VALIDATE_PATIENT, VIEW_PATIENT_DETAILS, UPDATE_USERS, VIEW_STAFF, ROLE_ID, DOCTOR_RECORD,USERS_DATA,
                            CREATE_PATIENT, SHOW_SHIFT, INSERT_HSM_TABLE, AVAILABLE_DEPARTMENTS, INSERT_IN_DOCTOR, DEPARTMENT_ID,
                            VALIDATE_DOCTOR,VALIDATE_USER,INSERT_SHIFT_M_TABLE,STAFF_WITH_ID,VALIDATE_SHIFT,
                            ALL_STAFF_SHIFT , ALL_DOCTOR_SHIFT, CREATE_DEPARTMENT, DELETE_DEPARTMENT,VALIDATE_BILL, UPDATE_BILL, 
                            VIEW_BILL, DELETE_BILL, UPDATE_DOCTOR , DELETE_USER , CHECK_ID , FETCH_PATIENT_DATA , DOCTORS_WITH_ID,
                            DUPLICATE_SHIFT_CHECK,STAFF_DUPLICATE_SHIFT_CHECK)

class AdminFeatures:

    def __init__(self,connection,user_id):

        self.connection = connection
        self.user_id = user_id
 
    def manage_patients(self):
        """ Using this method admin manage the patient information"""

        while True:
            try:
                print(ADMIN_PATIENT_MENU)
                choice = int(input(ENTER_CHOICE))
                if choice == 1:
                    self.view_patients()
                elif choice == 2:
                    self.update_patient_info()
                elif choice == 3:
                    print(RETURN_BACK)
                    break
                else:
                    print(INVALIDCHOICE)    

            except Exception as error:
                print(error)
    
    def view_patients(self):
        """ View the patient profile"""

        try:
            patient_id = int(input(PATIENT_ID))
            patient_exists = fetch_one(self.connection,VALIDATE_PATIENT,(patient_id,))

            if not patient_exists:
                print(PATIENT_ID_NOT_FOUND.format(patient_id = patient_id))
                return

            patients = fetch_all(self.connection, VIEW_PATIENT_DETAILS,(patient_id,))

            # display the patients
            if patients:
                print(LIST_PATIENT)
                table = PrettyTable()
                table.field_names = [FIELD_USER_ID, FIELD_PATIENT_ID, FIELD_NAME, FIELD_AGE, FIELD_GENDER, FIELD_BLOOD_GROUP, FIELD_PHONE_NUMBER]
                
                for patient in patients:
                    table.add_row(patient)
                print(table)

            else:
                print(NO_PATIENT_FOUND)

        except Exception as error:
            print(PATIENT_VIEW_ERROR,error)

    def update_patient_info(self):
        """Update the patient information"""
        try:
            # Get patient ID
            self.view_patients()
            user_id = input(USER_ID)

            user_record = fetch_one(self.connection, FETCH_PATIENT_DATA, (user_id,))
            users_id = user_record [0]
            # Input new values or keep existing ones
            name = input(f"{PATIENT_NAME} ({user_record[1]}): ") or user_record[1]
            valid_name(name)

            age = input(f"{PATIENT_AGE} ({user_record[2]}): ") or user_record[2]
            valid_age(age)

            gender = input(f"{PATIENT_GENDER} ({user_record[3]}): ") or user_record[3]
            valid_gender(gender)

            blood_group = input(f"{USER_BLOOD_GROUP} ({user_record[4]}): ") or user_record[4]
            valid_blood_group(blood_group)

            phone_number = input(f"{PATIENT_PHONE_NUMBER} ({user_record[5]}): ")
            try:
                phone_number = valid_number(phone_number, current_number=user_record[5])
            except ValueError as error:
                print(error)
                return

            email = input(f"{PATIENT_EMAIL} ({user_record[6]}): ") or user_record[6]
            valid_email(email)

            address = input(f"{PATIENT_ADDRESS} ({user_record[7]}): ") or user_record[7]
            updated_by = self.user_id
            
            update_data = (name, age, gender, blood_group, phone_number, email, address, updated_by,users_id)
            execute_query(self.connection, UPDATE_USERS,update_data)
            
            print(PATIENT_UPDATE.format(user_id = users_id))
            
        except Exception as error:
            print(error)

    def manage_staff(self):
        
        while True:
            try:
                print(HOSPITAL_STAFF_MENU)

                choice = int(input(ENTER_CHOICE))

                if choice == 1:
                    self.view_staff()
                elif choice == 2:
                    self.create_staff()
                elif choice == 3:
                    self.update_staff()
                elif choice == 4:
                    self.delete_staff()
                elif choice == 5:
                    print(RETURN_BACK)
                    break       
                else:
                    print(INVALIDCHOICE)    

            except Exception as error:
                print(error)

    def generate_random_password(self, length=8):
        """Generate a random password  (letter , digit , and special character)."""
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        return password

    def view_staff(self):

        """ Show Hospital Staff Details """
        try:
            # Query to  fetch  all staff members
            staff = fetch_all(self.connection,VIEW_STAFF)
            
            # Display Staff
            if staff:
                print(HOSPITAL_STAFF_MEMBER)
                table = PrettyTable()
                table.field_names = [FIELD_USER_ID, FIELD_NAME, FIELD_ROLE]

                for staff_member in staff:
                    table.add_row(staff_member)
                print(table)
            else:
                print(HOSPITAL_STAFF_NOT_FOUND)
        except Exception as error:
            print(DATABASE_ERROR, error)

    def create_staff(self):

        """Register a new user, assign role, and store details"""

        try:

            # Collect user detail
            name = input(USER_NAME)
            valid_name(name)

            age = input(USER_AGE)
            valid_age(age)

            gender = input(USER_GENDER)
            valid_gender(gender)

            blood_group = input(USER_BLOOD_GROUP)
            valid_blood_group(blood_group)

            phone_number = input(USER_PHONE_NUMBER)
            valid_number(phone_number)

            # Email also used as Login Id 
            email = input(USER_EMAIL)
            valid_email(email)

            address = input(USER_ADDRESS)

            # Set random generated password as final password 
            password = self.generate_random_password()

            # Show the user password for login
            print(USERS_PASSWORD.format(password = password))

            created_by = updated_by = self.user_id

            role_name = input(ENTER_ROLE_NAME)

            # Fetch role_id from the roles table
            role_id = fetch_one(self.connection, ROLE_ID, (role_name,))

            if not role_id:
                print(ROLE_NOT_FOUND.format(role_name = role_name))
                return

            role_id = role_id[0]

            # Insert entry into the users table with the role
            user_data = (name, age, gender, blood_group, phone_number, email, address, password, role_id, created_by, updated_by)
            execute_query(self.connection,CREATE_PATIENT, user_data)

            # Fetch the user ID 
            user_id = self.connection.cursor_connection.fetchone()[0]

            # Put the nurse and receptionist to seperate table for shift 
            if role_name.lower() == FIELD_NURSE or role_name.lower() == FIELD_RECEPTIONIST:
                print(HOSPITAL_STAFF_ADDED)

            # Put role of Doctor with the additional information into the doctors_detail table
            if role_name.lower() == FIELD_DOCTOR:
                self.doctor_details(user_id, created_by, updated_by)

            # Print final result
            print(ROLE_REGISTER.format(name = name , role_name = role_name))

        except Exception as error:
            print(USER_REGISTRATION_ERROR, error)

    def doctor_details(self, user_id, created_by, updated_by):

        """Add Aditional Doctor Details and Add Into Doctor Table """
        
        try:

            # Collect doctor-specific details
            joining_date = input(DOCTOR_JOINING_DATE)
            consultation_fees = int(input(CONSULTANT_FEE))

            self.view_departments()
            
            department_id = input(DEPARTMENT_Id)

            # Insert additional doctor details into the doctor table
            doctor_data = (user_id, joining_date, consultation_fees, department_id, created_by, updated_by)
            self.connection.cursor_connection.execute(INSERT_IN_DOCTOR, doctor_data)
            
            print(DOCTOR_REGISTER)
        
        except Exception as error:
            print(DELETION_ERROR, error)
        
    def update_staff(self):
        
        try:    
            while True:
                print(UPDATE_STAFF_MENU)
                choice = int(input(ENTER_CHOICE))

                if choice == 1: 
                    try:
                        self.doctors_data()
                        doctor_id = int(input(ENTER_DOCTOR_ID))
                        
                        # Check if doctor exists in doctor_details table                    
                        doctor =  fetch_one(self.connection ,VALIDATE_DOCTOR , (doctor_id,) )
                        
                        if not doctor:
                            print(DOCTOR_ID_NOT_EXIST)
                            return
                        
                        doctor_record = fetch_one(self.connection ,DOCTOR_RECORD , (doctor_id,) )                    
                        joining_date = input(f"{DOCTOR_JOINING_DATE} ({doctor_record[0]}): ") or doctor_record[0]
                            
                        consultation_fees = input(f"{CONSULTANT_FEE} ({doctor_record[1]}): ") or doctor_record[1]
                        
                        self.view_departments()
                            
                        department_id = input(f"{DEPARTMENT_Id} ({doctor_record[2]}): ") or doctor_record[2]
                        updated_by = self.user_id

                        # Update doctor details
                        update_data = (joining_date, consultation_fees, department_id, updated_by , doctor_id )
                        execute_query(self.connection , UPDATE_DOCTOR, (update_data))
                        print(DOCTOR_UPDATE.format(doctor_id = doctor_id))
                            
                    except Exception as error:
                        print(error)
                        
                elif choice == 2:
                    try:
                        
                        self.doctors_data()
                        user_id = int(input(USER_ID))
                        
                        # Check if doctor exists in doctor_details table                    
                        doctor =  fetch_one(self.connection ,VALIDATE_USER,(user_id,) )
                        
                        if not doctor:
                            print(USER_ID_NOT_FOUND.format(user_id = user_id))
                            return
                        
                        doctor_biodata = fetch_one(self.connection , USERS_DATA, ( user_id,))  
                                          
                        users_id = doctor_biodata [0]
                        # Input new values or keep existing ones
                        name = input(f"{USER_NAME} ({doctor_biodata[1]}): ") or doctor_biodata[1]
                        valid_name(name)

                        age = input(f"{USER_AGE} ({doctor_biodata[2]}): ") or doctor_biodata[2]
                        valid_age(age)

                        gender = input(f"{USER_GENDER} ({doctor_biodata[3]}): ") or doctor_biodata[3]
                        valid_gender(gender)

                        blood_group = input(f"{USER_BLOOD_GROUP} ({doctor_biodata[4]}): ") or doctor_biodata[4]
                        valid_blood_group(blood_group)

                        phone_number = input(f"{USER_PHONE_NUMBER} ({doctor_biodata[5]}): ")
                        try:
                            phone_number = valid_number(phone_number, current_number=doctor_biodata[5])
                        except ValueError as error:
                            print(error)
                            return

                        email = input(f"{USER_EMAIL} ({doctor_biodata[6]}): ") or doctor_biodata[6]
                        valid_email(email)

                        address = input(f"{USER_ADDRESS} ({doctor_biodata[7]}): ") or doctor_biodata[7]
                        updated_by = self.user_id
                        
                        update_data = (name, age, gender, blood_group, phone_number, email, address, updated_by, users_id)
                        execute_query(self.connection, UPDATE_USERS, update_data)
                        
                        print(DOCTOR_UPDATE)
                        
                    except Exception as error:
                        print(error)
                
                elif choice == 3:
                    try:
                        
                        self.staff_data()
                        user_id = int(input(USER_ID))
                        
                        # Check if doctor exists in doctor_details table                    
                        doctor =  fetch_one(self.connection , VALIDATE_USER, (user_id,) )
                        
                        if not doctor:
                            print(USER_ID_NOT_FOUND. format(user_id = user_id))
                            return
                        
                        staff_biodata = fetch_one(self.connection , USERS_DATA, ( user_id,))  
                                          
                        users_id = staff_biodata [0]
                        # Input new values or keep existing ones
                        name = input(f"{USER_NAME} ({staff_biodata[1]}): ") or staff_biodata[1]
                        valid_name(name)

                        age = input(f"{USER_AGE} ({staff_biodata[2]}): ") or staff_biodata[2]
                        valid_age(age)

                        gender = input(f"{USER_GENDER} ({staff_biodata[3]}): ") or staff_biodata[3]
                        valid_gender(gender)

                        blood_group = input(f"{USER_BLOOD_GROUP} ({staff_biodata[4]}): ") or staff_biodata[4]
                        valid_blood_group(blood_group)

                        phone_number = input(f"{USER_PHONE_NUMBER} ({staff_biodata[5]}): ")
                        try:
                            phone_number = valid_number(phone_number, current_number=staff_biodata[5])
                        except ValueError as error:
                            print(error)
                            return

                        email = input(f"{USER_EMAIL} ({staff_biodata[6]}): ") or staff_biodata[6]
                        valid_email(email)

                        address = input(f"{USER_ADDRESS} ({staff_biodata[7]}): ") or staff_biodata[7]
                        updated_by = self.user_id
                        
                        update_data = (name, age, gender, blood_group, phone_number, email, address, updated_by, users_id)
                        execute_query(self.connection, UPDATE_USERS, update_data)
                        
                        print(HOSPITAL_STAFF_UPDATED)
                        
                    except Exception as error:
                        print(error)
                            
                elif choice == 4:
                    break       
                else:
                    print(INVALIDCHOICE)                 
        except Exception as error:
            print(error)
            
    def delete_staff(self):
        try:

            self.view_staff()
            user_id = int(input(USER_ID))
            user_exist = fetch_one(self.connection , VALIDATE_USER ,(user_id,))
            
            if not user_exist:
                print(USER_ID_NOT_FOUND.format(user_id = user_id)) 
                
            execute_query(self.connection , DELETE_USER , (user_id,))
            print(DELETE_DOCTOR_ID.format(user_id = user_id) )
            
        except Exception as error:
            print(error)

    # Dutie

    def manage_shift(self):   
        while True:
            try:
                print(MANAGE_SHIFT)
                choice = int(input(ENTER_CHOICE))

                if choice == 1:
                    self.staff_shift()
                elif choice == 2:
                    self.doctor_shift()
                elif choice == 3:
                    self.view_shifts() 
                elif choice == 4:
                    print(RETURN_BACK)
                    break          
                else:
                    print(INVALIDCHOICE)    

            except Exception as error:
                print(error)

    def shift_table(self):
        # List all available shifts
        shifts = fetch_all(self.connection,SHOW_SHIFT)
            
        if not shifts:
            print(NO_SHIFT)
            return

        # Display shifts
        print(SHIFT_AVAILABLE)
        shifts_table = PrettyTable()
        shifts_table.field_names = [FIELD_SHIFT_ID, FIELD_DAY]
        for shift in shifts:
            shifts_table.add_row(shift)
        print(shifts_table)

    def doctors_data(self):
        
        doctor_data = fetch_all(self.connection,DOCTORS_WITH_ID)

        if not doctor_data:
            print(DOCTOR_DATA_NOT_EXIST)
            return
            
        print(DOCTORS)
        data_table = PrettyTable()
        data_table.field_names = [FIELD_USER_ID, FIELD_DOCTOR_ID , FIELD_NAME , FIELD_DEPARTMENT_ID, FIELD_DEPARTMENT_NAME , FIELD_CONSULTATION_FEES , FIELD_JOINING_DATE]
        for data in doctor_data:
            data_table.add_row(data)
        print(data_table)

    def staff_data(self):

        staff_data = fetch_all(self.connection,STAFF_WITH_ID)

        if not staff_data:
            print(STAFF_DATA_NOT_EXIST)
            return
            
        print(STAFF)
        data_table = PrettyTable()
        data_table.field_names = [FIELD_USER_ID, FIELD_NAME, FIELD_ROLE ]
        for data in staff_data:
            data_table.add_row(data)
        print(data_table)
            
    def staff_shift(self):

        """Assign a shift to a staff member (nurse/receptionist)."""
        try:

            # List all available shifts
            self.staff_data()

            user_id = int(input(USER_ID))
            validate_id = fetch_one(self.connection ,VALIDATE_USER , (user_id,))
            
            if not validate_id:
                print(STAFF_ID_NOT_FOUND)
                return
            
            self.shift_table()
            # Display available shifts and proceed
            shift_id = int(input(SHIFT_ID))
            
            validate_shift_id = fetch_one(self.connection ,VALIDATE_SHIFT, (shift_id,))
            
            if not validate_shift_id:
                print(INVALID_SHIFT_ID)
                return
            
            existing_shift = fetch_one(self.connection, STAFF_DUPLICATE_SHIFT_CHECK, (user_id, shift_id))

            if existing_shift:
                print(STAFF_DUPLICATE_SHIFT.format(user_id= user_id))
                return
            
            # Admin user ID
            created_by = updated_by = self.user_id
            # Assign shift to staff
            execute_query(self.connection , INSERT_HSM_TABLE, (shift_id, user_id, created_by, updated_by))

            print(SHIFT_SUCCESS)
        except Exception as error:
            print(ERROR_SHIFT_ASSIGN, error)

    def doctor_shift(self):

        """Assign a shift to a doctor."""
        
        try:
            # Available shifts
            
            self.doctors_data()            
            doctor_id = int(input(ENTER_DOCTOR_ID))
            doctor_exists = fetch_one(self.connection , VALIDATE_DOCTOR , (doctor_id,))
            
            if not doctor_exists:
                print(DOCTOR_ID_NOT_EXIST)
                return
            
            self.shift_table()
            shift_id = int(input(SHIFT_ID))
            
            validate_shift_id = fetch_one(self.connection ,VALIDATE_SHIFT, (shift_id,))
            
            if not validate_shift_id:
                print(INVALID_SHIFT_ID)
                return
            
            # Check if the doctor already has a shift assigned for the same day
            existing_shift = fetch_one(self.connection, DUPLICATE_SHIFT_CHECK, (doctor_id, shift_id))

            if existing_shift:
                print(DUPLICATE_SHIFT.format(doctor_id=doctor_id))
                return
            
            # Assign shift to doctor
            execute_query(self.connection , INSERT_SHIFT_M_TABLE , (doctor_id, shift_id))
            print(SHIFT_SUCCESS)
        
        except Exception as error:
            print(ERROR_SHIFT_ASSIGN, error)

    def view_shifts(self):
        """View all shifts of staff"""
        try:
            # Query for nurse and receptionist shift
            staff_shifts = fetch_all(self.connection , ALL_STAFF_SHIFT)
            
            # Display nurse/receptionist shifts
            print(VIEW_SHIFT)
            staff_table = PrettyTable()
            staff_table.field_names = [FIELD_USER_ID, FIELD_NAME, FIELD_ROLE ,FIELD_DAY]

            if staff_shifts:
                for shift in staff_shifts:
                    staff_table.add_row(shift)
                print(staff_table)
            else:
                print(NO_SHIFT_ASSIGN)

            # Query for doctor shifts
            doctor_shifts = fetch_all(self.connection , ALL_DOCTOR_SHIFT)
            # Display doctor shifts
            print(DOCTOR_SHIFT)
            doctor_table = PrettyTable()
            doctor_table.field_names = [FIELD_USER_ID, FIELD_DOCTOR_ID, FIELD_NAME, FIELD_DEPARTMENT_NAME, FIELD_DAY]

            if doctor_shifts:
                for shift in doctor_shifts:
                    doctor_table.add_row(shift)
                print(doctor_table)
            else:
                print(NO_SHIFT_ASSIGN)

        except Exception as error:
            print(ERROR_FETCH_SHIFT, error)

# manage departments

    def manage_departments(self):   
        while True:
            try:
                print(DEPARTMENT_MENU)
                choice = int(input(ENTER_CHOICE))

                if choice == 1:
                    self.view_departments()
                elif choice == 2:
                    self.create_departments()
                elif choice == 3:
                    self.delete_departments() 
                elif choice == 4:
                    print(RETURN_BACK)
                    break     
                else:
                    print(INVALIDCHOICE)    

            except Exception as error:
                print(error)

    def view_departments(self):
        """ View department dyanmically  """
        try:

            departments = fetch_all(self.connection , AVAILABLE_DEPARTMENTS)
            
            if not departments:
                print(NO_DEPARTMENT)
                return

            print(DEPARTMENT)
            department_table = PrettyTable()
            department_table.field_names = [FIELD_DEPARTMENT_ID, FIELD_DEPARTMENT_NAME]

            for department in departments:
                department_table.add_row(department)

            print(department_table)

        except Exception as error:
            print(error)

    def create_departments(self):
        """Create new department """
        try:
            
            self.view_departments()
            name = input(DEPARTMENT_NAME)
            valid_name(name)

            existing_department = fetch_one(self.connection , DEPARTMENT_ID , (name,))
            if existing_department:
                print(DEPARTMENT_EXIST)
                return
            
            execute_query(self.connection, CREATE_DEPARTMENT, (name,))
            print(DEPARTMENT_CREATE_SUCESS)

        except Exception as error:
            print(error)

    def delete_departments(self):
        """Delete Existing Department"""
        try:
            
            self.view_departments()
            department_id = int(input(DEPARTMENT_Id))
            existing_department = fetch_one(self.connection , CHECK_ID , (department_id,))
            
            if not existing_department:
                print(DEPARTMENT_NOT_EXIST)
                return
            
            execute_query(self.connection , DELETE_DEPARTMENT, (department_id,))
            print(DEPARTMENT_DELETE_SUCESS)
            
        except Exception as error:
            print(error) 
    
# bills
    
    def manage_bill(self):

        while True:
            try:
                print(BILL_MENU)
                choice = int(input(ENTER_CHOICE))

                if choice == 1:
                    self.view_bill()
                elif choice == 2:
                    self.update_bill()
                elif choice == 3:
                    self.delete_bill()
                elif choice == 4:
                    print(RETURN_BACK)
                    break
                else:
                    print(INVALIDCHOICE)    

            except Exception as error:
                print(error)        

    def view_bill(self):
        """ View patient all bills """
        try:
            
            patient_id = int(input(PATIENT_ID))
            
            # Validate Patient ID
            patient_exists = fetch_one(self.connection , VALIDATE_PATIENT , (patient_id, ))

            if not patient_exists:
                print(PATIENT_ID_NOT_FOUND.format(patient_id = patient_id))
                return
            
            # Query for fetching bill
            bills = fetch_all(self.connection , VIEW_BILL , (patient_id,))

            print(BILL)
            if bills:
                table = PrettyTable()
                table.field_names = [FIELD_BILL_ID, FIELD_APPOINTMENT_ID ,FIELD_PATIENT_NAME, FIELD_APPOINTMENT_DETAILS, FIELD_TOTAL_AMOUNT]
                for bill in bills:
                    table.add_row(bill)
                print(table)
            else:
                print(BILL_NOT_FOUND)
        except Exception as error:
            print(BILL_ERROR , error)

    def update_bill(self):

        """ Update patient bill """

        try:
            
            self.view_bill()
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
            
            self.view_bill()
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

    def admin_main_menu(self):

        while True:

            print(ADMIN_MAIN_MENU)

            try:

                choice = int(input(OPERATION_CHOICE))

                if choice == 1:
                    self.manage_patients()
                elif choice == 2:
                    self.manage_staff()
                elif choice == 3:
                    self.manage_shift()
                elif choice == 4:
                    self.manage_departments()
                elif choice == 5:
                    self.manage_bill()
                elif choice == 6:
                    print(EXIT)
                    break
                else:
                    print(INVALIDCHOICE)
            except Exception as error:
                print(error)
         
                

