#Fields 

FIELD_USER_ID = "User ID"
FIELD_PATIENT_ID = "Patient ID"
FIELD_NAME = "Name"
FIELD_AGE = "Age"
FIELD_EMAIL = "Email"
FIELD_GENDER = "Gender"
FIELD_BLOOD_GROUP = "Blood Group"
FIELD_PHONE_NUMBER = "Phone Number"
FIELD_ADDRESS = "Address"
FIELD_ROLE = "Role"

FIELD_NURSE = "nurse"
FIELD_RECEPTIONIST = "receptionist"
FIELD_DOCTOR = "doctor"

FIELD_DOCTOR_ID = "Doctor Id"
FIELD_DOCTOR_NAME = "Doctor Name"
FIELD_SHIFT_ID = "Shift Id"
FIELD_DAY = " Shift Day"

FIELD_JOINING_DATE = "JOINING DATE"
FIELD_CONSULTATION_FEES = "CONSULATATION FEES"

FIELD_BILL_ID = "Bill ID"
FIELD_APPOINTMENT_ID = "Appointment Id"
FIELD_PATIENT_NAME = "Patient Name"
FIELD_APPOINTMENT_DETAILS = "Appointment Details"
FIELD_TOTAL_AMOUNT = "Total Amount"

FIELD_REPORT_ID = "Report ID"
FIELD_REPORT_NAME = "Report Name"
FIELD_REPORT_DESCRIPTION = "Description"
FIELD_CREATED_AT = "Created At"
FIELD_DATE = "Date"

FIELD = "Field"
DETAILS = "Details"
FIELD_CURRENT_VALUE = "Current Value"

# Department
FIELD_DEPARTMENT_ID = "DEPARTMENT ID"
FIELD_DEPARTMENT_NAME = "DEPARTMENT NAME"





#Database 
DATABASE_CONNECTION_ERROR = "Database connection error !"
DATABASE_SUCCESS = "Database created successfully!"
DATABASE_INERTION_ERROR = "Database insertion error !"
DATABASE_ERROR = "Database Error: "
SIGN_IN_ERROR = "Error in sign in ..!"
DB_ERROR = "Database error"

# Errors
INVALIDCHOICE = "Invalid Choice !"
VALIDCHOICE = "Please Enter Valid Choice !"
PATIENT_UPDATE_ERROR = "Error while updating patient:"

#Admin
ADMIN_PATIENT_MENU = """
        ------ MANAGE PATIENT ------
              1.View Patient Information
              2.Update Patient Information
              3.Return Back
            """

UPDATE_STAFF_MENU = """
        ------ UPDATE STAFF ------
              1.UPDATE THE DOCTOR'S PROFESSIONAL INFORMATION
              2.UPDATE THE DOCTOR'S PERSONAL INFORMATION
              3.UPDATE THE NURSE / RECEPTIONIST INFORMATION
              4.RETURN BACK
            """
            
ADMIN_MAIN_MENU = """
       ------ Admin Features ------
            1.Manage Patients
            2.Manage Hospital Staff
            3.Manage Duties
            4.Manage Departments
            5.Bill Management
            6.Exit
           """

MANAGE_SHIFT = """
        ------ MANAGE SHIFT ------
              1.Assign Shift (Nurse, Receptionist)
              2.Assign Shift Doctor
              3.View All Shift
              4.Return Back
            """


RETURN_BACK = " Return Back "

HOSPITAL_STAFF_MENU = """
        ------ Manage Hospital Staff ------
              1.View Hospital Staff
              2.Create Hospital Staff
              3.Update Hospital Staff
              4.Delete Hospital Staff
              5.Return Back
            """
HOSPITAL_STAFF_MEMBER = " ----- Hospital Staff Members ----- "
HOSPITAL_STAFF_NOT_FOUND = "No staff found."

USER_TYPE = "Enter user type to delete (doctor,nurse, receptionist): "
USER_ID_WITH_ROLE = " Enter {} User ID to delete: "
USER_DELETED = "{} ID {} deleted successfully."


#Main File 

HEADING = "==== Welcome to Hospital Management System ===="
LOGIN_MENU = """
        ------ Login Features ------
              1.Login
              2.Exit
            """
