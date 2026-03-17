import re
phone = input("Enter phone number: ")
email = input("Enter email ID: ")

#sample patterns
phone_pattern = "^[6-9]\d{9}$"  #exactly 10 digits
email_pattern = "^\w+@\w+\.\w{2,}$" #basic email format

#check phone number
if re.match(phone_pattern,phone):
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")

#chech email
if re.match(email_pattern,email):
    print("Valid Email ID")
else:
    print("Invalid Email ID")
