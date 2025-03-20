from prettytable import PrettyTable
from constant import ( PATIENT, PROFILE_NOT_FOUND, PATIENT_VIEW_ERROR, APPOINTMENTS, APPOINTMENT_VIEW, APPOINTMENT_VIEW_ERROR, REPORT,
                        NO_REPORT_FOUND, REPORT_VIEW_ERROR, BILL, BILL_NOT_FOUND, BILL_VIEW_ERROR, PATIENT_MENU, ENTER_CHOICE,
                        RETURN_BACK, INVALIDCHOICE , PROFILE_FETCH_ERROR,FIELD , DETAILS, FIELD_NAME , FIELD_AGE , FIELD_GENDER ,
                        FIELD_BLOOD_GROUP, FIELD_PHONE_NUMBER ,FIELD_EMAIL , FIELD_ADDRESS, FIELD_APPOINTMENT_ID , FIELD_APPOINTMENT_DETAILS 
                        ,FIELD_DATE, FIELD_DOCTOR, FIELD_REPORT_NAME , FIELD_REPORT_DESCRIPTION , FIELD_CREATED_AT, FIELD_BILL_ID,
                        FIELD_TOTAL_AMOUNT,)


from database_query import (PATIENT_ID, VIEW_PROFILE, VIEW_APPOINTMENT, VIEW_REPORTS, VIEW_BILLS)
from fetch import fetch_all , fetch_one

class PatientFeatures:

    def __init__(self, connection, user_id):
        self.connection = connection
        self.user_id = user_id
        self.patient_id = None

        # Fetch and store patients_detail_id
        try:
            patient = fetch_one(self.connection ,PATIENT_ID, (self.user_id,))

            if patient:
                # from patients_detail_id fetch patient_id
                self.patient_id = patient[0] 
            else:
                print(PROFILE_FETCH_ERROR)
        except Exception as error:
            print(error)

    def view_profile(self):

        """Patient can view their own profile details."""
        try:
            profile = fetch_one(self.connection ,VIEW_PROFILE, (self.user_id,) )

            # Display Details
            if profile:
                table = PrettyTable()
                table.field_names = [FIELD , DETAILS]
                table.add_row([FIELD_NAME, profile[0]])
                table.add_row([FIELD_AGE, profile[1]])
                table.add_row([FIELD_GENDER, profile[2]])
                table.add_row([FIELD_BLOOD_GROUP, profile[3]])
                table.add_row([FIELD_PHONE_NUMBER, profile[4]])
                table.add_row([FIELD_EMAIL, profile[5]])
                table.add_row([FIELD_ADDRESS, profile[6]])
                print(PATIENT)
                print(table)
            else:
                print(PROFILE_NOT_FOUND)
        except Exception as error:
            print(PATIENT_VIEW_ERROR, error)

    def view_appointment(self):

        """Patient can view all apointments."""
        
        try:
            appointments = fetch_all(self.connection ,VIEW_APPOINTMENT, (self.patient_id,))
            # Display appointments
            if appointments:
                table = PrettyTable()
                table.field_names = [FIELD_APPOINTMENT_ID , FIELD_APPOINTMENT_DETAILS ,FIELD_DATE, FIELD_DOCTOR]
                for appointment in appointments:
                    table.add_row(appointment)
                print(APPOINTMENTS)
                print(table)
            else:
                print(APPOINTMENT_VIEW)
        except Exception as error:
            print(APPOINTMENT_VIEW_ERROR, error)

    def view_reports(self):

        """ Patient can view their report history """
        try:

            # Query to fetch patient-specific report
            
            # Execute the query
            reports = fetch_all(self.connection ,VIEW_REPORTS, (self.patient_id,) )

            # Display Reports
            if reports:
                table = PrettyTable()
                table.field_names = [FIELD_REPORT_NAME , FIELD_REPORT_DESCRIPTION , FIELD_CREATED_AT]
                for report in reports:
                    table.add_row(report)
                print(REPORT)
                print(table)
            else:
                print(NO_REPORT_FOUND)
        except Exception as error:
            print(REPORT_VIEW_ERROR, error)

    def view_bills(self):

        """Patient can view all bills"""
        try:
            # Query For Fetching Bill
            bills = fetch_all(self.connection ,VIEW_BILLS, (self.patient_id,) )

            # Display bills
            if bills:
                table = PrettyTable()
                table.field_names = [FIELD_BILL_ID,FIELD_APPOINTMENT_DETAILS,FIELD_TOTAL_AMOUNT,FIELD_CREATED_AT]
                for bill in bills:
                    table.add_row(bill)
                print(BILL)
                print(table)
            else:
                print(BILL_NOT_FOUND)
        except Exception as error:
            print(BILL_VIEW_ERROR , error)

    def patient_menu(self):

        """Menu For select features."""
        while True:
            try:
                print(PATIENT_MENU)

                choice = int(input(ENTER_CHOICE))

                if choice == 1:
                    self.view_profile()
                elif choice == 2:
                    self.view_appointment()
                elif choice == 3:
                    self.view_reports()
                elif choice == 4:
                    self.view_bills()
                elif choice == 5:
                    print(RETURN_BACK)
                    break
                else:
                    print(INVALIDCHOICE)
            except Exception as error:
                print(error)