USER_LOGIN_SUCCESS = "Login Successful ! Welcome , {name} ({role_name})"

EXIT = "Exiting the system. Goodbye!"

DEPARTMENT_NAME = "Enter Department Name : "
DEPARTMENT_Id = "Enter Department ID : "
DEPARTMENT_CREATE_SUCESS = "Department Created Successfully !"
DEPARTMENT_DELETE_SUCESS = "Department Deleted Successfully !"
DEPARTMENT_NOT_FOUND = "Department not found!"
DEPARTMENT_EXIST = "Department already exist with id."
DEPARTMENT_NOT_EXIST = "Department with entered id not exist !!!"
DEPARTMENT_MENU = """
        ------ Manage Hospital Departments  ------
              1.View Hospital Departments
              2.Create Hospital Departments
              3.Delete Hospital Departments
              4.Return Back
              """
DEPARTMENT = "Availabel Departments"
NO_DEPARTMENT = "No departments available."

# Auth
SIGN_ERROR =  "Please enter valid Details for Sign_In !"
USER_NOT_EXIST = " User with Enter details not exist !"

# Patient
LIST_PATIENT = " ---- List Of Patient ---- "
PROFILE_NOT_FOUND = "No Profile Found !"
PATIENT = "--- Patient Profile ---"
PATIENT_VIEW_ERROR = "Error viewing patient details:"
NO_PATIENT_FOUND = "Patient Not Found."
PROFILE_FETCH_ERROR = "Profile Fetch Error."

STAFF_ID_NOT_FOUND = "Invalid Staff Id , Please enter valid staff Id ..!"

#Doctor

DOCTORS = "---- Doctors Profile ----"

STAFF = "---- Staff Profile ----"
DOCTOR_MENU = """
        ------ Doctor Features ------
              1.View Shifts
              2.View Profile
              3.Manage Patient Reports
              4.Manage Appointments
              5.Return Back
                    """

DOCTOR_JOINING_DATE = "Enter Joining Date (DD-MM-YYYY): "
CONSULTANT_FEE = "Enter Consultation Fees: "
DOCTOR_REGISTER= "Doctor details have been successfully added."
DELETION_ERROR = "Error while adding doctor details:"
DOCTOR_ID_NOT_EXIST = "Doctor ID does not exist."
ERROR_DOCTOR_FEATURE = "Error in DoctorFeatures:"
DELETE_DOCTOR_ID =" User With User Id : {user_id} deleted successfully."
DOCTOR_DATA_NOT_EXIST = "Error fetching the Doctors Data || Doctors data not availabel"
DOCTOR_UPDATE = "Doctor Details Successfully Updated"

STAFF_DATA_NOT_EXIST = "Error fetching the Staff Data || Staff data not availabel"
#User

USER_NAME = "Enter User Name: "
USER_AGE = "Enter Age: "
USER_GENDER = "Enter Gender (MALE / FEMALE ) : "
USER_BLOOD_GROUP = "Enter Blood Group ('A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-') : "
USER_PHONE_NUMBER = "Enter Phone Number: "
USER_EMAIL = "Enter User Email: "
USER_ADDRESS = "Enter Address: "
USER_PASSWORD = "Enter User Password : "
USERS_PASSWORD = "Your Password Is : {password} "
USER_REGISTRATION_ERROR = "Error while registering user: "
USER_PROFILE = "---- YOUR PROFILE ----"
USER_ID_NOT_FOUND = "User With User Id : {user_id} not exist in the system.!"

#Receptionist

 #==> Receptionist Menu
RECEPTIONIST_MENU = """
        ------ Receptionist Features ------
              1.View Profile
              2.Check Doctor Availability
              3.Appointment Management
              4.Patient Registration
              5.Bill Management
              6.Return Back
                    """

RECEPTIONIST_PROFILE = "--- Receptionist Profile ---"


  #==> Patient Registration
PATIENT_ID = " Enter Patient Id :- "
PATIENT_NAME = " Enter Patient Name : "
PATIENT_AGE = " Enter Patient Age : "
PATIENT_GENDER = " Enter Patient Gender : "
PATIENT_PHONE_NUMBER = " Enter Patient Phone Number : "
PATIENT_EMAIL = " Enter Patient Email Id : "
PATIENT_ADDRESS = " Enter Patient Address : "


