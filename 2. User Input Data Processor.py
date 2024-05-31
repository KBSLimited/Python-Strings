#Task 1: Input Length Validator

def validate_name_length(first_name, last_name):
    min_length = 2

    if len(first_name) < min_length or len(last_name) < min_length:
        print("Error: Both first name and last name should be at least 2 characters long.")
        return False
    else:
        return True

# Get user input for first name and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Validate the length of first name and last name
if validate_name_length(first_name, last_name):
    print("Both first name and last name are valid.")
else:
    print("Please enter valid first name and last name.")

#Task 2: Password Complexity Checker

def check_password_complexity(password):
    # Define complexity requirements
    min_length = 8
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)

    # Check if the password meets all complexity requirements
    if len(password) < min_length:
        print("Password should be at least 8 characters long.")
        return False
    elif not has_uppercase:
        print("Password should contain at least one uppercase letter.")
        return False
    elif not has_lowercase:
        print("Password should contain at least one lowercase letter.")
        return False
    elif not has_digit:
        print("Password should contain at least one digit.")
        return False
    else:
        print("Password meets complexity requirements.")
        return True
password = input("Enter your password:")

# Test the function

check_password_complexity(password)

#Task 3: Email Formatter

import re

def standardize_email(email):
    # Convert email to lowercase
    email = email.lower()

    # Remove leading and trailing whitespaces
    email = email.strip()

    # Define a regular expression pattern to validate email format
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Check if the email matches the pattern
    if re.match(pattern, email):
        return email
    else:
        print("Error: Invalid email format. Please enter a valid email address.")
        print("Example of a valid email address: example@example.com")
        return None

# Prompt the user to enter their email address
user_email = input("Enter your email address: ")

# Standardize the user's email address
standardized_email = standardize_email(user_email)
if standardized_email:
    print(f"Your standardized email address: {standardized_email}")

# Standardized email exail example: user321@example.com