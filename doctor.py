from constant import (DOCTOR_ID_NOT_EXIST, ERROR_DOCTOR_FEATURE, DOCTOR_NO_SHIFT, ERROR_VIEW_SHIFT, PROFILE_NOT_FOUND,FIELD_DATE,
                      PATIENT_VIEW_ERROR, PATIENT_ID, MANAGE_REPORT, ENTER_CHOICE, RETURN_BACK, INVALIDCHOICE, REPORT, ENTER_APPOINTMENT_DETAIL,
                      REPORT_ID_NOT_EXIST,NO_REPORT_FOUND, REPORT_VIEW_ERROR, REPORT_NAME, REPORT_DESCRIPTION,
                      REPORT_SUCCESS, REPORT_UPDATE_SUCCESS,ENTER_REPORT_ID, REPORT_DELETE_SUCCESS, APPOINTMENT_MENU,
                      APPOINTMENT_VIEW_ERROR, APPOINTMENT_DATE, APPOINTMENT_DETAILS, PATIENT_ID_NOT_FOUND,APPOINTMENT_CREATE, APPOINTMENT_ERROR,
                      ENTER_ID_FOR_UPDATE , APPOINTMENT_ID_NOT_EXIST, APPOINTMENTS, APPOINTMENT_UPDATE_DATE,ENTER_APPOINTMENT_ID, DELETION_ERROR,
                      APPOINTMENT_DELETE, DOCTOR_MENU, USER_PROFILE , APPOINTMENT_VIEW , DOCTOR_SHIFT, FIELD_SHIFT_ID , FIELD_DAY , FIELD_DOCTOR_ID ,
                      FIELD_NAME, FIELD_EMAIL ,  FIELD_PHONE_NUMBER ,FIELD_GENDER, FIELD_BLOOD_GROUP,FIELD_CONSULTATION_FEES ,
                      FIELD_JOINING_DATE  ,FIELD_APPOINTMENT_DETAILS, FIELD_PATIENT_NAME , FIELD_REPORT_NAME , FIELD_REPORT_ID , FIELD_REPORT_DESCRIPTION 
                      , FIELD_CREATED_AT, FIELD_APPOINTMENT_ID, FIELD_PATIENT_ID , FIELD, DETAILS,FIELD_CURRENT_VALUE,)

from prettytable import PrettyTable
from validations import valid_name
from database_query import (DOCTOR_FETCH_ID, DOCTOR_SHIFT, DOCTOR_PROFILE, VIEW_REPORT , REPORT_CREATE,  CREATE_REPORT_TYPE, 
                            UPDATE_REPORT, DELETE_REPORT, VIEW_APPOINTMENTS, VALIDATE_PATIENT, CREATE_APPOINTMENTS, VALIDATE_APPOINTMENT,
                            UPDATE_APPOINTMENT, DELETE_APPOINTMENTS, REPORT_RECORD, REPORT_ID)

from fetch import execute_query , fetch_all , fetch_one


