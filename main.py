from database_connection import DatabaseConnection
# from database_setup import DatabaseSetup
from config import Config
from auth import Authentication
from admin import AdminFeatures
from patient import PatientFeatures
from receptionist import ReceptionistFeatures
from doctor import DoctorFeatures
from nurse import NurseFeatures
from constant import (HEADING, LOGIN_MENU, ENTER_CHOICE, USER_EMAIL, USER_PASSWORD, USER_LOGIN_SUCCESS, ACCESS_DENIED, 
                      EXIT, INVALIDCHOICE)


def main():
    obj_config = Config()
    obj_db_connection = DatabaseConnection(obj_config)
    # obj_db_setup = DatabaseSetup(obj_db_connection)
    # obj_db_setup.create_table()
    # obj_db_setup.insert_data()
    auth = Authentication(obj_db_connection)

    print(HEADING)

    while True:
        print(LOGIN_MENU)

        choice = int(input(ENTER_CHOICE).strip())

        if choice == 1:
            # Login functionality
            email = input(USER_EMAIL)
            password = input(USER_PASSWORD)
            user = auth.login(email, password)

            if user:
                name = user.get('name')
                role_name = user.get('role_name')
                user_id = user.get('id')

                print(USER_LOGIN_SUCCESS.format(name = name , role_name = role_name))

                if role_name == 'Admin':
                    admin = AdminFeatures(obj_db_connection,user_id)
                    admin.admin_main_menu()

                elif role_name == 'Patient':
                    patient = PatientFeatures(obj_db_connection,user_id)
                    patient.patient_menu()

                elif role_name == 'Receptionist':
                    receptionist = ReceptionistFeatures(obj_db_connection, user_id)
                    receptionist.receptionist_menu()

                elif role_name == 'Doctor':
                    doctor = DoctorFeatures(obj_db_connection,user_id)
                    doctor.doctor_menu()

                elif role_name == 'Nurse':
                    nurse = NurseFeatures(obj_db_connection , user_id)
                    nurse.nurse_menu()

                else:
                    print(ACCESS_DENIED)

        elif choice == 2:
            print(EXIT)
            break

        else:
            print(INVALIDCHOICE)

if __name__ == '__main__':
    main()
    