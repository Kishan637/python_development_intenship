# Email validator

def validate_email(email):
    if "@" in email and "." in email:
        return "Valid Email "
    else:
        return "Invalid Email "

email = input("Enter your email: ")
print(validate_email(email))