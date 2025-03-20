from constant import (NURSE_MENU,NURSE_SHIFTS,ENTER_CHOICE,INVALIDCHOICE,RETURN_BACK,FIELD_DAY , FIELD_SHIFT_ID,
                        NO_SHIFT_ASSIGN, DOCTOR_AVAILABILITY, APPOINTMENT_UPDATE_DATE, ENTER_DOCTOR_ID, NURSE, PROFILE_NOT_FOUND,  PATIENT,
                        PATIENT_VIEW_ERROR,REPORT, NO_REPORT_FOUND, DOCTOR_NO_SHIFT, FIELD,DETAILS,
                        NURSE_APPOINTMENT_MENU, APPOINTMENT_VIEW, APPOINTMENT_VIEW_ERROR, PATIENT_ID, APPOINTMENTS, APPOINTMENT_DATE,
                        APPOINTMENT_DETAILS, PATIENT_ID_NOT_FOUND, DOCTOR_ID_NOT_EXIST, APPOINTMENT_CREATE, APPOINTMENT_ERROR, 
                        ENTER_ID_FOR_UPDATE ,ENTER_APPOINTMENT_DETAIL,ERROR_APPOINTMENT_DETAIL, DOCTOR_AVAILABILITY_ERROR,FIELD_USER_ID,
                        FIELD_NAME,FIELD_EMAIL,FIELD_PHONE_NUMBER,FIELD_GENDER,FIELD_BLOOD_GROUP , FIELD_PATIENT_ID, FIELD_AGE,
                        FIELD_PATIENT_NAME, FIELD_REPORT_NAME, FIELD_REPORT_DESCRIPTION, FIELD_CREATED_AT, FIELD_DOCTOR_NAME,
                        FIELD_APPOINTMENT_ID, FIELD_DATE, FIELD_DOCTOR_ID, FIELD_APPOINTMENT_DETAILS)
                        
from prettytable import PrettyTable

from database_query import (NURSE_SHIFT, NURSE_PROFILE, VIEW_PATIENT_DETAILS, VALIDATE_PATIENT, VIEW_PATIENT_REPORTS, VALIDATE_DOCTOR,
                            DOCTOR_AVAILABEL, VIEW_N_APPOINTMENT, CREATE_APPOINTMENTS, UPDATE_APPOINTMENT, VALIDATE_APPOINTMENT_ID)

from fetch import execute_query,fetch_all,fetch_one