class DoctorFeatures:

    def __init__(self, connection, user_id):

        self.connection = connection
        self.user_id = user_id
        self.doctor_id = None  # Fetch doctor_id

        # Fetch and store doctors_detail_id
        try:
            doctor = fetch_one(self.connection ,DOCTOR_FETCH_ID , (self.user_id,))
            if doctor:
                # from doctor_details_id fetch doctor_id
                self.doctor_id = doctor[0] 
            else:
                print(DOCTOR_ID_NOT_EXIST)
        except Exception as error:
            print(ERROR_DOCTOR_FEATURE, error)

    def view_shift(self, doctor_id):

        """A doctor can view their assigned shifts."""
        
        try:
            
            shifts = fetch_all(self.connection , DOCTOR_SHIFT ,(doctor_id,) )

            if not shifts:
                print(DOCTOR_NO_SHIFT)
                return

            # Display shifts
            print(DOCTOR_SHIFT)
            shift_table = PrettyTable()
            shift_table.field_names = [FIELD_SHIFT_ID, FIELD_DAY]

            for shift in shifts:
                shift_table.add_row(shift)

            print(shift_table)

        except Exception:
            print(ERROR_VIEW_SHIFT)

    def view_profile(self):
        """ Doctor Can View Their Own Profile Details """

        try:
            
            doctors = fetch_all(self.connection , DOCTOR_PROFILE , (self.user_id,))
            
            if doctors:
                table = PrettyTable()
                table.field_names = [FIELD_DOCTOR_ID, FIELD_NAME , FIELD_EMAIL , FIELD_PHONE_NUMBER ,FIELD_GENDER ,
                                     FIELD_BLOOD_GROUP , FIELD_JOINING_DATE , FIELD_CONSULTATION_FEES]
                for doctor in doctors:
                    table.add_row(doctor)
                print(USER_PROFILE)
                print(table)
            else:
                print(PROFILE_NOT_FOUND)
        except Exception as error:
            print(PATIENT_VIEW_ERROR, error)

    def manage_patient_report(self):
        """ Using this method doctor can manage reports of patients 
            type of option menu for reports """
        while True:
            try:
                print(MANAGE_REPORT)
                choice = int(input(ENTER_CHOICE))

                if choice == 1:
                    self.view_reports()
                elif choice == 2:
                    self.create_reports()
                elif choice == 3:
                    self.update_reports()
                elif choice == 4:
                    self.delete_reports()
                elif choice == 5:
                    print(RETURN_BACK)
                    break
                else:
                    print(INVALIDCHOICE)    

            except Exception as error:
                print(error)

    def view_reports(self):

        """ View all patient reports created by the doctor."""
        try:
            
            reports = fetch_all(self.connection , VIEW_REPORT , (self.user_id,))

            # Display Patient Report
            if reports:
                table = PrettyTable()
                table.field_names = [FIELD_REPORT_ID, FIELD_REPORT_NAME, FIELD_REPORT_DESCRIPTION, FIELD_APPOINTMENT_DETAILS , FIELD_PATIENT_NAME , FIELD_CREATED_AT]
                for report in reports:
                    table.add_row(report)
                print(REPORT)
                print(table)
            else:
                print(NO_REPORT_FOUND)
        except Exception as error:
            print(REPORT_VIEW_ERROR, error)       

    def create_reports(self):

        """Create a report for a patient."""
        
        try:
            self.view_appointments()
            appointment_id = int(input(ENTER_APPOINTMENT_ID))
            appointment = fetch_one(self.connection , VALIDATE_APPOINTMENT ,(appointment_id, self.doctor_id))
            if not appointment:
                print(APPOINTMENT_ID_NOT_EXIST)
                return
            
            report_name = input(REPORT_NAME)
            valid_name(report_name)
            report_description = input(REPORT_DESCRIPTION)
            created_by = updated_by = self.user_id

            # Insert into report table
            execute_query(self.connection , REPORT_CREATE , (appointment_id, created_by, updated_by) )
            report_id = self.connection.cursor_connection.fetchone()[0]

            # Insert into report_type table
            execute_query(self.connection ,CREATE_REPORT_TYPE , (report_id, report_name, report_description, created_by, updated_by) )

            print(REPORT_SUCCESS)
        except Exception as error:
            print(REPORT_VIEW_ERROR, error)

    def update_reports(self):

        """Update a report for a patient."""
        try:
            
            self.view_reports()
            
            report_id = int(input(ENTER_REPORT_ID))
            report_record = fetch_one(self.connection, REPORT_RECORD , (report_id,))
            new_report_name = input(f"{REPORT_NAME} ({report_record[0]}): ") or report_record[0]
            valid_name(new_report_name)
            
            new_report_description = input(f"{REPORT_DESCRIPTION} ({report_record[1]}): ") or report_record[1]

            execute_query(self.connection , UPDATE_REPORT , (new_report_name, new_report_description, self.user_id, report_id) )
            print(REPORT_UPDATE_SUCCESS)
        except Exception as error:
            print(REPORT_VIEW_ERROR, error)

    def delete_reports(self):

        """Delete a report of patient."""
        
        try:
            self.view_reports()
            report_id = int(input(ENTER_REPORT_ID))
            report_id_exist = fetch_one(self.connection , REPORT_ID , (report_id,)) 
        
            if not report_id_exist:
                print(REPORT_ID_NOT_EXIST)
                return
            
            # Delete from report table
            execute_query(self.connection , DELETE_REPORT , (report_id,))
            print(REPORT_DELETE_SUCCESS)
        except Exception as error:
            print(REPORT_VIEW_ERROR, error)

    def manage_appointments(self):

        while True:
            try:
                print(APPOINTMENT_MENU)
                choice = int(input(ENTER_CHOICE))

                if choice == 1:
                    self.view_appointments()
                elif choice == 2:
                    self.create_appointments()
                elif choice == 3:
                    self.update_appointments()
                elif choice == 4:
                    self.delete_appointments()
                elif choice == 5:
                    print(RETURN_BACK)
                    break
                else:
                    print(INVALIDCHOICE)    

            except Exception as error:
                print(error)

    def view_appointments(self):

        """ View all appointments for the doctor with patient and doctor details."""
        try:

            # Query to get appointment
            appointments = fetch_all(self.connection , VIEW_APPOINTMENTS , (self.doctor_id,))
            
            # Display appointments
            if appointments:
                table = PrettyTable()
                table.field_names = [FIELD_APPOINTMENT_ID, FIELD_DATE, FIELD_PATIENT_ID, FIELD_PATIENT_NAME, FIELD_APPOINTMENT_DETAILS]

                for appointment in appointments:
                    table.add_row(appointment)
                print(table)
            else:
                # If no appointments are found
                print(APPOINTMENT_VIEW)

        except Exception as error:
            print(APPOINTMENT_VIEW_ERROR ,error)

    def create_appointments(self):

        """Create a new appointment for a patient."""
        try:
            
            # Input Details
            patient_id = int(input(PATIENT_ID))
            doctor_id = self.doctor_id
            appointment_date = input(APPOINTMENT_DATE).strip()
            appointment_details = input(APPOINTMENT_DETAILS).strip()

            # Validate Patient ID
            patient_exists = fetch_one(self.connection , VALIDATE_PATIENT , (patient_id,))

            if not patient_exists:
                print(PATIENT_ID_NOT_FOUND.format(patient_id = patient_id))
                return

            # when doctor logged-in , he is creating this
            created_by = updated_by = self.doctor_id
            
            # Insert the appointment
            entered_data = (patient_id, doctor_id, appointment_date, appointment_details, created_by, updated_by)
            execute_query(self.connection , CREATE_APPOINTMENTS , entered_data )

            print(APPOINTMENT_CREATE)

            # Display appointment details
            table = PrettyTable()
            table.field_names = [FIELD, DETAILS]
            table.add_row([FIELD_PATIENT_ID, patient_id])
            table.add_row([FIELD_DOCTOR_ID, doctor_id])
            table.add_row([FIELD_DATE, appointment_date])
            table.add_row([FIELD_APPOINTMENT_DETAILS, appointment_details])
            print(table)

        except Exception as error:
            print(APPOINTMENT_ERROR.format(error))

    def update_appointments(self):

        """Update details of an existing appointment."""
        try:
            
            self.view_appointments()
            # Input for Appointment ID
            appointment_id = int(input(ENTER_ID_FOR_UPDATE ))

            # Validate Appointment ID and with doctor_id
            appointment = fetch_one(self.connection ,VALIDATE_APPOINTMENT , (appointment_id, self.doctor_id))
            
            if not appointment:
                print(APPOINTMENT_ID_NOT_EXIST)
                return

            # Display current appointment
            current_table = PrettyTable()
            current_table.field_names = [FIELD, FIELD_CURRENT_VALUE]
            current_table.add_row([FIELD_APPOINTMENT_ID, appointment[0]])
            current_table.add_row([FIELD_DATE, appointment[1]])
            current_table.add_row([FIELD_APPOINTMENT_DETAILS, appointment[2]])
            print(APPOINTMENTS)
            print(current_table)

            # Input new details for the appointment
            new_date = input(APPOINTMENT_UPDATE_DATE).strip() or appointment[1]
            new_details = input(ENTER_APPOINTMENT_DETAIL).strip() or appointment[2]

            # Update the appointment
            execute_query(self.connection,UPDATE_APPOINTMENT,(new_date, new_details, self.doctor_id, appointment_id))
            
            # Display updated appointment
            updated_table = PrettyTable()
            current_table.field_names = [FIELD, FIELD_CURRENT_VALUE]
            current_table.add_row([FIELD_APPOINTMENT_ID, appointment[0]])
            current_table.add_row([FIELD_DATE, new_date])
            current_table.add_row([FIELD_APPOINTMENT_DETAILS, new_details])
            print(APPOINTMENTS)
            print(updated_table)

        except Exception as error:
            print(APPOINTMENT_ERROR , error)

    def delete_appointments(self):

        """Delete an appointment by ID """
        try:
            self.view_appointments()
            # Input for Appointment ID
            appointment_id = int(input(ENTER_APPOINTMENT_ID))
            
            # validate Appointment id
            appointment = fetch_one(self.connection , VALIDATE_APPOINTMENT , (appointment_id, self.doctor_id))
            if not appointment:
                print(APPOINTMENT_ID_NOT_EXIST)
                return

            # Delete the appointment
            execute_query(self.connection ,DELETE_APPOINTMENTS ,(appointment_id, self.doctor_id))
            print(APPOINTMENT_DELETE)
        except Exception as error:
            print(f"{DELETION_ERROR}: {error}")

    def doctor_menu(self):

        while True:

            print(DOCTOR_MENU)

            choice = int(input(ENTER_CHOICE))

            if choice == 1:
                self.view_shift(self.doctor_id)
            elif choice == 2:
                self.view_profile()
            elif choice == 3:
                self.manage_patient_report()
            elif choice == 4:
                self.manage_appointments()
            elif choice == 5:
                print(RETURN_BACK)
                break
            else:
                print(INVALIDCHOICE)    