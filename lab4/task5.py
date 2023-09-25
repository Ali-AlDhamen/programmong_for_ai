password = input("Enter password: ")
valid = True

if len(password) < 6 or len(password) > 16:
    valid = False
if not any(i.islower() for i in password):
        valid = False
if not any(i.isupper() for i in password):
        valid = False
if not any(i.isdigit() for i in password):
        valid = False
if not any(i in "$#@" for i in password):
        valid = False


if valid:
    print("Valid password")
else:
    print("Invalid password")
