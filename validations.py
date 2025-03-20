import re
from constant import (VALID_NAME , VALID_EMAIL , VALID_PASSWORD_1 , VALID_PASSWORD_2 , VALID_PASSWORD_3 , VALID_PASSWORD_4, 
                      VALID_PASSWORD_5 , VALID_PHONE_1 , VALID_PHONE_2 , VALID_AGE , VALID_DATE , VALID_GENDER, VALID_BLOOD_GROUP)

def valid_name(name):
    """Validate name to ensure it contains only letters and spaces."""
    if not name or not re.match(r"^[A-Za-z\s]+$", name):
        raise ValueError(VALID_NAME)
    return name

def valid_email(email):
    """Validate email format."""
    if not email or not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
        raise ValueError(VALID_EMAIL)
    return email

def valid_password(password):
    """Validate password strength."""
    if len(password) < 8:
        raise ValueError(VALID_PASSWORD_1)
    if not re.search(r"[A-Z]", password):
        raise ValueError(VALID_PASSWORD_2)
    if not re.search(r"[a-z]", password):
        raise ValueError(VALID_PASSWORD_3)
    if not re.search(r"[0-9]", password):
        raise ValueError(VALID_PASSWORD_4)
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        raise ValueError(VALID_PASSWORD_5)
    return password

def valid_number(number, current_number=None):
    """Validate phone number format (10-digit number) or retain current."""
    if not number: 
        if current_number:
            return current_number
        raise ValueError(VALID_PHONE_1)

    if not re.match(r"^\d{10}$", number):
        raise ValueError(VALID_PHONE_2)
    return number

def valid_age(age):
    """Validate age to ensure it's a positive number and within a reasonable range."""
    if int(age) < 0 or int(age) > 120:
        raise ValueError(VALID_AGE)
    return int(age)

def valid_gender(gender):
    """Validate gender input (male or female)."""
    valid_genders = ['Male', 'Female','male','female','FEMALE','MALE']
    if gender not in valid_genders:
        raise ValueError(VALID_GENDER)
    return gender

def valid_blood_group(blood_group):
    """Validate blood group (A+, B+, O+, AB+, etc.)."""
    valid_blood_groups = ['A+', 'A-', 'B+', 'B-', 'O+', 'O-', 'AB+', 'AB-']
    if blood_group not in valid_blood_groups:
        raise ValueError(VALID_BLOOD_GROUP)
    return blood_group

def valid_date(date):
    if not date or not re.match("^[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}$",date):
        raise ValueError(VALID_DATE)
    return date