class NurseFeatures:
    def __init__(self, connection, user_id):
        self.connection = connection
        self.user_id = user_id

    def nurse_menu(self):
        while True:

            print(NURSE_MENU)
            try:
                input_choice = int(input(ENTER_CHOICE))

                if input_choice == 1:
                    self.view_shifts()
                elif input_choice == 2:
                    self.view_profile()
                elif input_choice == 3:
                    self.view_patient_details()
                elif input_choice == 4:
                    self.view_patient_report()
                elif input_choice == 5:
                    self.doctor_avalibility()
                elif input_choice == 6:
                    self.manage_appointments()
                elif input_choice == 7:
                    print(RETURN_BACK)
                    break
                else:
                    print(INVALIDCHOICE)

            except Exception as error:
                print(error)

    def view_shifts(self):

        """View the shifts which assigned by admin"""
        
        try:
            shifts = fetch_all(self.connection , NURSE_SHIFT ,(self.user_id,) )
            if shifts:
                print(NURSE_SHIFTS)
                table = PrettyTable()
                table.field_names = [FIELD_SHIFT_ID,FIELD_DAY]
                for shift in shifts:
                    table.add_row(shift)
                print(table)
            else:
                print(NO_SHIFT_ASSIGN)
        except Exception as error:
            print(error)

    def view_profile(self):

        """Nurse can view own profile"""
        
        try:
            # Query fetch details form user table using nurse role roles table
            profile = fetch_one(self.connection , NURSE_PROFILE , (self.user_id,))

            # Display details
            if profile:
                print(NURSE)
                table = PrettyTable()
                table.field_names = [FIELD,DETAILS]
                table.add_row([FIELD_USER_ID, profile[0]])
                table.add_row([FIELD_NAME, profile[1]])
                table.add_row([FIELD_EMAIL, profile[2]])
                table.add_row([FIELD_PHONE_NUMBER, profile[3]])
                table.add_row([FIELD_GENDER, profile[4]])
                table.add_row([FIELD_BLOOD_GROUP, profile[5]])
                print(table)
            else:
                print(PROFILE_NOT_FOUND)
        except Exception as error:
            print(PATIENT_VIEW_ERROR, error)

    def view_patient_details(self):

        """View details of a specific patient using patient_id."""
        try:
            patient_id = int(input(PATIENT_ID))
            
            # Query to fetch patient details
            patient = fetch_one(self.connection , VIEW_PATIENT_DETAILS ,(patient_id,))

            if patient:
                # Display details
                print(PATIENT)
                table = PrettyTable()
                table.field_names = [FIELD, DETAILS]
                table.add_row([FIELD_USER_ID, patient[0]])
                table.add_row([FIELD_PATIENT_ID, patient[1]])
                table.add_row([FIELD_NAME, patient[2]])
                table.add_row([FIELD_AGE,patient[3]])
                table.add_row([FIELD_GENDER, patient[4]])
                table.add_row([FIELD_BLOOD_GROUP, patient[5]])
                table.add_row([FIELD_PHONE_NUMBER, patient[6]])
                print(table)
            else:
                print(PATIENT_ID_NOT_FOUND.format(patient_id = patient_id))
        except Exception as error:
            print(PATIENT_VIEW_ERROR, error)

    def view_patient_report(self):

        """View the reports using patient_id for specific patient."""
        try:
            patient_id = int(input(PATIENT_ID))
            # Validate Patient ID
            patient_exists = fetch_one(self.connection,VALIDATE_PATIENT, (patient_id,))
            
            if not patient_exists:
                print(PATIENT_ID_NOT_FOUND.format(patient_id = patient_id))
                return
            # Query to fetch patient name and their report details
            reports = fetch_all(self.connection , VIEW_PATIENT_REPORTS, (patient_id,))
            
            if reports:

                # Display patient name and reports
                table = PrettyTable()
                table.field_names = [FIELD_PATIENT_NAME, FIELD_REPORT_NAME, FIELD_REPORT_DESCRIPTION , FIELD_CREATED_AT]
                
                # Report Details
                for report in reports:
                    table.add_row(report)

                print(REPORT)
                print(table)
            else:
                print(NO_REPORT_FOUND)
        except Exception as error:
            print(PATIENT_VIEW_ERROR, error)

    def doctor_avalibility(self):

        """Nurse Check availability of a specific doctor by Doctor ID. """


        try:

            # Input for Doctor ID
            doctor_id = int(input(ENTER_DOCTOR_ID))

            # Validate Doctor ID
            doctor_exists = fetch_one(self.connection ,VALIDATE_DOCTOR, (doctor_id,) )
            if not doctor_exists:
                print(DOCTOR_ID_NOT_EXIST)
                return    
            
            # Query to check if the doctor has any shifts assigned
            doctor_availability = fetch_all(self.connection , DOCTOR_AVAILABEL, (doctor_id,))

            # Display the availability
            print(DOCTOR_AVAILABILITY)
            if doctor_availability:
                availability_table = PrettyTable()
                availability_table.field_names = [FIELD_DOCTOR_NAME, FIELD_DAY]
                for doctor in doctor_availability:
                    availability_table.add_row(doctor)
                print(availability_table)
            else:
                print(DOCTOR_NO_SHIFT)

        except Exception as error:
            print(DOCTOR_AVAILABILITY_ERROR, error)

    def manage_appointments(self):

        """Manage the appointments for patients."""
        
        while True:
            print(NURSE_APPOINTMENT_MENU)

            try:
                choice = int(input(ENTER_CHOICE))

                if choice == 1:
                    self.view_appointments()
                elif choice == 2:
                    self.create_appointment()
                elif choice == 3:
                    self.update_appointment()
                elif choice == 4:
                    print(RETURN_BACK)
                    break
                else:
                    print(INVALIDCHOICE)
            except Exception as error:
                print(error)

    def view_appointments(self):

        """ View all appointments for patient using patient and doctor details"""
        try:

            # query to fetch details from different tables
            appointments = fetch_all(self.connection , VIEW_N_APPOINTMENT)
            # Display Appointments
            if appointments:
                print(APPOINTMENTS)
                table = PrettyTable()
                table.field_names = [FIELD_APPOINTMENT_ID, FIELD_DATE, FIELD_APPOINTMENT_DETAILS, FIELD_PATIENT_ID, FIELD_PATIENT_NAME,
                                     FIELD_DOCTOR_ID , FIELD_DOCTOR_NAME]
                for appointment in appointments:
                    table.add_row(appointment)
                print(table)
            else:
                print(APPOINTMENT_VIEW)
        except Exception as error:
            print(APPOINTMENT_VIEW_ERROR, error)

    def create_appointment(self):

        """Create a new appointment for a patient."""
        try:
            # Input patient and doctor ID
            patient_id = int(input(PATIENT_ID))
            doctor_id = int(input(ENTER_DOCTOR_ID))
            appointment_date = input(APPOINTMENT_DATE).strip()
            appointment_details = input(APPOINTMENT_DETAILS).strip()

            # Validate Patient ID
            patient_exists = fetch_one(self.connection ,VALIDATE_PATIENT, (patient_id,) )
            if not patient_exists:
                print(PATIENT_ID_NOT_FOUND.format(patient_id = patient_id))
                return

            # Validate Doctor ID
            doctor_exists = fetch_one(self.connection,VALIDATE_DOCTOR, (doctor_id,))
            if not doctor_exists:
                print(DOCTOR_ID_NOT_EXIST)
                return

            created_by = updated_by = self.user_id
            
            # Insert the appointment if both IDs are valid
            execute_query(self.connection,
                CREATE_APPOINTMENTS, (patient_id, doctor_id, appointment_date, appointment_details,created_by,updated_by)
            )
            print(APPOINTMENT_CREATE)
            
            appointment_id = self.connection.cursor_connection.fetchone()[0]
            
            # Display appointment details
            table = PrettyTable()
            table.field_names = [FIELD, DETAILS]
            table.add_row([FIELD_APPOINTMENT_ID , appointment_id])
            table.add_row([FIELD_PATIENT_ID, patient_id])
            table.add_row([FIELD_DOCTOR_ID, doctor_id])
            table.add_row([FIELD_DATE, appointment_date])
            table.add_row([FIELD_APPOINTMENT_DETAILS, appointment_details])
            print(table)

        except Exception as error:
            print(APPOINTMENT_ERROR, error)

    def update_appointment(self):

        """Update an existing appointment"""
        try:

            # Get the Appointment ID
            appointment_id = int(input(ENTER_ID_FOR_UPDATE ))
        
            # Check if the appointment exists
            appointment = fetch_one(self.connection ,VALIDATE_APPOINTMENT_ID, (appointment_id,) )
            
            # Display the existing appointment details
            if appointment:
                print(ERROR_APPOINTMENT_DETAIL)
                
                table = PrettyTable()
                table.field_names = [FIELD, DETAILS]
                table.add_row([FIELD_APPOINTMENT_ID, appointment[0]])
                table.add_row([FIELD_DOCTOR_ID, appointment[1]])
                table.add_row([FIELD_PATIENT_ID, appointment[2]])
                table.add_row([FIELD_DATE, appointment[4]])
                table.add_row([FIELD_APPOINTMENT_DETAILS, appointment[3]])
                print(table)

                # Ask for new details
                new_date = input(APPOINTMENT_UPDATE_DATE)
                appointment_details = input(ENTER_APPOINTMENT_DETAIL).strip()

                # Query for update the appointment
                execute_query(self.connection, UPDATE_APPOINTMENT, 
                    (new_date,appointment_details, self.user_id, appointment_id))

                print(APPOINTMENT_CREATE)

                # Show updated appointment details
                print(ENTER_APPOINTMENT_DETAIL)
                table.clear_rows()
                table.add_row([FIELD_APPOINTMENT_ID, appointment_id])
                table.add_row([FIELD_DOCTOR_ID, appointment[1]]) 
                table.add_row([FIELD_PATIENT_ID, appointment[2]])  
                table.add_row([FIELD_DATE, new_date])
                table.add_row([FIELD_APPOINTMENT_DETAILS, appointment_details])
                print(table)

            else:
                print(APPOINTMENT_VIEW)
        
        except Exception as error:
            print(APPOINTMENT_ERROR, error)