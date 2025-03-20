
LOGIN_QUERY = """ 
			SELECT users.id AS user_id, users.name, roles.role_name 
			FROM users 
			JOIN roles ON users.role_id = roles.id 
			WHERE users.email = %s AND users.password = %s
			"""


#--------------------------------------------- Admin -------------------------------------------------------

FETCH_AND_VERIFY = """ SELECT u.id FROM users u
                JOIN patients_detail p ON u.id = p.user_id
                WHERE p.id = %s;
                """

UPDATE_USERS = """UPDATE users 
                SET name = %s, age = %s, gender = %s, blood_group = %s, phone_number = %s, email = %s, address = %s,updated_by = %s
                WHERE id = %s;"""


VIEW_STAFF = """ SELECT users.id, users.name, roles.role_name 
                FROM users
                JOIN roles ON users.role_id = roles.id
                WHERE roles.id IN (2, 4, 5) 
                ORDER BY roles"""

VALIDATE_USER = """SELECT id FROM users WHERE id = %s"""
VALIDATE_SHIFT = """SELECT id from shift WHERE id = %s"""

DELETE_USER = """DELETE FROM users WHERE id = %s"""

ALL_STAFF_SHIFT = """SELECT hs.user_id, u.name AS staff_name, r.role_name As user_role, s.day_name AS shift_day
                FROM hospital_staff_details hs
                JOIN users u ON hs.user_id = u.id
                JOIN roles r ON r.id = u.role_id
                JOIN shift s ON hs.shift_id = s.id"""

ALL_DOCTOR_SHIFT = """SELECT u.id AS user_id , sm.doctors_detail_id AS doctor_id, u.name AS doctor_name, de.department_name  , s.day_name AS shift_day
                FROM shift_manage sm
                JOIN doctors_detail dd ON sm.doctors_detail_id = dd.id
                JOIN users u ON dd.user_id = u.id
                JOIN department_details de ON de.id =  dd.department_id
                JOIN shift s ON sm.shift_id = s.id """



#----------------------------------------- Doctor's ---------------------------------------------


USERS_DATA = """ SELECT id , name , age , gender , blood_group , phone_number, email, address from users where id = %s"""


DOCTOR_FETCH_ID = """
                SELECT id 
                FROM doctors_detail
                WHERE user_id = %s
            """
                   

DOCTORS_WITH_ID = """SELECT u.id As user_id , d.id As Doctor_id , u.name As Doctor_Name , d.department_id, de.department_name AS Department_name , 
                    d.consultation_fees , d.joining_date
                    FROM users u
                    JOIN doctors_detail d ON d.user_id = u.id
                    JOIN department_details de ON de.id =  d.department_id"""
                    
STAFF_WITH_ID = """SELECT users.id, users.name, roles.role_name 
                FROM users
                JOIN roles ON users.role_id = roles.id
                WHERE roles.id IN (4, 5) 
                ORDER BY roles"""                    

REPORT_RECORD = """SELECT rt.report_name , rt.report_description from report_type rt
                    join report ON report.id = rt.report_id WHERE report_id = %s """

VALIDATE_DOCTOR = """SELECT id FROM doctors_detail WHERE id = %s"""
            
DOCTOR_SHIFT = """SELECT 
                    s.id AS shift_id, 
                    s.day_name 
                FROM 
                    shift_manage sm
                JOIN 
                    shift s ON sm.shift_id = s.id
                WHERE 
                    sm.doctors_detail_id = %s"""

DOCTOR_RECORD = """SELECT d.joining_date , d.consultation_fees , d.department_id from doctors_detail d"""

DOCTOR_PROFILE = """SELECT u.id, u.name, u.email, u.phone_number,u.gender, u.blood_group, 
                    d.joining_date, d.consultation_fees FROM users u
                    JOIN doctors_detail d ON u.id = d.user_id
                    WHERE u.id = %s"""
                
PATIENT_DETAIL = """SELECT 
					u.id, u.name, u.email, u.phone_number, u.address, u.gender, u.blood_group, a.id AS appointment_id
                FROM users u
                JOIN patients_detail pd ON u.id = pd.user_id
                JOIN appointments a ON a.patients_detail_id = pd.id
                WHERE pd.id = %s AND a.doctors_detail_id = (
                    SELECT id FROM doctors_detail WHERE user_id = %s
                )"""

UPDATE_DOCTOR = """UPDATE doctors_detail SET joining_date = %s , consultation_fees = %s, department_id = %s ,updated_at = NOW() , 
                                        updated_by = %s WHERE id = %s"""


#------------------------------------ Reports & Report_type ---------------------------------