# CREATED_BY = "Enter Creator's Role Id : "
PATIENT_ROLE_NOT_FOUND = " Patient Role Id Not Found ! "
PATIENT_ID_NOT_FOUND = " No patient found with ID {patient_id} "
PATIENT_UPDATE = " Patient with (User ID: {user_id}) has been successfully updated."
PATIENT_REGISTRATION = """ Patient {name} Registration Successfully. Patient User ID : {user_id}  ,
                              Patient Id : {patient_id} And Patient Password : {password}."""

# == > Appointmnets
APPOINTMENT_VIEW = "No Appointments Availabel."
ENTER_APPOINTMENT_ID = " Enter the Appointment ID :-  "
APPOINTMENT_DELETE = "Appointment deleted successfully."
APPOINTMENT_ERROR = " Error In Appointment Section : "
APPOINTMENT_ID_NOT_EXIST = " Appointment ID does not exist."
APPOINTMENT_CREATE = " Appointment Created Successfully " 

APPOINTMENT_UPDATE = " Appointment updated successfully."
APPOINTMENT_UPDATE_DATE = " Enter the update appointment date (DD-MM-YYYY): "
ENTER_APPOINTMENT_DETAIL= " Update Appointment Details: "
ENTER_ID_FOR_UPDATE  = " Enter the Appointment ID to update: "

ENTER_DOCTOR_ID = " Enter Doctor ID: "
APPOINTMENT_DETAILS = " Enter Appointment Details: "
APPOINTMENT_DATE = " Enter Appointment Date (DD-MM-YYYY): "

APPOINTMENTS = "--- Appointments ---"
APPOINTMENT_VIEW_ERROR = "Error viewing appointments: "
ERROR_APPOINTMENT_DETAIL = "Existing Appointment Details:"

APPOINTMENT_MENU = """
        ------ Appointment Manage ------
              1.View Appointment
              2.Create Appointment 
              3.Update Appointment
              4.Delete Appointment
              5.Return Back
                    """

NURSE_APPOINTMENT_MENU = """
        ------ Appointment Manage ------
              1.View Appointment
              2.Create Appointment 
              3.Update Appointment
              4.Return Back
                    """

DELETION_ERROR = "Appointment Deletion Error !"

#Role

ENTER_ROLE_NAME = "Enter Role (Doctor, Nurse, Receptionist): "
ROLE_NOT_FOUND = "Role {role_name} not found!"
ROLE_REGISTER = "User {name} with role {role_name} has been successfully registered."

#bill

RECEPTIONIST_BILL_MENU = """
          ------ Manage Patient Bill ------
                  1.View Bill
                  2.Create Bill
                  3.Update Bill
                  4.Delete Bill
                  5.Return Back
            """


BILL_MENU = """
          ------ Manage Patient Bill ------
                  1.View Bill
                  2.Update Bill
                  3.Delete Bill
                  4.Return Back
"""

BILL = "--- Bills ---"
BILL_ERROR = "Error fetching bills: "
BILL_NOT_FOUND = "Bill Not Found !"
BILLS = "Bills of Patient ID"
BILL_ID = "Enter the Bill ID : "

BILL_UPDATE_SUCCESS = "Bill updated successfully."
DELETE_BILL = "Bill deleted successfully."
BILL_ID_NOT_FOUND = " Bill Id Not Found !"

NEW_BILL_AMOUNT = "Enter the new amount for the bill: "
TOTAL_BILL_AMOUNT = "Enter the total amount for the bill: "

BILL_UPDATE_SUCCESS = "Bill ID {bill_id} successfully updated."
BILL_CREATE_SUCCESS = "Bill created successfully."

BILL_VIEW_ERROR = "Error viewing the bill:"
BILL_CREATE_ERROR = "Error creating the bill"
BILL_UPDATE_ERROR = "Error updating the bill: "
BILL_DELETION_ERROR = "Error deleting the bill: "

DELETE_BILL_ID = "Bill ID {bill_id} successfully deleted."

PATIENT_MENU = """
        ------ Patient Features ------
              1.View Profile
              2.View Appointment 
              3.View Reports
              4.View Bill
              5.Return Back
                    """


