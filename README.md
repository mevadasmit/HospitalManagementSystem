# HospitalManagementSystem
Hospital Management System (HMS) - Python &amp; SQL ==> Terminal Based

## **Project Description**  
The **Hospital Management System (HMS)** is a robust and efficient system designed to streamline hospital operations, improve patient care, and optimize resource management. Built using **Python** and **SQL**, this system allows administrators to manage hospital staff, doctors, patients, appointments, and shifts efficiently.

The system ensures **data integrity**, **role-based access**, and **error handling**, making it ideal for real-world healthcare environments.  

---

## **Key Features**  

### **1. User Management**  
- Admin can create, update, and delete **hospital staff** (nurses, receptionists).  
- Doctors are managed separately under **doctors_detail** to maintain professional classification.  
- Secure authentication and user role management.  

### **2. Patient Management**  
- View patient records including **name, age, gender, medical history, and contact details**.  
- Ensure no duplicate patient entries exist.  
- Update patient information as required.  

### **3. Appointment Management**  
- Patients can book appointments with **available doctors**.  
- Doctors can **accept/reject** appointments.  
- Receptionists can **schedule** and **cancel** appointments.  
- Doctors' availability is validated before booking.  

### **4. Shift Management**  
- Admin assigns shifts to **doctors, nurses, and receptionists**.  
- Validation prevents the same user from getting multiple shifts on the same day.  
- Doctors and staff can view their **assigned shifts**.  

### **5. Department Management**  
- CRUD operations on hospital **departments**.  
- Prevent duplicate department creation.  

### **7. Database Operations & Queries**  
- Uses **MySQL/PostgreSQL** as the backend database.  
- Implements **advanced queries** (JOINs, Subqueries, Aggregation, GROUP BY, HAVING).  
- Uses **parameterized queries** to prevent SQL injection.  

---

## **Technology Stack**  

### **Backend**  
- **Python** (for business logic)  
- **MySQL/PostgreSQL** (for database management)  

### **Libraries Used**  
- `PrettyTable` (for tabular data representation)  
- `psycopg2/mysql-connector` (for database connection)  
- `datetime` (for handling date-based operations)  

---

## **Installation & Setup**  

### **1. Clone the Repository**
```bash
git clone https://github.com/mevadasmit/hospital-management-system.git
cd hospital-management-system
```

### **2. Install Dependencies**
```bash
pip install mysql-connector-python  # If using MySQL
pip install psycopg2  # If using PostgreSQL
pip install prettytable
```

### **3. Configure Database**  
- Create a **database** in MySQL/PostgreSQL.  
- Import the required **SQL schema** from `database.sql`.  
- Update **database connection settings** in `config.py`.  

- DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': '',
       'USER': '',
       'PASSWORD': '',
       'HOST': 'localhost',
       'PORT': ,
   }
}


### **4. Run the Application**  
```bash
python main.py
```

---

## **Project Structure**
```
hospital-management-system/
│── main.py                  # Entry point of the application
│── config.py                 # Database configuration
│── admin.py                  # Admin functionalities
│── doctors.py                # Doctor-related functions
│── patients.py               # Patient management
│── appointments.py           # Appointment scheduling
│── shifts.py                 # Shift management
│── departments.py            # Department CRUD operations
│── database.sql              # SQL schema & sample data
│── utils.py                  # Helper functions for database operations
└── README.md                 # Project documentation
```
---

## **License**  
This project is **open-source** and available under the MIT License.  

---

Project Author 

Mevada Smit