VIEW_REPORT = """SELECT 
					r.id, rt.report_name, rt.report_description, a.appointment_details, p.name AS patient_name,
                r.created_at FROM report r
                JOIN report_type rt ON r.id = rt.report_id
                JOIN appointments a ON r.appointment_id = a.id
                JOIN patients_detail pd ON a.patients_detail_id = pd.id
                JOIN users p ON pd.user_id = p.id
                WHERE a.doctors_detail_id = (
                    SELECT id FROM doctors_detail WHERE user_id = %s
                )"""            

REPORT_CREATE = """INSERT INTO report (appointment_id, created_by, updated_by)
                VALUES (%s, %s, %s)
                RETURNING id"""

CREATE_REPORT_TYPE = """ INSERT INTO report_type 
				(report_id, report_name, report_description, created_by, updated_by)
                VALUES (%s, %s, %s, %s, %s)
            """
            
UPDATE_REPORT = """UPDATE report_type
                SET report_name = %s, report_description = %s, updated_at = NOW(), updated_by = %s
                WHERE report_id = %s"""

DELETE_REPORT = """DELETE FROM report WHERE id = %s"""

REPORT_ID = """SELECT id from report WHERE id = %s"""


#------------------------------------------ Appointments -------------------------------------

VIEW_APPOINTMENTS = """SELECT 
                    appointments.id , appointment_date, patients_detail_id, users.name, appointment_details
                    FROM appointments
                    JOIN patients_detail ON appointments.patients_detail_id = patients_detail.id
                    JOIN users ON patients_detail.user_id = users.id
                    JOIN doctors_detail ON appointments.doctors_detail_id = doctors_detail.id
                    JOIN users doctor_users ON doctors_detail.user_id = doctor_users.id
                    WHERE appointments.doctors_detail_id = %s
                    ORDER BY appointment_date DESC
            	"""

CREATE_APPOINTMENTS = """
                		INSERT INTO appointments (patients_detail_id, doctors_detail_id, appointment_date, 
                  		appointment_details, created_by, updated_by)
                		VALUES (%s, %s, %s, %s, %s, %s) RETURNING id """

VALIDATE_APPOINTMENT_ID = """	SELECT * FROM appointments WHERE id = %s"""

VALIDATE_APPOINTMENT = """ SELECT 
							id, appointment_date, appointment_details
                		FROM appointments
                		WHERE id = %s AND doctors_detail_id = %s """
        
UPDATE_APPOINTMENT = """UPDATE appointments
                	SET appointment_date = %s, appointment_details = %s , updated_by = %s
                	WHERE id = %s
            		""" 

DELETE_APPOINTMENTS = """ DELETE FROM appointments
                WHERE id = %s AND doctors_detail_id = %s"""

DELETE_APPOINTMENTS_BY_RE = """DELETE FROM appointments WHERE id = %s"""



#------------------------------------ Receptionist -------------------------------------- 

ROLE_ID = """SELECT id from roles WHERE role_name = %s """

CREATE_PATIENT = """ INSERT INTO users (name, age, gender, blood_group, phone_number, email, address, password, role_id, created_by, updated_by)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s , %s ) 
                RETURNING id """

INSERT_PATIENT_TABLE = """INSERT INTO patients_detail (user_id,created_by,updated_by) VALUES (%s,%s,%s) RETURNING id"""


INSERT_HSM_TABLE = """INSERT INTO hospital_staff_details (shift_id, user_id, created_by, updated_by)
                VALUES (%s, %s, %s, %s)"""

INSERT_IN_DOCTOR = """INSERT INTO doctors_detail (user_id, joining_date, consultation_fees, department_id, created_by, updated_by)
                VALUES (%s, %s, %s, %s, %s, %s)"""

INSERT_SHIFT_M_TABLE = """ INSERT INTO shift_manage (doctors_detail_id, shift_id)
                VALUES (%s, %s)"""

DUPLICATE_SHIFT_CHECK = """ SELECT sm.id FROM shift_manage sm
                JOIN shift s ON sm.shift_id = s.id
                WHERE sm.doctors_detail_id = %s AND s.id = %s;
            """

STAFF_DUPLICATE_SHIFT_CHECK = """ SELECT hs.id FROM hospital_staff_details hs
            JOIN shift s ON hs.shift_id = s.id
            WHERE hs.user_id = %s AND s.id = %s;
            """
            
#--------------------------------- DEPARTMENTS ----------------------------------------

AVAILABLE_DEPARTMENTS = """SELECT id, department_name FROM department_details"""

DEPARTMENT_ID = """SELECT id FROM department_details WHERE LOWER(department_name) = LOWER(%s)"""

CREATE_DEPARTMENT = """INSERT INTO department_details (department_name) VALUES (%s)"""

DELETE_DEPARTMENT = """DELETE FROM department_details WHERE id= %s"""

CHECK_ID = """SELECT id FROM department_details WHERE id = %s"""