#shift

SHIFT_AVAILABLE = "Available Shifts : "
SHIFT_ID = "Enter the Shift ID : "
INVALID_SHIFT_ID = "Invalid shift ID , Enter valid shift id : "
ERROR_SHIFT_ASSIGN = "Error assigning shift:"
SHIFT_SUCCESS = "Shift Successfully assigned."
VIEW_SHIFT = "Nurse/Receptionist Shifts:"
NO_SHIFT_ASSIGN = "No shifts assigned."
ERROR_FETCH_SHIFT = "Error fetching shifts:"

DUPLICATE_SHIFT = "Doctor ID {doctor_id} already has a shift on this day.Cannot assign duplicate shifts."
STAFF_DUPLICATE_SHIFT = "User ID {user_id} already has a shift on this day.Cannot assign duplicate shifts."


NURSE_SHIFTS = "----- Nurse Shifts -----"

USER_ID = "ENTER USER ID :- "

DOCTOR_SHIFT = "Doctor Shifts:"
ENTER_DOCTOR_ID = "Enter Doctor ID :- "
DOCTOR_AVAILABILITY = "Doctor Availability:"

DOCTOR_AVAILABILITY_ERROR = "Error checking doctor availability:"
DOCTOR_NO_SHIFT = "Doctor ID has no shifts assigned."
ERROR_VIEW_SHIFT = "Error viewing shifts."

HOSPITAL_STAFF_ADDED = "Staff member added successfully."
HOSPITAL_STAFF_UPDATED = "Staff member Updated successfully."

HOSPITAL_STAFF_ERROR = "Error In Adding Staff :" 
NO_SHIFT = "No shifts available."

ROLE_CHECK = "You can't assign shifts to a {role_name}. Please enter a valid staff(user) ID for shift assign."
INVALID_STAFF = "Invalid staff ID. Please enter a valid staff_id (user_id)."

#Nurse 

NURSE_MENU = """
        ------ Nurse Features ------
              1. View Shifts
              2. View Profile
              3. View Patient Details
              4. View Patient Report
              5. Check Doctor Availability
              6. Manage Appointments
              7. Exit
              """
NURSE = "--- Nurse Profile ---"

#Reports

MANAGE_REPORT = """
        ------ MANAGE PATIENT REPORT  ------
              1. View Reports
              2. Create Reports
              3. Update Reports
              4. Delete Reports
              5. Return Back
              """

REPORT_ID_NOT_EXIST = "Report Id Not Exists."
REPORT = "--- Your Patients Reports ---"
NO_REPORT_FOUND = "No reports found of the patient."
REPORT_VIEW_ERROR = "Error reports:"
ENTER_REPORT_ID = "Enter the Report ID :"

REPORT_NAME = "Enter the Report Name: "
REPORT_DESCRIPTION = "Enter the Report Description: "
REPORT_SUCCESS = "Report created successfully."
REPORT_UPDATE_SUCCESS = "Report updated successfully."
REPORT_DELETE_SUCCESS = "Report deleted successfully."

# Main
ACCESS_DENIED = "Invalid Role. Access Denied"

# Operations 
OPERATION_CHOICE = "Kindly enter your opeation choice : "
ENTER_CHOICE = "Enter Your Choice : "
EXIT = "Exit. Thank You !"


# Validations 

VALID_NAME = "Invalid name. Only letters and spaces are allowed."
VALID_EMAIL = "Invalid email format ."
VALID_PASSWORD_1 = "Password must be at least 8 characters long."
VALID_PASSWORD_2 = "Password must contain at least one uppercase letter."
VALID_PASSWORD_3 = "Password must contain at least one lowercase letter."
VALID_PASSWORD_4 = "Password must contain at least one digit."
VALID_PASSWORD_5 = "Password must contain at least one special character."
VALID_PHONE_1 = "Phone number cannot be empty."
VALID_PHONE_2 = "Invalid phone number. Must be a 10-digit number."
VALID_AGE = "Invalid age. Age must be a positive number between 0 and 120."
VALID_DATE = "Please Enter Date With DD/MM/YYYY format"
VALID_GENDER = "Invalid gender."
VALID_BLOOD_GROUP = "Invalid blood group"