# ------------------------------------ SHIFTS -------------------------------------------

SHOW_SHIFT = """ SELECT id, day_name FROM shift"""



#--------------------------------------- Bills --------------------------------------------

VIEW_BILL = """ SELECT b.id, a.id As appointment_id, p.name AS patient_name, a.appointment_details, b.total_amount
                FROM bill b
                JOIN appointments a ON b.appointment_id = a.id
                JOIN patients_detail pd ON a.patients_detail_id = pd.id
                JOIN users p ON pd.user_id = p.id
                where pd.id = %s"""

CREATE_BILL = """ INSERT INTO bill (appointment_id, total_amount, created_by, updated_by)
                VALUES (%s, %s, %s, %s)"""

UPDATE_BILL = """UPDATE bill
                SET total_amount = %s, updated_at = NOW(), updated_by = %s
                WHERE id = %s """

DELETE_BILL = """ DELETE FROM bill WHERE id = %s"""

VALIDATE_BILL = """ SELECT id FROM bill WHERE id = %s"""




#-------------------------------------------- Nurse ----------------------------------------------

NURSE_SHIFT = """SELECT s.day_name, hs.shift_id
                FROM hospital_staff_details hs
                JOIN shift s ON hs.shift_id = s.id
                WHERE hs.user_id = %s"""

NURSE_PROFILE = """ SELECT u.id, u.name, u.email, u.phone_number, u.gender, u.blood_group
                FROM users u
                JOIN roles r ON u.role_id = r.id
                WHERE u.id = %s"""

                        
VIEW_PATIENT_DETAILS = """ SELECT u.id, pd.id , u.name, u.age, u.gender, u.blood_group, u.phone_number
                FROM users u
                JOIN patients_detail pd ON u.id = pd.user_id
                WHERE pd.id = %s"""
                
FETCH_PATIENT_DATA = """ SELECT u.id ,u.name, u.age, u.gender, u.blood_group, u.phone_number, u.email, u.address
                FROM users u
                WHERE u.id = %s"""

VIEW_PATIENT_REPORTS = """ SELECT u.name AS patient_name,rt.report_name, 
                    rt.report_description, r.created_at
                    FROM appointments a
                    JOIN report r ON a.id = r.appointment_id
                    JOIN report_type rt ON r.id = rt.report_id
                    JOIN patients_detail p ON a.patients_detail_id = p.id
                    JOIN users u ON p.user_id = u.id
                    WHERE a.patients_detail_id = %s"""

DOCTOR_AVAILABEL = """
                SELECT u.name AS doctoREPORT_NAME, s.day_name AS shift_day
                FROM shift_manage sm
                JOIN doctors_detail dd ON sm.doctors_detail_id = dd.id
                JOIN users u ON dd.user_id = u.id
                JOIN shift s ON sm.shift_id = s.id
                WHERE sm.doctors_detail_id = %s"""


VIEW_N_APPOINTMENT = """ SELECT 
                    appointments.id AS appointment_id, appointment_date,
                    appointment_details, patients_detail_id AS patient_id,
                    users.name AS patient_name, doctors_detail.id AS doctor_id,
                    doctor_users.name AS docto_name
                    FROM appointments
                    JOIN patients_detail ON appointments.patients_detail_id = patients_detail.id
                    JOIN users ON patients_detail.user_id = users.id
                    JOIN doctors_detail ON appointments.doctors_detail_id = doctors_detail.id
                    JOIN users doctor_users ON doctors_detail.user_id = doctor_users.id
                    ORDER BY appointment_date DESC"""



# -------------------------------- Patient ------------------------------------------------------

PATIENT_ID = """ SELECT id FROM patients_detail
                WHERE user_id = %s
            """
            
VIEW_PROFILE = """	SELECT name, age, gender, blood_group, phone_number, email, address
                FROM users
                WHERE id = %s
            """

VIEW_APPOINTMENT = """ SELECT a.id, a.appointment_details, a.appointment_date, u.name AS doctoREPORT_NAME
                FROM appointments a
                JOIN doctors_detail d ON a.doctors_detail_id = d.id
                JOIN users u ON d.user_id = u.id 
                WHERE a.patients_detail_id = %s"""

VIEW_REPORTS = """SELECT rt.report_name, rt.report_description, r.created_at
                FROM appointments a
                JOIN report r ON a.id = r.appointment_id
                JOIN report_type rt ON r.id = rt.report_id
                WHERE a.patients_detail_id = %s
            """

VIEW_BILLS = """SELECT b.id, a.appointment_details, b.total_amount, b.created_at
                FROM bill b
                JOIN appointments a ON b.appointment_id = a.id
                WHERE a.patients_detail_id = %s
            """
                
VALIDATE_PATIENT = """ SELECT id FROM patients_detail WHERE id = %s"""